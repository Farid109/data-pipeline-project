# ETL Project

## Overview
This project is an ETL (Extract, Transform, Load) pipeline designed to process weather data for analytics

The pipeline automates the process of extracting data (using airbyte) from openweathermap , loading the raw data into Amazon S3, transforming it into a desired format using DBT, and loading it into Amazon Redshift.

---

## Features
- **Extract**: from https://openweathermap.org/current using airbyte
- **Load**: into Amazon S3
- **Transform**: using DBT
- **Load**: Upload final data into Amazon Redshift

---

## Project Structure

---

## Requirements
- Python 
- Docker
- SQL
- Amazon S3
- Amazon Redshift
- DBT
- Airbyte
- API
- Airflow
---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Farid109/data-pipeline-project.git