This Python script extracts "Avis et Communiqués" documents from the CMF website, downloads them, and stores metadata to avoid duplicate downloads.

## Description
The script automatically navigates through the CMF announcements section, downloads all matching PDF files in "avis23_pdf" folder, and stores their SHA-256 hashes in a JSON file to prevent re-downloading the same files.

## Requirements
- Python 3.8+
- requests
- beautifulsoup4
- schedule
- selenium
- parse
- Standard libraries (included with Python):
  - os
  - re
  - json
  - hashlib

## Installation
1. Install Python 3.8+ if not already installed.
2. Install the required libraries using pip:
```bash
pip install requests beautifulsoup4 schedule selenium parse
