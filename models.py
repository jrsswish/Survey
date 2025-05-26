import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import mpld3


def mean_age():
  with open('data.csv', 'r') as infile:
    df = pd.read_csv(infile)
    X = df[['Age']]

    age_mean = np.mean(X)

    return age_mean

def gender_count():
  with open('data.csv', 'r') as infile:
    df = pd.read_csv(infile)
    X = df[df['Gender'] == 'male'].value_counts
    X2 = df[df['Gender'] == 'female'].value_counts
    X3 = df[df['Gender'] == 'others'].value_counts

    return X, X2, X3

def graph():
  # creates the plot
  mean_val = mean_age()  

  fig, ax = plt.subplots()

  # creates line from 0-1 x value and mean value-mean value y value
  ax.plot([0, 1], [mean_val, mean_val], label=f"Mean Age: {mean_val:.2f}")  
  ax.set_title("Mean Age")
  ax.set_title("Age mean")

  # convert plot to html string
  html_str = mpld3.fig_to_html(fig)

  return html_str

