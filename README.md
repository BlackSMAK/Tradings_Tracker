# Tradings Tracker
A web-based trade/import job-card management system built with **Python Flask** and **Oracle Database**. It allows users to create, view, and filter trading job cards along with their associated accounts, goods, companies, countries, categories, and statuses.
---
## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Database Schema](#database-schema)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup & Installation](#setup--installation)
- [Running the Application](#running-the-application)
- [Routes Overview](#routes-overview)
---
## Features
- **Home Dashboard** – Two main actions: *View Job Cards* and *Add Job Cards*.
- **Add Job Card (multi-step form)**
  1. Enter bill/account details (Bill No, Item Cost, Duties, Taxes, Total Cost).
  2. Assign a status and payment status.
  3. Complete the job card with company, country, goods, category, and date.
- **View & Filter** – Browse and filter data from six tables:
  - Goods
  - Accounts
  - Categories
  - Status (with optional join against Accounts)
  - Countries
  - Companies
- **Auto-ID Generation** – IDs (e.g., `JOB001`, `ST001`) are automatically generated with sequential numbering.
---
## Tech Stack
| Layer     | Technology                          |
|-----------|-------------------------------------|
| Backend   | Python 3, Flask                     |
| Database  | Oracle Database XE (via `cx_Oracle`) |
| Frontend  | HTML5, CSS3 (Jinja2 templates)      |
---
## Database Schema
Six tables make up the schema (defined in `Backend_SQL.txt`):
| Table             | Primary Key   | Description                                   |
|-------------------|---------------|-----------------------------------------------|
| `Accounts_Table`  | `Bill_No`     | Financial details per bill (costs, duties, taxes) |
| `Category_Table`  | `Category_ID` | Goods categories                              |
| `Companies`       | `Company_ID`  | Trading companies                             |
| `Countries`       | `Country_ID`  | Countries of origin/destination               |
| `Goods_Table`     | `Good_ID`     | Individual goods linked to a job card         |
| `Job_Card`        | `Job_ID`      | Core job card linking all other entities      |
| `Status_Table`    | `Status_ID`   | Shipment and payment status per job card      |
### Key Relationships
- `Job_Card` references `Accounts_Table`, `Category_Table`, `Companies`, and `Countries`.
- `Goods_Table` and `Status_Table` reference `Job_Card`.
- `Status_Table` joins with `Accounts_Table` via `Bill_No` for combined financial/status views.
---
## Project Structure
```
Tradings_Tracker/
├── App.py                          # Main Flask application
├── Backend_SQL.txt                 # Oracle SQL schema (table creation + constraints)
├── static/
│   ├── styles.css                  # Home page styles
│   ├── Add.css                     # Add form styles
│   ├── View.css                    # View/selection page styles
│   ├── *.png                       # UI button and background images
└── templates/
    ├── main.html                   # Home page
    ├── view_job_card.html          # View selection menu
    ├── Add_Job_Card.html           # Add job card form
    ├── Add_Status.html             # Add status form
    ├── Bill_No_Entry.html          # Add account/bill form
    ├── Selected_View_For_Goods.html
    ├── Selected_View_For_Accounts.html
    ├── Selected_View_For_Category.html
    ├── Selected_View_For_Status.html
    ├── Selected_View_For_Countries.html
    └── Selected_View_For_Company.html
```
---
## Prerequisites
- Python 3.8+
- Oracle Database XE (running locally on port `1521` with SID `xe`)
- Oracle Instant Client (required by `cx_Oracle`)
- pip packages: `flask`, `cx_Oracle`
---
## Setup & Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/SMAhmedKhalid/Tradings_Tracker.git
   cd Tradings_Tracker
   ```
2. **Install Python dependencies**
   ```bash
   pip install flask cx_Oracle
   ```
3. **Set up the Oracle database**
   - Ensure Oracle XE is running on `localhost:1521` with SID `xe`.
   - Create a database user and run the schema script:
     ```sql
     CREATE USER ProjectDB IDENTIFIED BY Fast123;
     GRANT CONNECT, RESOURCE TO ProjectDB;
     ```
   - Execute all statements in `Backend_SQL.txt` while connected as `ProjectDB`.
4. **Configure the database connection** *(optional)*
   - The connection details are hardcoded in `App.py` inside `get_db_connection()`. Update `host`, `port`, `sid`, `user`, and `password` as needed.
---
## Running the Application
```bash
python App.py
```
The app starts in debug mode and is accessible at **http://127.0.0.1:5000**.
---
## Routes Overview
| Method     | Route                              | Description                              |
|------------|------------------------------------|------------------------------------------|
| GET        | `/`                                | Home page                                |
| GET        | `/view`                            | View job cards selection menu            |
| GET        | `/view/<option>`                   | Navigate to a specific view page         |
| GET/POST   | `/Selected_View_For_Goods`         | View/filter goods                        |
| GET/POST   | `/Selected_View_For_Countries`     | View/filter countries                    |
| GET/POST   | `/Selected_View_For_Category`      | View/filter categories                   |
| GET/POST   | `/Selected_View_For_Company`       | View/filter companies                    |
| GET/POST   | `/Selected_View_For_Accounts`      | View/filter accounts                     |
| GET/POST   | `/Selected_View_For_Status`        | View/filter status (with optional join)  |
| GET/POST   | `/add_account`                     | Step 1 – Add bill/account details        |
| GET/POST   | `/add_status`                      | Step 2 – Add status entry                |
| GET/POST   | `/add_job_card/<bill_no>/<status_id>` | Step 3 – Complete the job card        |
