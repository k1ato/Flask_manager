#!/bin/bash
python -m pip install argparse
python -m pip install requests
python -m pip install importlib
python -m pip install sys
python -m pip install requests
python -m pip install argparse
python -m pip install cmd
python -m pip install re
python -m pip install base64
python -m pip install urllib
python -m pip install nmap                       
python -m pip install pymysql
python -m pip install os

chmod +x flask_manager.py
ln -sf $(pwd)/flask_manager.py /usr/local/bin/flask_manager
