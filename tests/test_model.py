import unittest
import numpy as np
from src.models.model import create_model
from src.models.train import compile_and_train

class TestModel(unittest.TestCase):
    def test_create_model(self):
        model = create_model(input_shape=(32, 32, 3))
        self.assertEqual(len(model.layers), 7)  # Verifique o número de camadas na rede

    def test_compile_and_train(self):
        model = create_model(input_shape=(32, 32, 3))
        x_train = np.random.rand(10, 32, 32, 3)  # Dados de treino fictícios
        y_train = np.random.randint(10, size=(10, 1))  # Rótulos de treino fictícios
        x_test = np.random.rand(5, 32, 32, 3)  # Dados de teste fictícios
        y_test = np.random.randint(10, size=(5, 1))  # Rótulos de teste fictícios
        history = compile_and_train(model, x_train, y_train, x_test, y_test, epochs=1)
        self.assertIn('accuracy', history.history)

if __name__ == '__main__':
    unittest.main()
