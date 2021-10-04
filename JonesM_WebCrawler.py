# File: Fantasy Football Web Scraper


# Beautiful Soup learned from https://beautiful-soup-4.readthedocs.io/en/latest/

import requests                                 #import
from bs4 import BeautifulSoup
import pandas as pd

players = []                                    #create lists to contain data for every category
PassingYds = []
PassingTD = []
Interceptions = []
RushingYds = []
RushingTD = []
FantasyPts = []

URL = "https://fantasy.nfl.com/research/scoringleaders?position=1#researchScoringLeaders=researchScoringLeaders%2C%2Fresearch%2Fscoringleaders%253Fposition%253D2%2526statCategory%253Dstats%2526statSeason%253D2021%2526statType%253DseasonStats%2526statWeek%253D4%2Creplace"

page = requests.get(URL)                                                       #convert URL to usable page

soup = BeautifulSoup(page.content, "html.parser")                              #set up Beautiful Soup from URL


#for loop to obtain every item from the URl where the pattern exists
#this pattern finds every a object with the playerCard class (to find player name)
for item in soup.select("a.playerCard"):
    players.append(item.text)                           #add each name to the players list

players.remove("View News")                             #item returns one incorrect value of "View News", so we remove it

#this pattern finds every span object with the statId-5 class (to find passing yards)
for item in soup.select("span.statId-5"):
    PassingYds.append(item.text)

#this pattern finds every span object with the statId-6 class (to find passing touchdowns)
for item in soup.select("span.statId-6"):
    PassingTD.append(item.text)

#this pattern finds every span object with the statId-7 class (to find interceptions)
for item in soup.select("span.statId-7"):
    Interceptions.append(item.text)

#this pattern finds every span object with the statId-14 class (to find rushing yards)
for item in soup.select("span.statId-14"):
    RushingYds.append(item.text)

#this pattern finds every span object with the statId-15 class (to find rushing touchdowns)
for item in soup.select("span.statId-15"):
    RushingTD.append(item.text)

#this pattern finds every span object with the playerSeasonTotal class (to find faantasy points)
for item in soup.select("span.playerSeasonTotal"):
    FantasyPts.append(item.text)

# print(len(players))                                      #test code to make sure each list has the same length
# print(len(PassingYds))
# print(len(PassingTD))
# print(len(Interceptions))
# print(len(RushingYds))
# print(len(RushingYds))
# print(len(FantasyPts))

#set column names for each list
d = {"Players": players,
     "Passing Yards": PassingYds,
     "Passing Touchdowns": PassingTD,
     "Interceptions": Interceptions,
     'Rushing Yards': RushingYds,
     "Rushing Touchdowns": RushingYds,
     "Fantasy Points": FantasyPts
     }
#create new data frame from the new columns
df = pd.DataFrame(data=d)
#export dataframe to csv file
df.to_csv(r"C:\Users\Max\Desktop\FF.csv", index=False, header=True)
