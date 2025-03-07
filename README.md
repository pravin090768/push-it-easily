
This repository contains automation tests that validate the functionality of logging into hudl.com using Python, Selenium, and pytest. The login credentials (username and password) are securely stored in a .env file, and pytest is used to run the tests.

Prerequisites
Before running the tests, make sure you have the following dependencies installed:

Python 3.x
Selenium
pytest
python-dotenv (to load environment variables from the .env file)
WebDriver for your Chrome browser

Creating the .env File
Before running the tests, you need to create a .env file that contains your login credentials (username and password). This file should be placed in the root directory of the project.

.env file:
USER_NAME=your_username_here
USER_PASSWORD=your_password_here

Replace your_username_here and your_password_here with your actual login credentials.
