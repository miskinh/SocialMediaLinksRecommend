#TwitterScraper

TwitterScraper is a Python implemented scrapper for Twitter to access the URLs that followers have posted

##Overview

TwitterScraper uses the [TwitterAPI](https://github.com/geduldig/TwitterAPI) to access an authorised user's followers, tweets and the urls contained within tweets. Then [newspaper](https://github.com/codelucas/newspaper) to obtain the text from the urls.

##To Run

To run this application its best to use a virtual environment. The requirements of the files that should be installed in the virtual environment can be found in `requirements.txt`. The process I suggest for this is as follows.

**Install Python2.7**

Follow this [tutorial](http://joequery.me/guides/install-python27-pip-virtualenv/) on installing Python2.7 with pip and virtualenv

**Navigate to the local directory containing this repository in terminal**
```
  $ cd FOLDER_PATH
```
**Create a new virtual environment in this directory**
```
  $ virtualenv venv
```
**Activate the virtual environment**
```
  $ source venv/bin/activate
```
**Install requirements using pip**
```
  (venv)$ pip install -r requirements.txt --allow-all-external
```

Errors encountered here may well be resolved by looking at either [TwitterAPI](https://github.com/geduldig/TwitterAPI) or [newspaper](https://github.com/codelucas/newspaper)] installation instructions.

If errors are encountered installing `lxml` then refer to StackOverflow for [OS X](http://stackoverflow.com/questions/19548011/cannot-install-lxml-on-mac-os-x-10-9) or [Ubuntu](http://stackoverflow.com/questions/6504810/how-to-install-lxml-on-ubuntu).

**Create secret file**

Copy the `SecretExample.py` file name it `Secret.py` then populate the all keys with values obtained from the Application Management of your Twitter App 

**Test the functionality** - using any of the following commands
```
  (venv)$ python ArticleScraper.py
  (venv)$ python TwitterURLs.py
  (venv)$ python TwitterScraper.py
```
If any of these commands do not work then look at the corresponding Python document to asses the problem

**Deactivate the virtual environment**
```
  (venv)$ deactivate
```
##Licence

Please refer to the Licence file in the parent directory

