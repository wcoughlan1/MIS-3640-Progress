# -*- coding: utf-8 -*-
"""
Created on Mon Mar 8 19:37:25 2021

@author: wcoughlan1

This program is intended for use with a .csv data set containing statistics for a stock price

The program reads a .csv data set into an array and stores the corresponding data values in a dict
with the column name as the key.

It then produces descriptive statistics for any column of data requested by user

It will produce a line graph for any column requested by user

And it will close by producing a histogram of monthly percent change 
"""

import numpy as np
import math
import matplotlib.pyplot as plt


csv_name = False
file_name = ""

while csv_name == False:
    file_name = input("Enter .csv file name to open: ")
    if file_name.endswith('.csv') == True:
        csv_name = True
    else:
        print("File not found!")


import pandas as pd
df=pd.read_csv(file_name, sep=',',header=None)
data_array = df.values

#   Creating a dictionary to hold column names as keys and their data as values
data = dict()
header = []
for i in range(data_array.shape[1]):
    a = data_array[:,i]
    a = a.tolist()      #   creating column data as list before keeping in dictionary
    header.append(a.pop(0))
    data[str(data_array[:,i][0])] = a


#   Cleaning the data
for i in range(len(header)):

    if header[i] == "Change %":
        data[header[i]] = [float(j.rstrip("%")) for j in data[header[i]]]
        
    if header[i] == "Vol.":
        data[header[i]] = [float(j.rstrip("BM")) for j in data[header[i]]]

    if header[i] != "Date" and header[i] != "Vol." and header[i] != "Change %":
        data[header[i]] = [float(j) for j in data[header[i]]]


def stats():
    stat_ans=True
    while stat_ans:
        print ("""
        P. Descriptive statistics for "Price" column
        O. Descriptive statistics for "Open" column
        H. Descriptive statistics for "High" column
        L. Descriptive statistics for "Low" column
        V. Descriptive statistics for "Vol." column
        C. Descriptive statistics for "Change %" column
        G. Continue to graphs
        Q. Quit
        """)
        stat_ans=input("Specify a column to generate its descriptive statistics? ") 

        if stat_ans == "P": 
            descriptive_stats(data, "Price")
        elif stat_ans == "O":
            descriptive_stats(data, "Open") 
        elif stat_ans == "H":
            descriptive_stats(data, "High")
        elif stat_ans == "L":
            descriptive_stats(data, "Low")
        elif stat_ans == "V":
            descriptive_stats(data, "Vol.")
        elif stat_ans == "C":
            descriptive_stats(data, "Change %")
        elif stat_ans == "G":
            stat_ans = None
            graphs()
        elif stat_ans == "Q":
            stat_ans = None
            print("\n Goodbye") 
        elif stat_ans !="":
            print("\n Not A Valid Choice, Please try again")

#   writing a method to compute and display descriptive statistics
def descriptive_stats(data, column_name):
    lst = data[str(column_name)]
    count = len(lst)
    mean = sum(lst) / len(lst)
    variance = sum([((x - mean) ** 2) for x in lst]) / len(lst)
    std = variance ** 0.5
    minimum = min(lst)
    maximum = max(lst)
    p25 =  percentile(lst, 25)
    p50 =  percentile(lst, 50)
    p75 =  percentile(lst, 75)

    print("\nDescriptive statistics for ", column_name, 
          "\n---------------------------------\nCount\t", round(count, 2), 
          "\nMean\t",  "${:,.2f}". format(round(mean, 2)), 
          "\nStd\t\t", "${:,.2f}". format(round(std, 2)), 
          "\nMin\t\t", "${:,.2f}". format(round(minimum, 2)), 
          "\n25 %\t", "${:,.2f}". format(round(p25, 2)), 
          "\n50 %\t", "${:,.2f}". format(round(p50, 2)), 
          "\n75 %\t", "${:,.2f}". format(round(p75, 2)), 
          "\nMax\t\t", "${:,.2f}". format(round(maximum, 2)))


#   Writing a method to compute percentile
def percentile(myData, percentile):
    size = len(myData)
    return sorted(myData)[int(math.ceil((size * percentile) / 100)) - 1]


#   Creating menu for plotting the graphs of columns
def graphs():
    graph_ans = True
    while graph_ans:
        print ("""
        P. Plot graph for "Price" column
        O. Plot graph for "Open" column
        H. Plot graph for "High" column
        L. Plot graph for "Low" column
        Q. Quit & plot Histogram of % Change
        """)
        graph_ans=input("Specify a column to plot its graph: ") 
        if graph_ans == "P": 
            draw_plot(data, "Price")
        elif graph_ans == "O":
            draw_plot(data, "Open") 
        elif graph_ans == "H":
            draw_plot(data, "High")
        elif graph_ans == "L":
            draw_plot(data, "Low")
        elif graph_ans == "Q":
            graph_ans = None
            plotHist()
        elif graph_ans != "":
            print("\n Not Valid Choice Try again")
            
            
#   writing a method to plot the graph of a given column
def draw_plot(data, column_name):
    plt.plot(data[str(column_name)])
    titleText = "Plot for "+ column_name
    plt.title(titleText)
    plt.show()


def plotHist():
    plt.title("Monthly Percent change in MSFT")
    plt.hist(data['Change %'])


stats()