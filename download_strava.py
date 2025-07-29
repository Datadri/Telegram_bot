
import requests
import pandas as pd
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Authentication with Strava
auth_url = "https://www.strava.com/oauth/token"
activities_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    "client_id": "166781",
    "client_secret": "3a48619d7ad2617f3b98e6b8ef3b87a7d809a3de",
    "refresh_token": "f3eb957aa63dc1b58b6d6d90e4ac3b9e88c2dd92",
    "grant_type": "refresh_token"
}

res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()["access_token"]
header = {"Authorization": "Bearer " + access_token}

# Download all activities
all_activities = []
page = 1
while True:
    r = requests.get(activities_url, headers=header, params={"per_page": 200, "page": page})
    data = r.json()
    if not data:
        break
    all_activities.extend(data)
    page += 1

# Save to CSV
df = pd.json_normalize(all_activities)
df.to_csv("strava_activities.csv", index=False)
