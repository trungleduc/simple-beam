from cosapp.systems import System
from simple_beam.systems import BeamGeo, BeamMeca 


class Main(System):
    def setup(self):
        self.add_inward("maintest",0)
        self.add_child(BeamGeo("geo"))
        self.add_child(BeamMeca("meca"))
        self.connect(self.geo.outwards, self.meca.inwards, ["I", "grid"])

  