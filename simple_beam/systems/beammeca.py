from cosapp.systems import System
import numpy as np

class BeamMeca(System):
    def setup(self):
        
        self.add_inward('E', 270, desc = "Young modulus",  valid_range = [100,150],limits = [50,200])
        self.add_inward("grid", np.zeros(101), valid_range = [2,4],limits = [-np.inf,10] )
        self.add_inward("I", 1., desc='Second area moment' )
        self.add_inward("force", -1., desc='Force value', unit = 'N' )
        self.add_inward("position", 0.5, desc="force relative position",limits= [0.2,0.3], valid_range = [0.1,0.8] )
        self.add_outward("M", np.zeros(1), desc = "Bending moments" )
        self.add_outward("Q", np.zeros(1), desc = "Shear forces" )
        self.add_outward("W", np.zeros(1), desc = "Deflections" )
        self.add_outward("maxW", 0, desc = "Max deflections" )
        self.add_outward("f_position", 0.5, desc="force  position")
        self.add_outward("maxW_loc", 0, desc = "Max deflections location" )
    def compute(self):

        if self.position > 1.:
            position = 0.99
        elif self.position < 0:
            position = 0.
        else:
            position = self.position
        mesh_size = len(self.grid)
        L = self.grid[-1]
        b = (1.- position)*L
        a = position*L
        M =[]
        Q = []
        W = []
        for i in range(0, int(mesh_size*position)):
            x = self.grid[i]
            M.append(self.force*b*x/L)
            Q.append(self.force*b/L)
            W.append(self.force*b*x*(L**2 - b**2 - x**2)/(6*L*self.E*self.I))  
        for j in range(int(mesh_size*position), mesh_size):
            x = self.grid[j]
            M.append(self.force*a*(L - x)/L)
            Q.append(self.force*(b/L-1))
            W.append(self.force*b*x*(L**2 - b**2 - x**2)/(6*L*self.E*self.I)+ self.force*(x-a)**3/(6*self.E*self.I))
        self.M = np.array(M)
        self.Q = np.array(Q) 
        self.W = np.array(W)
        self.maxW_loc = int(np.argmax(np.absolute(self.W)))-1
        self.maxW = self.W[self.maxW_loc]
        self.f_position = mesh_size*position