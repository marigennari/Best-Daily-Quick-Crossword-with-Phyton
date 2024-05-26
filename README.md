# What is this project about?

This project is about using visual studio code and python to test the following scenario for the game Best Daily Quick Crossword powered by Arkadium:
- Start the game;
- Navigate to a specific day within the game;
- Verify that the date of puzzle (day) was loaded correctly;
- Interact with the game controls (buttons, navigations) to complete the puzzle;
- Take a screenshot of the finished puzzle;

----------------------------------------------------------------------------------------------------------------------------------

## Prerequisites

**Python:** Make sure you have Python installed (version 3.6 or later). You can download it from python.org.

**Visual Studio Code:** A code editor for running and editing Python scripts. Download and install it from code.visualstudio.com.

**Python Extension for Visual Studio Code:** Install the Python extension for VS Code to enhance the Python development experience. You can find it in the VS Code marketplace.

**pip:** This is the package installer for Python. It is included by default with Python installations.

**Google Chrome:** The project uses the Chrome browser for automation. Download and install Google Chrome from google.com/chrome.

**ChromeDriver:** This is needed to drive the Chrome browser. Download the version that matches your installed Chrome version from chromedriver.chromium.org.

**Selenium:** A Python package for web automation. Install it using pip:
```
pip install selenium
```

**PyAutoGUI:** A Python package for GUI automation. Install it using pip:
```
pip install pyautogui
```

----------------------------------------------------------------------------------------------------------------------------------

## Setting Up the Environment

**Clone the Repository:**
```
git clone <repository-url>
cd <repository-name>
```

**Download and Configure ChromeDriver:**

- Download ChromeDriver from chromedriver.chromium.org and place it in a directory of your choice (remember to check the correct chromedriver version according to your current version of Google Chrome).
- Update the driver_path variable in the script to point to the location of your ChromeDriver executable.

**Running the Script**

Ensure your driver_path is correctly set to the location of your ChromeDriver executable in the script:

Example:
```
driver_path = 'C:/Users/marig/chromedriver.exe'  # Update this path to your ChromeDriver path
```

**Open the project in Visual Studio Code**
```
code .
```

**Run the script using Python:**
```
python CrosswordTest.py
```

----------------------------------------------------------------------------------------------------------------------------------

## Script Overview

**Here’s a brief overview of what the script does:**

**Setup and Initialization:**
Sets up logging.
Configures and initializes the Chrome WebDriver.


**Navigates to the Crossword Page:**
Opens the specified URL.
Switches to the required iframes and closes any advertisement.


**Interacts with the Game:**
Maximizes the browser window.
Clicks the "Play" button.
Enables "Auto Check".
Iterates through each letter of the alphabet, testing it in the crossword square.


**Reveals the Puzzle:**
Clicks the necessary buttons to reveal the entire puzzle.


**Takes a Screenshot:**
Captures a screenshot of the final state and saves it to the specified path.

----------------------------------------------------------------------------------------------------------------------------------

## Notes
- Adjust all paths as necessary to match your local setup.
- Ensure you have the necessary permissions to run the script and save files in the specified locations.
- You might need to adjust sleep times and coordinates based on your screen resolution and browser settings.
