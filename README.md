<h1 align="center">
    <img alt="Logo" src="https://github.com/BrianRuizy/favours/blob/master/favours/static/assets/favours_light.png" width="100"> </br>
    Favours
</h1>

## Installation

Prerequisites for installation django web-application include Python 3.7+, and pip.

1. Fork and clone repo to local system

```bash
git clone https://github.com/<your-username>/favours.git
```

2. Create local virtual environment inside project directory, and activate.

```bash
python -m venv env

source env/bin/activate  # Linux/Mac
env/Scripts/activate  # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run development Django server

```bash
python manage.py runserver --settings=favours.settings.dev
```
