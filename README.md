# sync-evernote
 ```This is software that is going to be made for Nextcloud as an extension. Support for Linux will also be coming.```
 
 ```Right now Only Windows is supported so far.```

# Software Needed
 1) ```windows```

 
 2) ```Python```

 
 3) ```Git```


# Downloading 
 ```git clone https://github.com/ars-4/sync-evernote.git```

# setting it up
 1) ```create virtualenv venv && venv\Scripts\activate.bat```

 2) ```pip install -r requirements.txt```

 3) ```cd evernote` then `py setup.py install```

 4) ```py manage.py makemigrations && py manage.py migrate```

 5) ```py manage.py runserver```

 6) ```Open browser and go to http://127.0.0.1:8000/evernote/create/  create a note and check on the link with signed in evernote account```
