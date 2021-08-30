# Converter CSV

**Converter CSV** by LimberDuck (pronounced *ˈlɪm.bɚ dʌk*) is a GUI tool
which lets you convert multiple large csv files to xlsx files keeping
your operational memory usage at a low level. You can run it on your
operating system no matter if it is Windows, MacOS or Linux. It's free
and open source tool. The reason this tool was created is to speed-up
your tasks.

[![PyPI - Downloads](https://img.shields.io/pypi/dm/converter-csv?logo=PyPI)](https://pypi.org/project/converter-csv/) [![License](https://img.shields.io/github/license/LimberDuck/converter-csv.svg)](https://github.com/LimberDuck/converter-csv/blob/main/LICENSE) [![Repo size](https://img.shields.io/github/repo-size/LimberDuck/converter-csv.svg)](https://github.com/LimberDuck/converter-csv) [![Code size](https://img.shields.io/github/languages/code-size/LimberDuck/converter-csv.svg)](https://github.com/LimberDuck/converter-csv) [![Supported platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey.svg)](https://github.com/LimberDuck/converter-csv)

![](https://user-images.githubusercontent.com/9287709/57588063-d4b2f280-750e-11e9-9ba8-e2d301d38cbc.png)

## Main features

* select one or more csv files at once
* select directory to get all csv files from it and from all it's subdirectories
* change separator to desired char, or leave it default (comma "`,`")
* change target directory for output files to desired one, or leave it default (the same as source files)

## Usage

1. Go to Menu `File`.
2. Choose one of below options:
    - `Open file\-s` if you want to open one or more csv files at once.
    - `Open directory` if you want to open all csv files from selected directory and its subdirectories.
3. Click `Start` button to initiate conversion of all selected files.

## Options

* Click `Change` button (next to separator filed) to change separator to desired by you eg. "`;`".
* Click `Change` button (next to directory field) to change target directory and use it for all output files.
* Mark checkbox `add suffix with "_YYYYMMDD_HHMMSS"` to add into each file name suffix with current time with given format.
* Key-in custom suffix and mark checkbox `add custom suffix` to add into each file name suffix with given text.
* Click `Open` button to open current working directory.

## Installation

> **Note:**
> It's advisable to use python virtual environment for below instructions. Read more about python virtual environment in [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/dev/virtualenvs/)
> 
>Read about [virtualenvwrapper in The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/dev/virtualenvs/#virtualenvwrapper): [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io) provides a set of commands which makes working with virtual environments much more pleasant.


1. Install **Converter CSV**
    
    `pip install converter-csv`

2. Run **Converter CSV**

    `converter-csv`

### Additional steps

#### Linux (Ubuntu)

If you see below error:

```shell
~$ converter-csv
converter-csv: command not found
```

Add below to `~/.bashrc`

```bash
# set PATH so it includes user's private ~/.local/bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
```

If you see below error:

```shell
~$ converter-csv
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl, xcb.

Aborted (core dumped)
```

Run to fix the error:

```shell
sudo apt-get install --reinstall libxcb-xinerama0
```

## Build executable file

<details>
  <summary>Click to see instruction for Windows</summary>

### Windows

1. Clone **Converter CSV** repository using below command

    ```
    git clone https://github.com/LimberDuck/converter-csv.git
    ```

2. Install requirements using below command

    ```
    pip install -r requirements.txt
    ```

3. Run **Converter CSV** using below command
    
    ```
    python -m converter_csv
    ```

4. Upgrade setuptools using below command

    ```
    pip install --upgrade setuptools
    ```

5. Install PyInstaller

   ```
   pip install PyInstaller
   ```

6. Build your own executable file using below command

   ```
   pyinstaller --onefile --windowed --icon=.\icons\LimberDuck-converter-csv.ico --name converter-csv converter_csv\__main__.py
   ```

7. Go to `dist` catalog to find executable file `converter-csv.exe`

</details>

<details>
  <summary>Click to see instruction for Linux (Ubuntu)</summary>

### Linux (Ubuntu)

1. Clone **Converter CSV** repository using below command

   ```
   git clone https://github.com/LimberDuck/converter-csv.git
   ```

2. Install requirements using below command

   ```
   pip install -r requirements.txt
   ```

6. Run **Converter CSV** using below command

   ```
   python -m converter_csv
   ```

7. Upgrade setuptools using below command

   ```
   pip install --upgrade setuptools
   ```

5. Install PyInstaller

   ```
   pip install PyInstaller
   ```

8. Build your own executable file using below command

   ```
   pyinstaller --onefile --windowed --icon=./icons/LimberDuck-converter-csv.ico --name converter-csv converter_csv/__main__.py
   ```

9. Go to `dist` catalog to find executable file `converter-csv`.

</details>

<details>
  <summary>Click to see instruction for macOS</summary>

### macOS

1. Clone **Converter CSV** repository using below command

   ```
   git clone https://github.com/LimberDuck/converter-csv.git
   ```

2. Install requirements using below command

   ```
   pip install -r requirements.txt
   ```

3. Run **Converter CSV** using below command

   ```
   python -m converter_csv
   ```

4. Upgrade setuptools using below command

   ```
   pip install --upgrade setuptools
   ```

5. Install PyInstaller

   ```
   pip install PyInstaller
   ```

6. Build your own executable file using below command

   ```
   pyinstaller --onefile --windowed --icon=./icons/LimberDuck-converter-csv.ico --name converter-csv converter_csv/__main__.py
   ```

7. Go to `dist` catalog to find executable file `converter-csv`.

</details>

## Meta

### Change log

See [CHANGELOG].


### Licence

GNU GPLv3: [LICENSE].


### Authors

[Damian Krawczyk] created **Converter CSV** by LimberDuck.

[Damian Krawczyk]: https://damiankrawczyk.com
[CHANGELOG]: https://github.com/LimberDuck/converter-csv/blob/master/CHANGELOG.md
[LICENSE]: https://github.com/LimberDuck/converter-csv/blob/master/LICENSE
