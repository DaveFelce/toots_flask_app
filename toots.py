from flask import Flask, render_template
import json
import os
from utils import *

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('home.html')

@app.route('/authors')
def authors():

    toots_data = json.loads(read_file_from_disk(os.path.join(app.root_path, 'data', 'toots.json')))
    toots = get_toots(data=toots_data)
    authors_data = json.loads(read_file_from_disk(os.path.join(app.root_path, 'data', 'authors.json')))
    authors = get_authors(data=authors_data)

    context = {'authors':authors, 'toots':toots}
    return render_template('authors.html', **context)

@app.route('/author/<author_id>')
def toot_threads_by_author(author_id):

    author_id_to_filter = int(author_id)
    toots_data = json.loads(read_file_from_disk(os.path.join(app.root_path, 'data', 'toots.json')))
    toots = get_toots_by_author(data=toots_data, author_id_to_filter=author_id_to_filter)
    authors_data = json.loads(read_file_from_disk(os.path.join(app.root_path, 'data', 'authors.json')))
    authors = get_authors(data=authors_data)

    context = {'authors':authors, 'toots':toots}
    return render_template('toots_by_author.html', **context)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')