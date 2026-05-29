@echo off
title PyTutor
echo ================================
echo    🐍 Arrancando PyTutor...
echo ================================
echo.

REM Verificar que Ollama está corriendo
tasklist /fi "imagename eq ollama.exe" 2>NUL | find /i "ollama.exe" >NUL
if errorlevel 1 (
    echo Iniciando Ollama...
    start "" ollama serve
    timeout /t 3 /nobreak >NUL
)

REM Arrancar Flask y abrir navegador
cd C:\pytutor
start "" http://127.0.0.1:5000
python app.py