import sys
from enum import Enum
from typing import Any, Optional, Dict

import pandas as pd

from pm4py.util import constants, xes_constants, exec_utils


class Parameters(Enum):
    CASE_ID_KEY = constants.PARAMETER_CONSTANT_CASEID_KEY
    ATTRIBUTE_KEY = constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY
    MIN_REP = "min_rep"
    MAX_REP = "max_rep"


def apply(df: pd.DataFrame, value: Any, parameters: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
    """
    Filters the trace of the dataframe where the given attribute value is repeated
    (in a range of repetitions that is specified by the user)

    Parameters
    ----------------
    df
        Dataframe
    value
        Value that is investigated
    parameters
        Parameters of the filter, including:
        - Parameters.ATTRIBUTE_KEY => the attribute key
        - Parameters.MIN_REP => minimum number of repetitions
        - Parameters.MAX_REP => maximum number of repetitions
        - Parameters.CASE_ID_KEY => the columns of the dataframe that is the case identifier

    Returns
    ----------------
    filtered_df
        Filtered dataframe
    """
    if parameters is None:
        parameters = {}

    case_id_key = exec_utils.get_param_value(Parameters.CASE_ID_KEY, parameters, constants.CASE_CONCEPT_NAME)
    attribute_key = exec_utils.get_param_value(Parameters.ATTRIBUTE_KEY, parameters, xes_constants.DEFAULT_NAME_KEY)
    min_rep = exec_utils.get_param_value(Parameters.MIN_REP, parameters, 2)
    max_rep = exec_utils.get_param_value(Parameters.MAX_REP, parameters, sys.maxsize)

    filtered_df = df[df[attribute_key] == value]
    filtered_df = filtered_df.groupby(case_id_key).size().reset_index()
    filtered_df = filtered_df[filtered_df[0] >= min_rep]
    filtered_df = filtered_df[filtered_df[0] <= max_rep]

    return df[df[case_id_key].isin(filtered_df[case_id_key])]