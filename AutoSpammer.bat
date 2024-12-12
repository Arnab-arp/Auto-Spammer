@echo off

echo AUTOSPAMMER RUNNING . . .
echo Press Ctrl + C to Exit.


python main.py
if %errorlevel% neq 0 (
    powershell -command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('An error occurred while running main.py', 'Error', 'OK', 'Error')"
)

