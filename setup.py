from setuptools import setup


setup(
    name = "chakin",
    version = "0.0.1",
    description = "The downloader of pre-trained word vectors",
    keywords = ["machine learning", "natural language processing", "word embeddings", "downloader"],
    author = "Hironsan",
    author_email = "hiroki.nakayama.py@gmail.com",
    license="MIT",
    packages = [
        "chakin",
        ],
    url = "https://github.com/chakki-works/chakin",
    install_requires=[
        "requests>=2.14.2",
        "pandas>=0.20.1",
    ],
)