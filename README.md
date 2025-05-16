# mars-rover-ui
A U/I for mars rover

![large](https://github.com/user-attachments/assets/5cda5c41-c3da-49e8-8370-4aeb6cf16941)


**Project Overview:**
To create a custom state of the art UI for our mars rover project that displays telemetry and provides an interface for controlling the rover.
We are integrating 3 ESP32s in total - 2 traditional ones and 1 ESP32-CAM. The idea is to host a server using a computer, and connect to it via ESP32. The data will be trasnsmitted using websockets and be used by the clients (the ground control station and ESP32s) for communication. 

**Objective:**
1. Build the interface using tkinter.
2. Add elements to check for connection between server and ESP32. (reconnect if not available)
3. After successfull connection, display the simulation of the rover on a canvas.

**How to Build the App:**
1. clone using: `git clone https://github.com/Dasux/mars-rover-ui`
2. enter the directory: `cd mars-rover-ui`
3. create a virtual environment if your python is managed by your OS (like in most linux distros): `python3 -m venv myvenv`
4. activate the virtual environment: `source myvenv/bin/activate` for Linux .... `myvenv/bin/activate` for Windows.
5. install custom tkinter: `pip install customtkinter`
6. run the python scrip `main.py`
