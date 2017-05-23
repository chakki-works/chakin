# -*- coding: utf-8 -*-
import os
import urllib.request

import pandas as pd
from progressbar import Bar, ETA, FileTransferSpeed, ProgressBar, Percentage, RotatingMarker


def load_datasets(path=os.path.join(os.path.dirname(__file__), 'datasets.csv')):
    datasets = pd.read_csv(path)
    return datasets


def download(name, save_dir='./'):
    df = load_datasets()
    row = df[df.Name==name]
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
    save_path = os.path.join(save_dir, file_name)
    urllib.request.urlretrieve(url, save_path, reporthook=dlProgress)
    pbar.finish()


def search(lang=''):
    df = load_datasets()
    if lang == '':
        print(df[['Name', 'Dimension', 'Corpus', 'VocabularySize', 'Method', 'Language', 'Author']])
    else:
        rows = df[df.Language==lang]
        print(rows[['Name', 'Dimension', 'Corpus', 'VocabularySize', 'Method', 'Language', 'Author']])
