## Description 

This script parse HERE POI description from the page and display POI category name and the corresponding id in JSON format.

Example output:
```
{"id": "100", "name": "Eat and Drink"}
{"id": "100-1000-0000", "name": "Restaurant"}
{"id": "100-1000-0001", "name": "Casual Dining"}
{"id": "100-1000-0002", "name": "Fine Dining"}
```

## How to use

1. Install dependencies using the command **poetry install** 
2. To run a script use a command **poetry run python parse_page.py**