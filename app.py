from flask import Flask, render_template, request, redirect, url_for, abort
from forms import Addshow
from imports import read_file, write_file, search, delete

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

@app.route('/edit/<string:name>', methods=['GET', 'POST'])
def edit(name):
    show = search(name)
    form = Addshow()
    if request.method == 'GET':
        form.name.data = show['name']
        form.type.data = show['type']
        form.season.data = show['season']
        form.last_ep.data = show['last_ep']
        return render_template('edit.html', form = form, show=show)
    else:
        if request.form['action'] == 'Edit':
            if form.validate_on_submit():
                delete(form.name.data)
                show = form.name.data + ',' + form.type.data + ','+ form.season.data + ',' + form.last_ep.data
                write_file(show)
                return redirect(url_for('home'))
        elif request.form['action'] == 'Delete':
            delete(form.name.data)
            return redirect(url_for('home'))
        else:
            abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
