## How to run ##
cd database
python -m venv venv
# Activate the virtual environment 
source venv/bin/activate
# install sqlite if not installed
source venv/bin/activate
# install faker
pip install faker
# create the database and tables 
sqlite3 health_fitness_app.db  
# read database, then exit sqlite
.read base.sql
command+C
# populate data
python generate_fake_data.py
# run quereis 
sqlite3 health_fitness_app.db < queries.sql  
