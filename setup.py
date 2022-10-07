import setuptools

setuptools.setup(
    name='emailsentiment',
    version='0.0.1',
    author='Shail Patel',
    author_email='shailpatel1812@gmail.com',
    description='Sentiment analysis on emails',
    long_description_content_type="text/markdown",
    url='https://github.com/shail-1812/emailsentiment.git',
    packages=['emailsentiment'],
    install_requires=['keras_preprocessing', 'spacy', 'nlppreprocess'],
    include_package_data=True,
    package_data={'': ['emailsentiment/*.sav', 'emailsentiment/*.pickle']},
)