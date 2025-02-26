import tkinter as tk
from tkinter import messagebox

class FloodRiskAnalyzer:
    def __init__(self, rainfall, river_level, wind_speed):
        self.rainfall = rainfall  # in mm
        self.river_level = river_level  # in meters
        self.wind_speed = wind_speed  # in km/h
        self.alerts = []

    def check_rainfall(self):
        if self.rainfall > 100:
            self.alerts.append("⚠️ Heavy Rainfall Alert! Risk of flooding.")
    
    def check_river_level(self):
        if self.river_level > 5:
            self.alerts.append("🚨 River Level Critical! Flood warning issued.")

    def check_wind_speed(self):
        if self.wind_speed > 80:
            self.alerts.append("🌪️ High Wind Speed Alert! Risk of storm-related flooding.")

    def check_urban_flood_risk(self):
        if self.rainfall > 80 and self.river_level > 4:
            self.alerts.append("⚠️ Urban Drainage Overflow Warning! Increased flood risk.")

    def check_combined_risk(self):
        if len(self.alerts) >= 2:
            self.alerts.append("🚨🚨 EMERGENCY ALERT! Multiple flood risk factors detected!")

    def analyze(self):
        self.check_rainfall()
        self.check_river_level()
        self.check_wind_speed()
        self.check_urban_flood_risk()
        self.check_combined_risk()

        return self.alerts if self.alerts else ["✅ No immediate flood risks detected."]


# GUI Application
def analyze_flood_risk():
    try:
        rainfall = float(rainfall_entry.get())
        river_level = float(river_level_entry.get())
        wind_speed = float(wind_speed_entry.get())

        analyzer = FloodRiskAnalyzer(rainfall, river_level, wind_speed)
        alerts = analyzer.analyze()

        # Show results in a messagebox
        result_text = "\n".join(alerts)
        if "EMERGENCY ALERT" in result_text:
            messagebox.showerror("🚨 SEVERE FLOOD WARNING!", result_text)
        elif "Critical" in result_text or "Heavy Rainfall" in result_text:
            messagebox.showwarning("⚠️ Flood Risk Alert", result_text)
        else:
            messagebox.showinfo("✅ No Immediate Risk", result_text)

    except ValueError:
        messagebox.showerror("Input Error", "❌ Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("Flood Risk Analyzer")
root.geometry("400x350")
root.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Flood Risk Analyzer", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="black")
title_label.pack(pady=10)

# Input Fields
tk.Label(root, text="Enter Rainfall (mm):", bg="#f0f0f0").pack()
rainfall_entry = tk.Entry(root)
rainfall_entry.pack()

tk.Label(root, text="Enter River Level (m):", bg="#f0f0f0").pack()
river_level_entry = tk.Entry(root)
river_level_entry.pack()

tk.Label(root, text="Enter Wind Speed (km/h):", bg="#f0f0f0").pack()
wind_speed_entry = tk.Entry(root)
wind_speed_entry.pack()

# Analyze Button
analyze_button = tk.Button(root, text="Analyze Flood Risk", command=analyze_flood_risk, bg="blue", fg="white", font=("Arial", 12))
analyze_button.pack(pady=15)

# Run the GUI
root.mainloop()
