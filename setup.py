from setuptools import setup


setup(
    name = "chakin",
    version = "0.0.5",
    description = "Downloader for pre-trained word vectors",
    keywords = ["machine learning", "natural language processing", "word embeddings", "downloader"],
    author = "Hironsan",
    author_email = "hiroki.nakayama.py@gmail.com",
    license="MIT",
    packages = [
        "chakin",
        ],
    url = "https://github.com/chakki-works/chakin",
    install_requires=[
        "pandas>=0.20.1",
        "progressbar2>=3.20.0",
        "six>=1.10.0"
    ],
    package_data={
        '': ['*.csv'],
    }
)