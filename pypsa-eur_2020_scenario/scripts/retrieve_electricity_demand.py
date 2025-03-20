# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2023-2024 The PyPSA-Eur Authors
#
# SPDX-License-Identifier: MIT
"""
Retrieve electricity prices from OPSD.
"""

import logging

import pandas as pd
from _helpers import configure_logging, set_scenario_config

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    if "snakemake" not in globals():
        from _helpers import mock_snakemake

        snakemake = mock_snakemake("retrieve_electricity_demand")
        rootpath = ".."
    else:
        rootpath = "."
    configure_logging(snakemake)
    set_scenario_config(snakemake)

    local_file = "data/load_2020_time_series.csv"

    
    df = pd.read_csv(local_file, index_col=0, parse_dates=[0])

    
    df.to_csv(snakemake.output[0])

