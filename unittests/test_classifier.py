import os
import unittest
import warnings

from squat.Classifier.ClassifierUtil import ClassifierUtilRaw


class TestClassifierUtilRaw(unittest.TestCase):

    def setUp(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path =  os.path.join(BASE_DIR, 'squat', 'Classifier', 'out')
        self.widget = ClassifierUtilRaw(model_dir=model_path)

    def test_cheque(self):
        cat, accuracy = self.widget.get_cat('Cheque 0956277')
        self.assertEqual(cat, 'cheque')
        self.assertGreaterEqual (accuracy, .7)

    def test_cash(self):
        cat, accuracy = self.widget.get_cat('Cash Deposit')
        self.assertEqual(cat, 'cash')
        self.assertGreaterEqual(accuracy, .7)

    def test_food(self):
        cat, accuracy = self.widget.get_cat('KFC bbsr')
        self.assertEqual(cat, 'food')
        self.assertGreaterEqual(accuracy, .7)


if __name__ == '__main__':
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        unittest.main()