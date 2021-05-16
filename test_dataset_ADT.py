import dataset_ADT

import unittest

from unittest import TestCase

class TestDataSetADT(TestCase):
    def setUp(self):
        dataset = dataset_ADT.DataframeDataset()
        dataset.read_data('test_db.xlsx')

    def test_is_in(self):
        self.assertTrue(self.is_in('element0'), 'Failed ingredient is in database test')
        self.assertTrue(self.is_in('element5'), 'Failed ingredient is in database test')
        self.assertTrue(self.is_in('element10'), 'Failed ingredient is in database test')
        self.assertFalse(self.is_in('element15'), 'Failed ingredient is not in database test')
        self.assertFalse(self.is_in('name'), 'Failed ingredient is not in database test')
        self.assertFalse(self.is_in('ELEMENT0'), 'Failed ingredient (caps) is not in database test')