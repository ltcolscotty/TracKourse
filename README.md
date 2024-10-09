# registerASU
Project for automating notifications and signups for asu

The goal of this project:
Periodically scan through desired class codes. This project assumes the student has done their due dilligence on what classes they are qualified to take and that they've planned out their schedule.

Running this should:
- Search the class portal for open spots
- View the professor, if the professor and class code match, an email will be sent to the target email

## Setup

``.env`` format
```python
LOGIN_USERNAME=''
LOGIN_PASSWORD=''
EMAIL_USER=''
EMAIL_PASSWORD=''
TARGET_EMAIL=''

CLASSES=["CLASS_CODES"]
CLASS_DICT={"class_code", "professor"}
```