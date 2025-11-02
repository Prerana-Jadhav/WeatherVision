# WeatherVision API Examples

Complete examples for using the WeatherVision REST API.

## Base URL
```
http://localhost:8000/api
```

## 1. Create a Weather Record

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
    "wind_direction": 180,
    "api_source": "manual"
  }'
```

**Response:**
```json
{
  "id": 1,
  "city": "London",
  "country": "UK",
  "temperature": "15.50",
  "humidity": 65,
  "pressure": 1013,
  "description": "Partly cloudy",
  "wind_speed": "5.20",
  "wind_direction": 180,
  "recorded_at": "2024-01-15T10:30:00Z",
  "api_source": "manual"
}
```

## 2. List All Weather Records

```bash
curl http://localhost:8000/api/records/
```

**Response (Paginated):**
```json
{
  "count": 50,
  "next": "http://localhost:8000/api/records/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "city": "London",
      "country": "UK",
      "temperature": "15.50",
      ...
    }
  ]
}
```

## 3. Get a Specific Weather Record

```bash
curl http://localhost:8000/api/records/1/
```

## 4. Update a Weather Record (Full Update)

```bash
curl -X PUT http://localhost:8000/api/records/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "city": "London",
    "country": "UK",
    "temperature": 16.0,
    "humidity": 70,
    "pressure": 1015,
    "description": "Sunny",
    "wind_speed": 4.5,
    "wind_direction": 175,
    "api_source": "manual"
  }'
```

## 5. Partial Update a Weather Record

```bash
curl -X PATCH http://localhost:8000/api/records/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "temperature": 17.5,
    "humidity": 68
  }'
```

## 6. Delete a Weather Record

```bash
curl -X DELETE http://localhost:8000/api/records/1/
```

## 7. Get Latest Weather Record

```bash
curl http://localhost:8000/api/records/latest/
```

## 8. Filter Records by City

```bash
curl "http://localhost:8000/api/records/by_city/?city=London"
```

## 9. Fetch Weather from OpenWeatherMap API

This endpoint fetches current weather data from OpenWeatherMap and automatically saves it to the database.

```bash
curl -X POST http://localhost:8000/api/records/fetch_from_api/ \
  -H "Content-Type: application/json" \
  -d '{
    "city": "London"
  }'
```

**Note:** Requires `OPENWEATHER_API_KEY` to be set in your `.env` file.

## 10. Get Weather Statistics

Get statistical analysis of weather data with optional filters.

```bash
# All records
curl "http://localhost:8000/api/records/statistics/"

# Filter by city
curl "http://localhost:8000/api/records/statistics/?city=London"

# Filter by city and last 7 days
curl "http://localhost:8000/api/records/statistics/?city=London&days=7"

# Last 30 days
curl "http://localhost:8000/api/records/statistics/?days=30"
```

**Response:**
```json
{
  "avg_temperature": 15.75,
  "max_temperature": 22.50,
  "min_temperature": 8.30,
  "avg_humidity": 65.50,
  "avg_pressure": 1013.25,
  "total_records": 100
}
```

## 11. Python Example

```python
import requests

BASE_URL = "http://localhost:8000/api/records"

# Create a record
response = requests.post(f"{BASE_URL}/", json={
    "city": "New York",
    "country": "US",
    "temperature": 20.5,
    "humidity": 60,
    "pressure": 1015,
    "description": "Clear sky",
    "wind_speed": 3.5,
    "wind_direction": 90
})
print(response.json())

# Fetch from API
response = requests.post(f"{BASE_URL}/fetch_from_api/", json={
    "city": "Tokyo"
})
print(response.json())

# Get statistics
response = requests.get(f"{BASE_URL}/statistics/?days=7")
print(response.json())
```

## 12. JavaScript/Fetch Example

```javascript
const API_BASE = 'http://localhost:8000/api/records';

// Create a record
async function createRecord(data) {
  const response = await fetch(`${API_BASE}/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });
  return await response.json();
}

// Fetch from OpenWeatherMap
async function fetchWeatherFromAPI(city) {
  const response = await fetch(`${API_BASE}/fetch_from_api/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ city }),
  });
  return await response.json();
}

// Get statistics
async function getStatistics(city, days) {
  const params = new URLSearchParams();
  if (city) params.append('city', city);
  if (days) params.append('days', days);
  
  const response = await fetch(`${API_BASE}/statistics/?${params}`);
  return await response.json();
}

// Usage
createRecord({
  city: 'Paris',
  temperature: 18.5,
  humidity: 65,
  pressure: 1013,
  description: 'Cloudy',
  wind_speed: 4.2,
}).then(console.log);
```

## Visualization Page

Visit the visualization page in your browser:
```
http://localhost:8000/api/visualization/
```

You can add query parameters:
- `?city=London` - Filter by city
- `?days=7` - Analyze last N days
- `?city=London&days=30` - Combine filters

