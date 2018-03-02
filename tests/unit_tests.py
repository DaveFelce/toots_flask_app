import unittest
import json
import os

import toots
from utils import *

import pprint


class TootsTest(unittest.TestCase):

    def setUp(self):
        self.test_file = os.path.join(toots.app.root_path, 'fixtures', 'toots_small.json')

    def test_make_structured_data(self):
        data = json.loads(read_file_from_disk(self.test_file))
        structured_data = make_structured_data(data)

        pprint.pprint(structured_data)
        self.assertEqual(len(structured_data), 3)
        self.assertEqual(len(structured_data[0].get('children')), 2)
        self.assertEqual(len(structured_data[0]['children'][0].get('children')), 1)
        self.assertEqual(structured_data[0]['children'][1]['children'][0]['children'][0].get('text'), 'zoot choot!')
        self.assertEqual(structured_data[0]['children'][1]['children'][0]['children'][0].get('parent_id'), 97)




