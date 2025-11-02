@echo off
REM Setup script for WeatherVision project (Windows)

echo Setting up WeatherVision...

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo Creating .env file from example...
    copy ENV_EXAMPLE.txt .env
    echo Please edit .env file with your configuration!
)

REM Run migrations
echo Running database migrations...
python manage.py migrate

echo.
echo Setup complete!
echo.
echo Next steps:
echo 1. Edit .env file with your database credentials and API keys
echo 2. Create a superuser: python manage.py createsuperuser
echo 3. Run the server: python manage.py runserver
echo 4. Visit http://localhost:8000/api/

pause

