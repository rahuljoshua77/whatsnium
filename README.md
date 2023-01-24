# Whatsnium

## Description
This project is a simple WhatsApp API that allows you to send messages to WhatsApp numbers (now just via API) via a web interface. You can also check your login status and send messages to spesific numbers.

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

API Documentation
=======================

  

Endpoint: `/check_login`
------------------------

This endpoint is used to check if the user is logged in to WhatsApp Web.

### Method: `GET`

### Response:

This endpoint will return a JSON object with the following structure:

    {
        "status": "logged in"
    }
    

If the user is logged in, the "status" value will be "logged in". If the user is not logged in, the "status" value will be "not logged in". If an error occured while checking the connection, the "status" value will be "error" and it will include a "message" value with the error message.

Endpoint: `/send_message`
-------------------------

### Method: `POST`

#### Payload:

    {
        "contact": "6282\*\*72412",
        "message": "Hello, this is a test message"
    }
    

#### Description

This endpoint is used to send a message to a specific contact on WhatsApp. The `contact` field should contain the phone number of the recipient in international format (with the country code included), and the `message` field should contain the message text that you want to send.

#### Response:

Upon a successful request, the API will return a `200 OK` status and the message will be sent to the specified contact. If there is an error, such as an invalid phone number or an error with the WhatsApp Web session, the API will return a `400 Bad Request` status with an error message.

#### Example

Sending a message to contact `62821***2412` with message text "Hello, this is a test message":

    curl -X POST http://api-wa.my.id//send\_message -H "Content-Type: application/json" -d '{"contact": "628217\*\*\*2412", "message": "Hello, this is a test message"}'
