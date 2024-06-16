# Image Classifier

### Criar o ambiente virtual e iniciar o projeto:
```sh
python3 scripts/init_project.py
```
```sh
source venv/bin/activate
```

### Descrição das Pastas e Arquivos

    data/: Diretório para armazenamento de dados.
        raw/: Dados brutos (não processados) baixados ou coletados.
        processed/: Dados processados prontos para uso no modelo.
        external/: Dados externos de fontes como datasets públicos.

    notebooks/: Notebooks Jupyter para exploração de dados, treinamento de modelos e avaliação.
        data_exploration.ipynb: Análise exploratória dos dados.
        model_training.ipynb: Treinamento do modelo.
        model_evaluation.ipynb: Avaliação do modelo treinado.

    src/: Código fonte do projeto.
        data/: Scripts para carregamento e pré-processamento de dados.
            load_data.py: Funções para carregar dados.
            preprocess.py: Funções para pré-processar dados.
        models/: Scripts relacionados aos modelos de machine learning.
            model.py: Definição do modelo.
            train.py: Funções para treinar o modelo.
        utils/: Scripts utilitários.
            helpers.py: Funções auxiliares.
        evaluation/: Scripts para avaliação do modelo.
            evaluate.py: Funções para avaliar o modelo.

    scripts/: Scripts independentes para executar tarefas específicas.
        download_data.sh: Script para baixar dados.
        preprocess_data.py: Script para pré-processar dados.
        train_model.py: Script para treinar o modelo.
        evaluate_model.py: Script para avaliar o modelo.

    tests/: Testes unitários para o código fonte.
        test_load_data.py: Testes para o script de carregamento de dados.
        test_preprocess.py: Testes para o script de pré-processamento.
        test_model.py: Testes para o script de definição de modelo.
        test_evaluate.py: Testes para o script de avaliação.

    .gitignore: Arquivo para especificar arquivos e pastas a serem ignorados pelo Git.

    README.md: Documentação do projeto.

    requirements.txt: Lista de dependências do projeto.

    setup.py: Script de configuração para instalação do pacote.