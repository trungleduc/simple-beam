"""CoSApp project Simple beam

CoSApp mechanical modelling of beam
"""
from ._version import __version__


def find_resources(filename: str = "") -> str:
    """Returns the fullpath of a file in resources folder.
    
    Parameters
    ----------
    filename: str, optional
        File or directory looked for; default resources folder
    
    Returns
    -------
    str
        Full path to resources
    """
    import os
    fullpath = os.path.realpath(os.path.join(__path__[0], "resources", filename))
    if not os.path.exists(fullpath):
        raise FileNotFoundError(fullpath)
    return fullpath


from simple_beam import tools, ports, systems, drivers

__all__ = ["drivers", "ports", "systems", "tools"]


def _cosapp_lab_load_module(*args):
    """
    Function to initialize interface.
    """
    from simple_beam.systems import Main     
    from cosapp_lab.widgets import SysExplorer
    main = Main("main")
    main.run_drivers()
    a = SysExplorer( main, anchor = "tab-after", template = find_resources("simple_beam.json"))

def _cosapp_lab_module_meta():
    """
    Meta-data for CoSApp Lab interface.
    """
    return {"title": "Simple beam modelling", "description": "A simple mechanical model of beams implemented in CoSApp"}