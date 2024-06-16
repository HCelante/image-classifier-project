import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from src.models.model import create_model
from src.models.train import compile_and_train
from src.utils.helpers import create_dir_if_not_exists

def main():
    create_dir_if_not_exists('models/')
    
    x_train = np.load('data/processed/x_train.npy')
    y_train = np.load('data/processed/y_train.npy')
    x_test = np.load('data/processed/x_test.npy')
    y_test = np.load('data/processed/y_test.npy')

    model = create_model()
    history = compile_and_train(model, x_train, y_train, x_test, y_test)

    model.save('models/image_classifier_model.h5')
    print("Modelo treinado e salvo em models/image_classifier_model.h5")

if __name__ == "__main__":
    main()
