#!/bin/bash

apt-get update -qy
apt-get install -y python-dev python-pip
pip install -r requirements.txt
python src/manage.py test

