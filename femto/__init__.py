"""A comprehensive toolkit for predicting free energies"""

import importlib.metadata
import logging

import importlib.metadata
import logging
import sys


def _setup_femto_logging():
    logger = logging.getLogger("femto")

    if logger.handlers:
        # Logging is already set up — avoid adding another handler
        return

    handler = logging.StreamHandler(sys.stderr)

    formatter = logging.Formatter(
        fmt="[{levelname}]:[{name}] {asctime} {message}",
        datefmt="%Y-%m-%d %H:%M:%S",
        style="{"
    )
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)

    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False  # Prevent duplication via root logger


_setup_femto_logging()

class __FilterSimTKDeprecation(logging.Filter):
    """Disable the deprecation warning from SimTK triggered by ParmEd which spams any
    CLI output / logs."""

    def filter(self, record):  # pragma: no cover
        return "importing 'simtk.openmm' is deprecated" not in record.getMessage()


__root_logger = logging.getLogger()
__root_logger.addFilter(__FilterSimTKDeprecation())

del __root_logger
del __FilterSimTKDeprecation

try:
    __version__ = importlib.metadata.version("femto")
except importlib.metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = "0+unknown"

__all__ = ["__version__"]
