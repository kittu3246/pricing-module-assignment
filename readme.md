# Pricing Module Assignment

## Overview

This Django web app implements a configurable pricing module for ride services, supporting differential pricing based on distance, time, waiting, and day of the week.

## Features

- Multiple active pricing configurations
- Time multipliers for different ride durations
- Waiting charges after free wait time
- Admin panel to create/update pricing configs with logs
- REST API endpoint to calculate ride price

## Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/kittu3246/pricing-module-assignment.git
2. Create and activate a virtual environment:

	python -m venv venv
	venv\Scripts\activate  # Windows
3. install dependencies
	pip install -r requirements.txt
4.Run migrations
	python manage.py migrate
5.Run the development server
	python manage.py runserver




-----------------------api usage-----------------------------
	type localhost:8000/pricing/calculate-price/ in the url after running the server
	{
  	"distance": 5.0,
  	"duration": 40,
  	"waiting_time": 5
	}
	
	type localhost:8000/admin for admin page to configure the prices and check logs in the url

