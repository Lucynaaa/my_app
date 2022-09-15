import datetime
from apka import app
from flask import request

msg = "Hello again :) "
moje_imie = "<font color=green>Lucyna</font>. Hello<font color=green> Michu</font>! <br> Today is " + str(datetime.datetime.today())


@app.route('/')
def index():
   return msg + moje_imie
