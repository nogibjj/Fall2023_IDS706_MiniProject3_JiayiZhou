"""Main function goes here"""
import pandas as pd
import matplotlib.pyplot as plt

def describe_file(input1):
    """define a function read a file"""
    df1 = pd.read_csv(input1)
    summary_statistics= df1.describe()
    summary_html = summary_statistics.to_html("summary_statistics.html")
    return summary_statistics, summary_html

def plot_file(input1):
    """define a function plot relationship in a dataframe"""
    df1 = pd.read_csv(input1)
    df1.plot(x='CAPFAC', y='PLNGENAN', kind='scatter', 
             title="Plant Capacity Factor vs Plant Annual Net Generation")
    # Save the plot as a figure
    plt.savefig('plant_capacity_factor.png')
