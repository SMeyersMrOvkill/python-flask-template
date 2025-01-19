#!/bin/bash

# Install dependencies
sudo apt-get install -y python3-pip python3-dev
pip install -r requirements.txt
npm i
npm run start