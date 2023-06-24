# Sense Hat Temperature and Humidity display

This is a simple python script to display the current temperature and humidity on a Raspberry Pi with a Sense Hat's built-in sensors. It switches between a scrolling message and a visual colour indicator using the Sense Hat's LED matrix.

The file can be set to automatically run on boot by adding the following line to the `/etc/rc.local` file:

`sudo python /home/pi/picam_simple.py &`

The `&` is important as it allows the script to run in the background.

The script can be stopped by running the following command:

`sudo killall python`

