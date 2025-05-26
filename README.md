### Freebie Tracker
A Python SQLAlchemy project that models a many-to-many relationship between companies and developers through a join table of freebies. It supports data tracking, querying, and relationship logic, and includes migrations using Alembic.

### Features
Company Management: Create companies and track which freebies they’ve given.

Developer Management: Create developers and track received freebies.

Freebie Tracking: Each freebie has an item name and a value, and links a company to a developer.

Relationships:

Many-to-many: A developer can receive many freebies from different companies.

A company can give many freebies to different developers.

Aggregate Methods:

Total freebies per developer or company.

Find the most generous company.

Determine which developer received a specific freebie.

Input Validation: Basic validation included in seed logic and model relationships.

Database Migrations: Handled via Alembic.

Interactive Debugging: debug.py opens an ipdb shell for hands-on testing.

Unit Testing: Organized under a tests/ directory and run using pytest.

### Project Structure

freebie-tracker/
├── alembic/
│   ├── versions/
│   │   ├── 06ce942574fb_Add relationships
│   │   ├── 7fd88b70e08d_Create freebies table
│   │   └── 79f491ad095c_Create dev, company, and freebie tables
│   ├── env.py
│   ├── README
│   └── script.py.mako
├── alembic.ini
├── lib/
│   ├── __pycache__/
|   |__ migrations/
|   |     |__ versions/
|   |           |__5f72c58bf48c_ create companies, devs
|   |           |__7a71dbf71c64_create db
|   |     |__env.py 
|   |     |__README
|   |     |__script.py.mako
│   ├── debug.py
│   ├── models.py
│   ├── seed.py
│   └── alembic.ini
└── README.md

### Installation & Setup
### Fork and Clone the Repository
fork - https://github.com/Waith93/freebie-tracker.git
then clone.
in your terminal:
cd to where you want to store the file. 
cd freebie-tracker, then git clone

### Create and Activate a Virtual Environment

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### To Generate a New Migration:

alembic revision --autogenerate -m "Your message here"
To Apply Migrations (Create or Upgrade the DB):

alembic upgrade head

If you're running this for the first time, head will apply all migrations and create the required tables.

### Seeding the Database
To populate the database with sample data, run:

python lib/seed.py
You should see sample data printed to confirm insertion.

### Running the Debug Shell
To experiment with models and queries interactively:

python lib/debug.py
This will start an ipdb shell with access to your SQLAlchemy session and models.

### Database Schema Diagram
You can open the database schema visualization in your browser:

https://dbdiagram.io/d/Freebies-diagram-6834cd896980ade2eb7e3872

### Author
Stacy Waithera