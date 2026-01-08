"""Binary Search Solutions Package

Professional implementations of binary search algorithms from super30admin/Binary-Search-31.

Modules:
    problem1_optimize_routes: Amazon Prime Air route optimization
    problem2_h_index_ii: H-Index II calculation with binary search

Author: EthanThePhoenix38
Date: 2026-01-08
"""

__version__ = "1.0.0"
__author__ = "EthanThePhoenix38"

from .problem1_optimize_routes import optimize_air_routes
from .problem2_h_index_ii import h_index

__all__ = [
    "optimize_air_routes",
    "h_index",
]
