#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template


app = Flask(__name__)


@app.route('/')
def root():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    list_ = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!',
    ]
    return '<br/>'.join(list_)


@app.route('/image_mars')
def image_mars():
    return """  <!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                    </head>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src='static/img/mars.png'>
                        <p>Вот она какая, красная планета.</p>
                    </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""  <!DOCTYPE html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                            <title>Колонизация</title>
                        </head>
                        <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src='static/img/mars.png'>
                            <div class="alert alert-dark" role="alert">
                                <b>Человечество вырастает из детства.</b>
                            </div>
                            <div class="alert alert-success" role="alert">
                                <b>Человечеству мала одна планета.</b>
                            </div>
                            <div class="alert alert-secondary" role="alert">
                                <b>Мы сделаем обитаемыми безжизенные пока планеты.</b>
                            </div>
                            <div class="alert alert-warning" role="alert">
                                <b>И начнем с Марса!</b>
                            </div>
                            <div class="alert alert-danger" role="alert">
                                <b>Присоединяйся!</b>
                            </div>
                        </body>
                    </html>"""


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return render_template('choice.html', title='Варианты выбора', planet=planet_name)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return render_template('results.html', title='Результаты', nickname=nickname, level=level, rating=rating)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')