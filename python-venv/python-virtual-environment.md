# Python Virtual Environment

A Python Virtual Environment is an isolated development environment with its own dependencies.

``` powershell
python -m venv [file path]\venv
```

You may also be prompted to upgrade pip

``` poweshell
.\venv\scripts\python.exe -m pip install --upgrade pip
```

You will have to execute the activate script in order to access the PIP commands

``` powershell
.\venv\Scripts\activate
```

You will see a green ```(venv)``` showing the environment is loaded

Once this is done you can execute pip commands like 

``` powershell
pip install matplotlib
```

Note: PIP Search is disabled due to ongoing overuse.

Go to ([pypi.org](https://pypi.org/)) and search there.
