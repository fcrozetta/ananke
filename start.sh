#!/bin/bash
cd backend
./.venv/bin/uvicorn src.main:app --port 8000 --host 0.0.0.0 &
cd ../frontend
npm run dev