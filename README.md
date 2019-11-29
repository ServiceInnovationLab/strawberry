# Strawberry

Reads actions from Trello (using the trello API) and saves each action as a row in output.csv

Note: This will not run on a DIA device (they are super locked down). You will need to ask a dev to run this for you.

## Installation

1. Use the version of python in .python-version (install pyenv to do this automaticaly)
1. Install the dependencies
  ```
  pip install -r requirements.txt
  ```
1. `cp env-example .env`
1. Get a Trello API key and token from <https://trello.com/app-key>
1. Place trello api key and token in `.env` file

## Usage

```bash
./run.py
```
