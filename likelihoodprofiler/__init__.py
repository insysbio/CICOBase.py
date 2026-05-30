"""Compatibility import path for the former ``likelihoodprofiler`` package.

New code should import from ``cicobase``.
"""

import importlib
import sys

from cicobase import *  # noqa: F401,F403

_SUBMODULES = (
    "cico_one_pass",
    "get_endpoint",
    "get_interval",
    "get_right_endpoint",
    "get_right_endpoint_by_lin_extrapol",
    "method_quadr_extrapol",
    "profile",
    "structures",
    "support_math_func",
)

for _name in _SUBMODULES:
    sys.modules[f"{__name__}.{_name}"] = importlib.import_module(f"cicobase.{_name}")

del importlib, sys, _name
