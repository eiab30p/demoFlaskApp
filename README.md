# Simple Application Demoing flask
*Eddy Verde (eiab30p)*
___
### *Note*

*Make sure you have Python2.7 and pip installed before continuing on with this
application.*

*Documentation in the code should follow python documentation rules and regulations*

___

##### *Tools (Stack)*
* MySQL
* Python
* Bootstrap
* HTML5
* CSS
* Docker
* Selenium
* pycco
* watchDog


##### *Python Packages:*
*Refer to Requirments.txt file;  my file will have descriptions and urls about each packages *


##### *Python Packages:*
* Graphs

___

#### *Starting Fresh*

Once you have python2.7 and pip installed we will start running some basic commands to get our DEV environment ready to code and run the program. We will first run and installing a virtual environment for flask. These commands are done in your terminal follow the below command.

```
pip install virtualenv
```
Once You have complete this step you will need to install flask into your virtualenv. Make sure you are in the project field you want for the rest of the steps.

```
virtualenv flask
```

This will take a little bit of time to run. Once it is done you should see a new folder named flask. Now for all other installs you will want to start them with the follow.

```
flask/bin/pip install
```

If you did not pull the git-repo you can download all packages used in this project with the following command. Before running the command make sure you have a copy of the requirements.txt file.

```
flask\Scripts\pip install -r requirements.txt
```

If you already have packages installed and want to see what you have you'll run the following command. If you did not create a virtualenv you'll just need to remove flask\Scripts\ part of the command.

```
flask\Scripts\pip freeze
```

The results will show something like the requirment.txt file but without the urls and descriptions. *NOTE* What I have in the requirements.txt are just the ones I physically installed but when installing they may depend on other packages.
___

#### *Running Python*

To Run the Application you will need to use the following command

```
flask\Scripts\python run.py
```

___

### *Resources*
* https://sqlalchemy-searchable.readthedocs.io/en/latest/index.html
* http://selenium-python.readthedocs.io/getting-started.html
* https://pip.pypa.io/en/latest/installing/
