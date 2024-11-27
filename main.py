from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
import uvicorn
import _config

# For images processing
from fastapi import File, UploadFile
from PIL import Image
from io import BytesIO

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================================================== GET Examples ==================================================

# ENDPOINT: /path_1
# Method 1: Can handle string contains "/" character
# > http://localhost:8888/path_1/?input_text_1=TYPE_INPUT_HERE_1
@app.get("/path_1/")
def booooo_1(input_text_1: str = "DEFAULT_TEXT_1"):
    return {
        "message_1": f"Hello {input_text_1}!"
    }

# ENDPOINT: /path_2
# Method 2: Shorter URL, variable name not matter
# > http://localhost:8888/path_2/TYPE_INPUT_HERE_2
@app.get("/path_2/{input_text_2}")
def booooo_2(input_text_2: str = "DEFAULT_TEXT_2"):
    return {
        "message_2": f"Hello {input_text_2}!"
    }

# ================================================== POST Examples ==================================================

myvar = 0

# ENDPOINT: /test_get
# > http://localhost:8888/test_get
@app.get("/test_get")
async def get_myvar():
    return {"myvar": myvar}

# ENDPOINT: /test_post
# > PowerShell: Invoke-RestMethod -Uri http://127.0.0.1:8888/test_post -Method POST
@app.post("/test_post")
async def toggle_myvar():
    global myvar
    myvar += 1
    return {"myvar": myvar}

# ================================================== Image Processing Examples ==================================================

# ENDPOINT: /imageinfo
# > CURL: curl/bin/curl.exe -X POST "http://localhost:8888/imageinfo" -H "Content-Type: multipart/form-data" -F "file=@test/test.jpg"
@app.post("/imageinfo")
async def image_info(file: UploadFile = File(...)):
    try:
        # Ensure the uploaded file is a valid JPG
        if file.content_type not in ["image/jpeg", "image/png"]:
            return {"error": "⚠️ Invalid file type. Please upload a JPG or PNG image."}
        # Open the image and get its size
        image = Image.open(BytesIO(await file.read()))
        width, height = image.size
        return {"width": width, "height": height}
    except Exception as e:
        return {"error": str(e)}

# ================================================== Serve HTML App ==================================================

# ENDPOINT: /app
# > http://localhost:8888/app
app.mount("/app", StaticFiles(directory="app", html=True), name="app")

# ==================================================  ==================================================
if _config.IS_DEVELOPING == False:
    uvicorn.run(
        app, 
        host = _config.API_HOST,
        port = _config.API_PORT,
    )
