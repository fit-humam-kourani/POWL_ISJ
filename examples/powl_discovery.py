import copy

import pm4py
from build.lib.pm4py.algo.discovery.powl.inductive.variants.dynamic_clustering_frequency.dynamic_clustering_frequency_partial_order_cut import \
    ORDER_FREQUENCY_RATIO
from examples import examples_conf
from pm4py.algo.discovery.powl.inductive.variants.powl_discovery_varaints import POWLDiscoveryVariant
from pm4py.objects.log.obj import EventLog, Trace
from pm4py.util import xes_constants
from pm4py.visualization.powl.visualizer import POWLVisualizationVariants


def filter_activities(log, max_num_act):
    # print(len(log))
    attribute_key = xes_constants.DEFAULT_NAME_KEY
    activity_freq = {}
    for trace in log:
        trace_activities = set()
        for event in trace:
            trace_activities.add(event[attribute_key])
        for act in trace_activities:
            freq = 1
            if act in activity_freq.keys():
                freq = activity_freq[act] + 1
            activity_freq[act] = freq

    # print(activity_freq)
    activities_to_keep = sorted(activity_freq.keys(), reverse=True, key=lambda a: activity_freq[a])[:max_num_act]
    # print(activities_to_keep)

    new_log = EventLog()
    for trace in log:
        new_trace = Trace()
        for event in trace:
            act = event[attribute_key]
            if act in activities_to_keep:
                new_trace.append(copy.deepcopy(event))
        if len(new_trace) > 0:
            new_log.append(new_trace)
    # print(len(new_log))
    return new_log


def execute_script():
    # log = pm4py.read_xes("../tests/compressed_input_data/13_SEPSIS_1t_per_variant.xes.gz",
    #                      return_legacy_log_object=True)
    log = pm4py.read_xes("../tests/input_data/BPI Challenge 2017.xes.gz",
                         return_legacy_log_object=True)
    log = filter_activities(log, 8)

    powl_model = pm4py.discover_powl(log, variant=POWLDiscoveryVariant.BRUTE_FORCE)
    print(powl_model)
    v = pm4py.visualization.powl.visualizer.apply(powl_model, variant=POWLVisualizationVariants.BASIC,
                                                  parameters={"format": "svg"})
    v.view()
    v = pm4py.visualization.powl.visualizer.apply(powl_model, variant=POWLVisualizationVariants.NET,
                                                  parameters={"format": "svg"})
    v.view()
    # from pm4py.algo.discovery.powl.algorithm import apply
    # powl_model = apply(log, variant=POWLDiscoveryVariant.DYNAMIC_CLUSTERING, parameters={ORDER_FREQUENCY_RATIO: 0.8})
    # print(powl_model)
    # v = pm4py.visualization.powl.visualizer.apply(powl_model, variant=POWLVisualizationVariants.BASIC,
    #                                               parameters={"format": "svg"})
    # v.view()
    # v = pm4py.visualization.powl.visualizer.apply(powl_model, variant=POWLVisualizationVariants.NET,
    #                                               parameters={"format": "svg"})
    # v.view()
    # powl_model = pm4py.discover_powl(log, variant=POWLDiscoveryVariant.BRUTE_FORCE)
    # print(powl_model)
    # v = pm4py.visualization.powl.visualizer.apply(powl_model, variant=POWLVisualizationVariants.BASIC,
    #                                               parameters={"format": "svg"})
    # v.view()
    # v = pm4py.visualization.powl.visualizer.apply(powl_model, variant= POWLVisualizationVariants.NET, parameters={"format":"svg"})
    # v.view()

    # powl_model = pm4py.discover_powl(log, variant=POWLDiscoveryVariant.DYNAMIC_CLUSTERING)
    # v = pm4py.visualization.powl.visualizer.apply(powl_model, variant=POWLVisualizationVariants.NET,
    #                                           parameters={"format": "svg"})
    # v.view()
    #
    # powl_model = pm4py.discover_powl(log, variant=POWLDiscoveryVariant.DYNAMIC_CLUSTERING, order_graph_filtering_threshold=0.8)
    # v = pm4py.visualization.powl.visualizer.apply(powl_model, variant=POWLVisualizationVariants.NET,
    #                                           parameters={"format": "svg"})
    # v.view()


if __name__ == "__main__":
    execute_script()
