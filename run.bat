call py --version
call py -m venv venv
call venv\Scripts\activate
call py -m pip install -U pip
call pip install -r requirements.txt
call py run.py
pause