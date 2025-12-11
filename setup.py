from setuptools import setup, find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='prometheus-es-exporter',
    version='0.14.1',
    description='Elasticsearch query Prometheus exporter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/braedon/prometheus-es-exporter',
    author='Braedon Vickers',
    author_email='braedon.vickers@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Monitoring',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    keywords='monitoring prometheus exporter elasticsearch',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.9',
    install_requires=[
        'click',
        'click-config-file',
        'elasticsearch >= 7.0.0, < 7.11',
        'jog',
        'prometheus-client >= 0.6.0',
    ],
    entry_points={
        'console_scripts': [
            'prometheus-es-exporter=prometheus_es_exporter:main',
        ],
    },
)
