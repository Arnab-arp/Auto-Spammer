@echo off

echo AUTOSPAMMER by Arnab...
echo (This project is Created and maintained by Arnab Pramanik. All rights reserved.)
echo For More Info, Visit:
echo Github: https://github.com/Arnab-arp

timeout /t 5

where python >nul 2>&1
if %errorlevel% == 0 (
	cls
	
	echo Python is installed.
    	echo Uninstalling Packages....
	
	timeout /t 3 /nobreak
	
	pip unstall -y PyAutoGUI
	echo --------------------------------------------------------------------------------------------
	echo All Packages Uninstalled Successfully!
	echo Safe To Delete The Project Folder

) else (
	echo Python is not installed.
	echo Please install Python before running this program again. 
)
pause
