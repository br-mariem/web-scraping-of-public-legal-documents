This Python script extracts "notes et circulaires" documents from the CBT website, downloads them, and stores metadata to avoid duplicate downloads.

## Description
The script automatically navigates through the CBT "notes et circulaires" section, downloads all matching PDF files in "notes_cbt" folder which has some folders named by years (from 2016 to 2025), and stores their SHA-256 hashes in a JSON file to prevent re-downloading the same files.

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