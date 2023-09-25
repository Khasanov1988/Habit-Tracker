# Habit Tracker

Habit Tracker is a web application built with Django that helps you keep track of your habits, set reminders, and stay
organized. Whether you want to build healthy habits or eliminate bad ones, this tool provides a convenient way to manage
your daily routines.

## Features

- **User Authentication**: Users can create accounts, log in, and manage their profiles.

- **Habit Management**: Create, edit, and delete habits with details such as name, location, time, action, and more.

- **Reminders**: Set reminders for each habit to receive notifications when it's time to perform them.

- **Pleasurable Habits**: Mark habits as pleasurable and link them to rewards or related habits.

- **Periodic Tasks**: Automatically schedule and manage periodic tasks using Celery.

- **Internationalization**: Supports multiple languages and time zones.

## Prerequisites

Before you start, ensure you have met the following requirements:

- Python 3.x
- Docker and Docker Compose
- Redis and PostgreSQL

## Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/Khasanov1988/Habit-Tracker.git
   ```

2. Start the Docker services for App, Redis, Celery, Celery beat and PostgreSQL:

   ```shell
   docker-compose up -d
   ```

## Usage

To interact with the Habit Tracker application, you will need to communicate with it through its API. You can find
detailed documentation on how to interact with the API by visiting the API Documentation (http://localhost:8000/redoc/
or http://localhost:8000/swagger/).

The API documentation provides comprehensive information on endpoints, request formats, and responses, allowing you to
manage your habits programmatically.

Here's how you can get started:

Explore the API Documentation to understand the available endpoints and their functionalities.

Make API requests to create, edit, and delete habits or set reminders for them.

Leverage the API to enjoy a more organized and productive lifestyle by effectively tracking your habits!

Feel free to refer to the API documentation for detailed instructions on how to use the Habit Tracker application
programmatically.

## Contributing

Contributions are welcome! Please feel free to open issues and pull requests.

## License

This project is licensed under the MIT License

## Acknowledgments

- Built with Django, Docker, Redis and Celery.
- Thanks to the open-source community for their valuable contributions.

## Contacts

Feel free to contact with me by email Khasanov1988@gmail.com