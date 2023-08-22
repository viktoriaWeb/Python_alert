0. Create virtuelenv:
```
virtualenv --python=python3 venv

```
1. Activate venv
```
.\venv\Scripts\deactivate
```
2. install dependencies, pip should be instaled

```
pip install -r requirements.txt
```

3. Run db populate
```
python db_populator.py
```

4. Run alert script:
```
python alert.py
```