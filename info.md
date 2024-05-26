# Fake Entities for Home Assistant

This project provides fake entities for Home Assistant, useful for testing and development purposes.

## Features

- Provides fake entities for various Home Assistant domains.
- Allows adding new domains via command-line arguments.
- Automatically creates Python files for new domains.

## Usage

To add a new domain, run the `create_domains.py` script with the domain name as an argument:

```sh
python create_domains.py new_domain