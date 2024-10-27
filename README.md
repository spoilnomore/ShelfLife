# ShelfLife

You need to set up a Firebase project on Google
and enable Google authentication

heres what GPT said so you dont have to waste
another water bottle asking it for a response.. ;)

## Google authentication setup

Steps to Enable Google Sign-In in Firebase

    Go to the Firebase Console:
        Open your browser and go to Firebase Console.

    Select Your Project:
        Choose the Firebase project you are working on (the one you initialized in your app).

    Navigate to Authentication:
        In the left sidebar, click on "Authentication."

    Go to Sign-in Method:
        Click on the "Sign-in method" tab at the top of the Authentication page.

    Enable Google Sign-In:
        Find Google in the list of providers and click on it.
        Toggle Enable to ON.
        You can optionally configure other settings, like your project’s support email.
        Click Save to apply the changes.

    Check Authentication Settings:
        Make sure other relevant configurations, like OAuth settings, are properly set up.
        Ensure your OAuth client ID is correctly configured if you need custom OAuth settings.


Then fix .env with the proper values that Firebase gives you.

Here is an example .env.

```
VUE_APP_SERVER_URL=/api
VUE_APP_FIREBASE_API_KEY=fillmeout
VUE_APP_FIREBASE_AUTH_DOMAIN=fillmeout
VUE_APP_FIREBASE_PROJECT_ID=fillmeout
VUE_APP_FIREBASE_STORAGE_BUCKET=fillmeout
VUE_APP_FIREBASE_MESSAGING_SENDER_ID=fillmeout
VUE_APP_FIREBASE_APP_ID=fillmeout
VUE_APP_FIREBASE_MEASUREMENT_ID=fillmeout
```

Just replace the `fillmeout` with the values.
