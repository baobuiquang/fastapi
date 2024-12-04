REM To kill the hidden process, open Task Manager,
REM search "cmd" and "python", end all tasks

Set objShell = CreateObject("WScript.Shell")
objShell.Run "run.bat", 0, True