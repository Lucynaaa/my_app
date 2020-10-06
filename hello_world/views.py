from hello_world import app
from flask import request

moje_imie = "Lucyna"
msg = "Hello: "


@app.route('/')
def index():
   return msg + moje_imie 
