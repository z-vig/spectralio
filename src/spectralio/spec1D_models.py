# Standard Libraries
from enum import StrEnum
from typing import Literal

# Dependencies
from pydantic import BaseModel, Field
import numpy as np

# Relative Imports
from .geospatial_models import PointGeolocation, PointModel
from .wvl_models import WvlModel

type Spec1DFileLiteral = Literal["rawspec"] | Literal["pntspec"] | Literal[
    "geospec"
]


class Spec1DFileTypes(StrEnum):
    RAW = ".rawspec"
    PNT = ".pntspec"
    GEO = ".geospec"


class Spectrum1D(BaseModel):
    """
    Object representing a single spectrum.

    Attributes
    ----------
    name: str
        Name of the spectrum.
    spectrum: list[float]
        Data of the spectrum (e.g. Reflectance, Emissivity, Transmittance)
    wavelength: WvlModel
        Wavelength Object corresponding to the spectrum.

    Notes
    -----
    See wvl_models.py for information on the Wavelength Object.
    """

    name: str
    spectrum: list[float]
    wavelength: WvlModel
    bbl_applied: bool = Field(default=False)

    def applybbl(self):
        self.spectrum = list(np.asarray(self.spectrum)[self.wavelength.bbl])
        self.bbl_applied = True


class PointSpectrum1D(Spectrum1D):
    """
    Object representing a spectrum pulled from a non-georeferenced spectral
    cube.

    Attributes
    ----------
    name: str
        Name of the spectrum.
    spectrum: list[float]
        Data of the spectrum (e.g. Reflectance, Emissivity, Transmittance)
    wavelength: WvlModel
        Wavelength Object corresponding to the spectrum.
    point: PointModel
        Just a standard X, Y ordered pair object.

    Notes
    -----
    See wvl_models.py for information on the Wavelength Object.
    See geospatial_models.py for information on the PointModel Object.
    """

    pixel: PointModel


class GeoSpectrum1D(Spectrum1D):
    """
    Object representing a spectrum pulled from a non-georeferenced spectral
    cube.

    Attributes
    ----------
    name: str
        Name of the spectrum.
    spectrum: list[float]
        Data of the spectrum (e.g. Reflectance, Emissivity, Transmittance)
    wavelength: WvlModel
        Wavelength Object corresponding to the spectrum.
    point: PointGeolocation
        Just a standard X, Y ordered pair object.

    Notes
    -----
    See wvl_models.py for information on the Wavelength Object.
    See geospatial_models.py for information on the PointModel Object.
    """

    point: PointGeolocation

    def location_str(self) -> str:
        """Returns a formatted string of location data."""
        return (
            f"({self.point.pixel_point.y}, {self.point.pixel_point.x})  --> "
            f"({self.point.map_point.y:.2f}, {self.point.map_point.y:.2f})"
        )

    def map_location(self) -> tuple[float, float]:
        """Returns a tuple containing the map point (y, x)"""
        return (self.point.map_point.y, self.point.map_point.x)

    def pixel_location(self) -> tuple[float, float]:
        """Returns a tuple containing the pixel point (x, y)"""
        return (self.point.pixel_point.x, self.point.pixel_point.y)
