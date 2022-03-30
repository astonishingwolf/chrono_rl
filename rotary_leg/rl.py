# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: 


import pychrono as chrono 
import builtins 

shapes_dir = 'rl_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('Part1-1')
body_1.SetPos(chrono.ChVectorD(0.0225,-0.18,0.0225))
body_1.SetRot(chrono.ChQuaternionD(0.707106781186548,-0.707106781186547,0,0))
body_1.SetMass(300.6982522957533)
body_1.SetInertiaXX(chrono.ChVectorD(9000.20393405498141e-05,1000.99411227791387e-05,9000.16024423683471e-05))
body_1.SetInertiaXY(chrono.ChVectorD(2000.64186085353777e-20,5000.58196256311102e-22,2000.04533596332166e-20))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.66300283576574e-17,-3.79188838442336e-17,0.0919188343911995),chrono.ChQuaternionD(1,0,0,0)))
mesh = chrono.ChTriangleMeshConnected()
mesh.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
mesh.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
material = chrono.ChMaterialSurfaceSMC()
body_1.GetCollisionModel().ClearModel()
body_1.GetCollisionModel().AddTriangleMesh(material,                # contact material
                                            mesh,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_1.GetCollisionModel().BuildModel()
body_1.SetBodyFixed(True)
body_1.SetCollide(False)

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_1.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_1)

# Rigid body part
body_2= chrono.ChBodyAuxRef()
body_2.SetName('Part1-2')
body_2.SetPos(chrono.ChVectorD(0.0775,-0.15,-0.00750000000000001))
body_2.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_1.SetMass(300.6982522957533)
body_1.SetInertiaXX(chrono.ChVectorD(9000.20393405498141e-05,1000.99411227791387e-05,9000.16024423683471e-05))
body_1.SetInertiaXY(chrono.ChVectorD(2000.64186085353777e-20,5000.58196256311102e-22,2000.04533596332166e-20))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-4.66300283576574e-17,-3.79188838442336e-17,0.0919188343911995),chrono.ChQuaternionD(1,0,0,0)))
mesh_2 = chrono.ChTriangleMeshConnected()
mesh_2.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
mesh_2.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
material_2 = chrono.ChMaterialSurfaceSMC()
body_2.GetCollisionModel().ClearModel()
body_2.GetCollisionModel().AddTriangleMesh(material_2,                # contact material
                                            mesh_2,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_2.GetCollisionModel().BuildModel()
body_2.SetBodyFixed(False)
body_2.SetCollide(False)

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_2.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_2)


# Mate constraint: Concentric1 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Part1-2 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.135,-0.15,0.0225)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(-0.08,-0.15,0.0225)
dB = chrono.ChVectorD(1,0,0)
link_1.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.135,-0.15,0.0225)
cB = chrono.ChVectorD(-0.08,-0.15,0.0225)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_2.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
exported_items.append(link_2)


# Mate constraint: Distance1 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Part1-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.055,-0.1725,0.1725)
cB = chrono.ChVectorD(0.045,0,0.045)
dA = chrono.ChVectorD(-1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_3.Initialize(body_2,body_1,False,cA,cB,dB)
link_3.SetDistance(-0.01)
link_3.SetName("Distance1")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.055,-0.1725,0.1725)
dA = chrono.ChVectorD(-1,0,0)
cB = chrono.ChVectorD(0.045,0,0.045)
dB = chrono.ChVectorD(1,0,0)
link_4.SetFlipped(True)
link_4.Initialize(body_2,body_1,False,cA,cB,dA,dB)
link_4.SetName("Distance1")
exported_items.append(link_4)


# Mate constraint: Coincident2 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)

link_5 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(6.93889390390723e-18,0,0)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,1.22464679914735e-16,-1)
dB = chrono.ChVectorD(0,0,1)
link_5.Initialize(body_1,body_0,False,cA,cB,dB)
link_5.SetDistance(0)
link_5.SetName("Coincident2")
#exported_items.append(link_5)

link_6 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(6.93889390390723e-18,0,0)
dA = chrono.ChVectorD(0,1.22464679914735e-16,-1)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,0,1)
link_6.SetFlipped(True)
link_6.Initialize(body_1,body_0,False,cA,cB,dA,dB)
link_6.SetName("Coincident2")
#exported_items.append(link_6)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0225,0,0.0225)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,1,1.22464679914735e-16)
dB = chrono.ChVectorD(0,1,0)
link_7.Initialize(body_1,body_0,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident3")
#exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0225,0,0.0225)
dA = chrono.ChVectorD(0,1,1.22464679914735e-16)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,1,0)
link_8.Initialize(body_1,body_0,False,cA,cB,dA,dB)
link_8.SetName("Coincident3")
#exported_items.append(link_8)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)

link_9 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(6.93889390390723e-18,0,0.045)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(-1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_9.Initialize(body_1,body_0,False,cA,cB,dB)
link_9.SetDistance(0)
link_9.SetName("Coincident4")
#exported_items.append(link_9)

link_10 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(6.93889390390723e-18,0,0.045)
dA = chrono.ChVectorD(-1,0,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(1,0,0)
link_10.SetFlipped(True)
link_10.Initialize(body_1,body_0,False,cA,cB,dA,dB)
link_10.SetName("Coincident4")
#exported_items.append(link_10)


# Mate constraint: Parallel2 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Part1-2 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0225,0,0.0225)
dA = chrono.ChVectorD(0,1,1.22464679914735e-16)
cB = chrono.ChVectorD(0.055,-0.1275,0.1725)
dB = chrono.ChVectorD(0,1,0)
link_11.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_11.SetName("Parallel2")
#exported_items.append(link_11)

