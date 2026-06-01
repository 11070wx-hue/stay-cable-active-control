"""Compatibility wrapper for the first public Python model module.

New code should import from :mod:`stay_cable_control`. This module remains so
early users can keep existing scripts that import ``src/python/cable_model.py``.
"""

from stay_cable_control.models import CableParameters, cable_state_rhs, linear_state_matrix

__all__ = ["CableParameters", "cable_state_rhs", "linear_state_matrix"]
