# registerASU
Project for automating notifications for asu

The goal of this project:
Periodically scan through desired class codes. This project assumes the student has done their due dilligence on what classes they are qualified to take and that they've planned out their schedule. Effectively, this will be a self-hosted, free for all version of a service like courseer with delay only being limited
by the server load balancing of ASU's class search system and the internet speed the device running the program has access to. 

Running this should:
- Search the class portal for open spots
- View the professor, if the professor and class code match, an email will be sent to the target email

## ToDo:
- Restructure to use playwright instead of selenium for increased speeds

## Setup

```pip install -r requirements.txt```
```playwright install``
---