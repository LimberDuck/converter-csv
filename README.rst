Converter CSV by LimberDuck
###########################

Converter CSV by LimberDuck (pronounced *ˈlɪm.bɚ dʌk*) is a GUI tool
which lets you convert multiple large csv files to xlsx files keeping
your operational memory usage at a low level. You can run it on your
operating system no matter if it is Windows, MacOS or Linux. It's free
and open source tool. The reason this tool was created is to speed-up
your tasks.

|license| |repo_size| |code_size| |supported_platform|

.. image:: https://user-images.githubusercontent.com/9287709/57588063-d4b2f280-750e-11e9-9ba8-e2d301d38cbc.png
   :width: 600

.. class:: no-web no-pdf

.. contents::

.. section-numbering::

Main features
=============

* select one or more csv files at once
* select directory to get all csv files from it and from all it's subdirectories
* change separator to desired char, or leave it default (comma ",")
* change target directory for output files to desired one, or leave it default (the same as source files)

Usage
=====
1. Go to Menu "File".
2. Choose:

 - "Open file\\-s" if you want to open one or more csv files at once.

 or

 - "Open directory" if you want to open all csv files from selected directory and its subdirectories.

3. Click "Start" button to initiate conversion of all selected files.

Options
=======
* Click "Change" button (next to separator filed) to change separator to desired by you eg. ";".
* Click "Change" button (next to directory field) to change target directory and use it for all output files.
* Mark checkbox "add suffix with "_YYYYMMDD_HHMMSS"" to add into each file name suffix with current time with given format.
* Key-in custom suffix and mark checkbox "add custom suffix" to add into each file name suffix with given text.
* Click "Open" button to open current working directory.

Build executable file
=====================

Windows
-------
1. If you don't have, install Python 3.6.0 or higher, you can download it via https://www.python.org/downloads
2. If you don't have, install latest version of Git, you can download it via https://git-scm.com/downloads
3. Clone LimberDuck Converter CSV repository using below command in Git Bash:

.. code-block:: powershell

 git clone https://github.com/LimberDuck/converter-csv.git

4. Install requirements using below command

.. code-block:: powershell

 pip install -r .\requirements.txt

5. Run limberduck-converter-csv using below command

.. code-block:: powershell

 python limberduck-converter-csv.py

6. Upgrade setuptools using below command

.. code-block:: powershell

 pip install --upgrade setuptools

7. Build your own executable file using below command

.. code-block:: powershell

 pyinstaller --onefile --windowed --icon=.\icons\LimberDuck-converter-csv.ico limberduck-converter-csv.py

8. Go to dist catalog to find executable file limberduck-converter-csv.exe

Linux (Ubuntu)
--------------
1. Python 3.6.7 should be already installed in Ubuntu 18.04.1 LTS, you can ensure with below command

.. code-block:: bash

 python3 --version

2. If you don't have, install git using below command

.. code-block:: bash

 sudo apt install git

3. Clone LimberDuck Converter CSV repository using below command

.. code-block:: bash

 git clone https://github.com/LimberDuck/converter-csv.git

4. If you don't have, install pip using below command

.. code-block:: bash

 sudo apt install python3-pip

5. Install requirements using below command

.. code-block:: bash

 pip3 install -r .\requirements.txt


6. Run limberduck-converter-csv using below command

.. code-block:: bash

 python3 limberduck-converter-csv.py

7. Upgrade setuptools using below command

.. code-block:: bash

 pip3 install --upgrade setuptools

8. Build your own executable file using below command

.. code-block:: bash

 ~/.local/bin/pyinstaller --onefile --windowed --icon=./icons/LimberDuck-converter-csv.ico limberduck-converter-csv.py

9. Go to dist catalog to find executable file limberduck-converter-csv

MacOS
-----
1. If you don't have, install Python 3.6.0 or higher, you can download it via https://www.python.org/downloads

2. Clone LimberDuck Converter CSV repository using below command

.. code-block:: bash

 git clone https://github.com/LimberDuck/converter-csv.git

3. Install requirements using below command

.. code-block:: bash

 pip3.6 install -r .\requirements.txt

4. Run limberduck-converter-csv using below command

.. code-block:: bash

 python3.6 limberduck-converter-csv.py

5. Upgrade setuptools using below command

.. code-block:: bash

 pip3.6 install --upgrade setuptools

6. Build your own executable file using below command

.. code-block:: bash

 pyinstaller --onefile --windowed --icon=./icons/LimberDuck-converter-csv.ico limberduck-converter-csv.py

7. Go to dist catalog to find executable file limberduck-converter-csv

Meta
====

Change log
----------

See `CHANGELOG`_.


Licence
-------

GNU GPLv3: `LICENSE`_.



Authors
-------

`Damian Krawczyk`_ created Converter CSV by LimberDuck.

.. _Damian Krawczyk: https://limberduck.org
.. _CHANGELOG: https://github.com/LimberDuck/converter-csv/blob/master/CHANGELOG.rst
.. _LICENSE: https://github.com/LimberDuck/converter-csv/blob/master/LICENSE


.. |license| image:: https://img.shields.io/github/license/LimberDuck/converter-csv.svg
    :target: https://github.com/LimberDuck/converter-csv/blob/master/LICENSE
    :alt: License

.. |repo_size| image:: https://img.shields.io/github/repo-size/LimberDuck/converter-csv.svg
    :target: https://github.com/LimberDuck/converter-csv

.. |code_size| image:: https://img.shields.io/github/languages/code-size/LimberDuck/converter-csv.svg
    :target: https://github.com/LimberDuck/converter-csv

.. |supported_platform| image:: https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey.svg
    :target: https://github.com/LimberDuck/converter-csv
