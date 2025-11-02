#!/usr/bin/env bash
set -e

echo "🚀 Starting Ubuntu GUI + Flask..."
# Chạy noVNC có sẵn từ base image
/etc/init.d/xvfb start || true
/etc/init.d/novnc start || true

# Chạy Flask
python3 main.py
