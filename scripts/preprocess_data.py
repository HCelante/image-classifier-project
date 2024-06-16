import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from src.data.load_data import load_data
from src.data.preprocess import normalize_images
from src.utils.helpers import create_dir_if_not_exists

def main():
    create_dir_if_not_exists('data/processed/')
    
    (x_train, y_train), (x_test, y_test) = load_data()
    x_train = normalize_images(x_train)
    x_test = normalize_images(x_test)

    np.save('data/processed/x_train.npy', x_train)
    np.save('data/processed/y_train.npy', y_train)
    np.save('data/processed/x_test.npy', x_test)
    np.save('data/processed/y_test.npy', y_test)
    print("Dados pré-processados e salvos em data/processed/")

if __name__ == "__main__":
    main()
