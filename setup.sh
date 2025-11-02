#!/bin/bash
# Setup script for WeatherVision project

echo "Setting up WeatherVision..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from example..."
    cp ENV_EXAMPLE.txt .env
    echo "Please edit .env file with your configuration!"
fi

# Run migrations
echo "Running database migrations..."
python manage.py migrate

echo ""
echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your database credentials and API keys"
echo "2. Create a superuser: python manage.py createsuperuser"
echo "3. Run the server: python manage.py runserver"
echo "4. Visit http://localhost:8000/api/"

