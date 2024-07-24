# App Usage Tracker

## Overview

The App Usage Tracker is a Python-based web application that monitors and logs the active windows on a user's computer, recording the time spent on each application. The collected data is stored in a JSON file and can be visualized in real-time through a web dashboard powered by Flask.

## Dependencies

Ensure the following Python packages are installed:

- `psutil`: Used for system and process utilities.
- `flask`: Provides the web framework for creating the dashboard.
- `json`: Handles reading and writing of JSON data.
- `datetime`: Manages date and time operations.
- `threading`: Allows tracking to run in a separate thread.
- `pywin32` (specifically `win32gui`): Required for accessing the active window information on Windows.

You can install the required packages using pip:





```sh
pip install psutil flask pywin32
```

## Directory Structure

The project follows this directory structure:

plaintext

Copy code
```sh
app_tracker/ ├── app.py # Main Flask application 
			├── templates/ # Directory for HTML templates
			 │ └── index.html # Main dashboard HTML template
			  ├── static/ # Directory for static files
			  │ └── styles.css # Custom CSS styles
```

## Constants

- `tracking_duration`: The duration for which the tracker runs, in seconds (default is 3600 seconds).
- `report_interval`: The interval at which the tracker logs the active window, in seconds (default is 10 seconds).
- `app_usage.json`: The filename where the app usage data is stored.

## Functions

### `get_active_window()`

Retrieves the name of the currently active window on the user's computer. This function uses the `win32gui` library, which is specific to Windows.

### `track_app_usage()`

Tracks the active window and updates the `app_usage` dictionary with the time spent on each application. This function runs in a separate thread to allow continuous tracking.

### `save_usage_to_json(app_usage, filename='app_usage.json')`

Saves the app usage data to a JSON file. This ensures that the data is persisted and can be loaded later.

### `signal_handler(sig, frame)`

Handles script interruptions (e.g., Ctrl+C) and ensures that the usage data is saved to the JSON file before the program exits.

### `index()`

Serves the main dashboard HTML template using Flask. This route renders the user interface for viewing the app usage data.

### `data()`

Provides the app usage data as a JSON response. This route is used by the frontend to fetch the latest app usage data and update the dashboard in real-time.

## Running the Flask Application

To run the App Usage Tracker, follow these steps:

1. Navigate to the directory where `app.py` is located.
    
2. Start the Flask application by executing the following command:

    `python app.py`
    
3. Open your web browser and go to `http://127.0.0.1:5000/` to view the dashboard.
    

## Dashboard
testing 
```sh
Hello Wolrd!;
```
The web dashboard, built with HTML and Bootstrap, provides a user-friendly interface for viewing the tracked application usage. It periodically fetches the latest data from the backend and displays it in a table format. The dashboard is styled using a custom CSS file to enhance its visual appeal.

## Notes

- Ensure you have the necessary permissions to access and manipulate the active window information on your operating system.
- The script is designed to work on Windows due to the use of `win32gui` for window management. Adaptations are required for other operating systems if you want cross-platform support.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.
