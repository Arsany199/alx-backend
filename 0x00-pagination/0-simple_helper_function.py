#!/usr/bin/env python3
"""model of a function named index_range"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function that return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes"""
    return (page - 1) * page_size, page * page_size
