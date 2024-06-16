import unittest
import numpy as np
import tensorflow as tf
from src.evaluation.evaluate import evaluate_model

class TestEvaluate(unittest.TestCase):
    def test_evaluate_model(self):
        model = tf.keras.Sequential([tf.keras.layers.Flatten(input_shape=(32, 32, 3)), tf.keras.layers.Dense(10)])
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        x_test = np.random.rand(5, 32, 32, 3)
        y_test = np.random.randint(10, size=(5,))
        test_loss, test_acc = evaluate_model(model, x_test, y_test)
        self.assertGreaterEqual(test_acc, 0)
        self.assertLessEqual(test_acc, 1)

if __name__ == '__main__':
    unittest.main()
