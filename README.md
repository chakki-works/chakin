# chakin
<div align="center">
  <img src="https://github.com/chakki-works/chakin/blob/master/docs/top.jpg?raw=true"><br><br>
</div>

-----------------

**chakin** is a downloader for pre-trained word vectors.
Word vectors are very important for many natural language processing tasks such as document classification, 
named entity recognition, question answering and so on. 
In such tasks, you can use the pre-trained word vectors  many people have published.
But it is troublesome that you find and download them by yourself. 
**This library lets you download pre-trained word vectors without troublesome work.**


# Installation

```shell
$ pip install chakin
```

# Download pre-trained vectors
You can download pre-trained word vectors as follows:

```shell
$ python
```

```python
>>> import chakin
>>> chakin.search(lang='en')
          Name Lang    Method
0  en-fastText   en  fastText

>>> chakin.download(name='en-fastText', save_path='model.vec')
```

# Supported vectors
So far, chakin supports following word vectors:


* fastText

|  |  |  |  |
|---|---|---|---|
| Arabic  | Chinese  | English  | French  |
| German  | Italian  | Japanese  | Korean  |
| Portuguese  | Russian  | Spanish  |   |
