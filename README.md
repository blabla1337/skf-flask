#Install requirements
pip3 install -r requirements.txt

# SKF initdb
export FLASK_APP=skf/app.py
flask initdb


# Configure Path
export PYTHONPATH=.:$PYTHONPATH

# Run the SKF app
python3.6 skf/app.py
