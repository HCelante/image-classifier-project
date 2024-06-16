import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import tensorflow as tf
from src.evaluation.evaluate import evaluate_model

def main():
    x_test = np.load('data/processed/x_test.npy')
    y_test = np.load('data/processed/y_test.npy')

    model = tf.keras.models.load_model('models/image_classifier_model.h5')
    test_loss, test_acc = evaluate_model(model, x_test, y_test)

    print(f"Accuracy: {test_acc}, Loss: {test_loss}")

if __name__ == "__main__":
    main()
