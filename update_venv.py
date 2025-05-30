pip install --upgrade pip
pip install --upgrade setuptools wheel
pip freeze > requirements.txt
pip install --upgrade -r "$REQ_FILE"
pip freeze > requirements.txt
