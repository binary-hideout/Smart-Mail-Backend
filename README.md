Smart-Mail-Backend
==================

The lightweight automatic call dashboard that fits your needs.

Install
-------

Clone the repository 

    $ git clone https://github.com/binary-hideout/Smart-Mail-Backend.git

Create a virtualenv and activate

    $ cd Smart-Mail-Backend
    $ virtualenv venv
    $ source venv/bin/activate

Install the requirements

    $ pip install -r requirements.txt

Run the tests
-------------

    $ pytest
    $ coverage run -m pytest
    $ coverage report
    $ coverage html

Create environment variables
----------------------------

Follow the .env.example file:

    DATABASE_URL = <your-database-connection-string>
    APP_SECRET_KEY = <your-app-secret-key>
    TESTING_DATABASE_URL = <sqlite:///data.db>
    TESTING_APP_SECRET_KEY = <your-testing-app-secret-key>
    TESTING_SETTINGS = testing_settings.py
    APPLICATION_SETTINGS = default_settings.py

Run the app
-----------

    $ export FLASK_APP=smartmail
    $ export FLASK_ENV=development
    $ flask run

Endpoints
---------

* **GET** `http://127.0.0.1:5000/contacts`
* **GET** `http://127.0.0.1:5000/contact/<string: email>`
* **POST** `http://127.0.0.1:5000/contact/<string: email>`
* **DELETE** `http://127.0.0.1:5000/contact/<string: email>`
* **PUT** `http://127.0.0.1:5000/contact/<string: email>`
* **GET** `http://127.0.0.1:5000/tags`
* **GET** `http://127.0.0.1:5000/tag/<string: title>`
* **POST** `http://127.0.0.1:5000/tag/<string: title>`
* **DELETE** `http://127.0.0.1:5000/tag/<string: title>`
* **PUT** `http://127.0.0.1:5000/tag/<string: title>`
* **GET** `http://127.0.0.1:5000/cases`
* **GET** `http://127.0.0.1:5000/case/<string: title>`
* **POST** `http://127.0.0.1:5000/case/<string: title>`
* **DELETE** `http://127.0.0.1:5000/case/<string: title>`
* **PUT** `http://127.0.0.1:5000/case/<string: title>`