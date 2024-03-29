import requests
from datetime import datetime, timedelta

# Fetch the RapidAPI key from the .env file
rapidapi_key = YOUR_RAPID_API_KEY
your_team_id = YOUR_TEAM_ID


url = "https://footapi7.p.rapidapi.com/api/team/"+your_team_id+"/matches/near"

headers = {
	"X-RapidAPI-Key": rapidapi_key,
	"X-RapidAPI-Host": "footapi7.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

data=response.json()

# Function to manually convert timestamp to Indian timezone
def convert_to_indian_timezone(timestamp):
    utc_time = datetime.utcfromtimestamp(timestamp)
    # Indian Standard Time (IST) offset from UTC is +5:30 hours
    ist_offset = timedelta(hours=5, minutes=30)
    indian_time = utc_time + ist_offset
    return indian_time.strftime('%Y-%m-%d %H:%M')

# Fetching nextEvent.awayTeam.name & startTimestamp (in Indian timezone)
next_away_team = data['nextEvent']['awayTeam']['name']
start_timestamp = data['nextEvent']['startTimestamp']

# Convert startTimestamp to Indian timezone
start_time_in_indian_timezone = convert_to_indian_timezone(start_timestamp)


# Displaying fetched data
print("Next:", next_away_team," MatchTime:", start_time_in_indian_timezone)