# HookCatcher

Generates perceptual diff of Kolibri states.

## Setup

### Install dependencies

```
$ pip install -r requirements.txt
```


### Reference data directory

You'll need a directory for storing data. You can either start from scratch with an empty directory, or use an existing database and image set. See <a href="#" onclick='window.open("https://github.com/MingDai/HookCatcherData");return false;'>this repo </a> for example.

To point at the data, create a new _user_settings.py_ file in the project root.
Add the local directory that your data is stored in:


```python
DATABASE_DIR = "../HookCatcherData"
```
Add the Github Repository API that you are testing for:
```python
GIT_REPO_API = "https://api.github.com/repos/YOUR_GITHUB_USERNAME/YOUR_GITHUB_REPO/"
```
Add your Github <a href="#" onclick='window.open("https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/");return false;'>personal access token</a>
```python
GIT_OAUTH = 'YOU_AUTH_ID_HERE'
```

### Start server

```
$ python manage.py runserver (port)
```

NOTE: port defaults to 8000

To view site enter the following website url into your browser:
http://127.0.0.1:8000/
