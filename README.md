# Wind Energy Assessment Tool

This project provides a comprehensive analysis of wind speed data, calculates capacity factors for specific wind turbines, and visualizes wind energy potential using the Rayleigh distribution.

## Key Features
* **Data Processing:** Automated cleaning and hourly-to-monthly reshaping of wind data.
* **Height Extrapolation:** Uses Hellmann's Power Law for wind speed estimation at hub height.
* **Statistical Modeling:** Rayleigh PDF and CFD-friendly performance metrics.
* **Power Analysis:** Capacity Factor (CF) calculation using numerical integration (Trapezoidal rule).

## Engineering Parameters
* **Turbine 1:** 7 MW Rated Power | 185m Hub Height
* **Turbine 2:** 3.456 MW Rated Power | 134m Hub Height
* **Surface Roughness ($\alpha$):** 1/7 (Standard inland)

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the analysis: `python main.py`

## Developer
* **[Senin Adın]** - Engineering Student at Istanbul Technical University (ITU)
