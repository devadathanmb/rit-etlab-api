# RIT Etlab Portal API

Unofficial API for accessing useful data for students from the [RIT Etlab portal](https://rit.etlab.in/user/login). This API allows you to perform actions such as login, logout, view attendance, access timetable, retrieve basic profile information, and more.

> [!NOTE]
> This API relies on web scraping techniques and may be subject to potential bugs if the structure of the RIT Etlab portal changes.

> [!TIP]
> Even though this project was made specifically for [RIT Etlab portal](https://rit.etlab.in/user/login), this project could be used for any **Etlab** implementations by making required changes to the `BASE_URL` and `COOKIE_KEY` present in `config.py`

## Table of Contents

- [Features](#features)
- [Installation](#installation)
  - [With Docker](#with-docker)
  - [Without Docker](#without-docker)
- [Usage](#usage)
- [Documentation](#documentation)
- [Known Issues](#known-issues)
- [Deployment](#deployment)
  - [Availability](#availability)
- [Contributing](#contributing)
- [License](#license)

## Features

- Login to RIT Etlab portal
- View attendance details
- Access timetable information
- Retrieve basic profile information
- View present attendance information
- View absent attendance information

## Installation

### With Docker

1. Ensure you have Docker and Docker compose installed on your machine.

2. Clone the repository:

   ```bash
   git clone https://github.com/devadathanmb/rit-etlab-api.git
   ```

3. Navigate to the project directory:

   ```bash
   cd rit-etlab-api/
   ```

4. Build and run the docker container

   ```bash
   docker compose up
   ```

5. That's it. The API would be live now. Check the status using

   ```bash
   curl http://localhost:5000/api/status
   ```

### Without Docker

1. Clone the repository:

   ```bash
   git clone https://github.com/devadathanmb/rit-etlab-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd rit-etlab-api
   ```

3. Create and activate a virtual environment (optional):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python run.py
   ```

   The API will be accessible at `http://127.0.0.1:5000/` by default.

---

## Usage

For detailed information on API endpoints and usage, refer to the [Swagger Documentation](https://rit-etlab-api.onrender.com/apidocs).

## Known Issues

- The API relies on web scraping and may encounter issues if the structure of the RIT Etlab portal changes.

## Deployment

The API is deployed at **https://rit-etlab-api.onrender.com/apidocs**. Visit the deployment for live usage.

### Availability

Monitor the API's availability in real-time using [Uptime Robot Status Page](https://stats.uptimerobot.com/pplYnfQOZQ).

## Contributing

Feel free to contribute to the development of this API. Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [GPL 3.0 License](./LICENSE.md).
