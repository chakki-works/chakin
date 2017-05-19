# -*- coding: utf-8 -*-
import os
import urllib.request

import pandas as pd
from progressbar import Bar, ETA, FileTransferSpeed, ProgressBar, Percentage, RotatingMarker


def load_datasets(path=os.path.join(os.path.dirname(__file__), 'datasets.csv')):
    datasets = pd.read_csv(path)
    return datasets


def download(name='en-fastText', save_path='./words.vec'):
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

    urllib.request.urlretrieve(url, save_path, reporthook=dlProgress)
    pbar.finish()


def search(lang=''):
    df = load_datasets()
    if lang == '':
        print(df[['Name', 'Lang', 'Method']])
    else:
        rows = df[df.Lang==lang]
        print(rows[['Name', 'Lang', 'Method']].head(n=30))
