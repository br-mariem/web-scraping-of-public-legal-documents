# Web Scraping of Public Legal Documents

> Automated collection, download, and organization of publicly available legal and institutional documents from Tunisian government websites.

---

## Overview

This project automates the retrieval of different types of public documents — bulletins, public notices, annual reports, legal notes, and other institutional publications — from official websites. It handles both static and dynamic web pages, prevents duplicate downloads via SHA-256 hashing, and runs on an automated schedule.

---

## Features

- Automated web scraping of public institutional websites
- Download of PDF and HTML documents
- Extraction of document metadata: title, date, number, URL
- Automatic organization of downloaded files into structured folders
- **SHA-256 hashing** to detect and skip duplicates
- **Incremental scraping** — only newly published documents are downloaded
- Dynamic web scraping using **Selenium** (headless browser)
- **Scheduled execution** via the `schedule` library
- Modular architecture: API / Job / Task / Utils separation
- Persistent state storage in JSON files

---

## Document Types

| Category | Description |
|----------|-------------|
| Bulletins | Official government bulletins |
| Public notices | Announcements and public notices (`avis`) |
| Annual reports | Institutional annual reports (`rapports annuels`) |
| Legal notes | Legal and institutional notes |
| Guides | Other institutional publications |

Each category has its own scraping workflow adapted to the structure of the corresponding website.

---

## Technologies

| Library | Role |
|---------|------|
| `Python` | Main programming language |
| `Requests` | HTTP requests and document downloading |
| `BeautifulSoup` | HTML parsing — static pages |
| `Selenium` | Dynamic page scraping — headless browser |
| `Schedule` | Periodic and automated task execution |
| `Hashlib / SHA-256` | Duplicate detection |
| `JSON` | Metadata and hash storage |

---

## Project Architecture

Each scraping workflow follows the same modular pattern:

```
CBT/
├── CBTapi.py       # HTTP requests and document downloading
├── CBTjob.py       # Main scraping and processing logic
├── CBTmain.py      # Entry point and scheduler
├── CBTtask.py      # Task execution management
└── CBTutils.py     # Shared utilities (hashing, file management)
```

The same structure is replicated for each document category (`bulletins`, `avis`, `RapportsAnnuels`, etc.).

### Full project structure

```
brmarieminternship/
│
├── CBTapi.py / CBTjob.py / CBTmain.py / CBTtask.py / CBTutils.py
├── bulletinsapi.py / bulletinsjob.py / bulletinsmain.py / ...
├── avisapi.py / avisjob.py / avismain.py / ...
├── RapportsAnnuelsapi.py / RapportsAnnuelsjob.py / ...
│
├── scraperCBT.py
├── scraperbulletins22.py
├── scraperravis23.py
├── newscraperrapportsann.py
│
├── bulletin_hashes.json
├── hashes_bct.json
├── avis23.json
├── requirements.txt
└── README.md
```

---

## Scraping Workflow

```
Public Website
      │
      ▼
Fetch Web Page  (Requests or Selenium)
      │
      ▼
Parse HTML Content  (BeautifulSoup)
      │
      ▼
Extract Document URLs
      │
      ▼
Generate SHA-256 Hash
      │
      ├─────────────────────┐
      │                     │
      ▼                     ▼
Already processed        New URL
      │                     │
    Skip              Download document
                            │
                            ▼
                    Organize into folder
                            │
                            ▼
                      Save hash to JSON
```

---

## Duplicate Detection

A SHA-256 hash is generated from each document URL before downloading:

```python
hash_value = hashlib.sha256(url.encode("utf-8")).hexdigest()
```

Hashes are stored in JSON files between runs:

```
bulletin_hashes.json
hashes_bct.json
avis23.json
```

This makes each execution **incremental** — the scraper only processes documents not yet seen in previous runs.

---

## Dynamic Web Scraping

For websites that generate content via JavaScript, Selenium is used with a headless browser:

```python
opts = Options()
opts.add_argument("--headless")
driver = webdriver.Firefox(options=opts)
driver.get(url)
# Wait for dynamic content, then extract
```

This makes the system suitable for both **static** and **dynamic** websites.

---

## Automated Scheduling

The `schedule` library automates periodic execution:

```python
schedule.every().day.at("10:00").do(task_run, base_page)

while True:
    schedule.run_pending()
    time.sleep(60)
```

The scraper runs daily at a configured time without manual intervention.

---

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/br-mariem/brmarieminternship.git
cd brmarieminternship
```

**2. Create a virtual environment**

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

Key dependencies: `requests`, `beautifulsoup4`, `selenium`, `schedule`

---

## Usage

Each document category has its own entry point:

```bash
# Central Bank of Tunisia documents
python CBTmain.py

# Official bulletins
python bulletinmain.py

# Public notices
python avismain.py

# Annual reports
python RapportsAnnuelsmain.py
```

On each run, the scraper:
1. Accesses the target page
2. Extracts available document URLs
3. Checks each URL against stored hashes
4. Downloads only new documents
5. Organizes files into the output directory
6. Stores hashes for future runs

---

## Output

Downloaded documents are organized by type:

```
documents/
├── bulletins/
├── notices/
├── annual_reports/
└── notes/
```

JSON files track processed documents and hashes between executions, maintaining persistent state across runs.

---

## Future Improvements

- Centralized configuration file (`.env` or `config.yaml`)
- Complete logging system
- Improved error handling and retry logic
- Relational database for document metadata
- Parallel scraping across multiple sources
- Docker containerization
- REST API for accessing scraped documents
- Web dashboard for monitoring scraping activities
- Automated tests
- Email/notification alerts for newly published documents

---

## Author

**Mariem Braham**  
Industrial Computer Science Engineering Student  

Interests: Artificial Intelligence · Robotics · Embedded Systems · Software Engineering · Intelligent Automation

---

## License

This project was developed for educational and professional purposes.
