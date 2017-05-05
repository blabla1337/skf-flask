#Install requirements
pip3 install -r requirements.txt

# SKF initdb
export FLASK_APP=skf/app.py
flask initdb


# Configure Path & warnings
export PYTHONPATH=.:$PYTHONPATH
export PYTHONWARNINGS="ignore"

# Run the SKF app
python3.6 skf/app.py

OR 

# run python testing
python3.6 setup.py test

OR

# run python testing and coverage
python3.6 tests/run.py 

