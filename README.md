# Discussion Board App

## Installation

Installation instructions assume that Python and PostgreSQL are installed on the device. 

### Instructions:

1. Clone the repository to your local device.

2. Create virtual environment for the program:

```bash
python3 -m venv venv
```

3. Activate virtual environment:

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Initialize database:

```bash
psql (database name) < schema.sql
```

6. Start the program:

```bash
flask run
```

## Documentation

[Project Specification](https://github.com/Deepthetics/discussion-board-app/blob/main/documentation/project_specification.md)
