#!/bin/bash
echo "entering backend"
cd backend
echo "installing backend"
rm -rf ./.venv
python3 -m venv ./.venv
./.venv/bin/pip install -r requirements.txt

echo "entering frontend"
cd ../frontend
echo "installing frontend"
npm install