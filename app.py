from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <body>
    <h1>웹앱프로그래밍</h1>
    <p><a href="/hello">헬로 페이지</a></p>
    <p><a href="/naver">네이버 페이지</a></p>
    </body>
    </html>
    '''

@app.route('/hello')
def hello():
    return render_template("main.html")

@app.route('/naver')
def naver():
    return render_template("naver.html")


@app.route('/gonaver', methods=['GET', 'POST'])
def gonaver():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        search = request.form['fname']
        return "당신이 검색한 키워드(POST)<br>{}입니다1.".format(search)

if __name__ == '__main__':
    app.run()