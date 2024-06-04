import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept,r,p,se = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    new_x_label = np.arange(1880,2051)
    plt.plot(new_x_label,intercept+slope*new_x_label)
    # Create second line of best fit
    slope_1, intercept_1,r,p,se = linregress(df[df['Year']>=2000]['Year'],df[df['Year']>=2000]['CSIRO Adjusted Sea Level'])
    plt.plot(np.arange(2000,2051), intercept_1+slope_1*np.arange(2000,2051))
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()