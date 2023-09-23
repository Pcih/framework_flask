from flask import Flask
from flask import render_template
from data_temp import data_jacket, data_boots, data_clots 

app = Flask(__name__)


@app.route('/')
@app.route('/main/')
def get_index():

    context = {
        'title': 'Home',
        '_data_boots': data_boots,
        '_data_clots': data_clots,
        '_data_jacket': data_jacket
    }
    return render_template('index.html', **context)

@app.route('/boots/')
def get_boots():
    complex = {
        'title': 'Boots',
        '_data_boots': data_boots
    }
    return render_template('boots.html', **complex)

@app.route('/clothes/')
def get_clothes():
    complex = {
        'title': 'Clothes',
        '_data_clots': data_clots
    }
    return render_template('clothes.html', **complex)

@app.route('/jacket/')
def get_jacket():
    complex = {
        'title': 'Jacket',
        '_data_jacket': data_jacket
    }
    return render_template('jacket.html', **complex)

if __name__ == '__main__':
    app.run(debug=True)

