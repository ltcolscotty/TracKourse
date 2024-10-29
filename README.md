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
- Search the class portal for open spots on the specified list
- Notify the selected email and/or phone number of a spot opening when a change is detected

## System requirements
- Node.js (https://nodejs.org/en/download/package-manager)
- Python 3.11.5 or higher (https://www.python.org/downloads/)
- Google Chrome
- Windows 10/11

## To-Do:
- (2025) Proper hybrid class handling
- (2025) Package implementation for easy download and usage

## Executable Distribution setup
- Ensure ```trackourse_config.ini``` is in the same folder as alert_tester and main
- Set up ```trackourse_config.ini``` using the instructions provided below
- Ensure you get pinged when you run alert_tester, if you don't recieve messages, something might be wrong
- Run main once you have your desired classes and notification methods set up

## Manual program setup

1. Set up a python environment and run ```pip install -r requirements.txt```
2. Run to install playwright tools ```playwright install```
3. Set up ```trackourse_config.ini``` with the classes that are desired
5. CD into src/trackourse and run the command: ```python alert_test.py```, if you recieve your messages in the specified email or phone number, you can continue
6. CD int src/trackourse and run main.py with ```python main.py```, use ctrl+c to stop the program if you need to make adjustments to constants and rerun the program

### Manual Execution Production
- Ensure your python environment has ```pyinstaller```
- Run the command below in the root directory of the project, and check the newly created ```dist``` folder
```bash
pyinstaller --onefile --add-data="trackourse_config.ini" --icon=Trackourse.ico src/trackourse/main.py
```

## trackourse_config.ini file setup:

```notif_method``` you can set this to be: sms, email, both

```url_year``` Set this to be class search's last 4 digits in the url. This can also be broken down as 2xxx where 2 is default, x25x as in the year, and xxx1 where 1 is spring, 7 is fall. An example: 2027 fall is expected to be 2277, or 2030 spring is expected to be 2301.

```wait_time``` time between scans in seconds. Don't set this to be anything below 15 seconds as it could cause a crash

```id_list``` list of 5 digit ids of classes you want to keep an eye on. Put them in the format xxxxx, xxxxx, xxxxx, (so on and so forth)

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
```
notif_method = sms
url_year = 2251
wait_time = 15
id_list = 12345, 54321, 09876
SENDER_EMAIL=exampleSender@gmail.com
SENDER_PASSWORD=aaaa bbbb cccc dddd
TARGET_EMAIL=my.email@gmail.com
PHONE_NUMBER=11234567890
CARRIER=att
```

**Do not under any circumstances publish your trackourse.ini file on the internet**

## Curious about how this works?
Most of the main code uses default python packages, with the exception of these packages<br>
- Webscraping tool: ``Playwright``
- Message Sending: ```smtplib```

Copyright © Aidan Yung