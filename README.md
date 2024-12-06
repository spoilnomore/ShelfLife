# ShelfLife

This application helps you keep track of the food in your pantry.

ShelfLife is a scalable application that allows for multiple
households to sign up and share food entries with each other.
Each household only sees their own food.

To run this application, you need to set up a Firebase project 
on Google and enable Google authentication. You also need
Docker and you need `make` if you are on Windows (just use
chocolatey and do `choco install make`).

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

MAIL_SERVER=smtp.youremailprovider.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=fillmeout
MAIL_PASSWORD=fillmeout
MAIL_DEFAULT_SENDER=fillmeout@yep.com
```

Just replace the `fillmeout` with the values.

## Running

```bash
make
```

...yep.
its that easy ..
if youre on windows then you need chocolatey for `choco install make`.. and docker

## Lessons Learned

If you are coding in a cross-platform cross-OS development team then Docker is the
best thing. Windows users are kind of left to run the extra mile but still is worth
it when having to deploy to production, real-world scenarios. Servers run on Linux
etc so Windows developers get to play a more fun game of customizing their setup to be
more Unix like

This involves downloading git bash, chocolatey, and installing make (makefiles are also
extremely potent and useful)

`git config --global core.autocrlf false`

^ we encountered an issue where shell script was invisible to docker and docker db would
not initialize with an sql script, well it was because windows was cloning crlf instead of
lf. this command is actually not necessary if using .gitattributes * eol = lf