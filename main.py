from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
import uvicorn
import _config

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ENDPOINT: /api
# Method 1: Can handle string contains "/" character
# > http://localhost:8888/path_1/?input_text_1=TYPE_INPUT_HERE_1
@app.get("/path_1/")
def booooo_1(input_text_1: str = "DEFAULT_TEXT_1"):
    return {
        "message_1": f"Hello {input_text_1}!"
    }

# ENDPOINT: /api
# Method 2: Shorter URL, variable name not matter
# > http://localhost:8888/path_2/TYPE_INPUT_HERE_2
@app.get("/path_2/{input_text_2}")
def booooo_2(input_text_2: str = "DEFAULT_TEXT_2"):
    return {
        "message_2": f"Hello {input_text_2}!"
    }

# ENDPOINT: /app
# > http://localhost:8888/app
app.mount("/app", StaticFiles(directory="app", html=True), name="app")

if _config.IS_DEVELOPING == False:
    uvicorn.run(
        app, 
        host = _config.API_HOST,
        port = _config.API_PORT,
    )
