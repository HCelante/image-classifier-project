from setuptools import find_packages, setup

setup(
    name='image-classifier-project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tensorflow',
        'numpy',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'download-data=scripts.download_data:main',
            'preprocess-data=scripts.preprocess_data:main',
            'train-model=scripts.train_model:main',
            'evaluate-model=scripts.evaluate_model:main',
        ],
    },
)
