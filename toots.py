from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def index():
    # TODO: render threads!
    data = json.loads(read_file_from_disk('data/toots.json'))
    structured_data = make_structured_data(data)
    # TODO: send structured_data to renderer
    return render_toot(None)


@app.route('/author/<author_name>')
def toot_threads_by_author(author_name):
    # TODO: Implement me!
    return '<span>Specific Toot threads for {author_name}</span>'.format(author_name=author_name)


def render_toot(toot):
    author_name = 'Someone' # FIXME
    text = 'Not a real Toot' # FIXME

    return """
    <li>
        <span><a href="/author/{author_name}">{author_name}</a></span>
        <span>:</span>
        <span>{text}</span>
    </li>
    """.format(
        author_name=author_name,
        text=text,
    )

def read_file_from_disk(filename):
    with open(filename, mode='r') as file:
        lines = file.read()

    return lines

def make_structured_data(data):
    """
    Create a structured parent/child list of dicts based on id

    :param data: list of dicts
    :return: structured list of dicts
    """
    structured_data = []
    for node in data:
        parent_id = node.get('parent_id')
        if parent_id is None:
            structured_data.append(node)
            node['children'] = get_children(node.get('id'), data)

def get_children(parent_id, data):
    """
    Recursive function to create child node list for current node

    :param parent_id:
    :param data: the full original data structure
    :return: list of children
    """
    child_nodes = [d for d in data if d['parent_id'] == parent_id]
    if not child_nodes:
        return []
    else:
        for child_node in child_nodes:
            child_node['children'] = get_children(child_node.get('id'), data)

        return child_nodes
