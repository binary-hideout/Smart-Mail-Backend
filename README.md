Smart-Mail-Backend
==================

The lightweight automatic call dashboard that fits your needs.

Install
-------

    # clone the repository 
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
    APPLICATION_SETTINGS = default_settings.py

Endpoints
---------

* **GET** `http://127.0.0.1:5000/contacts`
* **GET** `http://127.0.0.1:5000/contact/<string: name>`
* **POST** `http://127.0.0.1:5000/contact/<string: name>`
* **DELETE** `http://127.0.0.1:5000/contact/<string: name>`
* **PUT** `http://127.0.0.1:5000/contact/<string: name>`