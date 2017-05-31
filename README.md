# chakin
**chakin** is a downloader for pre-trained word vectors. [Supported many vectors](#supported-vectors)

This library lets you download pre-trained word vectors without troublesome work.
<div align="center">
  <img src="https://github.com/chakki-works/chakin/blob/master/docs/top.jpg?raw=true"><br>
</div>

-----------------

<!--
Word vectors are very important for many natural language processing tasks such as document classification, 
named entity recognition, question answering and so on. 
In such tasks, you can use the pre-trained word vectors  many people have published.
But it is troublesome that you find and download them by yourself. 

-->


# Installation
To install chakin, simply:

```shell
$ pip install chakin
```

# Usage
You can download pre-trained word vectors as follows:

```shell
$ python
```

```python
>>> import chakin
>>> chakin.search(lang='English')
                   Name  Dimension                     Corpus VocabularySize  
2          fastText(en)        300                  Wikipedia           2.5M   
11         GloVe.6B.50d         50  Wikipedia+Gigaword 5 (6B)           400K   
12        GloVe.6B.100d        100  Wikipedia+Gigaword 5 (6B)           400K   
13        GloVe.6B.200d        200  Wikipedia+Gigaword 5 (6B)           400K   
14        GloVe.6B.300d        300  Wikipedia+Gigaword 5 (6B)           400K   
15       GloVe.42B.300d        300          Common Crawl(42B)           1.9M   
16      GloVe.840B.300d        300         Common Crawl(840B)           2.2M   
17    GloVe.Twitter.25d         25               Twitter(27B)           1.2M   
18    GloVe.Twitter.50d         50               Twitter(27B)           1.2M   
19   GloVe.Twitter.100d        100               Twitter(27B)           1.2M   
20   GloVe.Twitter.200d        200               Twitter(27B)           1.2M   
21  word2vec.GoogleNews        300          Google News(100B)           3.0M 

>>> chakin.download(number=2, save_dir='./') # select fastText(en)
Test: 100% ||               | Time: 0:00:02  60.7 MiB/s
'./wiki.en.vec'
```

# Supported vectors
So far, chakin supports following word vectors:

| Name                | Dimension | Corpus                    | VocabularySize | Method   | Language   |
|---------------------|-----------|---------------------------|----------------|----------|------------|
| fastText(ar)        | 300       | Wikipedia                 | 610K           | fastText | Arabic     |
| fastText(de)        | 300       | Wikipedia                 | 2.3M           | fastText | German     |
| fastText(en)        | 300       | Wikipedia                 | 2.5M           | fastText | English    |
| fastText(es)        | 300       | Wikipedia                 | 985K           | fastText | Spanish    |
| fastText(fr)        | 300       | Wikipedia                 | 1.2M           | fastText | French     |
| fastText(it)        | 300       | Wikipedia                 | 871K           | fastText | Italian    |
| fastText(ja)        | 300       | Wikipedia                 | 580K           | fastText | Japanese   |
| fastText(ko)        | 300       | Wikipedia                 | 880K           | fastText | Korean     |
| fastText(pt)        | 300       | Wikipedia                 | 592K           | fastText | Portuguese |
| fastText(ru)        | 300       | Wikipedia                 | 1.9M           | fastText | Russian    |
| fastText(zh)        | 300       | Wikipedia                 | 330K           | fastText | Chinese    |
| GloVe.6B.50d        | 50        | Wikipedia+Gigaword 5 (6B) | 400K           | GloVe    | English    |
| GloVe.6B.100d       | 100       | Wikipedia+Gigaword 5 (6B) | 400K           | GloVe    | English    |
| GloVe.6B.200d       | 200       | Wikipedia+Gigaword 5 (6B) | 400K           | GloVe    | English    |
| GloVe.6B.300d       | 300       | Wikipedia+Gigaword 5 (6B) | 400K           | GloVe    | English    |
| GloVe.42B.300d      | 300       | Common Crawl(42B)         | 1.9M           | GloVe    | English    |
| GloVe.840B.300d     | 300       | Common Crawl(840B)        | 2.2M           | GloVe    | English    |
| GloVe.Twitter.25d   | 25        | Twitter(27B)              | 1.2M           | GloVe    | English    |
| GloVe.Twitter.50d   | 50        | Twitter(27B)              | 1.2M           | GloVe    | English    |
| GloVe.Twitter.100d  | 100       | Twitter(27B)              | 1.2M           | GloVe    | English    |
| GloVe.Twitter.200d  | 200       | Twitter(27B)              | 1.2M           | GloVe    | English    |
| word2vec.GoogleNews | 300       | Google News(100B)         | 3.0M           | word2vec | English    |
| word2vec.Wiki-NEologd.50d | 50  | Wikipedia                 | 335K           | word2vec + NEologd | Japanese |
