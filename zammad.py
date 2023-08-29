import json
import requests
######################################################################################
def zammad_a104():
	endpoint = "http://sandycay.int.colorado.edu/api/v1/ticket",
	head = {"Authorization":  "Token token=pVuWXy_46IAqKBzXmisJTyc2YIX4JaRCwh4bx8sEjmGbO1wCSBnJcQYx_bICVTzv", "Content-Type": "application/json"}	
	data = {
		"title": "A104 requires immediate AV Help",
        	"group": "bit-help",
        	"customer_id" : "1",
        	"article": {
        		"from": "bit-help@colorado.edu",
                	"subject": "A104 AV Problem",
                	"internal": False,
			"body": "A user has requested AV assistance via QR Code in room: A104",
                	#"sender": "BIT Help",
                	"type": "note",
			}
		}
	r = requests.post(url='https://sandycay.int.colorado.edu/api/v1/tickets', json = data, headers = head)
	print(r.json)
	print(r.text)
######################################################################################
######################################################################################
def zammad_a108():
        endpoint = "http://sandycay.int.colorado.edu/api/v1/ticket",
        head = {"Authorization":  "Token token=pVuWXy_46IAqKBzXmisJTyc2YIX4JaRCwh4bx8sEjmGbO1wCSBnJcQYx_bICVTzv", "Content-Type": "application/json"}
        data = {
                "title": "A108 requires immediate AV Help",
                "group": "bit-help",
                "customer_id" : "1",
                "article": {
                        "from": "bit-help@colorado.edu",
                        "subject": "A108 AV Problem",
                        "internal": False,
                        "body": "A user has requested AV assistance via QR Code in room: A108",
                        #"sender": "BIT Help",
                        "type": "note",
                        }
                }
        r = requests.post(url='https://sandycay.int.colorado.edu/api/v1/tickets', json = data, headers = head)
        print(r.json)
        print(r.text)
######################################################################################
######################################################################################
def zammad_a115():
        endpoint = "http://sandycay.int.colorado.edu/api/v1/ticket",
        head = {"Authorization":  "Token token=pVuWXy_46IAqKBzXmisJTyc2YIX4JaRCwh4bx8sEjmGbO1wCSBnJcQYx_bICVTzv", "Content-Type": "application/json"}
        data = {
                "title": "A115 requires immediate AV Help",
                "group": "bit-help",
                "customer_id" : "1",
                "article": {
                        "from": "bit-help@colorado.edu",
                        "subject": "A115 AV Problem",
                        "internal": False,
                        "body": "A user has requested AV assistance via QR Code in room: A115",
                        "type": "note",
                        }
                }
        r = requests.post(url='https://sandycay.int.colorado.edu/api/v1/tickets', json = data, headers = head)
        print(r.json)
        print(r.text)
######################################################################################
######################################################################################
def zammad_a171h():
        endpoint = "http://sandycay.int.colorado.edu/api/v1/ticket",
        head = {"Authorization":  "Token token=pVuWXy_46IAqKBzXmisJTyc2YIX4JaRCwh4bx8sEjmGbO1wCSBnJcQYx_bICVTzv", "Content-Type": "application/json"}
        data = {
                "title": "A171H requires immediate AV Help",
                "group": "bit-help",
                "customer_id" : "1",
                "article": {
                        "from": "bit-help@colorado.edu",
                        "subject": "A171H AV Problem",
                        "internal": False,
                        "body": "A user has requested AV assistance via QR Code in room: A171H",
                        "type": "note",
                        }
                }
        r = requests.post(url='https://sandycay.int.colorado.edu/api/v1/tickets', json = data, headers = head)
        print(r.json)
        print(r.text)
######################################################################################
######################################################################################
def zammad_a400():
        endpoint = "http://sandycay.int.colorado.edu/api/v1/ticket",
        head = {"Authorization":  "Token token=pVuWXy_46IAqKBzXmisJTyc2YIX4JaRCwh4bx8sEjmGbO1wCSBnJcQYx_bICVTzv", "Content-Type": "application/json"}
        data = {
                "title": "A400 requires immediate AV Help",
                "group": "bit-help",
                "customer_id" : "1",
                "article": {
                        "from": "bit-help@colorado.edu",
                        "subject": "A400 AV Problem",
                        "internal": False,
                        "body": "A user has requested AV assistance via QR Code in room: A400",
                        "type": "note",
                        }
                }
        r = requests.post(url='https://sandycay.int.colorado.edu/api/v1/tickets', json = data, headers = head)
        print(r.json)
        print(r.text)
