# SBSP-PyPSA

**Assess Space-Based Solar Power in European-Scale Power System Decarbonization**

[![Zenodo](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXX)

## Overview

This repository contains the code and data used in our research on integrating Space-Based Solar Power (SBSP) into a high-resolution, Europe-wide energy system model using PyPSA-Eur. The study aims to evaluate the techno-economic feasibility of two representative SBSP designs under net-zero constraints in 2020 and 2050 scenarios.

We model SBSP generation profiles and costs, integrate them into the PyPSA-Eur framework, and perform multi-scenario optimization and sensitivity analyses. This work explores SBSP’s potential to complement terrestrial renewables and reduce system costs, storage needs, and intermittency issues in future decarbonized energy systems.

> If you use this repository in your research, please cite our paper and/or reference this GitHub project. (DOI and citation will be added later.)

---

## Repository Structure

The repository consists of three main components:

### `sbsp_modeling/`
Original code developed for this study to simulate SBSP technology performance:

- `cost/`: Computes capital and marginal costs of SBSP for both RD1 and RD2 designs in 2020 and 2050, based on NASA projections and engineering assumptions.
- `generation/`: Constructs high-resolution generation profiles for both SBSP designs, accounting for orbital dynamics and wireless power transmission losses.

### `pypsa-eur/`
A forked and lightly modified copy of the official [PyPSA-Eur](https://github.com/PyPSA/pypsa-eur) repository, which provides the core functionality for capacity expansion and dispatch modeling across Europe. All original credits go to the PyPSA-Eur developers. We use this base as the foundation for SBSP integration.

- **Disclaimer:** Most code and data here are not original work. They are adapted from PyPSA-Eur v0.X to ensure compatibility with our SBSP extensions. In addition, some input data have been adjusted to reflect the specific requirements of our 2020 and 2050 scenario settings.
- If using this repository, please also follow [PyPSA-Eur’s license and citation instructions](https://github.com/PyPSA/pypsa-eur#license).

### `integration_optimization/`
Scripts to integrate SBSP into the PyPSA-Eur model and run system-level optimizations:

- `2020_scenario/` and `2050_scenario/`: Define baseline European power system models with and without SBSP under respective decarbonization targets.
- `sensitivity_analyses/`: Evaluate the system impact of varying SBSP capital costs. Identify cost thresholds for SBSP viability.

---

## Data Availability

Due to the size of raw input data (e.g., weather files, network shapefiles), we host key datasets on [Zenodo](https://zenodo.org/). Please download the data archive before running the full modeling pipeline.

**Zenodo data archive:** [https://doi.org/10.5281/zenodo.XXXXX](https://doi.org/10.5281/zenodo.XXXXX)

### The dataset contains the following input data files:

- `powerplants.csv`: Power plant-level technical and geographic data used to generate input for PyPSA-Eur, including fuel type, capacity, location, efficiency, and commissioning year.
- `electricity_demand.csv`: Hourly electricity demand by country for one full year (in MW), used as demand input for PyPSA-Eur.
- `europe-2020-era5.nc`: Hourly capacity factors for renewable energy sources by country and technology, derived from ERA5 reanalysis data (in per unit).
- `sbsp_rd1_profile_2020.nc`, `sbsp_rd2_profile_2020.nc`: Hourly normalized generation profiles for SBSP RD1 and RD2 designs in 2020 (in per unit).
- `sbsp_rd1_profile_2050.nc`, `sbsp_rd2_profile_2050.nc`: Hourly normalized generation profiles for SBSP RD1 and RD2 designs in 2050 (in per unit).
- `costs.csv`: Cost assumptions used in the model; units are specified in the "units" column.
- `resources/`: Geospatial and technology-specific data used by PyPSA-Eur, including regional boundaries, renewable resource maps, siting constraints, and power plant references.

### The dataset also includes intermediate model outputs:

- `elec_s_37_ec_lcopt_Co2L0.7-3H.nc`: 2020 PyPSA-Eur network prior to SBSP integration.
- `elec_s_37_ec_lcopt_Co2L0.0-3H_maximum.nc`: 2050 network assuming maximum projected technology costs.
- `elec_s_37_ec_lcopt_Co2L0.0-3H_minimum.nc`: 2050 network assuming minimum projected technology costs.
- `elec_s_37_ec_lcopt_Co2L0.0-3H.nc`: 2050 network assuming average projected technology costs.

### The dataset includes model output files for all SBSP scenarios:

Folders correspond to different scenario years (e.g., 2020, 2050) and SBSP capital costs (in EUR/MW). Each folder contains full model outputs for a specific scenario.

For example, in the folder `2050_RD1_267869` (2050 scenario with RD1 at 267,869 EUR/MW), the following files are provided:

- `optimized_2050_rd1_267869_network.nc`: Optimized PyPSA-Eur network for 2050 with RD1 integrated.
- `2050_middle_rd1_hourly_energy_supply.csv`: Hourly energy supply by technology (in MW).
- `2050_middle_rd1_optimization_output.txt`: Full solver output from optimization.
- `2050_middle_rd1_statistics_cleaned.csv`: Summary statistics of key components in the system.
- `active_rd1_SBSP_buses.txt`: List of buses (nodes) where SBSP is actively installed.
- `generators_2050_rd1_267869.csv`: Parameters of all generators in the optimized network.
- `storage_units_2050_rd1_267869.csv`: Parameters of all storage units.
- `stores_2050_rd1_267869.csv`: Parameters of all stores.
- `sbsp_rd1_p_nom_opt_results.csv`: Optimized installed SBSP capacity per node (in MW).

Each scenario folder follows the same naming convention and structure, allowing comparative analysis across years and cost assumptions.

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/CHEperb/SBSP-PyPSA.git
cd SBSP-PyPSA
pip install -r requirements.txt
