#!/usr/bin/env python3

"""
Implement a method named get_page that takes two integer
arguments page with default value 1 and page_size
with default value 10.
"""

import csv
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function index_range
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        return the correct page of the dataset
        """
        assert isinstance(page, int) and page > 0, \
            "page must be > 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be > 0"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset) or start_index < 0:
            return []

        return dataset[start_index:end_index]
