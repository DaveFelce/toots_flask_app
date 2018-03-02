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

    return structured_data

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

def make_authors(data):
    """
    Create a lookup dict keyed on author id with name as value

    :param data: dict of authors
    :return: lookup dict keyed on author id
    """

    authors = {d['id']: d['name'] for d in data}
    return authors