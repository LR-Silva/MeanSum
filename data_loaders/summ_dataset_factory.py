# summ_dataset_factory.py

"""
Class to create SummDataset instances.

In part here in a separate file to avoid circular imports
"""

from .amazon_dataset import AmazonDataset
from .yelp_dataset import YelpDataset


class SummDatasetFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def get(name):
        if name == 'amazon':
            return AmazonDataset()
        elif name == 'yelp':
            return YelpDataset()
