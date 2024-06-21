import datetime
import time
import json
import win32gui
import matplotlib.pyplot as plt
import pyautogui as gui
import logging

# Constants
ACTIVITIES_FILE = "activities.json"
MIN_ACTIVITY_DURATION = 1  # Minimum duration threshold in seconds
GRACE_PERIOD = 10  # Grace period between activity switches in seconds

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_active_window_name():
    """Returns the name of the currently active window."""
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

def load_activities(filepath):
    """Loads activities from a JSON file."""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_activities(filepath, activities):
    """Saves activities to a JSON file."""
    with open(filepath, "w") as f:
        json.dump(activities, f, indent=4)

def add_time_entry(activities, activity_name, start_time, end_time):
    """Adds a time entry to the activities dictionary."""
    if activity_name not in activities:
        activities[activity_name] = []
    activities[activity_name].append({
        "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "end_time": end_time.strftime("%Y-%m-%d %H:%M:%S"),
        "duration": (end_time - start_time).total_seconds()
    })

def merge_duplicate_activities(activities):
    """Merge or combine entries for duplicate activities."""
    merged_activities = {}
    for activity_name, entries in activities.items():
        if activity_name.lower() in merged_activities:
            merged_activities[activity_name.lower()].extend(entries)
        else:
            merged_activities[activity_name.lower()] = entries
    return {k: v for k, v in merged_activities.items()}

def plot_activities(activities):
    """Plots the durations of the activities over time."""
    activities = merge_duplicate_activities(activities)
    num_activities = len(activities)
    if num_activities == 0:
        print("No activities recorded yet.")
        return

    fig, axs = plt.subplots(1, num_activities, figsize=(20, 10))

    if num_activities == 1:
        axs = [axs]

    for i, (activity_name, entries) in enumerate(activities.items()):
        durations = [entry["duration"] / 3600 for entry in entries]
        axs[i].hist(durations, alpha=0.8)
        axs[i].set_title(activity_name)
        axs[i].set_xlabel('Duration (hours)')
        axs[i].set_ylabel('Frequency')
        axs[i].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()

def is_idle(start_time, threshold):
    """Checks if the cursor position remains unchanged for the threshold duration."""
    end_time = datetime.datetime.now()
    initial_pos = gui.position()
    while (end_time - start_time).total_seconds() < threshold:
        time.sleep(1)  # Check every second
        if gui.position() != initial_pos:
            return False
        end_time = datetime.datetime.now()
    return True

def consolidate_short_activities(activities, max_gap=10):
    """Consolidates short activities into longer entries if they occur close together."""
    consolidated_activities = {}
    for activity_name, entries in activities.items():
        if activity_name not in consolidated_activities:
            consolidated_activities[activity_name] = []

        entries.sort(key=lambda x: x['start_time'])
        current_entry = entries[0]
        for entry in entries[1:]:
            gap = datetime.datetime.strptime(entry['start_time'], "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(current_entry['end_time'], "%Y-%m-%d %H:%M:%S")
            if gap.total_seconds() <= max_gap:
                current_entry['end_time'] = entry['end_time']
                current_entry['duration'] += entry['duration']
            else:
                consolidated_activities[activity_name].append(current_entry)
                current_entry = entry
        consolidated_activities[activity_name].append(current_entry)
    return consolidated_activities

def track_activities():
    """Tracks the active window and records time spent on each activity."""
    activities = load_activities(ACTIVITIES_FILE)
    active_window_name = ""
    start_time = datetime.datetime.now()

    try:
        while True:
            new_window_name = get_active_window_name()
            logging.debug(f"Active window changed: {new_window_name}")
            if new_window_name != active_window_name:
                if active_window_name:
                    if not is_idle(start_time, GRACE_PERIOD):
                        end_time = datetime.datetime.now()
                        duration = (end_time - start_time).total_seconds()
                        if duration >= MIN_ACTIVITY_DURATION:
                            logging.debug(f"Recording activity: {active_window_name} ({duration} seconds)")
                            add_time_entry(activities, active_window_name, start_time, end_time)
                            save_activities(ACTIVITIES_FILE, activities)
                    start_time = datetime.datetime.now()
                active_window_name = new_window_name
            time.sleep(1)
    except KeyboardInterrupt:
        end_time = datetime.datetime.now()
        if not is_idle(start_time, GRACE_PERIOD):
            duration = (end_time - start_time).total_seconds()
            if duration >= MIN_ACTIVITY_DURATION:
                add_time_entry(activities, active_window_name, start_time, end_time)
                save_activities(ACTIVITIES_FILE, activities)
        activities = consolidate_short_activities(activities)
        save_activities(ACTIVITIES_FILE, activities)
        plot_activities(activities)

if __name__ == "__main__":
    track_activities()
