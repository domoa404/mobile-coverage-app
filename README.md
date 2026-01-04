Mobile Coverage Analyzer 

This is a simple web application built with Python using Flask,
with an HTML-based interface.

It explains, in a practical way, why mobile network signal
can be strong in one place and weak in another.

The app works by letting the user change common real-world factors
such as location, distance from the cell tower, walls, movement,
and network type (3G / 4G / 5G / Wi-Fi).

Based on these inputs, the system estimates signal quality
and shows how different conditions affect network performance.

This is an educational demo,
not a real signal measurement tool.

Source code and run instructions:
https://github.com/domoa404/mobile-coverage-app

Originally created as an assignment
for the Mobile Computing course.



## Screenshots

<img src="images/ui-main.jpg" width="400">
<img src="images/ui-result.jpg" width="400">


How to run the project

 1) Clone the repository
```bash
git clone https://github.com/domoa404/mobile-coverage-app.git
cd mobile-coverage-app
Install requirements

Make sure Python is installed, then run:

2)pip install -r requirements.txt

3) Run the application
python app.py

4) Open in browser

Open your browser and go to:

http://127.0.0.1:5000

