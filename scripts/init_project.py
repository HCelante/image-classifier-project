import os
import subprocess
import sys
import shutil

def create_venv():
    """Cria um ambiente virtual na pasta venv e adiciona uma chamada para scripts/menu.py na ativação"""
    try:
        subprocess.run([sys.executable, '-m', 'venv', 'venv'])
        print("Ambiente virtual criado com sucesso.")

        # Adicionar chamada ao scripts/menu.py na ativação do venv
        if os.name == 'nt':
            activate_script = os.path.join('venv', 'Scripts', 'activate.bat')
        else:
            activate_script = os.path.join('venv', 'bin', 'activate')
        
        with open(activate_script, 'a') as f:
            if os.name == 'nt':
                f.write(f'\npython {os.path.abspath("scripts/menu.py")}\n')
            else:
                f.write(f'\npython3 {os.path.abspath("scripts/menu.py")}\n')

        print("Chamada para scripts/menu.py adicionada na ativação do ambiente virtual.")
    except Exception as e:
        print(f"Erro ao criar o ambiente virtual: {e}")

def install_dependencies():
    """Instala as dependências listadas no arquivo requirements.txt"""
    try:
        if os.name == 'nt':
            pip_executable = os.path.join('venv', 'Scripts', 'pip')
        else:
            pip_executable = os.path.join('venv', 'bin', 'pip')
        
        subprocess.run([pip_executable, 'install', '-r', 'requirements.txt'])
        print("Dependências instaladas com sucesso.")
    except Exception as e:
        print(f"Erro ao instalar as dependências: {e}")

def activate_venv():
    """Ativa o ambiente virtual"""
    if os.name == 'nt':
        activate_script = os.path.join('venv', 'Scripts', 'activate.bat')
    else:
        activate_script = os.path.join('venv', 'bin', 'activate')
    
    if os.path.exists(activate_script):
        print(f"Para ativar o ambiente virtual, execute: source {activate_script}")
    else:
        print("O ambiente virtual não existe. Por favor, crie-o primeiro.")

def main_menu():
    """Exibe o menu principal e solicita a escolha do usuário"""
    while True:
        print("\nMenu:")
        print("1. Criar ambiente virtual e instalar dependências")
        print("2. Ativar ambiente virtual")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            create_venv()
            install_dependencies()
        elif choice == '2':
            activate_venv()
        elif choice == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main_menu()
