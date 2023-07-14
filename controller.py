#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author：keko_rand
# email: kekorand@gmail.com
# 2023/7/14 11:48
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'hello'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30003, debug=True)