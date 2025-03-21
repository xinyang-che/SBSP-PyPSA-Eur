#!/usr/bin/env python
# coding: utf-8

# In[1]:

#1
import pypsa
import pandas as pd
import xarray as xr
import sys
n = pypsa.Network("elec_s_37_ec_lcopt_Co2L0.0-3H.nc")
with open('2050_middle_network_summary_2.txt', 'w') as f:
    f.write(str(n))


#3
import matplotlib.pyplot as plt

#6
n.add("Carrier", "SBSP", co2_emissions=0.0)

ac_buses = n.buses[n.buses['carrier'] == 'AC']

for bus in ac_buses.index:
    n.add("Generator", f"SBSP Generator at {bus}", 
          bus=bus,  
          carrier="SBSP",  
          p_nom_min=0.0,  # MW
          marginal_cost=0.0,  # EUR/MWh
          capital_cost=150000,  # EUR/MW
          p_nom_extendable=True  
         )

sbsp_limits = xr.open_dataset("sbsp_rd1_profile_2050.nc")
effective_power = sbsp_limits["Effective Power Ratio"].to_dataframe()

effective_power.index = pd.to_datetime(effective_power.index)

daily_effective_power = effective_power.resample('3H').mean()

for gen_id in n.generators.index:
    if n.generators.loc[gen_id, 'carrier'] == 'SBSP':

        for timestamp in daily_effective_power.index:
            n.generators_t.p_max_pu.loc[timestamp, gen_id] = daily_effective_power.loc[
                timestamp, 'Effective Power Ratio']

#3
snapshots_to_optimize = n.snapshots[:2928]

log_file = '2050_middle_rd1_150000_optimization_output.txt'
with open(log_file, 'w') as f:
    sys.stdout = f
    sys.stderr = f

    print("begin")

    n.optimize(snapshots=snapshots_to_optimize, solver_name='gurobi')

    print("finished")

sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__

print(f"save to {log_file}")

with open('2050_middle_rd1_150000_objective_constant.txt', 'w') as f:
    f.write(str(n.objective_constant))

n.export_to_netcdf('optimized_2050_rd1_150000_network.nc')
n.stores.to_csv('stores_2050_rd1_150000.csv', index=False)
n.storage_units.to_csv('storage_units_2050_rd1_150000.csv', index=False)
n.generators.to_csv('generators_2050_rd1_150000.csv', index=False)
#14
import matplotlib.pyplot as plt
import pandas as pd

supply_data = n.statistics.supply(comps=["Generator", "StorageUnit", "Store"], aggregate_time=False)

supply_data = supply_data.droplevel(0).T

print("Available columns (energy types):")
print(supply_data.columns)

supply_data.to_csv('2050_middle_rd1_150000_hourly_energy_supply.csv', index=True)

print("2050_middle_rd1_150000_hourly_energy_supply.csv")

#15
SBSP_generators = n.generators[n.generators['carrier'] == 'SBSP']

SBSP_generation = n.generators_t.p[SBSP_generators.index]

active_SBSP_generators = SBSP_generation.loc[:, (SBSP_generation != 0).any(axis=0)]

active_SBSP_buses = SBSP_generators.loc[active_SBSP_generators.columns, 'bus'].unique()

output_file = 'active_rd1_150000_SBSP_buses.txt'
with open(output_file, 'w') as f:
    f.write("Buses with active SBSP generators:\n")
    for bus in active_SBSP_buses:
        f.write(str(bus) + '\n')

print(f"save as {output_file}")


sbsp_generators = n.generators[n.generators['carrier'] == 'SBSP']

total_p_nom_opt_sbsp = sbsp_generators['p_nom_opt'].sum()

sbsp_p_nom_opt = sbsp_generators['p_nom_opt']

output_file = 'sbsp_rd1_150000_p_nom_opt_results.txt'
with open(output_file, 'w') as f:
    f.write("Total p_nom_opt for all SBSP generators:\n")
    f.write(str(total_p_nom_opt_sbsp) + "\n\n")

    f.write("p_nom_opt for each SBSP generator:\n")
    f.write(sbsp_p_nom_opt.to_string())

print(f"save as {output_file}")

# CapEx
total_capex = n.statistics.capex()

# OpEx
total_opex = n.statistics.opex(aggregate_time="sum")

# total_cost
total_cost = total_capex + total_opex

with open("total_cost_summary_rd1_150000.txt", "w") as f:
    f.write(f"Total CapEx: {total_capex}\n")
    f.write(f"Total OpEx: {total_opex}\n")
    f.write(f"Total Cost (CapEx + OpEx): {total_cost}\n")

print("Results saved to total_cost_summary.txt")