import json
import requests
webhook_url = "https://o365coloradoedu.webhook.office.com/webhookb2/7b645959-2845-4047-8ad3-e49e1e88c1af@3ded8b1b-070d-4629-82e4-c0b019f46057/IncomingWebhook/182c029251034bd8bcdaacd3381f0453/ec71f836-1fac-46f6-95c9-63555bc3ee64"
#####
def teams_a104():
	global webhook_url
	a104 =  {
  		"title": "A104 has requested assistance with an AV issue",
  		"text": "A104 Needs AV Assistance, please open a ticket for the issue at 'https://sandycay.int.colorado.edu/#ticket/create/' once details are retrieved.",
  		"potentialAction": [
 		{
      		"@context": "https://schema.org",
      		"@type": "ContentCard",
  			}	
  		]
	}	
	requests.post(webhook_url, data=json.dumps(a104), headers={'Content-Type': 'application/json'})
#####
def teams_a108():
	global webhook_url 
	a108 =  {
                "title": "A108 has requested assistance with an AV issue",
                "text": "A108 Needs AV Assistance, please open a ticket for the issue at 'https://sandycay.int.colorado.edu/#ticket/create/' once details are retrieved.",
                "potentialAction": [
                {
                "@context": "https://schema.org",
                "@type": "ContentCard",
                        }
                ]
        }

	requests.post(webhook_url, data=json.dumps(a108), headers={'Content-Type': 'application/json'})
#####
def teams_a115():
	global webhook_url
	a115 =  {
                "title": "A115 has requested assistance with an AV issue",
                "text": "A115 Needs AV Assistance, please open a ticket for the issue at 'https://sandycay.int.colorado.edu/#ticket/create/' once details are retrieved.",
                "potentialAction": [
                {
                "@context": "https://schema.org",
                "@type": "ContentCard",
                        }
                ]
        }
	requests.post(webhook_url, data=json.dumps(a115), headers={'Content-Type': 'application/json'})
#####
def teams_a171h():
	global webhook_url
	a171h =  {
                 "title": "A171H has requested assistance with an AV issue",
                "text": "A171H Needs AV Assistance, please open a ticket for the issue at 'https://sandycay.int.colorado.edu/#ticket/create/' once details are retrieved.",
                "potentialAction": [
                {
                "@context": "https://schema.org",
                "@type": "ContentCard",
                        }
                ]
        }
	requests.post(webhook_url, data=json.dumps(a171h), headers={'Content-Type': 'application/json'})
#####
def teams_a400():
	global webhook_url
	a400 =  {
                "title": "A400 has requested assistance with an AV issue",
                "text": "A400 Needs AV Assistance, please open a ticket for the issue at 'https://sandycay.int.colorado.edu/#ticket/create/' once details are retrieved.",
                "potentialAction": [
                {
                "@context": "https://schema.org",
                "@type": "ContentCard",
                        }
                ]
        }
	requests.post(webhook_url, data=json.dumps(a400), headers={'Content-Type': 'application/json'})
#####
def teams_b115():
	global webhook_url
	b115 =  {
                "title": "B115 has requested assistance with an AV issue",
                "text": "B115 Needs AV Assistance, please open a ticket for the issue at 'https://sandycay.int.colorado.edu/#ticket/create/' once details are retrieved.",
                "potentialAction": [
                {
                "@context": "https://schema.org",
                "@type": "ContentCard",
                        }
                ]
        }
	requests.post(webhook_url, data=json.dumps(b115), headers={'Content-Type': 'application/json'})
#####
def teams_b231():
	global webhook_url
	b231 =  {
                "title": "B231 has requested assistance with an AV issue",
                "text": "B231 Needs AV Assistance, please open a ticket for the issue at 'https://sandycay.int.colorado.edu/#ticket/create/' once details are retrieved.",
                "potentialAction": [
                {
                "@context": "https://schema.org",
                "@type": "ContentCard",
                        }
                ]
        }
	requests.post(webhook_url, data=json.dumps(b231), headers={'Content-Type': 'application/json'})
