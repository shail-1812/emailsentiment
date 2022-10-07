import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='emailsentiment',
    version='0.0.1',
    author='Shail Patel',
    author_email='shailpatel1812@gmail.com',
    description='Sentiment analysis on emails',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/shail-1812/emailsentiment.git',
    packages=['emailsentiment'],
    install_requires=['kera_preprocessing', 'spacy', 'nlppreprocess'],
)