######################################################################################
######################################################################################
def zammad_b115():
        endpoint = "http://sandycay.int.colorado.edu/api/v1/ticket",
        head = {"Authorization":  "Token token=pVuWXy_46IAqKBzXmisJTyc2YIX4JaRCwh4bx8sEjmGbO1wCSBnJcQYx_bICVTzv", "Content-Type": "application/json"}
        data = {
                "title": "B115 requires immediate AV Help",
                "group": "bit-help",
                "customer_id" : "1",
                "article": {
                        "from": "bit-help@colorado.edu",
                        "subject": "B115 AV Problem",
                        "internal": False,
                        "body": "A user has requested AV assistance via QR Code in room: B115",
                        "type": "note",
                        }
                }
        r = requests.post(url='https://sandycay.int.colorado.edu/api/v1/tickets', json = data, headers = head)
        print(r.json)
        print(r.text)
######################################################################################
######################################################################################
def zammad_b231():
        endpoint = "http://sandycay.int.colorado.edu/api/v1/ticket",
        head = {"Authorization":  "Token token=pVuWXy_46IAqKBzXmisJTyc2YIX4JaRCwh4bx8sEjmGbO1wCSBnJcQYx_bICVTzv", "Content-Type": "application/json"}
        data = {
                "title": "B231 requires immediate AV Help",
                "group": "bit-help",
                "customer_id" : "1",
                "article": {
                        "from": "bit-help@colorado.edu",
                        "subject": "B231 AV Problem",
                        "internal": False,
                        "body": "A user has requested AV assistance via QR Code in room: B231",
                        "type": "note",
                        }
                }
        r = requests.post(url='https://sandycay.int.colorado.edu/api/v1/tickets', json = data, headers = head)
        print(r.json)
        print(r.text)
######################################################################################
######################################################################################
def zammad_b331():
        endpoint = "http://sandycay.int.colorado.edu/api/v1/ticket",
        head = {"Authorization":  "Token token=pVuWXy_46IAqKBzXmisJTyc2YIX4JaRCwh4bx8sEjmGbO1wCSBnJcQYx_bICVTzv", "Content-Type": "application/json"}
        data = {
                "title": "B331 requires immediate AV Help",
                "group": "bit-help",
                "customer_id" : "1",
                "article": {
                        "from": "bit-help@colorado.edu",
                        "subject": "B331 AV Problem",
                        "internal": False,
                        "body": "A user has requested AV assistance via QR Code in room: B331",
                        "type": "note",
                        }
                }
        r = requests.post(url='https://sandycay.int.colorado.edu/api/v1/tickets', json = data, headers = head)
        print(r.json)
        print(r.text)
######################################################################################
def zammad_e1b11():
	endpoint = "http://sandycay.int.colorado.edu/api/v1/ticket",
	head = {"Authorization":  "Token token=pVuWXy_46IAqKBzXmisJTyc2YIX4JaRCwh4bx8sEjmGbO1wCSBnJcQYx_bICVTzv", "Content-Type": "application/json"}	
	data = {
		"title": "E1B11 requires immediate AV Help",
        	"group": "bit-help",
        	"customer_id" : "1",
        	"article": {
        		"from": "bit-help@colorado.edu",
                	"subject": "E1B11 AV Problem",
                	"internal": False,
			"body": "A user has requested AV assistance via QR Code in room: E1B11",
                	#"sender": "BIT Help",
                	"type": "note",
			}
		}
	r = requests.post(url='https://sandycay.int.colorado.edu/api/v1/tickets', json = data, headers = head)
	print(r.json)
	print(r.text)
####
def zammad_e125():
	endpoint = "http://sandycay.int.colorado.edu/api/v1/ticket",
	head = {"Authorization":  "Token token=pVuWXy_46IAqKBzXmisJTyc2YIX4JaRCwh4bx8sEjmGbO1wCSBnJcQYx_bICVTzv", "Content-Type": "application/json"}	
	data = {
		"title": "E125 requires immediate AV Help",
        	"group": "bit-help",
        	"customer_id" : "1",
        	"article": {
        		"from": "bit-help@colorado.edu",
                	"subject": "E125 AV Problem",
                	"internal": False,
			"body": "A user has requested AV assistance via QR Code in room: E125",
                	#"sender": "BIT Help",
                	"type": "note",
			}
		}
	r = requests.post(url='https://sandycay.int.colorado.edu/api/v1/tickets', json = data, headers = head)
	print(r.json)
	print(r.text)
