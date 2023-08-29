import json
import requests
webhook_url = "<Your Teams Webhook URL>"
#####Replace <new title> with your desired identifier, just repeat this function with new names for each QR code in question.#####
def teams_<new title>():
	global webhook_url
	<new title> =  {
  		"title": "Example Title",
  		"text": "Message to send over webhook",
  		"potentialAction": [
 		{
      		"@context": "https://schema.org",
      		"@type": "ContentCard",
  			}	
  		]
	}	
	requests.post(webhook_url, data=json.dumps(<new title>), headers={'Content-Type': 'application/json'})
