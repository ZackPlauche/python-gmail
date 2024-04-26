# Python Gmail 🐍📨
The bare minimum api to send emails from your gmail account using Python.

## Features
- Easy API
- Common defaults for using smtp with Gmail so you don't have to think about it.
- Supports emojis in text by default

### Not Features
- Getting previous emails
- Getting contacts
- Changing email settings
- Etc.

## Requirements
- Must have a Gmail account
- Must have 2 factor authentication setup on your gmail account
- Must create an app password for your gmail account

## Installation
Pip install this for your system:
```cmd
pip install git+https://www.github.com/zackplauche/python-gmail
```

## Quickstart
Create your instance and send an email
```py
>>> from gmail import Client
>>> client = Client(email='yourgmail@gmail.com', app_password='aaaa aaaa aaaa aaaa')
>>> client.send_email(to='otheremail@gmail.com', subject='Hello! 👋', body='How are you today? 👀❓')
```
or send to multiple emails separately
```py
>>> client.send_email(to=['other1@email.com', 'other2@gmail.com'], subject='Hello! 👋', body='How are you today? 👀❓')
```
That's it!
## Basic Usage
### Creating an Instance

You can create a gmail instance from just your gmail account email and your gmail account app password
```py
>>> from gmail import Client
>>> client = Client(email='yourgmail@gmail.com', app_password='aaaa aaaa aaaa aaaa')
```
### Creating an Instance from environment variables
If you wish to create instantiate a client **more securely**, you can create your instance from environment variables using the `GMAIL_EMAIL` and `GMAIL_APP_PASSWORD` environment variable names. 

1. Create a `.env` file in your directory and add the following: 
```.env
GMAIL_EMAIL=example@gmail.com
GMAIL_APP_PASSWORD=aaaa aaaa aaaa aaaa
```
2. Create your instance:
```py
>>> client = Client.from_env()
```

### Sending Emails
You can send an email by writing the following:
```py
>>> client.send_email(
...     to='other@gmail.com',
...     subject='Hello! 👋',
...     body='How are you doing? 👀❓'
... )
```
This will send an email with a subject and body.

**Important Note:** Where usually you would see the name of your gmail account, you will only see your email **unless** you specify a name in the `from_` field, like this:
```py
>>> client.send_email(
...     from_=f'Example Email <{client.email}>', 
...     to='other@email.com',
...     subject='Howdy! 🤠',
...     body='Good morning neighbor! ☀️🏠🥓'
... )
```
For convenience, you can also create this at the instantiation and not have to think about it later:
```py
>>> # Name will be Bob <example@gmail.com>
>>> client = Client(email='example@gmail.com', name='Bob', app_password=...)
>>> # or from env vars
>>> client = gmail.from_env(name='Bob')  # OR set GMAIL_NAME as an environment variable
```
Then you can send an email without the `from_` argument and it will have your name in it.
## Authors Note and Links
Enjoy! 📨📨📨
- Website: https://www.zackplauche.com
- YouTube: https://www.youtube.com/@zackplauche
