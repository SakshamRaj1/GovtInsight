# GovtInsight

GovtInsight is a Flask web application designed to help citizens explore government schemes, monitor implementation progress, vote on schemes, and file complaints related to government initiatives.

## Overview

The application provides a simple interface for:

- Browsing central and state government schemes
- Viewing implementation status and government program summaries
- Upvoting or downvoting schemes
- Logging in or signing up as a user
- Filing complaints with supporting documents
- Viewing personal profile activity and complaint history
- Admin review of complaint submissions and status updates

## Features

- User authentication with login and signup
- Central and state government scheme views
- Scheme voting system
- Complaint filing system with document upload support
- Admin complaint dashboard
- Progress analytics and visual summaries
- SQLite database support by default

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- WTForms
- SQLite
- HTML/CSS/JavaScript

## Project Structure

```text
GovtInsight/
├── app.py                 # Main Flask application
├── config.py              # Application configuration
├── model.py               # Database models
├── requirements.txt       # Python dependencies
├── instance/              # Runtime files / SQLite data
├── static/                # CSS, JS, and static assets
├── templates/             # HTML templates for the frontend
├── govtinsight.db         # SQLite database created at runtime
└── README.md              # Project documentation
