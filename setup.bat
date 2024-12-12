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
    	echo Installing Necessary Packages ....
	
	timeout /t 3
	
	python.exe -m pip install --upgrade pip
    	pip install PyAutoGUI

	echo --------------------------------------------------------------------------------------------	
	echo All Packages Installed Successfully!

) else (
	echo Python is not installed.
	echo Go to > https://www.python.org/downloads/ < website to download Python 
	echo Please install Python before running this program again. 
)
pause
