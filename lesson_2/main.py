import secrets
from flask import Flask, render_template, request, session, make_response, flash, redirect, url_for

app_secret_key = secrets.token_hex()
app = Flask(__name__)
app.secret_key = app_secret_key


@app.route('/')
def index():
    if request.cookies.get('username'):
        session['username'] = request.cookies.get('username')
        print(session['username'])
        return render_template('index.html', **session )
    return render_template('index.html')

@app.route('/sign_in/', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        if not request.form['username']:
            flash('Ведите имя пользователя!', 'danger')
            return render_template('sign_in.html')
        elif not request.form['userpass']:
            flash('Ведите пароль!', 'danger')
            return render_template('sign_in.html')
        # response = make_response(render_template('index.html'))
        flash('Вход выполнен!', 'success')
        response = make_response(redirect(url_for('index')))
        response.headers['new_head'] = 'New value'
        response.set_cookie('username', request.form.get('username'))
        return response
    return render_template('sign_in.html')
    


@app.route('/sign_up/', methods=['GET', 'POST'])
def sing_up():
    if request.method == 'POST':
        if not request.form['username']:
            flash('Ведите имя пользователя!', 'danger')
            return render_template('sign_up.html')
        elif not request.form['usermail']:
            flash('Ведите почту!', 'danger')
            return render_template('sign_up.html')
        elif not request.form['usermail']:
            flash('Ведите пароль!', 'danger')
            return render_template('sign_up.html')
        flash('Вы зарегестрырованны!!', 'success')
        session['username'] = request.form.get('username')
        session['usermail'] = request.form.get('usermail')
        session['userpass'] = request.form.get('userpass')
    return render_template('sign_up.html')

@app.route('/hello_cookie/')
def hello_cookie():
    name = request.cookies.get('username')
    return render_template('hello_cookie.html', name)

@app.route('/sign_out/')
def sign_out():
    response = make_response(redirect(url_for('index')))
    response.headers['new_head'] = 'New value'
    response.set_cookie('username', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)

