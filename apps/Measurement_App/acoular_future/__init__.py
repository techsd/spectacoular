# coding=UTF-8
#------------------------------------------------------------------------------
# Copyright (c) 2019, Acoular Development Team.
#------------------------------------------------------------------------------

"""
Plugin classes for acoular to be used with spectacoular
"""

from .spectra import SpectraInOut, CSMInOut, PowerSpectraSetCSM
from .tbeamform import BeamformerFreqTime
from .fastFuncs import handle_dynamic_acoustic_conditions, handle_acoustic_conditions_claps_explosions, handle_acoustic_conditions_engines, handle_acoustic_conditions_voices, handle_acoustic_conditions_non_natural_sounds

__all__ = [
    'SpectraInOut',
    'CSMInOut',
    'PowerSpectraSetCSM',
    'BeamformerFreqTime',
    'handle_dynamic_acoustic_conditions',
    'handle_acoustic_conditions_claps_explosions',
    'handle_acoustic_conditions_engines',
    'handle_acoustic_conditions_voices',
    'handle_acoustic_conditions_non_natural_sounds'
]
