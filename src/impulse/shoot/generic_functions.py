# -*- coding: latin-1 -*-
import math


def carbon_acquisition(PAR, nitrogen, area):
    """
    A model of carbon acquisition: Farquhar, RUE, hyperbolic models...
    """
    SLN = nitrogen / area
    Pm = (2 / (1 + math.exp(-1.2 * (SLN - 1))) - 1) * 25
    calculated_carbon_acquisition = (1/1.5) * (0.045 * PAR + Pm - ((0.045 * PAR) ** 2 - 0.0135 * PAR * Pm) ** 0.5)
    return calculated_carbon_acquisition * area


def respiration(area, temperature):
    """
    Maintenance respiration
    """
    maintenance_respiration = 0.3 * 2.5 * area * 2 ** (temperature - 25) / 10
    return maintenance_respiration


def senescence(nitrogen, area, PAR, carbon):
    """ """
    carbon_remobilisation = 0
    nitrogen_remobilisation = 0

    if (nitrogen / area) * PAR < 100:
        area = 0
        carbon_remobilisation = carbon
        nitrogen_remobilisation = nitrogen

    return area, carbon_remobilisation, nitrogen_remobilisation


def plant_net_C(plant_carbon_acquisition, plant_respiration, plant_carbon_remobilisation):
    """Calculate plant net C """
    return plant_carbon_acquisition - plant_respiration + plant_carbon_remobilisation


def carbon_allocation(organ_potential_demand, plant_potential_demand, plant_net_C):
    """ Allocation C for each organ including roots"""

    return plant_net_C * (organ_potential_demand / plant_potential_demand)


def nitrogen_allocation(organ_transpiration, plant_transpiration, plant_nitrogen_influx):
    """Allocation of N according to transpiration"""
    return plant_nitrogen_influx * (organ_transpiration / plant_transpiration)


def nitrogen_influx_from_roots(conc_nitrates_roots, plant_transpiration):
    conc_nitrates_roots * (plant_transpiration / (plant_transpiration + 1))