#####
def teams_b331():
	global webhook_url
	b331 =  {
                "title": "B331 has requested assistance with an AV issue",
                "text": "B331 Needs AV Assistance, please open a ticket for the issue at 'https://sandycay.int.colorado.edu/#ticket/create/' once details are retrieved.",
                "potentialAction": [
                {
                "@context": "https://schema.org",
                "@type": "ContentCard",
                        }
                ]
        }
	requests.post(webhook_url, data=json.dumps(b331), headers={'Content-Type': 'application/json'})
###############
def teams_e1b11():
        global webhook_url
        e1b11 =  {
                "title": "E1B11 has requested assistance with an AV issue",
                "text": "E1B11 Needs AV Assistance, please open a ticket for the issue at 'https://sandycay.int.colorado.edu/#ticket/create/' once details are retrieved.",
                "potentialAction": [
                {
                "@context": "https://schema.org",
                "@type": "ContentCard",
                        }
                ]
        }
        requests.post(webhook_url, data=json.dumps(e1b11), headers={'Content-Type': 'application/json'})
####
def teams_e125():
        global webhook_url
        e125 =  {
                "title": "E125 has requested assistance with an AV issue",
                "text": "E125 Needs AV Assistance, please open a ticket for the issue at 'https://sandycay.int.colorado.edu/#ticket/create/' once details are retrieved.",
                "potentialAction": [
                {
                "@context": "https://schema.org",
                "@type": "ContentCard",
                        }
                ]
        }
        requests.post(webhook_url, data=json.dumps(e125), headers={'Content-Type': 'application/json'})
####
def teams_e225():
        global webhook_url
        e225 =  {
                "title": "E225 has requested assistance with an AV issue",
                "text": "E225 Needs AV Assistance, please open a ticket for the issue at 'https://sandycay.int.colorado.edu/#ticket/create/' once details are retrieved.",
                "potentialAction": [
                {
                "@context": "https://schema.org",
                "@type": "ContentCard",
                        }
                ]
        }
        requests.post(webhook_url, data=json.dumps(e225), headers={'Content-Type': 'application/json'})
###
def teams_b159():
        global webhook_url
        b159 =  {
                "title": "B159 has requested assistance with an AV issue",
                "text": "B159 Needs AV Assistance, please open a ticket for the issue at 'https://sandycay.int.colorado.edu/#ticket/create/' once details are retrieved.",
                "potentialAction": [
                {
                "@context": "https://schema.org",
                "@type": "ContentCard",
                        }
                ]
        }
        requests.post(webhook_url, data=json.dumps(b159), headers={'Content-Type': 'application/json'})
###
def teams_b160():
        global webhook_url
        b160 =  {
                "title": "B160 has requested assistance with an AV issue",
                "text": "B160 Needs AV Assistance, please open a ticket for the issue at 'https://sandycay.int.colorado.edu/#ticket/create/' once details are retrieved.",
                "potentialAction": [
                {
                "@context": "https://schema.org",
                "@type": "ContentCard",
                        }
                ]
        }
        requests.post(webhook_url, data=json.dumps(b160), headers={'Content-Type': 'application/json'})
###
def teams_b171():
        global webhook_url
        b171 =  {
                "title": "B171 has requested assistance with an AV issue",
                "text": "B171 Needs AV Assistance, please open a ticket for the issue at 'https://sandycay.int.colorado.edu/#ticket/create/' once details are retrieved.",
                "potentialAction": [
                {
                "@context": "https://schema.org",
                "@type": "ContentCard",
                        }
                ]
        }
        requests.post(webhook_url, data=json.dumps(b171), headers={'Content-Type': 'application/json'})
####
def teams_b180():
        global webhook_url
        b180 =  {
                "title": "B180 has requested assistance with an AV issue",
                "text": "B180 Needs AV Assistance, please open a ticket for the issue at 'https://sandycay.int.colorado.edu/#ticket/create/' once details are retrieved.",
                "potentialAction": [
                {
                "@context": "https://schema.org",
                "@type": "ContentCard",
                        }
                ]
        }
        requests.post(webhook_url, data=json.dumps(b180), headers={'Content-Type': 'application/json'})
####


