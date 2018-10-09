# Google Translation API Code Challenge

### Objective: 
Write a script that uses the Google Translate API to fill in missing strings in a translation file.

### Details:
Translations are stored in a JSON file like the one attached ("translations.json"). The top level keys are the locales. For example, "de-de" means German from Germany. The keys inside each locale are the strings in English and the values are the translated strings in the specified language.
Some of the translations (values) are empty strings and they should be filled in. The output should look like the attached file below "translations_after.json".

### Requirements:
- A script that takes the path of the "translations.json" file as a flag and modifies the file in place
- The script can be written in any of the following: C#  Go  Java Node.js  Php  Python  Ruby
- The script should use the Google Translate API (https://cloud.google.com/translate/docs/apis)
- If a translation string is already filled in, then it shouldn't be modified or overwritten
- The script should handle any locales found in the JSON file, not just "de-de"
- The final output should be valid JSON
- There is no need to obtain or provide a real Google Translate API key


## Get Started
This project is written in Python 3.7.0. Please make sure that the test environment is based on Python 3.6 or later.

### Install and Implement Test Environment
Visit https://cloud.google.com/translate/docs/reference/libraries to obtain Google Translation service key and setup environment variable.

```buildoutcfg
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
```

### Install Essential Site Package

```buildoutcfg
pip3 install -r requirements.txt
``` 

### Obtain Translated File

```buildoutcfg
python3 main.py
``` 


## Authors

* **Shawn Xu** - Programmer

  shawnxu0420@gmail.com
