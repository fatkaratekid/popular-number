To install requirements for your local intepreter you may want to run this first

    pip install -r requirements.txt

Now it's time to connect to heroku

    heroku login
    heroku create choose-some-name

which is short for

   heroku apps:create choose-some-name

verify git remote server is on heroku

    git remote -v

add scheduler

    heroku addons:create scheduler:standard

to open scheduler in browser

    heroku addons:create scheduler:standard

let's install mongodb add-on

    heroku addons:create mongolab:sandbox

After some time it will be initialized. Now you have env variable MONGODB_URI to access it in your code.

Set env varables for CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

    heroku config:set CONSUMER_KEY=consumer-key-from-tweeter-app
    heroku config:set CONSUMER_SECRET=consumer-secret-from-tweeter-app
    heroku config:set ACCESS_TOKEN=access-token-from-tweeter-app
    heroku config:set ACCESS_SECRET=access-secret-from-tweeter-app

You can create a script to run this, just put it in a file, for example env_init.sh. From terminal add the -x permission.

    chmod +x env_init.sh

And just run it

    ./env_init.sh

In a few moments you will have environment variables locally and on Heroku. YOu will have to run python code through Heroku CLI - heroku local (we'll deal with it soon).

Verify that all variables are there.

    heroku config

Now store those vars in a local file (you probably want a different set for produciton, but this is just an example)
    heroku config -s > .env

Be sure to add .env to .gitignore, you don't want to share this with the world

    echo .env >> .gitignore

Now you can run Fabric to test the setup is working locally.
    heroku local:run fab get_twitter_numbers 

You should get something like this from the log:
    INFO:root:[(2017.0, 1), (35.0, 1), (4.0, 1), (5.0, 1), (12.0, 1), (9711.0, 1), (23.0, 1)]





  
