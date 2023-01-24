# Project Title: Whatsnium

## Description
This project is a simple WhatsApp API that allows you to send messages to WhatsApp numbers via a web interface. You can also check your login status and send messages to spesific numbers.

## Installation
- Make sure you have Python and Flask installed on your machine
- Clone the repository
- Create a virtual environment and activate it
- Run `pip install -r requirements.txt` to install the necessary packages
- Run `python app.py` to start the server
- Go to `http://localhost:5000` in your browser

## Usage
- Go to `http://localhost:5000` in your browser
- Scan the QR code to log in to WhatsApp Web
- Once logged in, you can send messages to numbers by going to `http://localhost:5000/send_message` and providing the necessary information in the payload
- You can also check your login status by going to `http://localhost:5000/check_login`

## To-Do
- Add more functionality to the API such as sending media and documents
- Implement a way for the user to log out of WhatsApp Web
- Add a way for the user to see their chat history
- Add a way for the user to create groups and add members to the groups
