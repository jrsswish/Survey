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
    # get the count of each gender
    gender_count = df['Gender'].value_counts()
    # put the count of each gender into variable
    # Note: added 0 to prevent NoneType error
    male = gender_count.get('male', 0)
    female = gender_count.get('female', 0)
    other = gender_count.get('other', 0)

    return male, female, other

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

def graph2():
  # creates the plot
  male, female, other = gender_count()  
  

  fig, ax = plt.subplots()

  # creates line from 0-1 x value and mean value-mean value y value
  ax.bar(['male', 'female', 'other'], [male, female, other], color=['blue', 'pink', 'red'] )  
  ax.set_title("Gender Count")
  ax.set_ylabel("Count")

  # convert plot to html string
  html_str = mpld3.fig_to_html(fig)

  return html_str

