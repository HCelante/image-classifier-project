import os
import sys
import subprocess

def set_pythonpath():
    os.environ['PYTHONPATH'] = os.getcwd()

def preprocess_data():
    set_pythonpath()
    subprocess.run([sys.executable, 'scripts/preprocess_data.py'])

def train_model():
    set_pythonpath()
    subprocess.run([sys.executable, 'scripts/train_model.py'])

def evaluate_model():
    set_pythonpath()
    subprocess.run([sys.executable, 'scripts/evaluate_model.py'])

def main():
    while True:
        print("Escolha uma opção:")
        print("1. Pré-processar os dados")
        print("2. Treinar o modelo")
        print("3. Avaliar o modelo")
        print("4. Sair")
        choice = input("Digite o número da opção e pressione Enter: ")

        if choice == '1':
            preprocess_data()
        elif choice == '2':
            train_model()
        elif choice == '3':
            evaluate_model()
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
