@echo off
:START
cls
set /p type= "Name of input file: "
echo Generating parse tree.... && py tree.py %type%
set /p choice= "Do you want to restart? Press 'Enter' for Yes or 'n' for Exit:"
if '%choice%'=='' goto START
if '%choice%'=='n' exit
