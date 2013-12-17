* Install [Python2.7][0] and make sure python is added in env variabales
* config.py is the config file
* change the following in config.py
	* PUBLISHSETTINGS_FILE <\<path of publish setting file>>
	* LOG_FILE <\<path for the log file>>
	* FILE_PATH <\<path for the Json log file>>
	* CERT_FILE <\<path for the .pem file>>
	* SUBSCRIPTION_ID <\<Subscription id of azure account>>
* open cmd prompt and cd to proj folder(where AutomationScript.py and config.py are present)
* run the script using following command "python AutomationScript.py"

# Note 
* if GLOBAL_FLAG=0 then only those command which has its flag value as 1 will execute
* if GLOBAL_FLAG=1 the all the commands will execute
* in GLOBAL_FLAG=0 mode change flag variables(present below #**FLAG VALUES**) to run or skip commands
 
[0]: http://www.python.org/download/releases/2.7.3/