####
def zammad_e225():
	endpoint = "http://sandycay.int.colorado.edu/api/v1/ticket",
	head = {"Authorization":  "Token token=pVuWXy_46IAqKBzXmisJTyc2YIX4JaRCwh4bx8sEjmGbO1wCSBnJcQYx_bICVTzv", "Content-Type": "application/json"}	
	data = {
		"title": "E225 requires immediate AV Help",
        	"group": "bit-help",
        	"customer_id" : "1",
        	"article": {
        		"from": "bit-help@colorado.edu",
                	"subject": "E225 AV Problem",
                	"internal": False,
			"body": "A user has requested AV assistance via QR Code in room: E225",
                	#"sender": "BIT Help",
                	"type": "note",
			}
		}
	r = requests.post(url='https://sandycay.int.colorado.edu/api/v1/tickets', json = data, headers = head)
	print(r.json)
	print(r.text)
####
def zammad_b159():
	endpoint = "http://sandycay.int.colorado.edu/api/v1/ticket",
	head = {"Authorization":  "Token token=pVuWXy_46IAqKBzXmisJTyc2YIX4JaRCwh4bx8sEjmGbO1wCSBnJcQYx_bICVTzv", "Content-Type": "application/json"}	
	data = {
		"title": "B159 requires immediate AV Help",
        	"group": "bit-help",
        	"customer_id" : "1",
        	"article": {
        		"from": "bit-help@colorado.edu",
                	"subject": "B159 AV Problem",
                	"internal": False,
			"body": "A user has requested AV assistance via QR Code in room: B159",
                	#"sender": "BIT Help",
                	"type": "note",
			}
		}
	r = requests.post(url='https://sandycay.int.colorado.edu/api/v1/tickets', json = data, headers = head)
	print(r.json)
	print(r.text)
####
def zammad_b160():
	endpoint = "http://sandycay.int.colorado.edu/api/v1/ticket",
	head = {"Authorization":  "Token token=pVuWXy_46IAqKBzXmisJTyc2YIX4JaRCwh4bx8sEjmGbO1wCSBnJcQYx_bICVTzv", "Content-Type": "application/json"}	
	data = {
		"title": "B160 requires immediate AV Help",
        	"group": "bit-help",
        	"customer_id" : "1",
        	"article": {
        		"from": "bit-help@colorado.edu",
                	"subject": "B160 AV Problem",
                	"internal": False,
			"body": "A user has requested AV assistance via QR Code in room: B160",
                	#"sender": "BIT Help",
                	"type": "note",
			}
		}
	r = requests.post(url='https://sandycay.int.colorado.edu/api/v1/tickets', json = data, headers = head)
	print(r.json)
	print(r.text)
####
def zammad_b171():
	endpoint = "http://sandycay.int.colorado.edu/api/v1/ticket",
	head = {"Authorization":  "Token token=pVuWXy_46IAqKBzXmisJTyc2YIX4JaRCwh4bx8sEjmGbO1wCSBnJcQYx_bICVTzv", "Content-Type": "application/json"}	
	data = {
		"title": "B171 requires immediate AV Help",
        	"group": "bit-help",
        	"customer_id" : "1",
        	"article": {
        		"from": "bit-help@colorado.edu",
                	"subject": "B171 AV Problem",
                	"internal": False,
			"body": "A user has requested AV assistance via QR Code in room: B171",
                	#"sender": "BIT Help",
                	"type": "note",
			}
		}
	r = requests.post(url='https://sandycay.int.colorado.edu/api/v1/tickets', json = data, headers = head)
	print(r.json)
	print(r.text)
####
def zammad_b180():
	endpoint = "http://sandycay.int.colorado.edu/api/v1/ticket",
	head = {"Authorization":  "Token token=pVuWXy_46IAqKBzXmisJTyc2YIX4JaRCwh4bx8sEjmGbO1wCSBnJcQYx_bICVTzv", "Content-Type": "application/json"}	
	data = {
		"title": "B180 requires immediate AV Help",
        	"group": "bit-help",
        	"customer_id" : "1",
        	"article": {
        		"from": "bit-help@colorado.edu",
                	"subject": "B180 AV Problem",
                	"internal": False,
			"body": "A user has requested AV assistance via QR Code in room: B180",
                	#"sender": "BIT Help",
                	"type": "note",
			}
		}
	r = requests.post(url='https://sandycay.int.colorado.edu/api/v1/tickets', json = data, headers = head)
	print(r.json)
	print(r.text)


