## Python Robot Arm

I aimed to use a web GUI to control the robot arm, but encountered an error. To control your robot arm, please use the `TKGui.py` file.

The Python Robot Arm comes with a startup file to make it easier for users. This allows you to launch the program without worrying about dependencies or additional software needed to run it.

### Instructions:

1. Clone this repository using Git.
2. Open the terminal on your chosen Raspberry Pi.
3. Navigate to the directory where you downloaded the software.
4. Run the `startup.sh` script to download all the dependencies for the application by entering the command: `sudo ./startup.sh`
5. After that, run the command: `python3 TKGui.py`
6. You will now see the user interface (refer to the picture below).
7. Always home the robot first to ensure that the software and hardware are synchronized.
8. You now have full control to instruct the robot to move in any direction. 
