#!/usr/bin/env python
# coding: utf-8

# In[1]:

#1
import pypsa
import pandas as pd
import xarray as xr
import sys
n = pypsa.Network("elec_s_37_ec_lcopt_Co2L0.0-3H.nc")
with open('2050_middle_network_summary.txt', 'w') as f:
    f.write(str(n))


#2
snapshots_to_optimize = n.snapshots[:2928]

log_file = '2050_middle_optimization_output.txt'
with open(log_file, 'w') as f:
    sys.stdout = f
    sys.stderr = f

    print("begin")

    n.optimize(snapshots=snapshots_to_optimize, solver_name='gurobi', solver_options={'Threads': 64})

    print("finished")

sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__

print(f"save to {log_file}")

with open('2050_middle_objective_constant.txt', 'w') as f:
    f.write(str(n.objective_constant))

n.export_to_netcdf('optimized_2050_3h_network.nc')
#3
import matplotlib.pyplot as plt
import pandas as pd

supply_data = n.statistics.supply(comps=["Generator", "StorageUnit", "Store"], aggregate_time=False)

supply_data = supply_data.droplevel(0).T

print("Available columns (energy types):")
print(supply_data.columns)

supply_data.to_csv('2050_middle_hourly_energy_supply.csv', index=True)

print("2050_middle_hourly_energy_supply.csv")

n.stores.to_csv('stores_2050_3h.csv', index=False)
n.storage_units.to_csv('storage_units_2050_3h.csv', index=False)
n.generators.to_csv('generators_2050_3h.csv', index=False)

# CapEx
total_capex = n.statistics.capex()

# OpEx
total_opex = n.statistics.opex(aggregate_time="sum")

# total_cost
total_cost = total_capex + total_opex

with open("total_cost_summary_2050.txt", "w") as f:
    f.write(f"Total CapEx: {total_capex}\n")
    f.write(f"Total OpEx: {total_opex}\n")
    f.write(f"Total Cost (CapEx + OpEx): {total_cost}\n")

print("Results saved to total_cost_summary.txt")
