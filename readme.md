# FastAPI Boilerplate

## Installation

Run `run.bat` 

(Automatically create virtual environment, install dependencies, and run `run.py`)

## Development

Config:
```
_config.IS_BUILDING_DOCKER = False
_config.IS_DEVELOPING = True
```

Run API (Hot reload):
```
venv\Scripts\activate
uvicorn main:app --reload --host 127.0.0.1 --port 8888
```

Run APP (Hot reload):

`VSCode Live Server`

## Production

### 1. Docker

Config:
```
_config.IS_BUILDING_DOCKER = True
_config.IS_DEVELOPING = False
```

Build image:
```
docker build -t my-fastapi-app .
```

Save image (Optional):
```
docker save -o my-fastapi-app-image.tar my-fastapi-app
```

Load image (Optional):
```
docker load -i my-fastapi-app-image.tar
```

Run:
```
docker run -p 8888:8888 -p 9999:9999 my-fastapi-app
```

### 2. Batch

Config:
```
_config.IS_BUILDING_DOCKER = False
_config.IS_DEVELOPING = False
```

Run:
`run.bat`

### 3. Manual

Config:
```
_config.IS_BUILDING_DOCKER = False
_config.IS_DEVELOPING = False
```

Run:
```
venv\Scripts\activate
py run.py
```

## Quicklinks

### Auto-generated API Docs
* http://localhost:8888/docs
* http://localhost:8888/redoc

### Test Boilerplate
* http://localhost:8888/path_1/?input_text_1=TYPE_INPUT_HERE_1
* http://localhost:8888/path_2/TYPE_INPUT_HERE_2
* http://localhost:9999 (Open console log)