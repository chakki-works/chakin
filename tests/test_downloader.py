# -*- coding: utf-8 -*-
import os
import unittest.case

import pandas as pd

from chakin.downloader import load_datasets, download


class TestDownloader(unittest.TestCase):

    name = 'word2vec.Wiki-NEologd.50d'
    number = 22  # 'word2vec.Wiki-NEologd.50d'

    def test_load_datasets(self):
        datasets = load_datasets()
        self.assertIsInstance(datasets, pd.DataFrame)

    def test_download_default(self):
        path = download(number=self.number)
        self.assertTrue(os.path.exists(path))
        os.remove(path)

    def test_download_by_name(self):
        path = download(name=self.name)
        self.assertTrue(os.path.exists(path))
        os.remove(path)

    def test_download_dir(self):
        dir_name = 'data'
        path = download(number=self.number, save_dir=dir_name)
        self.assertTrue(os.path.exists(path))
        os.remove(path)
        os.rmdir(dir_name)

    def test_download_nest_dir(self):
        dir_name = 'data/ja'
        path = download(number=self.number, save_dir=dir_name)
        self.assertTrue(os.path.exists(path))
        os.remove(path)
        os.removedirs(dir_name)
