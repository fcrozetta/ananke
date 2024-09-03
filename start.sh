#!/bin/bash
cd backend
source .env
./.venv/bin/uvicorn src.main:app --port 8000 --host 0.0.0.0 &
cd ../frontend
npm run dev
