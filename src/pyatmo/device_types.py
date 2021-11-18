"""Deifinitions of Netatmo devices types."""
from __future__ import annotations

import logging
from enum import Enum

LOG = logging.getLogger(__name__)

# pylint: disable=W0613,R0201


class NetatmoDeviceType(Enum):
    """Class to represent Netatmo device types."""

    # temporarily disable locally-disabled and locally-enabled
    # pylint: disable=I0011,C0103

    # Climate/Energy
    NRV = "NRV"  # Smart valve
    NATherm1 = "NATherm1"  # Smart thermostat
    OTM = "OTM"  # OpenTherm modulating thermostat
    NAPlug = "NAPlug"  # Relay
    OTH = "OTH"  # OpenTherm relay

    # Cameras/Security
    NOC = "NOC"  # Smart Outdoor Camera (with Siren)
    NACamera = "NACamera"  # Smart Indoor Camera
    NSD = "NSD"  # Smart Smoke Detector
    NIS = "NIS"  # Smart Indoor Siren
    NACamDoorTag = "NACamDoorTag"  # Smart Door and Window Sensors

    # Weather
    NAMain = "NAMain"  # Smart Home Weather Station
    NAModule1 = "NAModule1"
    NAModule2 = "NAModule2"
    NAModule3 = "NAModule3"
    NAModule4 = "NAModule4"

    # Home Coach
    NHC = "NHC"  # Smart Indoor Air Quality Monitor

    # pylint: enable=I0011,C0103