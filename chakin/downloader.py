# -*- coding: utf-8 -*-
import os

import pandas as pd
from progressbar import Bar, ETA, FileTransferSpeed, ProgressBar, Percentage, RotatingMarker
from six.moves.urllib.request import urlretrieve


def load_datasets(path=os.path.join(os.path.dirname(__file__), 'datasets.csv')):
    datasets = pd.read_csv(path)
    return datasets


def download(number=-1, name="", save_dir='./'):
    """Download pre-trained word vector
    :param number: integer, default ``None``
    :param save_dir: str, default './'
    :return: file path for downloaded file
    """
    df = load_datasets()

    if number > -1:
        row = df.iloc[[number]]
    elif name:
        row = df.loc[df["Name"] == name]

    url = ''.join(row.URL)
    if not url:
        print('The word vector you specified was not found. Please specify correct name.')

    widgets = ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets)

    def dlProgress(count, blockSize, totalSize):
        if pbar.max_value is None:
            pbar.max_value = totalSize
            pbar.start()

        pbar.update(min(count * blockSize, totalSize))

    file_name = url.split('/')[-1]
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    save_path = os.path.join(save_dir, file_name)
    path, _ = urlretrieve(url, save_path, reporthook=dlProgress)
    pbar.finish()
    return path


def search(lang=''):
    """Search pre-trained word vectors by their language
    :param lang: str, default ''
    :return: None
        print search result as pandas DataFrame
    """
    df = load_datasets()
    if lang == '':
        print(df[['Name', 'Dimension', 'Corpus', 'VocabularySize', 'Method', 'Language', 'Author']])
    else:
        rows = df[df.Language==lang]
        print(rows[['Name', 'Dimension', 'Corpus', 'VocabularySize', 'Method', 'Language', 'Author']])
