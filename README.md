Plivo 2 Factor Authentication (2FA) App
=======================================

## tl;dr

Click the button below to deploy the Plivo 2FA app directly to your heroku account:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## About

This example shows how [Plivo APIs](http://plivo.com/docs/api) can be used to integrate a two factor authentication system into your own web application. This example is built in Python using Flask application framework but the concept behind it language agnostic. So, be it Python, PHP, Ruby or Node, the concept remains the same.

The next section explains how the application works and in-turn how Plivo as a platform works. There is a separate section on deployment which explains how to deploy this application on Heroku.

## How to use it

[Here is a live demo](https://plivo-2fa.herokuapp.com/) of this sample application where you can try out how it works. This application verifies your phone number using the two factor authentication system. In the application, enter your phone number in [E.164](http://en.wikipedia.org/wiki/E.164) format and click on 'Send Verification Code'. This sends an SMS to that number with a random security code in it. The application now shows a text box to enter this code to verify your mobile number. Once you get the code in the SMS, enter the code in the text box and click 'Check'. This will tell you whether the code you entered is correct or not. If you enter the correct code, then the application knows that the phone number belongs to you and thus the number is verified.

## Requirements
- Git
- Python 2.7 with PIP and Virtualenv
- Redis Server

## Requirements
- Git
- Python 2.7 with PIP and Virtualenv
- Redis Server

## Running the application locally
You can run the app locally for testing by following these steps:

1. From a terminal window, run `git clone https://github.com/cachrisman/Plivo-2FA-App.git`
1. Removing the current `.git` folder in the project root using `rm -rf  .git/`.
1. Create a `.env` file in the project root with the following contents:
    ```
    PLIVO_AUTH_ID=XXXXXXXXXXXXXXXXXXXX
    PLIVO_AUTH_TOKEN=YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
    PLIVO_NUMBER=14155551234
    ```
    `PLIVO_AUTH_ID` and `PLIVO_AUTH_TOKEN` can be found in the [Plivo Dashboard](https://manage.plivo.com/dashboard/) homepage and `PLIVO_NUMBER` should be set to a valid [Plivo Number](https://manage.plivo.com/number) in your account from which you want to send the verification SMS.

1. Install the redis server on your local machine:
  - OS X with [Homebrew](http://brew.sh/): Run `brew install redis` to install, then `brew services start redis` to start the server
  - OS X without Homebrew: follow the quickstart instructions on the [redis website](http://redis.io/topics/quickstart) or google for `os x install redis -homebrew` for guides
  - Ubuntu: run `sudo apt-get update;sudo apt-get install redis-server` to install, then `sudo service redis-server start` to start the server
1. Create a [virtual environment](http://www.virtualenv.org/en/latest/) by running `virtualenv venv`. __NOTE__: _if you don't have `virtualenv` installed, run the command `sudo pip install virtualenv` to install `virtualenv`_
1. Activate the `virtualenv` using `source ./venv/bin/activate`.
1. Install all the application's dependencies specified in `requirements.txt` using `pip install -r requirements.txt`.
1. Now you can run the app locally by running this command `python app.py` in the project root and browsing to http://localhost:5000 to see if it works properly. When done testing, press `CTRL+C` to stop and exit the python server.

## Deployment on Heroku

### Initial Setup

This section explains how to prepare your system to deploy this app to Heroku.

1. [Create an account](https://signup.heroku.com/) on Heroku (its free!).
1. Verify your Heroku account and add a credit card. This app doesn't require any paid addons, but you still need to add your credit card to use free 3rd party Heroku addons.
1. Install the [Heroku toolbelt](https://toolbelt.heroku.com/).
1. Login to heroku from the toolbelt using the `heroku login` command. If you do not have an ssh public key in your system, it prompts to automatically create it. Hit 'Y' when prompted.
    ```
    $ heroku login
    Enter your Heroku credentials.
    Email: charlie@plivo.com
    Password:
    Could not find an existing public key.
    Would you like to generate one? [Yn]
    Generating new SSH public key.
    Uploading ssh public key /Users/charlie/.ssh/id_rsa.pub
    ```

1. Once this is done, you are ready to deploy the application.

### The Actual Deployment

Click the button below to deploy directly to your heroku account:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

or follow these instructions to deploy to heroku:

1. Run `heroku create` to create an application on Heroku and adds it as a remote to the local git repo.
1. Run `heroku addons:create redistogo:nano -a YOUR_APP_NAME` (replace YOUR_APP_NAME with the name of the app created in step 1) to install the [redistogo](https://addons.heroku.com/redistogo) addon for this application.
1. Push the local code to the heroku repo for deployment using `git push heroku master`.
1. To run one web process as specified in the `Procfile`, run the `heroku ps:scale web=1` command.
1. You can see if it is running by using the `heroku ps` command. It should return something like `web.1: up for 5s`.
1. You can check (and watch) the application logs using `heroku logs -t` command. Press `CTRL+C` to exit.
1. To open the application in the web browser, type `heroku open` and hit `ENTER`.
1. You'll see this application in the web browser.

Find the live demo of the application [here](http://plivo-2fa.herokuapp.com/). For more detailed information on deployment on heroku, visit the [official heroku documentation](https://devcenter.heroku.com/articles/python). More information about Plivo APIs can be found in the [offical API docs](http://plivo.com/docs/).

Helper libraries for various languages are available on the [Plivo github page](http://github.com/plivo).
