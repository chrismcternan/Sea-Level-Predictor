import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    with open('epa-sea-level.csv', 'r') as f:
      df = pd.read_csv(f, header=0)

    # Create scatter plot
    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1,)
    sns.scatterplot(x='Year', y='CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    linreg1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    pred_values_1 = []
    for i in range(1880, 2051):
      pred_values_1.append(i*linreg1.slope + linreg1.intercept)

    ax.plot(range(1880, 2051), pred_values_1)
    
    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    linreg2 = linregress(x=df_2000['Year'], y=df_2000['CSIRO Adjusted Sea Level'])
    pred_values_2 = []
    for i in range(2000, 2051):
      pred_values_2.append(i*linreg2.slope + linreg2.intercept)

    ax.plot(range(2000, 2051), pred_values_2)

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


if __name__ == '__main__':
  draw_plot()