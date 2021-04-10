#!/usr/bin/env python
"""Top-level module for datasets"""

from .version import version as __version__

from .birddb import BIRDDB

__all__ = [
    "BIRDDB",
]
