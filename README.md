# TuningForks
### (and Poll Goblin)

TuningForks is a Discord bot which captures input from an audio source on your computer and pipes it into a Discord voice channel. You should totally only use this to pipe audio files of sound effects  you've personally created earlier into your D&D games.

Poll Goblin is a simple, containerized AWS lambda function which grabs the top post of the week from a subreddit and sends an emoji poll to a Discord channel via webhook.

## TuningForks
### Config
Tuning forks requires secrets which should be stored either as environmental variables or in a `.env` file. `src/tuningforks/config.py` has lists of these required variables with default values where they are not secret.

### Set-up and Run
TuningForks requires python 3.9 and a simple `pip install .` in the root directory of the repo will install tuningforks.

Run with `python app.py`.


## Poll Goblin
Poll Goblin is a stand alone function which can be installed by `pip install -r poll_goblin/requirements.txt`. The lambda function can be run locally with `python poll_goblin/lambda_function.py`, just supply an env file to fill in the secrets.