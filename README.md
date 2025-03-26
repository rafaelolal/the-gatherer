# The Gatherer

This is a minimalistic tracker for card abilities in "Magic: The Gathering". This project helps reduce the cognitive load for noobie players who struggle to keep track of all the abilities in play.

## Features

* Create a section with a name. A section can represent anything that you want. It is essentially a grouping of cards.
* Add cards to a section.
* Check off abilities that are in play.
* Delete cards.
* Pass the turn, which will reset all abilities in play.

## Issues

* When first loading the webpage, it can be unresponsive because of the large datalist under the "Add Card" input. This is because the datalist is populated with all the cards in the database.
* Very minimal error handling and testing was done. This project was created in about three hours.

## Setup

1. Clone the repository.
2. Create a virtual environment.
3. Run `pip install -r requirements.txt` to install the required packages.
4. Populate the database with cards by running `python populate_db.py`.
5. Run `python manage.py runserver` to start the server.
6. Use `ngrok` to expose the server to the internet with `ngrok http 8000`.
7. Share the ngrok URL and enjoy!
