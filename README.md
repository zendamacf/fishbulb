# fishbulb

[![Build Status](https://travis-ci.com/zachdlang/fishbulb.svg?branch=master)](https://travis-ci.com/zachdlang/fishbulb)

## Service Setup
1. Copy the service files, so Gunicorn can be automatically started & reloaded.
	
	```
	cp <Location>/fishbulb/gu-app.service /etc/systemd/system/gu-fishbulb.service
	```

1. Activate the service file, enable it at boot/resart, and start the app.

	```
	systemctl daemon-reload
	systemctl enable gu-fishbulb
	systemctl start gu-fishbulb
	```