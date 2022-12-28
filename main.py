import requests
import json

# Set the access token for the Facebook Graph API
access_token = "YOUR_ACCESS_TOKEN"

# Set the Facebook group ID
group_id = "GROUP_ID"

# Set the time range for the week
start_time = "START_TIME"
end_time = "END_TIME"

# Set the URL for the Graph API endpoint to retrieve the list of posts
url = f"https://graph.facebook.com/v9.0/{group_id}/feed?fields=from&since={start_time}&until={end_time}&access_token={access_token}"

# Send a GET request to the Graph API endpoint
response = requests.get(url)

# Parse the response as JSON
data = json.loads(response.text)

# Initialize a dictionary to store the activity count for each member
activity_count = {}

# Iterate through the list of posts
for post in data['data']:
    # Get the name of the member who made the post
    member_name = post['from']['name']

    # Increment the activity count for the member
    if member_name in activity_count:
        activity_count[member_name] += 1
    else:
        activity_count[member_name] = 1

# Sort the activity count dictionary by value in descending order
sorted_activity_count = {k: v for k, v in sorted(activity_count.items(), key=lambda item: item[1], reverse=True)}

# Initialize a list to store the IDs of the top five most active members
top_five_member_ids = []

# Iterate through the sorted activity count dictionary
i = 1
for member, count in sorted_activity_count.items():
  
      # Add the member ID to the list of top five member IDs
    top_five_member_ids.append(post['from']['id'])
    i += 1
    if i > 5:
        break

# Set the message for the post
message = "Our top five most active members this week are:"

# Set the URL for the Graph API endpoint to create a new post
url = f"https://graph.facebook.com/v9.0/{group_id}/feed?access_token={access_token}"

# Set the payload for the POST request
payload = {
    "message": message,
    "tags": top_five_member_ids
}

# Send a POST request to the Graph API endpoint to create the new post
response = requests.post(url, json=payload)

# Parse the response as JSON
data = json.loads(response.text)

# Print the ID of the new post
print(f"Post ID: {data['id']}")

