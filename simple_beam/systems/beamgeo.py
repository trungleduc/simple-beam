from cosapp.systems import System
from simple_beam.ports import GeometryPort
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
import numpy as np
class BeamGeo(System):
    
    def setup(self):
        self.add_inward("file","path")
        self.add_inward("mesh_size",100)
        self.add_inward('width', 0.5, unit = 'm')
        self.add_inward('height',0.5, unit = 'm')
        self.add_inward('length', 5., unit = 'm')
        self.add_outward('I', desc='Second area moment')
        self.add_outward('grid', np.zeros(1))
        self.add_outward("section", [])
        self.add_output(GeometryPort, 'geom')
    def compute(self):
        self.I = self.width*self.height**3/12.
        self.grid = np.array([i*self.length/self.mesh_size for i in range(0,int(self.mesh_size)+1)])
        section = [[],[]]
        for i in range(0,100):
            section[0].append((- 0.5 + i/100.)*self.width)
            section[1].append(-0.5*self.height)
        for i in range(0,100):
            section[0].append(0.5*self.width)
            section[1].append((- 0.5 + i/100.)*self.height) 
        for i in range(0,100):
            section[0].append((0.5 - i/100.)*self.width)
            section[1].append(0.5*self.height)  
        for i in range(0,100):
            section[0].append( -0.5*self.width)
            section[1].append((0.5 - i/100.)*self.height)  
        self.section = section
        self.geom.shape ={
            "shape": BRepPrimAPI_MakeBox(self.length, self.width, self.height).Solid(),
            "edge": True,
            "transparent": True,
            "color": "blue"
        } 
