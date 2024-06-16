import unittest
import numpy as np
from src.data.preprocess import normalize_images

class TestPreprocess(unittest.TestCase):
    def test_normalize_images(self):
        x = np.array([0, 127, 255], dtype=np.uint8)
        x_normalized = normalize_images(x)
        np.testing.assert_array_almost_equal(x_normalized, [0.0, 0.498, 1.0], decimal=3)

if __name__ == '__main__':
    unittest.main()
