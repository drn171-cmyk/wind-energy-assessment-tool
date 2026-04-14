import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz
from scipy.interpolate import interp1d

# --- 1. Load and Clean Data ---
def load_data(file_path):
    try:
        # Reading Excel file (assuming data is in the first column)
        df = pd.read_excel(file_path, header=None)
        # Handling decimal comma/dot conversion if necessary
        raw_data = df[0].astype(str).str.replace(',', '.').astype(float)
        return raw_data.dropna().values
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

# --- 2. Wind Speed Extrapolation (Hellmann's Law) ---
def hellmann_law(v_ref, h_hub, h_ref=9.1, alpha=1/7):
    return v_ref * (h_hub / h_ref)**alpha

# --- 3. Capacity Factor Calculation (Vco Included) ---
def calculate_capacity_factor(v_m, v_ci, v_r, v_co=25):
    # Part A: Constant Terms (Exponential differences)
    const_factor = (np.pi**2 / 16)
    exp_1 = np.exp(-(np.pi/4) * (v_r / v_m)**2)
    exp_2 = np.exp(-(np.pi/4) * (v_co / v_r)**2)
    term1 = const_factor * (exp_1 - exp_2)
    
    # Part B: Integration (Trapezoidal Rule)
    v_vec = np.linspace(v_ci, v_r, 1000)
    term_inside = (np.pi/2) * ((v_vec / v_r)**3) * (v_vec / (v_m**2)) * \
                  np.exp(-(np.pi/4) * (v_vec**2 / v_m**2))
    integral_val = trapz(term_inside, v_vec)
    
    return term1 + integral_val

# --- Main Script ---
file_name = 'Hourly Wind Data.xlsx'
wind_data = load_data(file_name)

if wind_data is not None:
    # Basic Statistics
    avg_speed = np.mean(wind_data)
    sigma = np.sqrt(np.mean(wind_data**2) / 2)
    v_mp = sigma  # Most Probable Speed
    
    print(f"{'='*40}")
    print(f"WIND RESOURCE ANALYSIS REPORT")
    print(f"{'='*40}")
    print(f"Annual Average Speed: {avg_speed:.2f} m/s")
    print(f"Most Probable Speed (Vmp): {v_mp:.2f} m/s")

    # Turbine Parameters
    turbines = [
        {"name": "Turbine 1", "height": 185, "diameter": 170, "P_rated": 7.0, "v_r": 10.37},
        {"name": "Turbine 2", "height": 134, "diameter": 132, "P_rated": 3.456, "v_r": 11.5} # Example v_r
    ]

    for t in turbines:
        v_hub_avg = hellmann_law(avg_speed, t['height'])
        cf = calculate_capacity_factor(v_hub_avg, 0.1, t['v_r'])
        p_avg = cf * t['P_rated']
        
        print(f"\n>> {t['name']} ({t['P_rated']} MW)")
        print(f"   Hub Height: {t['height']} m")
        print(f"   Avg Speed at Hub: {v_hub_avg:.2f} m/s")
        print(f"   Capacity Factor (CF): {cf*100:.2f} %")
        print(f"   Estimated Avg Power: {p_avg:.2f} MW")

    # --- 4. Visualization ---
    plt.figure(figsize=(10, 6))
    plt.hist(wind_data, bins=30, density=True, alpha=0.6, color='gray', label='Observed Data')
    
    # Rayleigh Curve
    x = np.linspace(0, max(wind_data)+2, 100)
    y = (x / sigma**2) * np.exp(-x**2 / (2 * sigma**2))
    plt.plot(x, y, 'r-', lw=3, label='Rayleigh PDF')
    
    plt.title('Wind Speed Probability Distribution', fontsize=14)
    plt.xlabel('Speed (m/s)')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
