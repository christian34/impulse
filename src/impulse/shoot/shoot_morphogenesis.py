""" Simple carbon-responsive plant morphogenesis model"""

import os
from openalea.lpy import Lsystem, AxialTree
from openalea.mtg.io import lpy2mtg,mtg2lpy

lsysdir = os.path.dirname(__file__)

def shoot_init(carbon_seed_stock=0.1):
    lsys = Lsystem(str(os.path.join(lsysdir, 'morphogenesis.lpy')), {'carbon_seed_stock': carbon_seed_stock})
    axialtree = lsys.axiom
    scene = lsys.sceneInterpretation(axialtree)
    return lpy2mtg(axialtree, lsys, scene)

def shoot_grow(g, demand_only=True):
    lsys = Lsystem(str(os.path.join(lsysdir, 'morphogenesis.lpy')))
    lsys.axiom = mtg2lpy(g, lsys, AxialTree())
    axt = lsys.iterate()
    scene = lsys.sceneInterpretation(axt)
    return lpy2mtg(axt, lsys, scene)