import numpy as np
import pandas as pd

# Set the random seed for scientific consistency
# (Generates the same logical data every time you run the code)
np.random.seed(42)

# 1 Year of hourly data (365 days * 24 hours = 8760)
hour_number = 8760

# Scale parameter (sigma) for the Rayleigh distribution
# We set sigma to 6.5 to achieve an average wind speed of approximately 8 m/s
sigma = 6.5

# Generate wind speed data following a Rayleigh distribution
data = np.random.rayleigh(scale=sigma, size=hour_number)

# Round to 2 decimal places to simulate real-life anemometer measurements (e.g., 7.45)
data = np.round(data, 2)

# Convert the array into a Pandas DataFrame
df = pd.DataFrame(data=data, columns=['Wind Velocity_m_s'])

# Save the data as an Excel file (without headers and index numbers)
name = 'Hourly Wind Speed.xlsx'
df.to_excel(name, index=False, header=False)

print(f"Success! {hour_number} hours of sample data has been created as '{name}'.")
print(f"Annual average of the generated data: {np.mean(data):.2f} m/s")
