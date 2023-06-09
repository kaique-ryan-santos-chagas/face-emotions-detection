# Art Vibe Software: Human emotions detection.

<p align="center">
  <img src="https://github.com/kaique-ryan-santos-chagas/face-emotions-detection/assets/59677362/00726aba-da72-419f-904a-c566736b7117" />
</p>
 
### My graduate project that detect human emotions in audiovisual production. <img src="https://github.com/kaique-ryan-santos-chagas/face-emotions-detection/assets/59677362/b49efba4-ef09-496a-bd31-a1b0021ad23f" width="30" />

## Examples: detecting emotions in face expressions from react videos.

<img src="https://github.com/kaique-ryan-santos-chagas/face-emotions-detection/assets/59677362/7776bc6a-c22e-441d-b542-84b4b0a59732" />
<img src="https://github.com/kaique-ryan-santos-chagas/face-emotions-detection/assets/59677362/3437cff7-99d0-4529-87b0-62b31761c7f1" />
<img src="https://github.com/kaique-ryan-santos-chagas/face-emotions-detection/assets/59677362/a55a776b-e7a8-4c52-8ab4-5978cbad2a60" />

## Examples: detecting emotions in face expressions from audiovisual productions.

<img src="https://github.com/kaique-ryan-santos-chagas/face-emotions-detection/assets/59677362/9e53cea5-6087-44cb-8824-ab91839bff8f" />

## How to build the software:

Requirements:

* Python <= 3.10.9 

Steps to config:

* Install dependencies: 

```
pip install -r requirements.txt
```

* Authenticate with your Google Cloud Developer Account to send video files to Google Drive:

```
python drive.py
```

* Remember you need a App Password in your Google Account to send report e-mails with Python:

```
# Create a file called .env and add a variable called EMAIL_PASSWORD

EMAIL_PASSWORD={your_google_app_password}
```

