# new_dev_project-01


## README.md
# Employee Growth Analysis Project

This project follows the Ports and Adapters (Hexagonal) architecture to analyze employee growth using data from AWS S3.

## Installation
```sh
pip install -r requirements.txt
```

## Usage
```sh
python src/application/main.py
```

## Project Structure
- **core/**: Contains the business logic
- **adapters/**: Handles external data sources
- **ports/**: Defines interface layers
- **application/**: Orchestrates execution
