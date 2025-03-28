# SBSP-PyPSA

**Integrating Space-Based Solar Power into European-Scale Energy System Modeling with PyPSA-Eur**

[![Zenodo](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXX)

## Overview

This repository contains the code and data used in our research on integrating Space-Based Solar Power (SBSP) into a high-resolution, Europe-wide energy system model using PyPSA-Eur. The study aims to evaluate the techno-economic feasibility of two representative SBSP designs under net-zero constraints in 2020 and 2050 scenarios.

We model SBSP generation profiles and costs, integrate them into the PyPSA-Eur framework, and perform multi-scenario optimization and sensitivity analyses. This work explores SBSP’s potential to complement terrestrial renewables and reduce system costs, storage needs, and intermittency issues in future decarbonized energy systems.

> If you use this repository in your research, please cite our paper and/or reference this GitHub project. (DOI and citation to be added upon publication.)

---

## Repository Structure

The repository consists of three main components:

### `pypsa-eur/`
A forked and lightly modified copy of the official [PyPSA-Eur](https://github.com/PyPSA/pypsa-eur) repository, which provides the core functionality for capacity expansion and dispatch modeling across Europe. All original credits go to the PyPSA-Eur developers. We use this base as the foundation for SBSP integration.

- **Disclaimer:** Most code and data here are not original work. They are adapted from PyPSA-Eur v0.X to ensure compatibility with our SBSP extensions.
- If using this repository, please also follow [PyPSA-Eur’s license and citation instructions](https://github.com/PyPSA/pypsa-eur#license).

### `sbsp_modeling/`
Original code developed for this study to simulate SBSP technology performance:

- `cost/`: Computes capital and marginal costs of SBSP for both RD1 and RD2 designs in 2020 and 2050, based on NASA projections and engineering assumptions.
- `generation/`: Constructs high-resolution generation profiles for both SBSP designs, accounting for orbital dynamics and wireless power transmission losses.

### `integration_optimization/`
Scripts to integrate SBSP into the PyPSA-Eur model and run system-level optimizations:

- `2020_scenario/` and `2050_scenario/`: Define baseline European power system models with and without SBSP under respective decarbonization targets.
- `sensitivity_analyses/`: Evaluate the system impact of varying SBSP capital costs, generation profiles, and intermittency assumptions. Identify cost thresholds for SBSP viability.

---

## 🌍 Data Availability

Due to the size of raw input data (e.g., weather files, network shapefiles), we host key datasets on [Zenodo](https://zenodo.org/). Please download the data before running the full pipeline.

🔗 **Zenodo data archive:** [https://doi.org/10.5281/zenodo.XXXXX](https://doi.org/10.5281/zenodo.XXXXX)

Datasets include:

- PyPSA-Eur preprocessing data (e.g., demand, weather, generation potential)
- SBSP-specific inputs (e.g., orbital irradiance, transmission losses)
- Cost parameters for RD1 and RD2

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/CHEperb/SBSP-PyPSA.git
cd SBSP-PyPSA
pip install -r requirements.txt
