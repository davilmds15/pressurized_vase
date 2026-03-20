# Solid Rocket Motor – Structural Analysis of Propellant Grain and Metallic Case

This project implements an analytical structural mechanics model for a **solid rocket motor**, analysing the stress and strain state of a cylindrical propellant grain enclosed in a metallic case under combined **thermal and pressure loading**.

## Problem Description

The system consists of two concentric cylinders:
- **Inner cylinder (propellant grain):** viscoelastic solid with low stiffness
- **Outer cylinder (metallic case):** high-stiffness steel shell

The analysis is performed across two distinct loading phases:

| Phase | Description |
|-------|-------------|
| **Phase 2** | Thermal loading only — temperature drop from curing (65°C) to cold storage (−40°C) |
| **Phase 3** | Combined thermal + internal pressure — temperature at 20°C and internal combustion pressure of 20 MPa |

## Method

The Lamé equations for thick-walled cylinders under internal and external pressure are used to compute the radial stress, tangential (hoop) stress, and radial displacement distributions across each component.

The interface pressure between propellant and case is determined from the **thermal interference fit** caused by differential thermal expansion, accounting for the distinct coefficients of thermal expansion of each material.

## Material Properties

| Property | Propellant | Case (Steel) |
|----------|-----------|--------------|
| Young's Modulus | 60 MPa | 210,000 MPa |
| Poisson's Ratio | 0.5 | 0.3 |
| Thermal expansion coeff. | 93 × 10⁻⁶ /K | 11 × 10⁻⁶ /K |

## Geometry

| Parameter | Value |
|-----------|-------|
| Inner radius of grain (a) | 25 mm |
| Outer radius of grain / inner radius of case (b) | 50 mm |
| Case thickness (h) | 2 mm |
| Outer radius of case (c) | 52 mm |

## Outputs

For each phase and each component (propellant and case), the code plots:
- Radial stress distribution σᵣ(r)
- Tangential (hoop) stress distribution σ_θ(r)
- Radial strain distribution εᵣ(r)
- Tangential strain distribution ε_θ(r)

## Requirements

```
numpy
matplotlib
```

Install with:
```bash
pip install numpy matplotlib
```

## Usage

```bash
python pressurized_vase.py
```

## Academic Context

Developed as part of the **Aerospace Engineering BSc** at Universidade Federal de Santa Maria (UFSM), Brazil, within the structural mechanics curriculum.
