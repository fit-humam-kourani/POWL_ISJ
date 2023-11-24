from graphviz import Digraph
from enum import Enum
from pm4py.util import exec_utils
from typing import Optional, Dict, Any
from pm4py.visualization.common import gview
from pm4py.visualization.common import save as gsave
from pm4py.visualization.ocel.eve_to_obj_types.variants import graphviz
from pm4py.objects.ocel.obj import OCEL


class Variants(Enum):
    GRAPHVIZ = graphviz


def apply(ocel: OCEL, variant=Variants.GRAPHVIZ,
          parameters: Optional[Dict[Any, Any]] = None) -> Digraph:
    """
    Shows the relationships between the different event and object types of the
    object-centric event log.

    Minimum viable example:

        import pm4py
        from pm4py.visualization.ocel.eve_to_obj_types import visualizer

        ocel = pm4py.read_ocel('tests/input_data/ocel/example_log.jsonocel')
        gviz = visualizer.apply(ocel)
        visualizer.view(gviz)

    Parameters
    ---------------
    ocel
        Object-centric event log
    parameters
        Variant-specific parameters

    Returns
    --------------
    gviz
        Graphviz object
    """
    return exec_utils.get_variant(variant).apply(ocel, parameters=parameters)


def save(gviz: Digraph, output_file_path: str, parameters=None):
    """
    Save the diagram

    Parameters
    -----------
    gviz
        GraphViz diagram
    output_file_path
        Path where the GraphViz output should be saved
    """
    gsave.save(gviz, output_file_path, parameters=parameters)


def view(gviz: Digraph, parameters=None):
    """
    View the diagram

    Parameters
    -----------
    gviz
        GraphViz diagram
    """
    return gview.view(gviz, parameters=parameters)


def matplotlib_view(gviz: Digraph, parameters=None):
    """
    Views the diagram using Matplotlib

    Parameters
    ---------------
    gviz
        Graphviz
    """

    return gview.matplotlib_view(gviz, parameters=parameters)