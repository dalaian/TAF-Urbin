# READ ME
This is the solution for the QE Candidate Automation Challenge

# Requisites

You need the following in your computer to run the framework
* Selenium grid
* Python 2.7

If you already have these requirements, you only need to go to config/config.ini and check the seleniumAddress is correct

## How to install python
You have several ways to install python

You can download it from https://www.python.org/downloads

You can install it via npm
```
npm install python -g
```

or if you have a mac you can use brew
```
brew install python
```

## How to install Selenium grid
For this framework, we are going to install webdriver-manager as the selenium grid.
This is a pretty good grid since it manages and updates the web drivers pretty easily.

There are several ways to install it, you can use brew if you are on Mac 
but I'd recommend to install it using NodeJS because it will run on Windows or Mac

#### How to install NodeJS
Get the executable from the Node JS page https://nodejs.org/es/download/
and install it, or you can install it from brew

Once you are done, NodeJS and npm will be installed
> Remember to check that the commands *node --version* and *npm --version* work as expected

Run the following command to install the web-driver
```
npm i webdriver-manager -g
```

Run the following command to update it
```
webdriver-manager update
```

### Execute the Selenium Grid
Now, if everything is correct start the web manager by the command (or if you used another grid, start it as usually)
```
webdriver-manager start
```
>You should not close this terminal
>
>To check that the webdriver is up, check that at the end of the console it says
>Selenium Server is up and running on port 4444
>
>Also, you can verify going to http://localhost:4444/wd/hub/ in your browser


# Installing requirements

Open a terminal, and go to this folder in your computer

Run the following command to install the requirements file
```
pip install -r requirements.txt
```

# Executing the test
Execute the first test case by the command
```
python tests/TS001LoginSuccessful.py
```

Execute the second test case by the command
```
python tests/dashboard/TS002FilterByTicketAndCity.py 
```

## Parameters
It's possible to indicate in which browser you want to run the test case 
using the parameter **-b** or **--browser**, by default it is CHROME
```
python tests/TS001LoginSuccessful.py -b <CHROME/FIREFOX/SAFARI>
``` 
For instance:
```
python tests/TS001LoginSuccessful.py --browser FIREFOX
``` 
> Note: to run the automation on Safari you have to check the 'Allow Remote Automation' option in Safari's Develop menu, 
also Safari does not support headless mode yet

Or you can send a parameter to indicate to run the test case in headless mode, using the parameter 
**-hl** or **--headless**, by default it is not in headless mode
```
python tests/dashboard/TS002FilterByTicketAndCity.py --headless <True/1/T/t/true False/0/F/f/false>
``` 
For instance:
```
python tests/dashboard/TS002FilterByTicketAndCity.py -hl True
```

You can also see what parameters you can send using the **-h** parameter
```
python tests/dashboard/TS002FilterByTicketAndCity.py -h
``` 

So, a good example to test the parameters is with the command
```
python tests/TS001LoginSuccessful.py --browser FIREFOX -hl true
```
> Note that the browser is firefox and UI won't be displayed (headless mode)

## Reports
The automation generates certain reports to give more information to the QA Automation Engineer 
as well as for the stakeholders

Under **reports/** you can find xml reports about the results of the test cases. The only report I found was the
unit test one, which can be improved or could integrate a reporting tool to give a better report.

**reports/screenshots/** has all the screenshots taken if any error was present, 
the name says in which test case and step the error occurred
> The reports are ignored by .gitignore

## Logs
The logs are useful for the QA Automation Engineer, to recollect data about the test cases to improve them
and increase the robustness of the test cases

The framework logs all the actions done by the code under the folder **logs/**, any failure, warning or 
information will be here. The logs will be separated based on the browser

# Run
You can also execute the following command to run a bash with the test cases
```
./run.sh
```
> First runs the login test in Chrome on headless mode
>
> Then runs the filter test on Firefox not in headless mode