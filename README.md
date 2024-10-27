# TracKourseASU
Project for automating seat monitoring for courses during registering for asu

The goal of this project:
Periodically scan through desired class codes. This project assumes the student has done their due dilligence on what classes they are qualified to take and that they've planned out their schedule.
- Effectively, this will be a self-hosted, free for all version of a service like courseer with delay only being limited
by the server load balancing of ASU's class search system and the internet speed the device running the program has access to
- This project is expected to be maintained until 2028 with continual updates to adjust for UI changes on the class search site as needed.
- Advantages of using this project: Free (i like free stuff), No limit on classes you can track, the only bottleneck is internet and hardware speed
- Potential cons: Not the most user friendly config and running experience (yet), but I've written plenty of documention to alleviate this as much as possible

Running this should:
- Search the class portal for open spots
- View the professor, if the professor and class code match, a notification will be sent to the email or phone number desired.

## To-Do:
- (2025) Implement search_by_id to get more focused results
- (2025) Proper hybrid class handling
- (2025) Docker container & instructions for easy and consistent deployment

## Setup

1. Set up a python environment and run ```pip install -r requirements.txt```
2. Run to install playwright tools ```playwright install```
3. Set up ```const_config.py``` with the classes that are desired
4. Set up ```.env```: Create a file in this folder named '.env' and follow the instructions in the env setup
5. Run the command: ```python alert_test.py```, if you recieve your messages in the specified email or phone number, you can continue
6. Run main.py with ```python main.py```, use ctrl+c to stop the program if you need to make adjustments to constants and rerun the program

## .env file setup:

Copy and paste this into a file named .env
```python
SENDER_EMAIL=''
SENDER_PASSWORD=''
TARGET_EMAIL=''
PHONE_NUMBER=''
CARRIER=''
```

```SENDER_EMAIL``` Will be the sender gmail account. Using a gmail account, setup and enable 2fa, then

```SENDER_PASSWORD```
1. Go to https://myaccount.google.com/apppasswords
2. Sign in to your Google Account if prompted
3. Under "Select app", choose the app you're using or select "Other" and give it a name
4. Under "Select device", choose your device or select "Other" and name it
5. Click "Generate"
6. Copy the 16 letter code that appears, and set this in your ```SENDER_PASSWORD``` variable.

```TARGET_EMAIL``` should only be filled if you plan on recieving alerts through email.

```PHONE_NUMBER``` your entire phone number including country code

```CARRIER``` the carrier that you use. Supported carriers: 
- ``att``
- ``tmobile``
- ``verizon``
- ``sprint``
- ``boost``
- ``cricket``
- ``uscellular``
- ``virgin``

The finished product should look something like:
```python
SENDER_EMAIL='example1@gmail.com'
SENDER_PASSWORD='AAAA BBBB CCCC DDDD'
TARGET_EMAIL='my.email@gmail.com'
PHONE_NUMBER='11234567890' # US based phone number of (123)-456-7890, US Country code is '1'
CARRIER='att'
```

## Curious about how this works?
Most of the main code uses default python packages, with the exception of these packages<br>
- Webscraping tool: ``Playwright``
- Message Sending: ```smtplib```

Copyright © Aidan Yung