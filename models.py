import numpy as np
import pandas as pd
import matplotlib as plt 
import mpld3


def mean_age():
  with open('data.csv', 'r') as infile:
    df = pd.read_csv(infile)
    X = df[['Age']]

    age_mean = np.mean(X)

    return age_mean
  
def graph():
  # creates the plot
  fig, ax = plt.subplots()
  ax.plot(mean_age)
  ax.set_title("Age mean")

  # convert plot to html string
  html_str = mpld3.fig_to_html(fig)

  # save to html file
  with open("stats.html", "w", encoding="utf-8") as f:
    f.write(html_str)