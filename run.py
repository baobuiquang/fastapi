import subprocess
import _config

if _config.IS_BUILDING_DOCKER == False:
    command1 = ['py', 'main.py']
    command2 = ['py', '-m', 'http.server', '--directory', 'app', str(_config.APP_PORT), '--bind', str(_config.APP_HOST)]
else:
    command1 = ['python3', 'main.py']
    command2 = ['python3', '-m', 'http.server', '--directory', 'app', str(_config.APP_PORT), '--bind', str(_config.APP_HOST)]

print("> run.py initialized")

process1 = subprocess.Popen(command1)
process2 = subprocess.Popen(command2)

print("> run.py is running...")

process1.wait()
process2.wait()

print("> run.py ended")