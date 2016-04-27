from flask import Blueprint
auth = Blueprint('auth',__name__)
from redis import Redis
conn=Redis()

from . import views