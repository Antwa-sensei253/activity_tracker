import psutil
import time
import json
from datetime import datetime
from threading import Thread
import signal
import sys
from flask import Flask, render_template, jsonify

app = Flask(__name__)

app_usage = {}
tracking_duration = 3600 #(3600 seconds = 1 hour)
report_interval = 10

def get_active_window():
    import win32gui
    window = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(window)
    return window_title

def track_app_usage():
    global app_usage
    start_time = time.time()
    end_time = start_time + tracking_duration

    try:
        while time.time() < end_time:
            current_app = get_active_window()
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if current_app in app_usage:
                app_usage[current_app]['duration'] += report_interval
            else:
                app_usage[current_app] = {'start_time': current_time, 'duration': report_interval}

            time.sleep(report_interval)
    finally:
        save_usage_to_json(app_usage)

def save_usage_to_json(app_usage, filename='app_usage.json'):
    with open(filename, 'w') as f:
        json.dump(app_usage, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify(app_usage)

def signal_handler(sig, frame):
    global app_usage
    print("Interrupt received, saving usage data to JSON...")
    save_usage_to_json(app_usage)
    print("App usage tracking completed.")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    tracking_thread = Thread(target=track_app_usage)
    tracking_thread.start()

    app.run(debug=True)
