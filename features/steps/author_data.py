from behave import *
import toots
from utils import *
import os
import json
from nose.tools import *

@given(u'A test toots file and an author id')
def step_has_toots_file_and_author_id(context):

    test_toots_file = os.path.join(toots.app.root_path, 'fixtures', 'toots_small.json')
    context.toots_data = json.loads(read_file_from_disk(test_toots_file))
    context.author_id_to_filter = 5

@when(u'I fetch the toots for a single author')
def step_fetch_toots_for_single_author(context):

    context.toots = get_toots_by_author(data=context.toots_data, author_id_to_filter=context.author_id_to_filter)

@then(u'I get the expected data')
def step_check_expected_data(context):

    assert_equal(len(context.toots), 1)
    assert_equal(context.toots[0].get('author_id'), 5)
    assert_equal(len(context.toots[0].get('children')), 4)
