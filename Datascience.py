#!/usr/bin/env python
# coding: utf-8

# In[1]:


## This code is to:
## ● Perform ‘Exploratory Data Analysis’ on dataset ‘Indian Premier League’
## ● As a sports analysts, find out the most successful teams, players and factors
## contributing win or loss of a team.
## ● Suggest teams or players a company should endorse for its products.
## ● You can choose any of the tool of your choice (Python/R/Tableau/PowerBI/Excel/SAP/SAS)


# In[2]:


#first step: Exploratory Data Analysis:(Import livraries and Datasets)

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

ipl = pd.read_csv('C:/Users/zaina/Downloads/Indian Premier League/deliveries.csv')
ipl = pd.read_csv('C:/Users/zaina/Downloads/Indian Premier League/matches.csv')


# In[3]:


##check Dataset
ipl.head()


# In[4]:


## we need to clean our data and check missing values in each column:
ipl.isnull().sum()


# In[5]:


## drop rows of missing values
ipl.dropna(inplace=True)


# In[6]:


## Part 2: As a sports analysts, find out the most successful teams, players and factorscontributing win or loss of a team.
## Most successful team can be known by calculating number of wins for each team
team_wins = ipl['winner'].value_counts()


# In[7]:


## Visualizations:
plt.figure(figsize=(12,6))
sns.barplot(x=team_wins.index, y=team_wins.values, palette='dark')
plt.title('Most Successful IPL Teams')
plt.xlabel('Teams')
plt.ylabel('Number of Wins')
plt.xticks(rotation=90)
plt.show()


# In[8]:


## It can be shown that Chennai Super Kings is the team with most wins


# In[9]:


## Most Successul Player:
player_wins = ipl['player_of_match'].value_counts()[:10]

plt.figure(figsize=(12,6))
sns.barplot(x=player_wins.index, y=player_wins.values, palette='dark')
plt.title('Most Successful IPL Players')
plt.xlabel('Players')
plt.ylabel('Number of Player of Match Awards')
plt.xticks(rotation=90)
plt.show()


# In[10]:


## we have more than 1 successful player 


# In[11]:


## Factors Contributing loss and win
plt.figure(figsize=(12,6))
sns.histplot(ipl['win_by_runs'], bins=50)
plt.title('Distribution of Win Margin (Runs)')
plt.xlabel('Win Margin (Runs)')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(12,6))
sns.histplot(ipl['win_by_wickets'], bins=20)
plt.title('Distribution of Win Margin (Wickets)')
plt.xlabel('Win Margin (Wickets)')
plt.ylabel('Count')
plt.show()


# In[12]:


## As we can see from the histograms, most of the matches were won by a small margin (less than 20 runs or less than 6 wickets).


# In[13]:


## Correlation
ipl['toss_match_win'] = np.where(ipl['toss_winner']==ipl['winner'], 'Yes', 'No')

plt.figure(figsize=(10,6))
sns.countplot(x='toss_match_win', data=ipl, palette='dark')
plt.title('Toss Winner vs. Match Winner')
plt.xlabel('Toss Winner Matches Won')
plt.ylabel('Count')
plt.show()


# In[14]:


## Explore the relationship between the win margin and the decision to bat or bowl first.
plt.figure(figsize=(12,6))
sns.boxplot(x='toss_decision', y='win_by_runs', data=ipl, palette='dark')
plt.title('Win Margin vs. Toss Decision')
plt.xlabel('Toss Decision')
plt.ylabel('Win Margin (Runs)')
plt.show()

plt.figure(figsize=(12,6))
sns.boxplot(x='toss_decision', y='win_by_wickets', data=ipl, palette='dark')
plt.title('Win Margin vs. Toss Decision')
plt.xlabel('Toss Decision')
plt.ylabel('Win Margin (Wickets)')
plt.show()


# In[15]:


## Part 3: Suggestions:

player_popularity = ipl.groupby('player_of_match')['player_of_match'].count().sort_values(ascending=False)[:10]
team_popularity = ipl['winner'].value_counts()[:10]

plt.figure(figsize=(12,6))
sns.barplot(x=player_popularity.index, y=player_popularity.values, palette='dark')
plt.title('Most Popular IPL Players')
plt.xlabel('Players')
plt.ylabel('Popularity')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(12,6))
sns.barplot


# In[16]:


## Similar way:
# Calculate the total number of man of the match awards for each player
player_df = ipl.groupby('player_of_match')['player_of_match'].count().reset_index(name='awards')
player_df = player_df.sort_values(by='awards', ascending=False)

# Print the top 10 players based on man of the match awards
print("Top 10 Players:")
print(player_df.head(10))

# Calculate the total number of matches won by each team
team_df = ipl['winner'].value_counts().reset_index(name='wins')
team_df = team_df.rename(columns={'index': 'team'})

# Print the top 10 teams based on number of matches won
print("\nTop 10 Teams:")
print(team_df.head(10))


# In[ ]:




