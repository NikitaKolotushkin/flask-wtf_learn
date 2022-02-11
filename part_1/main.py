#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template


app = Flask(__name__)


@app.route('/<title_>')
@app.route('/index/<title_>')
def index(title_):
    return render_template('base.html', title=title_, img='')


@app.route('/training/<prof_>')
def training(prof_):
    return render_template('training.html', prof=prof_)


if __name__ == '__main__':
    app.debug = 1
    app.run(port=8080, host='127.0.0.1')