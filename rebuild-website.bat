@echo off
del website\static\clips\*.m4a
del website\data\clips\*.yaml
python process-spreadsheet.py
