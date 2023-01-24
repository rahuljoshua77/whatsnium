# Project Title: Whatsnium

## Description
This project is a simple WhatsApp API that allows you to send messages to WhatsApp numbers via a web interface. You can also check your login status and send messages to spesific numbers.

## Features
- QR code login
- Check login status
- Send a message

![Checking](https://user-images.githubusercontent.com/73378179/214401853-a55166c4-4179-4d9e-a7eb-464ab5c63d35.PNG)
![landing-page](https://user-images.githubusercontent.com/73378179/214401862-6a9d475e-36ff-4761-855d-1418f1376880.PNG)
![QR-code](https://user-images.githubusercontent.com/73378179/214401864-6a61736f-4b40-4b1a-bd9d-7097ece08453.PNG)
![welcome](https://user-images.githubusercontent.com/73378179/214401867-8e52371c-a06f-470c-a5f0-a1fc042937b8.PNG)

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
- Add a way for the user can chat all member groups
- Add a way for the user can add mass contact to groups
- Implement a way for the user to log out of WhatsApp Web
- Add a way for the user to see their chat history
- Add a way for the user to create groups and add members to the groups
