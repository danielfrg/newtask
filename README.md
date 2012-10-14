New Task
========

Python app to create new tasks on major task management web apps.

Use email (gmail) to send tasks to your favorite task management web app such as: [Nirvana](https://nirvanahq.com), [Asana](https://asana.com), [Do](https://Do.com), [Wunderlist](https://wunderlist.com), [Doit](https://doit.im), and many others that support task creation via email.

Features
--------

- Very simple and clean UI and functionality.
- Customizable settings.
- Hotkey (WIN+DEL) to summon the application.
- Hides on the notification area.
- AES encryption for the password.

Executables
-----------

- [Windows](https://github.com/dfrodriguez143/newtask/blob/master/dist.zip?raw=true).

How to use it
-------------

1. Download the [windows executable](https://github.com/dfrodriguez143/newtask/blob/master/dist.zip?raw=true) or the python source.
2. Execute the app:
	- On windows double click ```newtask.exe```
	- On other OS run from the terminal: ```python newtask.py```
3. Click the settings (gear icon) and fill the options: email@gmail.com, password, destinatary email address.
4. Write a new task and press enter to send an email, the app will automaticly go to the notification area.
5. Use the hotkey to summon the app again.

Required Libraries
------------------

If running from the source need the following python libraries

- [wxPython](http://wxpython.org/)
- [pycrypto](https://www.dlitz.net/software/pycrypto/)

Screenshots
-----------

![Main interface](http://4.bp.blogspot.com/-CiU0gq1CJA4/UHo4PSsdp-I/AAAAAAAAA_U/5NEHhXBmFCc/s1600/2012-10-13_22h57_27.png)
![Settings](http://2.bp.blogspot.com/-IbtR43ufPPo/UHo9tIwYMGI/AAAAAAAAA_w/_UH250scHw0/s1600/2012-10-13_23h20_48.png)
