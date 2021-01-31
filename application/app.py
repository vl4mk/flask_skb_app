import os
import subprocess

from flask import Flask, render_template

# from flask_sqlalchemy import SQLAlchemy


name_service = 'apache2'
start = 'systemctl start ' + name_service + '.service'
stop = 'systemctl stop ' + name_service + '.service'
restart = 'systemctl restart ' + name_service + '.service'
output = subprocess.getoutput('systemctl status ' + name_service + '.service | grep Active')  # variable for getstatus
status = output

app = Flask(__name__)


@app.route("/getstatus")  # function for get status
def getstatus():
    output1 = subprocess.getoutput('systemctl status ' + name_service + '.service | grep Active')  # .split()
    global status
    status = output1
    return render_template("index.html", status=status, name=name_service)


@app.route('/')
def index():
    return render_template("index.html", status=status, name=name_service)


@app.route('/background_process_start')  # function for start service
def background_process_start():
    os.system(start)
    getstatus()
    return "nothing"


@app.route('/background_process_stop')  # function for stop service
def background_process_stop():
    os.system(stop)
    getstatus()
    return "nothing"


@app.route('/background_process_restart')  # function for restart service
def background_process_restart():
    os.system(restart)
    getstatus()
    return "nothing"


if __name__ == "__main__":
    app.run()
