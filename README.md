# Server Side Caching Project with DRF APIs, Redis and Poetry Dependency Management

This project utilizes Django Rest Framework (DRF) to create APIs for managing device information. Redis is used for caching to improve performance, and Poetry is employed for dependency management.

## APIs Provided

### 1. Get Latest Device Information

- **Endpoint**: `/api/device/latest-info/<device_id>/`
- **Method**: GET
- **Description**: Returns the latest information of a device based on its ID.
- **Parameters**:
  - `device_id`: ID of the device for which information is requested.
- **Response**: JSON object containing the latest information of the device.

### 2. Get Start and End Location for a Device

- **Endpoint**: `/api/device/journey/<device_id>/`
- **Method**: GET
- **Description**: Returns the start and end locations (latitude, longitude) for a device based on its ID.
- **Parameters**:
  - `device_id`: ID of the device for which locations are requested.
- **Response**: JSON object containing the start and end locations of the device.

### 3. Get Location Points within a Time Range

- **Endpoint**: `/api/device/locations/<device_id>/<start_time>/<end_time>/`
- **Method**: GET
- **Description**: Returns all the location points (latitude, longitude, timestamp) for a device within a specified time range.
- **Parameters**:
  - `device_id`: ID of the device for which locations are requested.
  - `start_time`: Start time of the time range (format: `YYYY-MM-DDTHH:MM:SS`).
  - `end_time`: End time of the time range (format: `YYYY-MM-DDTHH:MM:SS`).
- **Response**: JSON array containing location points (latitude, longitude, timestamp) within the specified time range.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>

2. **Install Dependencies**:
   ```bash
   poetry install

3. **Install Dependencies**:
   - Install Redis and start the Redis server.
   - Configure Redis settings in `settings.py` for caching.

4. **Run Migrations**:
   ```bash
   python manage.py migrate

5. **Run the Development Server**:
   ```bash
   python manage.py runserver

