from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

list = [
    {'name': 'Bungou stray dogs',
     'type': 'Anime',
     'season': 3,
     'last_ep': 4
    },
    {'name': 'Dr.stone',
     'type': 'Anime',
     'season': 1,
     'last_ep': 8
    },
    {'name': 'Brooklyn Nine-Nine',
     'type': 'English series',
     'season': 3,
     'last_ep': 2
    },

]

@app.route('/')
def home(filter = 'all'):
    if filter == 'all':
        return render_template('home.html', list = list)

if __name__ == '__main__':
    app.run(debug=True)
