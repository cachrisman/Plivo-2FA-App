Plivo Two Factor Auth App
=======================================

## About

This example shows how [Plivo APIs](http://plivo.com/docs/api) can be used to integrate a two factor authentication system into your own web application. This example is built in Python using Flask application framework but the concept behind it language agnostic. So, be it Python, PHP, Ruby or Node, the concept remains the same.

The next section explains how the application works and in-turn how Plivo as a platform works. There is a separate section on deployment which explains how to deploy this application on Heroku.

## How to use it

[Here is a live demo](https://plivo-2fa.herokuapp.com/) of this sample application where you can try out how it works. This application verifies your phone number using the two factor authentication system. In the application, enter your phone number in [E.164](http://en.wikipedia.org/wiki/E.164) format (currently works for US numbers) and click on 'Send Verification Code'. This sends an SMS to that number with a random security code in it. The application now shows a text box to enter this code to verify your mobile number. Once you get the code in the SMS, enter the code in the text box and click 'Check'. This will tell you whether the code you entered is correct or not. If you enter the correct code, then the application knows that the phone number belongs to you and thus the number is verified.

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

1. Now you can run the app locally by running this command `python app.py` in the project root and browsing to http://localhost:5000 to see if it works properly.

## Deployment on Heroku

### Initial Setup

This section explains how to deploy this application on Heroku.
1. [Create an account](https://signup.heroku.com/) on Heroku (its free!).
2. Verify your Heroku account by adding a credit card. This app doesn't require any paid addons, but to use even free 3rd party Heroku addons you need to add your credit card.
2. Install the [Heroku toolbelt](https://toolbelt.heroku.com/)
3. Login to heroku from the toolbelt using the `heroku login` command.
If you do not have an ssh public key in your system, it prompts to automatically create it. Hit 'Y' when prompted.
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
    Once this is done, then we are ready to deploy the application.


### The Actual Deployment
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
1. Change to directory which contains the `Procfile`.
2. Create a [virtual environment](http://www.virtualenv.org/en/latest/) by running `virtualenv --distribute`.
__NOTE__: _if you don't have `virtualenv` installed, then install python setup tools first using `sudo apt-get install python-setuptools` and then install `virtualenv` using `sudo pip install virtualenv`_
3. Activate the `virtualenv` using `source ./venv/bin/activate`.
4. Install all the application's dependencies specified in `requirements.txt` using `pip install -r requirements.txt`.
5. Install the [redistogo](https://addons.heroku.com/redistogo) addon to use the heroku free data store for this application. To add a free redistogo data store to this application use `heroku addons:add redistogo` command.
6. Once, the dependencies are installed, start the application process locally using `foreman start` command. It should start the application locallly and should NOT throw any error or exception. If successfully started, do `CTRL+C` to stop it.
10. Create an application on Heroku server using `heroku create` which creates a remote git repo and updates the origin to the newly created git repo.
11. Now, push the local code to the heroku repo for deployment using `git push heroku master`.
12. To run one web process as specified in the `Procfile`, run the `heroku ps:scale web=1` command.
13. Now, the application should be successfully running if everything went right!
14. We can test it using `heroku ps` command. It should say something like `web.1: up for 5s`.
15. We can check the application logs using `heroku logs` command.
16. To open the application in the web browser, type `heroku open` and hit `ENTER`.
17. You'll see this application in the web browser.

Find the live demo of the application [here](http://shielded-hollows-9845.herokuapp.com/). For more detailed information on deployment on heroku, visit the [official heroku documentation](https://devcenter.heroku.com/articles/python). More information about Plivo APIs can be found in the [offical API docs](http://plivo.com/docs/).

Helper libraries for various languages are available on the [Plivo github page](http://github.com/plivo).
