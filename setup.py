from setuptools import setup

setup(
    name = 'graph-cd',
    version = '0.01',
    author = 'Oleksandr Lysenko',
    author_email = 'sashkolysenko@gmail.com',
    packages = ['cycles'],
    install_requires=[
        'argparse',
        'python-graph-core',
        'python-graph-dot'
    ]
)
