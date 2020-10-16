# Quickstart Guide

### Overview

The project is set up to work on a development environment with Docker Compose and two services running from Docker containers:

- A Python 3.7.6 service that includes Django 3.1.2 and the Django REST Framework package.
- A database service running PostgreSQL 10.12.

I'm using a basic configuration file (`config.yaml`) that is not under version control to store secrets such as database credentials and Django's secret key.

There's an exception, the database service is initialized with credentials from a `docker-compose.override.yml` file that is under version control but this should be all right as this is a database that should run locally.

Again, this is a setup for development so I tried to keep things simple and and for a production environment I'd store the credentials as secrets in a Kubernetes cluster.

The data from the CSV files is initially fed into PostgreSQL as instances of Django models (Location, Status, Company, and Launch) and then exposed via API endpoints managed with Django REST Framework, which gives us the option to use multiple filtering and authorization mechanisms later.

### Installation

### Starting the services

### The endpoints

#### Average launch cost (excluding nulls)

`curl example goes here`

#### Percent of launches where mission_status is success
#### The most popular month for rocket launches
#### Top three launch_locations
#### Top three countries where launch_locations take place

