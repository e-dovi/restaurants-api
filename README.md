## API to allow users to create and rate restaurants

# Clone and open the project
git clone https://github.com/e-dovi/restaurants-api
cd restaurants-api

# Create and activate the virtual environment
python3 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# Start the app
flask --app api.run run

## Environment variables
This project uses .env for config
New users should copy .env.example into .env with their actual secrets

DATABASE_URL – points to the SQLite database for the app
JWT_SECRET – secret key for signing/verifying JWT tokens

## Migrations
Migrations are set up in the code
But no migration history has been created or applied yet

To start a new migration run in order:
flask db init
flask db migrate -m"Initial migration"
flask db upgrade