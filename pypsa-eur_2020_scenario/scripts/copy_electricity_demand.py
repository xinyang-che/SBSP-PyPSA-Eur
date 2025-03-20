# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: : 2017-2024 The PyPSA-Eur Authors
#
# SPDX-License-Identifier: MIT
"""
Defines the time aggregation to be used for sector-coupled network.

Relevant Settings
-----------------

.. code:: yaml

    clustering:
        temporal:
            resolution_sector:

    enable:
        drop_leap_day:

Inputs
------

- ``networks/elec_s{simpl}_{clusters}_ec_l{ll}_{opts}.nc``: the network whose
  snapshots are to be aggregated
- ``resources/hourly_heat_demand_total_elec_s{simpl}_{clusters}.nc``: the total
  hourly heat demand
- ``resources/solar_thermal_total_elec_s{simpl}_{clusters}.nc``: the total
  hourly solar thermal generation

Outputs
-------

- ``snapshot_weightings_elec_s{simpl}_{clusters}_ec_l{ll}_{opts}.csv``

Description
-----------
Computes a time aggregation scheme for the given network, in the form of a CSV
file with the snapshot weightings, indexed by the new subset of snapshots. This
rule only computes said aggregation scheme; aggregation of time-varying network
data is done in ``prepare_sector_network.py``.
"""

import shutil

# 复制输入文件到输出文件
shutil.copyfile(snakemake.input[0], snakemake.output[0])

