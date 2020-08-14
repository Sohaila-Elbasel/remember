from flask import Flask, render_template, request, redirect, url_for
from forms import Addshow
from imports import read_file, write_file

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e14b0006b64d6f97042d224d38050df3'

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        list = read_file()
        if request.method == 'GET':
            return render_template('home.html', list=list, filter_value='all')
        else:
            filter = []
            select = request.form.get('filter')
            if select == 'all':
                return render_template('home.html', list=list, filter_value=select)
            else:
                for show in list:
                    if show['type'] == select:
                        filter.append(show)
                return render_template('home.html', list=filter, filter_value=select)
    except:
        return render_template('home.html', filter_value='all')

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = Addshow()
    if request.method == 'POST':
        if form.validate_on_submit():
            show = form.name.data + ',' + form.type.data + ','+ form.season.data + ',' + form.last_ep.data
            write_file(show)
            return redirect(url_for('home'))
    return render_template('add.html', form = form)

@app.route('/edit')
def edit():
    return render_template('edit.html')

if __name__ == '__main__':
    app.run(debug=True)
