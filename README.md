# chakin
**chakin** is a downloader of pre-trained word vectors.
Word vectors are very important for many natural language processing tasks such as document classification, 
named entity recognition, question answering and so on. 
In such tasks, you can use the pre-trained word vectors  many people have published.
But it is troublesome that you find and download them by yourself. 
This library lets you download pre-trained word vectors without troublesome work.


# Install

```commandline
pip install chakin
```

# Download pre-trained vectors
You can download pre-trained word vectors as follows:

```python
>>> import chakin

>>> chakin.search(lang='en')
>>> chakin.download('en-fastText')
```

# Supported vectors
