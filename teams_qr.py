from flask import Flask, render_template, after_this_request, request, url_for, redirect, session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS, cross_origin
from flask_executor import Executor
import datetime
import requests
import json
import teams 
import zammad

##########################################################
application = Flask(__name__, template_folder="templates")
executor = Executor(application)
CORS(application)
##########################################################
limiter = Limiter(
	 application,
	 key_func=get_remote_address,
	 default_limits=["10/5minutes"]
)
application.config['EXECUTOR_TYPE'] = 'thread'
application.config['EXECUTOR_MAX_WORKERS'] = 5
###Uncomment this section to redirect based on time of day. Change times as needed. Be sure to update URL###
#@application.before_request
#def check_time():
#    now = datetime.datetime.now().time()
#    start_time_1 = datetime.time(7, 0, 0)
#    end_time_1 = datetime.time(8, 59, 0)
#    start_time_2 = datetime.time(17, 1, 0)
#    end_time_2 = datetime.time(20, 0, 0)
#    if (start_time_1 <= now <= end_time_1 or start_time_2 <= now <= end_time_2) and '<your url goes here>' in request.host and request.path != "/test_dummy":
#        return redirect('/redir')
##########################################################

#####Define App Routes Below####
@application.route("/")
def index():
        	return render_template('index.html')
#######################Uncomment if using time based redir. This route will go to your redirect page.##################################
#@application.route("/redir")
#def redir2():
#    return redirect("<time based redirect url goes here, if using>")
####################replace example with your flask route######################################
@application.route("/EXAMPLE")
#Rate limiting at 1 scan per 5 minutes. 
@limiter.limit("1 per 5 minute")
#Insert actual teams_function name from teams.py#
def teams_<function name>():
		executor.submit(teams_function);
		return render_template('new.html')
##########################################################
#########
@application.route("/test_dummy")
def test_dummy():
	return render_template('new.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0')

