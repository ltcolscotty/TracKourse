# NotifyRegisterASU
Project for automating notifications for asu

The goal of this project:
Periodically scan through desired class codes. This project assumes the student has done their due dilligence on what classes they are qualified to take and that they've planned out their schedule.
- Effectively, this will be a self-hosted, free for all version of a service like courseer with delay only being limited
by the server load balancing of ASU's class search system and the internet speed the device running the program has access to. 
- This project is expected to be maintained until 2028 with continual updates to adjust for UI changes on the class search site as needed.

Running this should:
- Search the class portal for open spots
- View the professor, if the professor and class code match, a notification will be sent to the email or phone number desired.

## To-Do:
- Restructure to use playwright instead of selenium for increased speeds

## Setup

1. Set up a python environment and run ```pip install -r requirements.txt```
2. Run to install playwright tools ```playwright install```
3. Set up ```const_config.py``` with the classes that are desired
4. Run main.py; preferably keep it as a background task while you're out and about during the day and shut it down before you go to bed when you aren't going to want to recieve messages.
---