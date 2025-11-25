"""
# `spectralio`

I/O operations for working with spectral data in python.

---

## Implemented File Types
- .rawspec
- .pntspec
- .geospec
- .specgrp
- .spcub
- .geospcub
- .wvl
"""

from .reading import (
    read_spec1D,
    read_group,
    read_spec3D,
    read_wvl,
    read_geodata,
)
from .writing import (
    write_spec1D,
    write_group,
    write_spec3D,
    write_wvl,
    write_geodata,
)

__all__ = [
    "read_spec1D",
    "read_group",
    "read_spec3D",
    "read_wvl",
    "read_geodata",
    "write_spec1D",
    "write_group",
    "write_spec3D",
    "write_wvl",
    "write_geodata",
]
