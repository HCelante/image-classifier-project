import unittest
from src.data.load_data import load_data

class TestLoadData(unittest.TestCase):
    def test_load_data(self):
        (x_train, y_train), (x_test, y_test) = load_data()
        self.assertEqual(x_train.shape, (50000, 32, 32, 3))
        self.assertEqual(y_train.shape, (50000, 1))
        self.assertEqual(x_test.shape, (10000, 32, 32, 3))
        self.assertEqual(y_test.shape, (10000, 1))

if __name__ == '__main__':
    unittest.main()
