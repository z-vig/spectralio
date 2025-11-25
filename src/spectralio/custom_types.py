# Standard Library
from typing import Literal
from pathlib import Path
import os

type WvlUnit = Literal["nm", "um", "m", "v"]
type PathLike = str | Path | os.PathLike
