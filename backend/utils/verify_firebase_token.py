import requests
import jwt
import time
import os
import cryptography.x509
from cryptography.hazmat.backends import default_backend

# Get Firebase project ID from environment variables
FIREBASE_PROJECT_ID = os.getenv('VUE_APP_FIREBASE_PROJECT_ID')

if not FIREBASE_PROJECT_ID:
    raise Exception("Missing Firebase project ID. Please set VUE_APP_FIREBASE_PROJECT_ID in your environment variables.")

# Firebase issuer and audience
FIREBASE_ISSUER = f'https://securetoken.google.com/{FIREBASE_PROJECT_ID}'
FIREBASE_AUDIENCE = FIREBASE_PROJECT_ID

# URL to fetch Google's public keys
GOOGLE_CERTS_URL = 'https://www.googleapis.com/robot/v1/metadata/x509/securetoken@system.gserviceaccount.com'

def verify_firebase_token(id_token):
    try:
        # Fetch the public keys from Google
        certs_response = requests.get(GOOGLE_CERTS_URL)
        certs_response.raise_for_status()
        certs = certs_response.json()

        # Get the kid from the token header
        headers = jwt.get_unverified_header(id_token)
        kid = headers.get('kid')

        if not kid or kid not in certs:
            raise Exception('Invalid token: Key ID not found')

        # Get the public key (certificate)
        cert_str = certs[kid]
        
        # Load the certificate using cryptography
        cert = cryptography.x509.load_pem_x509_certificate(cert_str.encode(), default_backend())

        # Get the public key from the certificate
        public_key = cert.public_key()

        # Verify the token
        decoded_token = jwt.decode(
            id_token,
            public_key,
            algorithms=['RS256'],
            audience=FIREBASE_AUDIENCE,
            issuer=FIREBASE_ISSUER,
        )

        # Verify token expiration
        if decoded_token['exp'] < time.time():
            raise Exception('Token expired')

        return decoded_token  # Contains user information

    except Exception as e:
        print(f"Token verification failed: {e}")
        return None
