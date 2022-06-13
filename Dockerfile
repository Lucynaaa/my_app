from python:2.7
run pip install flask gunicorn
copy ./hello_world /usr/apka
copy main.py /usr/apka
CMD PYTHONPATH=$PYTHONPATH:/usr \
    FLASK_APP=apka flask run --host=0.0.0.0
