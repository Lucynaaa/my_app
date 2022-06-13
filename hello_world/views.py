from apka import app
from flask import request

moje_imie = "Lucyna"
msg = "Hello again "


@app.route('/')
def index():
   return msg + moje_imie
