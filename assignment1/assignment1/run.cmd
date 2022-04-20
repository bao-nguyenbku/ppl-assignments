@echo off
cd src
:START
cls
echo Running 'py run.py gen' command......
echo Generating......
py run.py gen

:CHOOSE
set /p type= "[1] for test LexerSuite. [2] for test ParserSuite. [3] for clean generated files. [4] for re-generate files"
if '%type%'=='1' echo Running test LexerSuite...... && py run.py test LexerSuite

if '%type%'=='2' echo Running test ParserSuite...... && py run.py test ParserSuite

if '%type%'=='3' echo Cleanning 'target' folder...... && del ..\target\* /q

if '%type%'=='4' echo Generating...... && goto START
set /p choice= "Do you want to restart? Press 'Enter' for Yes or 'n' for Exit:"
if '%choice%'=='' goto START
if '%choice%'=='n' exit
