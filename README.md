# WeatherVision - Django Weather Application

A full-featured Django web application with PostgreSQL integration, RESTful APIs, third-party weather API integration, and data visualization capabilities.

## Features

- ✅ **CRUD Operations**: Complete Create, Read, Update, Delete functionality via REST APIs
- ✅ **Third-Party API Integration**: OpenWeatherMap API integration for fetching real-time weather data
- ✅ **Data Visualization**: Interactive charts and graphs using Chart.js
- ✅ **Statistical Analysis**: Weather data statistics and reporting
- ✅ **Production Ready**: Configured for deployment on platforms like Heroku, Railway, Render, etc.

## Tech Stack

- **Backend**: Django 4.2 + Django REST Framework
- **Database**: PostgreSQL (compatible with Supabase)
- **API Integration**: OpenWeatherMap API
- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **Deployment**: Gunicorn, WhiteNoise

## Project Structure

```
WeatherVision/
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── weathervision/          # Main Django project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── weather/                # Weather app
│   ├── __init__.py
│   ├── models.py          # WeatherRecord model
│   ├── views.py           # API views and visualization
│   ├── serializers.py     # DRF serializers
│   ├── urls.py            # URL routing
│   ├── services.py        # OpenWeatherMap service
│   ├── admin.py
│   └── migrations/
└── templates/
    └── weather/
        └── visualization.html
```

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- PostgreSQL database (or Supabase account)
- OpenWeatherMap API key (get one free at https://openweathermap.org/api)

### 2. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd WeatherVision

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your configuration:
# - Database credentials (PostgreSQL or Supabase)
# - OpenWeatherMap API key
# - Django SECRET_KEY (generate a new one for production)
```

### 4. Database Setup

```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (optional, for admin access)
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## API Endpoints

### Weather Records CRUD

- `GET /api/records/` - List all weather records (paginated)
- `POST /api/records/` - Create a new weather record
- `GET /api/records/{id}/` - Retrieve a specific weather record
- `PUT /api/records/{id}/` - Update a weather record
- `PATCH /api/records/{id}/` - Partially update a weather record
- `DELETE /api/records/{id}/` - Delete a weather record

### Additional Endpoints

- `GET /api/records/latest/` - Get the latest weather record
- `GET /api/records/by_city/?city=London` - Filter records by city
- `POST /api/records/fetch_from_api/` - Fetch and save current weather from OpenWeatherMap API
  ```json
  {
    "city": "London"
  }
  ```
- `GET /api/records/statistics/?city=London&days=7` - Get statistical analysis
- `GET /api/visualization/` - Weather data visualization page

## Usage Examples

For detailed API examples with curl, Python, and JavaScript, see [API_EXAMPLES.md](API_EXAMPLES.md).

### Quick Examples

**Create a Weather Record:**
```bash
curl -X POST http://localhost:8000/api/records/ \
  -H "Content-Type: application/json" \
  -d '{
    "city": "London",
    "country": "UK",
    "temperature": 15.5,
    "humidity": 65,
    "pressure": 1013,
    "description": "Partly cloudy",
    "wind_speed": 5.2,
    "wind_direction": 180
  }'
```

**Fetch Weather from OpenWeatherMap API:**
```bash
curl -X POST http://localhost:8000/api/records/fetch_from_api/ \
  -H "Content-Type: application/json" \
  -d '{"city": "London"}'
```

**Get Statistics:**
```bash
curl "http://localhost:8000/api/records/statistics/?city=London&days=7"
```

## Database Configuration

### Using Local PostgreSQL

Set in `.env`:
```
DB_NAME=weathervision_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### Using Supabase

1. Create a project on https://supabase.com
2. Go to Project Settings > Database
3. Copy your database credentials
4. Set in `.env`:
```
SUPABASE_DB_NAME=postgres
SUPABASE_DB_USER=postgres
SUPABASE_DB_PASSWORD=your_supabase_password
SUPABASE_DB_HOST=db.your-project-id.supabase.co
SUPABASE_DB_PORT=5432
```
5. Update `settings.py` to use Supabase credentials (see commented section)

## Deployment

### Railway

1. Connect your GitHub repository to Railway
2. Add environment variables in Railway dashboard
3. Railway will automatically detect Django and run migrations

### Render

1. Create a new Web Service on Render
2. Connect your repository
3. Build Command: `pip install -r requirements.txt && python manage.py migrate`
4. Start Command: `gunicorn weathervision.wsgi:application`
5. Add environment variables

### Heroku

1. Install Heroku CLI
2. Create app: `heroku create your-app-name`
3. Add PostgreSQL: `heroku addons:create heroku-postgresql:hobby-dev`
4. Set config vars: `heroku config:set SECRET_KEY=your-secret-key`
5. Deploy: `git push heroku main`
6. Run migrations: `heroku run python manage.py migrate`

## Environment Variables

Required environment variables:
- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to `False` in production
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- Database credentials (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
- `OPENWEATHER_API_KEY` - Your OpenWeatherMap API key

## Admin Panel

Access the Django admin panel at `/admin/` after creating a superuser:
```bash
python manage.py createsuperuser
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.