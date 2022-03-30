# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 23:28:59 2022

@author: dasgu
"""
import pychrono as chrono
from pychrono import irrlicht as chronoirr
import numpy as np
import math
import os
import math
import time
import sys, getopt
import pychrono.postprocess as postprocess
import pychrono.vehicle as veh
chrono.SetChronoDataPath(r"C:\Users\dasgu\Documents\chrono_rl\rotary_leg\rl_shapes")
m_filename = "rl.py"
m_timestep = 0.01
m_length = 1.0
m_visualization = "irrlicht"
m_datapath = ""

class Model(object):
    def __init__(self,render):
       self.tire_rad = 0.8
       self.tire_vel_z0 = -3
       self.tire_center = chrono.ChVectorD(0, 0.02 + self.tire_rad, -1.5)
       self.tire_w0 = self.tire_vel_z0 / self.tire_rad
       self.mysystem = chrono.ChSystemSMC()
       self.ground = chrono.ChBody()
       self.ground.SetBodyFixed(True)
       self.m_absfilename = os.path.abspath(m_filename)
       self.m_modulename = os.path.splitext(self.m_absfilename)[0]
       chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.05)
       chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.05)
       self.exported_items = chrono.ImportSolidWorksSystem(self.m_modulename)
       self.it = []
       for my_item1 in self.exported_items:
           self.it.append(my_item1)
           for my_item in self.exported_items:
               self.mysystem.Add(my_item)
       self.terrain = veh.SCMDeformableTerrain(self.mysystem)
       self.terrain.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(0,-0.55,0), chrono.Q_from_AngX(-math.pi/2)))
       self.terrain.Initialize(4.0, 12.0, 0.004)
       self.terrain.SetSoilParameters(0.2e6,  # Bekker Kphi
                               0,      # Bekker Kc
                               1.1,    # Bekker n exponent
                               0,      # Mohr cohesive limit (Pa)
                               30,     # Mohr friction limit (degrees)
                               0.01,   # Janosi shear coefficient (m)
                               4e9,    # Elastic stiffness (Pa/m), before plastic yield, must be > Kphi
                               3e1     # Damping (Pa s/m), proportional to negative vertical speed (optional)
                               )
       self.terrain.SetPlotType(veh.SCMDeformableTerrain.PLOT_PRESSURE, 0, 30000.2)
       self.my_solver = chrono.ChSolverBB()
       self.mysystem.SetSolver(self.my_solver)
       self.my_solver.SetMaxIterations(6000)
       self.my_solver.EnableWarmStart(True);
       self.mysystem.Set_G_acc(chrono.ChVectorD(0,-9.8,0))
       self.myapplication = chronoirr.ChIrrApp(self.mysystem, 'Deformable soil', chronoirr.dimension2du(1280,720), False, True)
       self.myapplication.AddTypicalSky()
       self.myapplication.AddTypicalCamera(chronoirr.vector3df(2.0,1.4,0.0), chronoirr.vector3df(0,self.tire_rad,0))
       self.myapplication.AddTypicalLights()
       self.myapplication.AddLightWithShadow(chronoirr.vector3df(1.5,5.5,-2.5),    # point
                                 chronoirr.vector3df(0,0,0),           # aim point
                                 3,                                    # radius (power)
                                 2.2, 7.2,                             # near, far
                                 40,                                   # angle of FOV
                                 512,                                  # resoluition
                                 chronoirr.SColorf(0.8,0.8,1))         # light color
       self.myapplication.AssetBindAll()
       self.myapplication.AssetUpdateAll()
       self.myapplication.AddShadowAll()
    
    def reset(self):
        self.isdone = False
        self.mysystem.Clear()
        self.ground.SetBodyFixed(True)
        self.m_absfilename = os.path.abspath(m_filename)
        self.m_modulename = os.path.splitext(self.m_absfilename)[0]
        chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.05)
        chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.05)
        self.exported_items = chrono.ImportSolidWorksSystem(self.m_modulename)
        self.it = []
        for my_item1 in self.exported_items:
            self.it.append(my_item1)
            for my_item in self.exported_items:
                self.mysystem.Add(my_item)
        self.terrain = veh.SCMDeformableTerrain(self.mysystem)
        self.terrain.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(0,-0.55,0), chrono.Q_from_AngX(-math.pi/2)))
        self.terrain.Initialize(4.0, 12.0, 0.004)
        self.terrain.SetSoilParameters(0.2e6,  # Bekker Kphi
                                0,      # Bekker Kc
                                1.1,    # Bekker n exponent
                                0,      # Mohr cohesive limit (Pa)
                                30,     # Mohr friction limit (degrees)
                                0.01,   # Janosi shear coefficient (m)
                                4e9,    # Elastic stiffness (Pa/m), before plastic yield, must be > Kphi
                                3e1     # Damping (Pa s/m), proportional to negative vertical speed (optional)
                                )
        self.terrain.SetPlotType(veh.SCMDeformableTerrain.PLOT_PRESSURE, 0, 30000.2)
        self.my_solver = chrono.ChSolverBB()
        self.mysystem.SetSolver(self.my_solver)
        self.my_solver.SetMaxIterations(6000)
        self.my_solver.EnableWarmStart(True);
        self.mysystem.Set_G_acc(chrono.ChVectorD(0,-9.8,0))
        self.myapplication = chronoirr.ChIrrApp(self.mysystem, 'Deformable soil', chronoirr.dimension2du(1280,720), False, True)
        self.myapplication.AddTypicalSky()
        self.myapplication.AddTypicalCamera(chronoirr.vector3df(2.0,1.4,0.0), chronoirr.vector3df(0,self.tire_rad,0))
        self.myapplication.AddTypicalLights()
        self.myapplication.AddLightWithShadow(chronoirr.vector3df(1.5,5.5,-2.5),    # point
                                  chronoirr.vector3df(0,0,0),           # aim point
                                  3,                                    # radius (power)
                                  2.2, 7.2,                             # near, far
                                  40,                                   # angle of FOV
                                  512,                                  # resoluition
                                  chronoirr.SColorf(0.8,0.8,1))         # light color
        self.myapplication.AssetBindAll()
        self.myapplication.AssetUpdateAll()
        self.myapplication.AddShadowAll()
        self.steps = 0
        return
    
    def step(self):
        self.steps += 1
        self.myapplication.BeginScene()
        self.myapplication.DrawAll()
        self.myapplication.DoStep()
        self.myapplication.EndScene()
        self.rew = 1.0
        return 
        
        



       





        