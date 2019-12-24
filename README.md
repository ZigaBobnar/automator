# Automator
Concept app built for recording mouse movement and repeat it for automated testing


## Requirements
- Python 3 (developed using 3.8)
- virtualenv (optional, allows you to install packages only into this project and export them into requirements using `pip freeze > requirements.txt`)


## Set up project
- Check out this project and cd into it
- Run `virtualenv venv --no-site-packages` to create virtual environment (you can replace venv with something else as long as it is not present in the current directory). The --no-site-packages options is used so the globally installed packages are not copied into virtualenv
- Run `source venv/bin/activate` (Linux) or `.\venv\Scripts\activate` (Windows, you might need to enable running PowerShell scripts)
- Install required packages using `pip install -r requirements.txt`
- Use `python <script_name>` to run any of the scripts (main.py is the entrypoint of the program)

When you are done working with this project you can use `deactivate` command in order to exit the virtual environment. Always remember to activate the enviromnent again if you want to use it.


## Privacy concerns
Since this application intended purpose is to track and record your keypresses and mouse movements, one could assume that it works as a keylogger. However this is not the case. The point of this application is to record input when you want it to and replay it when needed, also the sources are released under the MIT license so anyone could take a look at it.

In future there might be a feature that could allow you to automate interaction based on the contents that are on the screen. This would be implemented by taking screen snippets and analyzing them for required patterns. As said before there is no intentions into malicious activity but the user should keep in ming that someone tampering with your scripts could lead to privacy leakage.

The developers of this app are not responsible for any of the damage the use of it could cause.
