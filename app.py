from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    return """<h1>Welcome to My Watchlist</h1>
           <img src="http://helloflask.com/totoro.gif">"""

@app.route('/user/<name>')
def user_page(name):
    return f'User:{escape(name)}'

@app.route('/test')
def test_url_for():
    # 调用示例（访问后在命令行窗口查看URL）；
    print(url_for('hello'))

    print(url_for('user_page', name='greyli'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))

    print(url_for('test_url_for', num=2))
    return 'Test page'