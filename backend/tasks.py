from app import celery
from datetime import datetime, timedelta
from models.food import Food
from models.user import User
from celery.utils.log import get_task_logger
import smtplib
import ssl
from email.mime.text import MIMEText
import logging
import os

logger = get_task_logger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

@celery.task
def send_expiration_emails():
    logger.info("Task send_expiration_emails started.")

    # Fetch email configurations directly from environment variables
    mail_server = os.getenv('MAIL_SERVER')
    mail_port = int(os.getenv('MAIL_PORT', 587))
    mail_username = os.getenv('MAIL_USERNAME')
    mail_password = os.getenv('MAIL_PASSWORD')
    mail_default_sender = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@shelflife.com')

    # Ensure all required email configurations are set
    if not all([mail_server, mail_port, mail_username, mail_password]):
        logger.error("Missing required email configurations. Check environment variables.")
        return

    today = datetime.utcnow().date()
    expiring_items = Food.query.filter(Food.expiration_date <= today).all()
    logger.info(f"Found {len(expiring_items)} expiring items.")

    owner_items = {}
    for item in expiring_items:
        if item.owner not in owner_items:
            owner_items[item.owner] = []
        owner_items[item.owner].append(item)

    for owner_username, items in owner_items.items():
        user = User.query.filter_by(username=owner_username).first()
        if user and user.email:
            try:
                item_list = '\n'.join([f"- {item.title} (expires on {item.expiration_date})" for item in items])
                email_body = f"Hello {user.username},\n\nThe following food items are expiring:\n{item_list}\n\nBest regards,\nShelfLife Team"

                msg = MIMEText(email_body)
                msg['Subject'] = 'Your food items are expiring soon!'
                msg['From'] = mail_default_sender
                msg['To'] = user.email

                # Create a secure SSL/TLS context
                context = ssl.SSLContext(ssl.PROTOCOL_TLS)

                # Use STARTTLS for port 587 (recommended for modern email servers)
                with smtplib.SMTP(mail_server, mail_port) as server:
                    server.ehlo()  # Identify to the SMTP server
                    server.starttls(context=context)  # Upgrade to a secure connection
                    server.ehlo()  # Re-identify after STARTTLS
                    server.login(mail_username, mail_password)
                    server.sendmail(msg['From'], [msg['To']], msg.as_string())

                logger.info(f"Sent email to {user.email}")
            except Exception as e:
                logger.error(f"Error sending email to {user.email}: {e}")
        else:
            logger.warning(f"User {owner_username} has no email.")
