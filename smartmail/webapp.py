from . import app

import os

from flask import Flask
from flask_restful import Api

from resources.contact import Contact, ContactList
from resources.case import Case, CaseList
from resources.tag import Tag, TagList

from apps.db import db
from apps.ma import ma

from dotenv import load_dotenv

