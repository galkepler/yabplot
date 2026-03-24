import pytest
import numpy as np
import yabplot as yab
import pyvista as pv

from yabplot.plotting import _load_bmesh


# tell PyVista to run in "off-screen" mode so it doesn't try to open a real window
pv.OFF_SCREEN = True

def test_version():
    """Check that the package has a version string."""
    assert yab.__version__ is not None

def test_none_returns_empty_dict():
    result = _load_bmesh(None)
    assert result == {}

def test_dict_passthrough():
    d = {'L': 'something', 'R': 'something_else'}
    result = _load_bmesh(d)
    assert result is d 

def test_polydata_wrapped_in_both():
    mesh = pv.Sphere()
    result = _load_bmesh(mesh)
    assert 'both' in result
    assert result['both'] is mesh

def test_plotter_instantiation():
    """
    Smoke test: Can we create a Plotter without crashing?
    This verifies VTK and PyVista are correctly linked to the system display.
    """
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(pv.Sphere())
    plotter.show()
    plotter.close()

def test_plot_cortical():
    """
    Integration test: Downloads 'aparc' and plots it.
    """
    yab.plot_cortical(atlas='aparc', display_type=None)

def test_plot_subcortical():
    """
    Integration test: Downloads 'aseg' and plots it.
    """
    yab.plot_subcortical(atlas='aseg', display_type=None)

def test_plot_tracts():
    """
    Integration test: Downloads 'xtract_tiny' and plots it.
    """
    yab.plot_tracts(atlas='xtract_tiny', display_type=None)

def test_plot_vertexwise():
    """
    Integration test: plot_vertexwise with synthetic sphere meshes.
    """
    lh = pv.Sphere()
    rh = pv.Sphere()
    lh['Data'] = np.random.rand(lh.n_points)
    rh['Data'] = np.random.rand(rh.n_points)
    yab.plot_vertexwise(lh, rh, display_type=None)