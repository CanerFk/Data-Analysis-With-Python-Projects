import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    data = pd.read_csv("epa-sea-level.csv")


    plt.scatter(data["Year"], data["CSIRO Adjusted Sea Level"], label="Sea Level Data")


    slope, intercept, r_value, p_value, std_err = linregress(data["Year"], data["CSIRO Adjusted Sea Level"])
    x_values = range(1880, 2051)
    y_values = [slope * x + intercept for x in x_values]
    plt.plot(x_values, y_values, color='red', label="Best Fit Line (1880-2050)")

 
    recent_data = data[data["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data["Year"], recent_data["CSIRO Adjusted Sea Level"])
    x_values_recent = range(2000, 2051)
    y_values_recent = [slope_recent * x + intercept_recent for x in x_values_recent]
    plt.plot(x_values_recent, y_values_recent, color='green', label="Best Fit Line (2000-2050)")

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    plt.legend()

    plt.savefig('sea_level_plot.png')
    return plt.gca()
