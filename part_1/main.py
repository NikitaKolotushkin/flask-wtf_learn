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
    return render_template('training.html', title_='Ваша схема корабля', prof=prof_)


@app.route('/list_prof/<type_>')
def list_prof(type_):
    professions = [
        'Инженер-исследователь',
        'Пилот',
        'Строитель',
        'Экзобиолог',
        'Врач',
        'Инженер по терраформированию',
        'Климатолог',
        'Специалист по радиационной защите',
        'Астрогеолог',
        'Гляциолог',
        'Инженер жизнеобеспечения',
        'Метеоролог',
        'Оператор марсохода',
        'Киберинженер',
        'Штурман',
        'Пилот дронов',
    ]
    return render_template('list_prof.html', list_=professions, list_type=type_)


if __name__ == '__main__':
    app.debug = 1
    app.run(port=8080, host='127.0.0.1')