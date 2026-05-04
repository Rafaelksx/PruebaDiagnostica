@echo off
echo === Iniciando instalacion de componentes - UNEG ===

:: Verificar Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python no esta instalado en el PATH.
    pause
    exit /b
)

:: Crear entorno virtual e instalar
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt

echo === Instalacion completada ===
pause