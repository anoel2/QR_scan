from flask import Flask, render_template, after_this_request, request, url_for, redirect, session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS, cross_origin
from flask_executor import Executor
import datetime
import requests
import json
from teams import teams_a104, teams_a108, teams_a115, teams_a171h, teams_a400, teams_b115, teams_b231, teams_b331, teams_e1b11, teams_e125, teams_e225, teams_b159, teams_b160, teams_b171, teams_b180
from zammad import zammad_a104, zammad_a108, zammad_a115,zammad_a171h, zammad_a400, zammad_b115, zammad_b231, zammad_b331, zammad_e1b11, zammad_e125, zammad_e225, zammad_b159, zammad_b160, zammad_b171, zammad_b180

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

###############UNCOMMENT IN ORDER TO ENABLE SERVICE NOW CHECKING################
@application.before_request
####checks datetime prior to running any functions. Redirects all URI to /redirect between 0700-0900, and 1700-1900####
#def check_time():
#    now = datetime.datetime.now().time()
#    start_time_1 = datetime.time(7, 0, 0)
#    end_time_1 = datetime.time(8, 59, 0)
#    start_time_2 = datetime.time(17, 1, 0)
#    end_time_2 = datetime.time(20, 0, 0)
#    if (start_time_1 <= now <= end_time_1 or start_time_2 <= now <= end_time_2) and 'adak.int.colorado.edu' in request.url:
#       return redirect('/redir')
#@app.before_request
def check_time():
    now = datetime.datetime.now().time()
    start_time_1 = datetime.time(7, 0, 0)
    end_time_1 = datetime.time(8, 59, 0)
    start_time_2 = datetime.time(17, 1, 0)
    end_time_2 = datetime.time(20, 0, 0)
    if (start_time_1 <= now <= end_time_1 or start_time_2 <= now <= end_time_2) and 'adak.int.colorado.edu' in request.host and request.path != "/test_dummy":
        return redirect('/redir')
##########################################################

#####Define App Routes Below####
@application.route("/")
def index():
        	return render_template('index.html')
##########################################################
@application.route("/redir")
def redir2():
    return redirect("https://buff.link/classroomsupport")
##########################################################
@application.route("/a104")
@limiter.limit("1 per 5 minute")
#@application.after_this_request
def a104():
		executor.submit(zammad_a104);
		executor.submit(teams_a104);
		return render_template('new.html')
##########################################################
@application.route("/a108")
@limiter.limit("1 per 5 minute")
def a108():
		executor.submit(zammad_a108);
		executor.submit(teams_a108);
		return render_template('new.html');
##########################################################
@application.route("/a115")
@limiter.limit("1 per 5 minute")
def a115():
		executor.submit(zammad_a115);
		executor.submit(teams_a115);
		return render_template('new.html')
##########################################################
@application.route("/a171h")
@limiter.limit("1 per 5 minute")
def a171h():
		executor.submit(zammad_a171h);
		executor.submit(teams_a171h);
		return render_template('new.html')
##########################################################
@application.route("/a400")
@limiter.limit("1 per 5 minute")
def a400():
		executor.submit(zammad_a400);
		executor.submit(teams_a400);
		return render_template('new.html')
##########################################################
@application.route("/b115")
@limiter.limit("1 per 5 minute")
def b115():
		executor.submit(zammad_b115);
		executor.submit(teams_b115);
		return render_template('new.html')
##########################################################
@application.route("/b231")
@limiter.limit("1 per 5 minute")
def b231():
		executor.submit(zammad_b231);
		executor.submit(teams_b231);
		return render_template('new.html')
##########################################################
@application.route("/b331")
@limiter.limit("1 per 5 minute")
def b331():
		executor.submit(zammad_b331);
		executor.submit(teams_b331);
		return render_template('new.html')
##########################################################
@application.route("/e1b11")
@limiter.limit("1 per 5 minute")
def e1b11():
		executor.submit(zammad_e1b11);
		executor.submit(teams_e1b11);
		return render_template('new.html')
#######	
@application.route("/e125")
@limiter.limit("1 per 5 minute")
def e125():
		executor.submit(zammad_e125);
		executor.submit(teams_e125);
		return render_template('new.html')
#######	
@application.route("/e225")
@limiter.limit("1 per 5 minute")
def e225():
		executor.submit(zammad_e225);
		executor.submit(teams_e225);
		return render_template('new.html')
#######	
@application.route("/b159")
@limiter.limit("1 per 5 minute")
def b159():
		executor.submit(zammad_b159);
		executor.submit(teams_b159);
		return render_template('new.html')
#######	
@application.route("/b160")
@limiter.limit("1 per 5 minute")
def b160():
		executor.submit(zammad_b160);
		executor.submit(teams_b160);
		return render_template('new.html')
#######		
@application.route("/b171")
@limiter.limit("1 per 5 minute")
def b171():
		executor.submit(zammad_b171);
		executor.submit(teams_b171);
		return render_template('new.html')
########		
@application.route("/b180")
@limiter.limit("1 per 5 minute")
def b180():
		executor.submit(zammad_b180);
		executor.submit(teams_b180);
		return render_template('new.html')
#########
@application.route("/test_dummy")
def test_dummy():
	return render_template('new.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0')

