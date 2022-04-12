# testsite_Cloud project
 Cloud Computing project using Django and AWS/Azure
 At first download the whole project as zip
 Extract after downloading and name it "testsite"
 Make a new folder and give it some name(eg. cloud)
 Make sure you have virtual environment is installed in your system.
 Installation Procedure:
 For Ubuntu:
 If pip is not in your system
 "sudo apt-get install python-pip"
 Then install virtual environment using "pip install virtualenv"
 Now check your installation using "virtualenv --version"
 Now, open the cloud folder in terminal and create a virtual environment using the command, "virtualenv virtualenv_name"
 After this command, a folder named virtualenv_name will be created.
 Now at last we just need to activate it, using command

$ source virtualenv_name/bin/activate
copy the testsite folder into the cloud(Dont close the terminal or deactivate the virtual environment)
now move to testsite folder in terminal.
now enter the command "python manage.py runserver" 
At first, it'll show some error. It may show that one module is not found (i think pygoscope or something like this(it will be written in the terminal). You'll have too install it using pip command. After that, open the testsite folder and go to settings.py file and make the postgres database part commented and sqlite database part active by removing the double inverted commas. Now save the file and run python manage.py migrate command in the terminal. Once the migrations are done, run the python manage.py runserver command again and it will start working.copy the url with http://127.0.0.1:8000/ from the terminal and paste it on the browser. It will run
