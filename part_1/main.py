#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template


app = Flask(__name__)


@app.route('/<title_>')
@app.route('/index/<title_>')
def index(title_):
    return render_template('base.html', title=title_)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')