# i3Blocks Next Match

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Prerequisites](#prerequisites)
4. [Contact](#contact)

## Introduction
A custom block to get the next match opposition and match time for your football club on your i3block installation.

## Installation
1. Clone this git repo.
2. Replace your RAPID_API_KEY & YOUR_TEAM_ID in the script
3. Add the below code to your i3blocks config.(/etc/i3blocks.conf)
```
[nextmatch]
command=python3 $HOME/LOCATION_OF_THE_CLONED_REPO/nextmatch.py
interval=once
```
4. Restart i3.($mod+shift+r)
5. TADAAAA!

## Prerequisites
Things you'll require 
1. RAPID API KEY to get the API Access
2. TEAM ID (Eg: Liverpool F.C Team id is 44)

### How to get RAPID_API_KEY ?
Go to https://rapidapi.com/fluis.lacasse/api/footapi7 & subscribe.
### How to get YOUR_TEAM_ID?
You can use the search endpoint in RAPID API: /api/search/{term} for tasks like that, it works for leagues, teams, players.

## Contact
Email : akshaypose@gmail.com (I might miss your mail with all the spam i've subscribed so connect with me on instagram)
Instagram : akshaypose
