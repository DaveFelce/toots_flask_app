import unittest
import json
import os

import toots
from utils import *


class TootsTest(unittest.TestCase):

    def setUp(self):
        self.test_toots_file = os.path.join(toots.app.root_path, 'fixtures', 'toots_small.json')
        self.test_authors_file = os.path.join(toots.app.root_path, 'fixtures', 'authors.json')

    def test_make_structured_data(self):
        data = json.loads(read_file_from_disk(self.test_toots_file))
        structured_data = get_toots(data)

        self.assertEqual(len(structured_data), 3)
        self.assertEqual(len(structured_data[0].get('children')), 2)
        self.assertEqual(len(structured_data[0]['children'][0].get('children')), 1)
        self.assertEqual(structured_data[0]['children'][1]['children'][0]['children'][0].get('text'), 'zoot choot!')
        self.assertEqual(structured_data[0]['children'][1]['children'][0]['children'][0].get('parent_id'), 97)

    def test_make_authors(self):
        authors_data = json.loads(read_file_from_disk(self.test_authors_file))
        authors = get_authors(data=authors_data)
        self.assertEqual(len(authors), 10)
        self.assertEqual(authors[5], 'Fred')
        self.assertEqual(authors[9], 'Jim')


    def test_toot_threads_by_author(self):

        toots_data = json.loads(read_file_from_disk(self.test_toots_file))
        author_id_to_filter = 5
        toots = get_toots_by_author(data=toots_data, author_id_to_filter=author_id_to_filter)

        self.assertEqual(len(toots), 1)
        self.assertEqual(toots[0].get('author_id'), 5)
        self.assertEqual(len(toots[0].get('children')), 4)


if __name__ == '__main__':
    unittest.main()
