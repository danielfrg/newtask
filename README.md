New Task
========

Desktop python app to create new tasks on major task management web apps.

__Objective__: Use GTD (task management) apps the correct way

__Problem__: The usual way to create tasks is:
```type app url -> hit enter -> wait for the app to load -> press hotkey to create task (if have it) -> type task -> hit enter```
That takes to long and it is distractive, GTD says task collection needs to be fast as possible without distracting you from your current task.

__Solution / What this app does__: A _very simple_ desktop app that use email (gmail) to create tasks quickly on your favorite task management web app such as: [Nirvana](https://nirvanahq.com), [Producteev](https://producteev.com), [Asana](https://asana.com), [Do](https://Do.com), [Wunderlist](https://wunderlist.com), [Doit](https://doit.im), [Orchestra](https://orchestra.com), and many others that support task creation via email.

Features
--------

- Very simple and clean UI and functionality
- Customizable settings
- Hotkey (WIN+DEL) to summon the application
- Hides on the notification area
- AES encryption for the password

Executables
-----------

- [Windows](https://github.com/dfrodriguez143/newtask/blob/master/dist.zip?raw=true)
- Other OSes: Sorry, don't have them :(

How to use it
-------------

1. Download the [windows executable](https://github.com/dfrodriguez143/newtask/blob/master/dist.zip?raw=true) or the python source from here.
2. Execute the app:
	- On windows double click ```newtask.exe```
	- On other OS run from the terminal: ```python newtask.py```
3. Click the settings (gear icon) and fill the options: ```your_email(at)gmail.com```, ```your_gmail_password``` and ```new_task@your_favorite_app.com```
4. Write a new task and press enter to send an email, the app will automaticly go to the notification area
5. Use the hotkey to summon the app again and create more tasks
6. Be productive

Required Libraries
------------------

If running from the source need the following python libraries:
- [wxPython](http://wxpython.org/)
- [pycrypto](https://www.dlitz.net/software/pycrypto/)

Screenshots
-----------

Main interface

![Main interface](http://ctrl68.files.wordpress.com/2012/10/2012-10-13_23h20_48.png)

Settings dialog

![Settings dialog](http://ctrl68.files.wordpress.com/2012/10/2012-10-13_22h57_271.png)
