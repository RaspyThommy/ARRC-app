ARRC-app

## **Android-phonegap robot controler**
This is an android and phonegap app that allows to control a robot built with a 3D printer ([Trendy (3&D)](https://www.google.com/maps/place/Trendy+(3%26D)/@45.450429,9.2187614,17z/data=!3m1!4b1!4m5!3m4!1s0x4786c5d95862bab9:0x810914cd302afcd9!8m2!3d45.4504253!4d9.2209501?hl=it)) run by a python server.

**Requirement**

- Android: Android Studio and a device with min API 29
- Phonegap: Phonagap and cordova plugin, Android Studio and a device with min API 24
- Python: Python 3.7 and opencv library

**3D project**

I changed a thingiverse project   with the new requirement to make space for:

- Battery for raspberry
- Battery for motors
- Motors
- Controler motors
- Pi-camera

**Circuit project**

This is the circuit project

**Server:**

- Python:
	we need to install rasbian os on the raspberry-pi and after that we install raspAP to allow raspberry create a Wi-Fi.
	This is the steps to install it:
	
	
		- open a terminal window and paste this code:
			`curl -sL https://install.raspap.com |bash`
		- the installation start automatically after the download
		- now we need to configure the access-point:
			- search on your browser the ip of your raspberry
			- enter the username and password:
				- admin
				- secret
			- configure your Wi-Fi
	
	After that you need to download opencv-python using this code:
	
	`pip3 install opencv-python`
	
	Now you can download the python script and run it on your raspberry.
	
**Client app**
	
- Andorid app:
	download the andorid folder and open it on Android Studio. 
	
- Phoegap app:
	To download phonegap go ti this [link](https://phonegap.com/getstarted/)
	download the phonegap folder. Open an android phone emulator and on termial write:
		`phonegap run android`
	
