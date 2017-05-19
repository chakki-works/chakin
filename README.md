# chakin
<div align="center">
  <img src="https://github.com/chakki-works/chakin/tree/master/docs/top.jpg"><br><br>
</div>

-----------------

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
          Name Lang    Method
0  en-fastText   en  fastText
1  ja-fastText   ja  fastText

>>> chakin.download(name='en-fastText', save_path='model.vec')
```

# Supported vectors
