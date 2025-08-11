This Python script extracts "Rapports Annuels" documents from the CMF website, downloads them, and stores metadata to avoid duplicate downloads.

## Description
The script automatically navigates through the CMF bulletins section, downloads all matching PDF files in "newrapports" folder, and stores their SHA-256 hashes in a JSON file to prevent re-downloading the same files.

## Requirements
- Python 3.8+
- `requests`
- `beautifulsoup4`
- schedule
- selenium
- parse
- Standard libraries (included with Python):
  - os
  - re
  - json
  - hashlib

## Installation
Install the required libraries:
```bash
pip install requests beautifulsoup4 schedule selenium