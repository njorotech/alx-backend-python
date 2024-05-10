#!/usr/bin/env python3
"""Complex types - mixed list"""

from typing import List, Union

mxd_lst: List[Union[int, str]]


def sum_mixed_list(mxd_lst) -> float:
    """
    A type-annotated function sum_mixed_list which takes a list mxd_lst of
    integers and floats and returns their sum as a float.
    """

    return float(sum(mxd_lst))
