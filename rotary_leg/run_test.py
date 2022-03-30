# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 03:07:56 2021

@author: dasgu
"""

def main():
    pass

if __name__ == '__main__':
    main()

import os
import math
import time
import sys, getopt
import pychrono as chrono
import pychrono.postprocess as postprocess
import pychrono.irrlicht as chronoirr
import pychrono.vehicle as veh
chrono.SetChronoDataPath(r"C:\Users\dasgu\Documents\chrono_rl\rotary_leg\rl_shapes")
m_filename = "rl.py"
m_timestep = 0.01
m_length = 1.0
m_visualization = "irrlicht"
m_datapath = ""

var_params = True

class MySoilParams (veh.SoilParametersCallback):
    def __init__(self):
        veh.SoilParametersCallback.__init__(self)
    def Set(self, x, y):
        if y > 0 :
            self.m_Bekker_Kphi = 0.2e6
            self.m_Bekker_Kc = 0
            self.m_Bekker_n = 1.1
            self.m_Mohr_cohesion = 0
            self.m_Mohr_friction = 30
            self.m_Janosi_shear = 0.01
            self.m_elastic_K = 4e7
            self.m_damping_R = 3e4
        else:
            self.m_Bekker_Kphi = 5301e3
            self.m_Bekker_Kc = 102e3
            self.m_Bekker_n = 0.793
            self.m_Mohr_cohesion = 1.3e3
            self.m_Mohr_friction = 31.1
            self.m_Janosi_shear = 1.2e-2
            self.m_elastic_K = 4e8
            self.m_damping_R = 3e4
tire_rad = 0.8
tire_vel_z0 = -3
tire_center = chrono.ChVectorD(0, 0.02 + tire_rad, -1.5)
tire_w0 = tire_vel_z0 / tire_rad
mysystem = chrono.ChSystemSMC()
it = []
ground = chrono.ChBody()
ground.SetBodyFixed(True)
mysystem.Add(ground)# Remove the trailing .py and add / in case of file without ./
m_absfilename = os.path.abspath(m_filename)
m_modulename = os.path.splitext(m_absfilename)[0]
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.05)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.05)
exported_items = chrono.ImportSolidWorksSystem(m_modulename)
mysystem = chrono.ChSystemSMC()
j=0
it = []
it1 = []
for my_item1 in exported_items:
    it.append(my_item1)
for my_item in exported_items:
	mysystem.Add(my_item)
for my_item in exported_items:
	print (my_item.GetName())
terrain = veh.SCMDeformableTerrain(mysystem)
terrain.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(0,-0.55,0), chrono.Q_from_AngX(-math.pi/2)))
terrain.Initialize(4.0, 12.0, 0.004)#gives us the dimension of the plane
my_params = MySoilParams()
if var_params:
    terrain.RegisterSoilParametersCallback(my_params)
else :
    terrain.SetSoilParameters(0.2e6,  # Bekker Kphi
                               0,      # Bekker Kc
                               1.1,    # Bekker n exponent
                               0,      # Mohr cohesive limit (Pa)
                               30,     # Mohr friction limit (degrees)
                               0.01,   # Janosi shear coefficient (m)
                               4e9,    # Elastic stiffness (Pa/m), before plastic yield, must be > Kphi
                               3e1     # Damping (Pa s/m), proportional to negative vertical speed (optional)
    )
terrain.SetPlotType(veh.SCMDeformableTerrain.PLOT_PRESSURE, 0, 30000.2)
my_solver = chrono.ChSolverBB()
mysystem.SetSolver(my_solver)
my_solver.SetMaxIterations(6000)
my_solver.EnableWarmStart(True);
mysystem.Set_G_acc(chrono.ChVectorD(0,-9.8,0))
if m_visualization == "irrlicht":
    myapplication = chronoirr.ChIrrApp(mysystem, 'Deformable soil', chronoirr.dimension2du(1280,720), False, True)
    myapplication.AddTypicalSky()
    #myapplication.AddTypicalLogo(chrono.GetChronoDataFile('logo_pychrono_alpha.png'))
    myapplication.AddTypicalCamera(chronoirr.vector3df(2.0,1.4,0.0), chronoirr.vector3df(0,tire_rad,0))
    myapplication.AddTypicalLights()
    myapplication.AddLightWithShadow(chronoirr.vector3df(1.5,5.5,-2.5),    # point
                                 chronoirr.vector3df(0,0,0),           # aim point
                                 3,                                    # radius (power)
                                 2.2, 7.2,                             # near, far
                                 40,                                   # angle of FOV
                                 512,                                  # resoluition
                                 chronoirr.SColorf(0.8,0.8,1))         # light color
    myapplication.AssetBindAll()
    myapplication.AssetUpdateAll()
    myapplication.AddShadowAll()
    myapplication.SetTimestep(0.1)
    while(myapplication.GetDevice().run()):
        myapplication.BeginScene()
        myapplication.DrawAll()
        myapplication.DoStep()
        myapplication.EndScene()
        