import os

import pm4py
from pm4py.algo.discovery.powl.inductive.variants.powl_discovery_varaints import POWLDiscoveryVariant as Variants


def execute_script():
    log = pm4py.read_xes("../tests/compressed_input_data/13_SEPSIS_1t_per_variant.xes.gz")

    # discovery
    powl_model = pm4py.discover_powl(log,
                                     variant=Variants.DYNAMIC_CLUSTERING,
                                     order_graph_filtering_threshold=0.8)

    # visualization with frequency tags
    pm4py.view_powl(powl_model)

    # visualization with frequency tags and decision gates
    pm4py.view_powl_net(powl_model)

    # export as Workflow Net
    petri_net, initial_marking, final_marking = pm4py.convert_to_petri_net(powl_model)
    pm4py.view_petri_net(petri_net, initial_marking, final_marking)
    pm4py.write_pnml(petri_net, initial_marking, final_marking, os.path.join("../models", "wf_net.pnml"))

    # export as BPMN
    bpmn = pm4py.convert_to_bpmn(powl_model)
    pm4py.view_bpmn(bpmn)
    pm4py.write_bpmn(bpmn, os.path.join("../models", "bpmn_graph.bpmn"))


if __name__ == "__main__":
    execute_script()
