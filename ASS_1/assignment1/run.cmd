@echo off
cd src
:START
cls
echo Generating......
py run.py gen

echo Running test.....
py run.py test LexerSuite
set /p choice= "Do you want to restart? Press 'Enter' for Yes or 'n' for Exit:"
if '%choice%'=='' goto START
if '%choice%'=='n' exit
