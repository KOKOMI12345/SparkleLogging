from setuptools import setup, find_packages

setup(
    name='SparkleLogging',
    version='1.0.8',
    packages=find_packages(),
    author='花火official',
    author_email='3072252442@qq.com',
    description='A logging library for Python',
    long_description=open('Readme.md','r',encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KOKOMI12345/SparkleLogging',
    install_requires=[
        'requests',
        'websockets',
        'colorlog',
        'httpx',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
