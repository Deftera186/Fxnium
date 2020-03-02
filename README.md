![Fxnium](https://i.imgur.com/1R8mlmt.png)

# Fxnium
This is a small project of mine that allows to interact with [fxp.co.il](https://www.fxp.co.il) with Selenium.

## Why Selenium?
During the project I used selenium to learn this tool.
What is selenium actually? Selenium automates browsers. That's it.

## Installation
To use this package, you need to download FIREFOX webdriver, [geckodriver.exe](https://github.com/mozilla/geckodriver/releases).
In addition, you need to download [FIREFOX](https://www.mozilla.org/en-US/firefox/new/).
```
pip install Fxnium
```
## Usage
```python
from Fxnium import *

bot = FxpBot()

bot.login('username', 'password')
bot.create_thread('31', 'This is the best package for interacting with FXP!', 'Check this out!', 'פרסום|')

bot.Quit()
```
