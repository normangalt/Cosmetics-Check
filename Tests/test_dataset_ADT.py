import dataset_ADT

import unittest

from unittest import TestCase

class TestDataSetADT(TestCase):
    def setUp(self):
        dataset = dataset_ADT.DataframeDataset()
        dataset.read_data('test_db.xlsx')

    def test_is_in(self):
        self.assertIsNotNone(self.is_in('element0'), 'Failed ingredient is in database test')
        self.assertIsNotNone(self.is_in('element5'), 'Failed ingredient is in database test')
        self.assertIsNotNone(self.is_in('element10'), 'Failed ingredient is in database test')
        self.assertIsNone(self.is_in('element15'), 'Failed ingredient is not in database test')
        self.assertIsNone(self.is_in('name'), 'Failed ingredient is not in database test')
        self.assertIsNone(self.is_in('ELEMENT0'), 'Failed ingredient (caps) is not in database test')

    def test_retrieve(self):
        self.assertEqual(self.dataset.retrieve('element0')['name'], 'element0', 'Failed to retrieve element')
        self.assertEqual(self.dataset.retrieve('element0')['property1'], 'comment0', 'Failed to retrieve element')
        self.assertEqual(self.dataset.retrieve('element1')['property0'], 'st1', 'Failed to retrieve element')
        self.assertEqual(self.dataset.retrieve('element15'), 'None', 'Failed to retrieve element that is not in dataset')
        self.assertEqual(self.dataset.retrieve('name'), 'None', 'Failed to retrieve element that is not in dataset')
