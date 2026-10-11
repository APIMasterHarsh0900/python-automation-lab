# Python Server Health Monitor

A simple Python program that keeps an eye on how your computer’s resources are doing and gives updates based on your chosen limits.

## What it can do

* Check CPU usage
* Check how much memory is being used
* Keep track of disk space
* Tell you if things are running normally or if there's a warning
* Use a handy, reusable function to check if numbers are within normal limits

## What it uses

* Python programming language
* psutil library to get system info

## How to set it up

Create a virtual space for the program, activate it, then install the needed tools:

powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r server-health-automation/requirements.txt


## How to run it

From the main folder of the project:

powershell
python .\server-health-automation\main.py


## Where things stand

This is the first version; it gathers data about your system and checks if it's within the set limits.

## Future improvements

* Adding time stamps to reports
* Better logging and error handling
* Automatic tests to ensure everything works correctly
* Options to customize settings through command-line
* Better disk checks across different operating systems