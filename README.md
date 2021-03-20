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
    $ cd venv
    $ cd Scripts
    $ activate.bat
    $ pip install -r requirements.txt

Run the tests
-------------

    $ pytest
    $ coverage run -m pytest

Create environment variables (.env)
-----------------------------------

    $
    $
    $

Endpoints
---------

* **GET** `http://127.0.0.1:5000/contacts`
* **GET** `http://127.0.0.1:5000/contact/<string: name>`
* **POST** `http://127.0.0.1:5000/contact/<string: name>`
* **DELETE** `http://127.0.0.1:5000/contact/<string: name>`
* **PUT** `http://127.0.0.1:5000/contact/<string: name>`