Mobile Coverage Analyzer is a small web application built with Python (Flask),
with a simple HTML interface.

The purpose of this app is to demonstrate how mobile network performance
can change based on real-world conditions, rather than treating signal strength
as a fixed value.

The user can adjust parameters such as environment, distance from the cell tower,
walls and obstacles, mobility, and network type.
Based on these inputs, the system produces a rule-based estimation of
signal quality, latency, and connection stability.

This approach helps translate theoretical concepts from Mobile Computing
into a visual and interactive form.

The application is intended for learning and demonstration purposes,
not for real signal measurement.


Originally developed as an assignment
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

