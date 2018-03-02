from flask import Flask, render_template
import json
import os
from utils import *

app = Flask(__name__)


@app.route('/')
def index():

    data = json.loads(read_file_from_disk(os.path.join(app.root_path, 'data', 'toots.json')))
    toots = make_structured_data(data)
    return render_template('home.html', toots=toots)

@app.route('/authors')
def authors():

    toots_data = json.loads(read_file_from_disk(os.path.join(app.root_path, 'data', 'toots.json')))
    toots = make_structured_data(toots_data)
    authors_data = json.loads(read_file_from_disk(os.path.join(app.root_path, 'data', 'authors.json')))
    authors = make_authors(authors_data)

    context = {'authors':authors, 'toots':toots}
    return render_template('authors.html', **context)

@app.route('/author/<author_name>')
def toot_threads_by_author(author_name):

    return '<span>Specific Toot threads for {author_name}</span>'.format(author_name=author_name)


if __name__ == '__main__':
    app.run()