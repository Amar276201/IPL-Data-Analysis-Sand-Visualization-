#importing the required libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#loading the ipl data from csv file to DataFrame object
ipl_data = pd.read_csv('IPL Matches.csv')

#showing the first five records of ipl dataset
ipl_data.head()

#finding the number of rows and columns in ipl dataset
ipl_data.shape

#Getting the information of all columns of ipl dataset
ipl_data.info()

#Getting total number of player of match awards
ipl_data['player_of_match'].value_counts()

#Getting top 10 players with most player of match awards
ipl_data['player_of_match'].value_counts()[0:10]

#Getting names of top 10 players with most player of match awards
list(ipl_data['player_of_match'].value_counts()[0:10].keys())

#Getting number of player of match awards of top 10 players
list(ipl_data['player_of_match'].value_counts()[0:10])

#Plotting a bar plot for top ten players with most player of match awards
plt.figure(figsize=(15,10))
plt.title("Top Ten Players with Most Players of the Match")
plt.xlabel("Players Names")
plt.ylabel("Number of Players of the Match Awards")
plt.bar(list(ipl_data['player_of_match'].value_counts()[0:10].keys()), 
list(ipl_data['player_of_match'].value_counts()[0:10]))
plt.show()

#Getting frequency of result column
ipl_data['result'].value_counts()

#Finding how many times every team won the toss  
ipl_data['toss_winner'].value_counts()

#Plotting a bar plot for top ten teams who won the toss most number of times
plt.figure(figsize=(15,10))
plt.title("Top Ten Teams with Most Numbers of Toss Won")
plt.xlabel("Team Name")
plt.ylabel("Number of Toss Won")
plt.xticks(rotation=45)
plt.bar(list(ipl_data['toss_winner'].value_counts()[0:10].keys()), 
list(ipl_data['toss_winner'].value_counts()[0:10]), color = 'g')
plt.grid(axis='y')
plt.show()

#Extracting records where team batting first won the match  
batting_first_data = ipl_data[ipl_data['result'] == 'runs']
batting_first_data.shape      

batting_first_data.head()

#Plotting a histogram plot for distribution of matches won by runs
plt.figure(figsize=(15,10))
plt.title("Distribution of matches won by runs")
plt.xlabel("Won by Runs")
plt.ylabel("Number of Matches")
plt.hist(batting_first_data['result_margin'], rwidth = .9)
plt.show()

#Finding how many times each team won batting first
batting_first_data['winner'].value_counts()

#Plotting a bar plot for top 3 teams who won the match batting first
plt.figure(figsize=(7, 7))
plt.title("Top Three Teams with Most Wins Batting First")
plt.xlabel("Team Name")
plt.ylabel("Number of Matches Won")
plt.bar(list(batting_first_data['winner'].value_counts()[0:3].keys()), 
list(batting_first_data['winner'].value_counts()[0:3]), color=['blue', 'yellow', 'purple'])
plt.show()

#Plotting a pie chart for showing the percentage of the matches won by each team batting first
plt.figure(figsize=(15, 10))
plt.title("Percentages of Matches Won by each Team Batting First")
plt.pie(list(batting_first_data['winner'].value_counts()), 
labels=list(batting_first_data['winner'].value_counts().keys()), autopct='%.1f%%')
plt.show()

batting_second_data = ipl_data[ipl_data['result'] == 'wickets']
batting_second_data.shape

batting_second_data.head()

#Plotting a histogram to show distribution of number of matches won by wickets
plt.figure(figsize=(15,10))
plt.title("Distribution of number of matches won by wickets")
plt.xlabel("Won by Wickets")
plt.ylabel("Number of Matches")
plt.hist(batting_second_data['result_margin'], bins = 10, rwidth = .9)
plt.show()

#Finding out how many times each team won matches batting second
batting_second_data['winner'].value_counts()

#Plotting a bar plot for top 3 teams who won the match batting first
plt.figure(figsize=(7, 7))
plt.title("Top Three Teams with Most Wins Batting Second")
plt.xlabel("Team Name")
plt.ylabel("Number of Matches Won")
plt.bar(list(batting_second_data['winner'].value_counts()[0:3].keys()), 
list(batting_second_data['winner'].value_counts()[0:3]), color=['purple', 'blue', 'yellow'])
plt.show()

#Plotting a pie chart for showing the percentage of the matchs won by each team batting second
plt.figure(figsize=(15, 10))
plt.title("Percentages of Matches Won by each Team Batting Second")
plt.pie(list(batting_second_data['winner'].value_counts()), 
labels=list(batting_second_data['winner'].value_counts().keys()), autopct='%.1f%%')
plt.show()
