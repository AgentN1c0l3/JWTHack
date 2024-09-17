# JWTHack

# JWT Handler Script

## Overview

This script is a simple utility for handling JSON Web Tokens (JWTs). It provides functionalities to:
1. Decode JWT header and payload.
2. Validate JWT with a secret or public key.
3. Make an HTTP request with the JWT as the Authorization header.

The script features a colorful ASCII art menu and handles errors gracefully.

## Features

- **Decode JWT**: Extract and display the JWT header and payload.
- **Validate JWT**: Check if the JWT is valid using a provided secret or public key.
- **Make HTTP Request**: Use the JWT as a bearer token in HTTP requests.

## Requirements

- Python 
- `pyfiglet` for ASCII art
- `colorama` for color support
- `pyjwt` for JWT handling
- `requests` for HTTP requests

You can install the necessary Python libraries using pip:

```bash
pip install pyfiglet colorama pyjwt requests
