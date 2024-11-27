# backend/routes/send_reminders.py

from flask import Blueprint, request, jsonify
from tasks import send_expiration_emails
from utils.verify_firebase_token import verify_firebase_token

send_reminders_bp = Blueprint('send_reminders', __name__)

@send_reminders_bp.route('/send-reminders', methods=['POST'])
def trigger_send_reminders():
    print('omg u called send reminders?!?!?!?')
    # Get the Authorization header
    auth_header = request.headers.get('Authorization', None)
    if not auth_header:
        print('NOT AUTH HEARDER')
        return jsonify({'error': 'Authorization header missing'}), 401

    # Extract the token
    parts = auth_header.split()
    if parts[0].lower() != 'bearer' or len(parts) != 2:
        return jsonify({'error': 'Invalid Authorization header'}), 401

    id_token = parts[1]

    # Verify the Firebase ID token
    decoded_token = verify_firebase_token(id_token)
    if not decoded_token:
        print('INVALID EXPIRED TOKEN')
        return jsonify({'error': 'Invalid or expired token'}), 401

    # Token is valid; you can access user information from decoded_token
    user_id = decoded_token['user_id']
    email = decoded_token.get('email', None)

    print('wow. you made it')
    # Proceed to trigger the task
    send_expiration_emails.delay()

    return jsonify({'message': 'Expiration emails are being sent.'}), 200
