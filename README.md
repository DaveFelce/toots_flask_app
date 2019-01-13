# toots_flask_app

## Install

### Chromedriver

brew tap homebrew/cask

brew cask install chromedriver

### Pipenv

#### If you get an error about: TypeError: 'module' object is not callable

Downgrade pip with this:

pipenv run pip install pip==18.0

Then:

Pipenv install

## To run in docker container

docker-compose up

## Run

FLASK_APP=toots.py; /Users/davidfelce/dev/toots_flask_app/toots.py

### Tests (from project dir)

python -m unittest discover -s tests -p '*test*.py'

### Behave tests

Make sure you have started the docker container, so the app is running on port 5000 locally, before running these in a demo!

You set up the behave tests in Pycharm by adding a runtime config of type Behave
