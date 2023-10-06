from typing import List, Optional, Dict, Any, Tuple, Type

from pm4py.algo.discovery.powl.inductive.cuts.concurrency import POWLConcurrencyCutUVCL
from pm4py.algo.discovery.powl.inductive.cuts.factory import S, T, CutFactory
from pm4py.algo.discovery.powl.inductive.cuts.loop import POWLLoopCutUVCL
from pm4py.algo.discovery.powl.inductive.cuts.sequence import POWLStrictSequenceCutUVCL
from pm4py.algo.discovery.powl.inductive.cuts.xor import POWLExclusiveChoiceCutUVCL
from pm4py.algo.discovery.inductive.dtypes.im_ds import IMDataStructureUVCL, IMDataStructure
from pm4py.algo.discovery.powl.inductive.variants.brute_force.bf_partial_order_cut import BruteForcePartialOrderCutUVCL
from pm4py.algo.discovery.powl.inductive.variants.powl_discovery_varaints import POWLDiscoveryVariant
from pm4py.objects.powl.obj import POWL


class CutFactoryPOBF(CutFactory):

    @classmethod
    def get_cuts(cls, obj: T, inst: POWLDiscoveryVariant, parameters: Optional[Dict[str, Any]] = None) -> List[Type[S]]:
        if type(obj) is IMDataStructureUVCL:
            return [POWLExclusiveChoiceCutUVCL, POWLStrictSequenceCutUVCL, POWLConcurrencyCutUVCL, POWLLoopCutUVCL, BruteForcePartialOrderCutUVCL]
        return list()

    @classmethod
    def find_cut(cls, obj: IMDataStructure, inst: POWLDiscoveryVariant, parameters: Optional[Dict[str, Any]] = None) -> Optional[
        Tuple[POWL, List[T]]]:
        for c in CutFactoryPOBF.get_cuts(obj, inst):
            r = c.apply(obj, parameters)
            if r is not None:
                return r
        return None