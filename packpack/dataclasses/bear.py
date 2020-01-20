from pymc3.model import PyMC3Variable
from dataclasses import dataclass


@dataclass
class Bear:
    """Bear threat"""

    sight: PyMC3Variable
    smell: PyMC3Variable
