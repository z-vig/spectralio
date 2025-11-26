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

from .wvl_models import WvlModel
from .spec1D_models import Spectrum1D, PointSpectrum1D, GeoSpectrum1D
from .specgroup_models import SpectrumGroup
from .spec3D_models import Spectrum3D, GeoSpectrum3D

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
    "WvlModel",
    "Spectrum1D",
    "PointSpectrum1D",
    "GeoSpectrum1D",
    "SpectrumGroup",
    "Spectrum3D",
    "GeoSpectrum3D",
]
