# Install
Auto: Run `run.bat`

Manual:
```
pip install fastapi uvicorn
```

# Usage

### Run API+APP (Production):
Method 1: Run `run.bat`

Method 2:
```
_config.IS_DEVELOPING = False
py run.py
```
### Run API
Production:
```
_config.IS_DEVELOPING = False
py main.py
```
Dev:
```
_config.IS_DEVELOPING = True
uvicorn main:app --reload --host 127.0.0.1 --port 8888
```

### Run APP
Production:
```
py -m http.server --directory app 9999 --bind 127.0.0.1
```
Dev: VSCode Live Server

# Auto API Docs
http://localhost:8888/docs

http://localhost:8888/redoc
