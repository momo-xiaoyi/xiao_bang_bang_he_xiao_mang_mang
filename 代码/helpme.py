from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base1.html')


@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        pass


@app.route('/register/',methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        pass


@app.route('/deal/', methods=['GET', 'POST'])
def deal():
    if request.method == 'GET':
        return render_template('deal.html')
    else:
        pass

if __name__ == '__main__':
    app.run()
