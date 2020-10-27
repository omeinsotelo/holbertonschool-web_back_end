#!/usr/bin/env python3
"""
Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    Returns the sum in floats of the mix list.
    """
    return sum(mxd_lst)
