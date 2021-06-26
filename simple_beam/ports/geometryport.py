from cosapp.ports import Port

class GeometryPort(Port):
    def setup(self):
        self.add_variable("visible", True, desc="Should this geometry be shown?")
        self.add_variable("shape", None, desc="Geometrical object")
        