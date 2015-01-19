#coding: utf-8
from flask import Flask, request, render_template
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template('1plus2.html')




if __name__ == '__main__':
    app.run(debug=True)
