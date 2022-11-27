
from setuptools import setup, find_packages

setup(name='prompt-lib',
      version='0.1',
      description="Library for running few-shot inference on large language models",
      packages=find_packages(),
      install_requires=['openai==0.23.0', 'pandas', 'requests==2.28.1', 'scikit_learn==1.1.2', 'statsmodels==0.13.2', 'tqdm==4.49.0', 'wandb==0.13.2'],
      license='MIT',
      long_description=open('README.md').read(),
)