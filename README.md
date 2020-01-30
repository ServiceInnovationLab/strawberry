# 🍓 Strawberry 🍓

Reads actions from Trello (using the trello API) and saves each action as a row in output.csv.

  Note for NZ gov / DIA users: This will not run on a DIA device (they are super locked down). You will need to ask a dev to run this for you.

## Installation

1. Use the version of python specified in `.python-version` (install [pyenv](https://github.com/pyenv/pyenv) to do this automatically)
1. Install the dependencies `pip install -r requirements.txt`
1. `cp env-example .env`
1. Get a Trello API key and token from <https://trello.com/app-key>
1. Place Trello api key and token in `.env` file

## Usage

```bash
./run.py
```
