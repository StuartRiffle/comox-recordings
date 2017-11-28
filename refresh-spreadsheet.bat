@echo off
setlocal
cd %~dp0
mkdir temp >NUL 2>NUL
wget --no-check-certificate --output-document=temp\new-spreadsheet.tsv https://docs.google.com/spreadsheets/d/e/2PACX-1vTjzLp3Wy32wp4V68xMk4GQn3G9_qcqg4ybzq2Xd43w6bz_gmmiRlfH3-TbqBwhSRvD4kuLLkA5IamB/pub?output=tsv 
if ERRORLEVEL 1 goto DONE
copy temp\new-spreadsheet.tsv spreadsheet.tsv /y
del temp\new-spreadsheet.tsv

:DONE
