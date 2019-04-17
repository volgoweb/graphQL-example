Example of API based on graphQL.

# Installation

1. Clone the repository:
    git clone ...
2. Create a virtual environment:
    virtualenv -p python3.6 graphQL-example-env
3. Install all requirements into the virtual environment:
    source graphQL-example-env/bin/activate && pip install -r graphQL-example/requirements.txt -y
4. Create db with structure:
    python3 manage.py create_db
5. Go to the folder with code (graphQL-example) and run the app:
    python3 run.py
