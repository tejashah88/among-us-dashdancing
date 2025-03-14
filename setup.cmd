@echo off

if not exist env\ (
    @REM Create environment
    python -m venv env
    call env\Scripts\activate.bat

    @REM Install dependencies
    python -m pip install --upgrade pip
    pip install -r requirements.txt
) else (
    @REM Activate environment
    call env\Scripts\activate.bat
)

echo Type "python service.py" (no quotes) to run the service
