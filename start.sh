#!/usr/bin/env bash
set -e

echo "🧠 Starting virtual display..."
export DISPLAY=:1
Xvfb :1 -screen 0 1024x768x24 &

echo "🪟 Starting desktop environment..."
startxfce4 &

echo "🔐 Starting x11vnc..."
x11vnc -forever -usepw -shared -rfbport 5900 -display :1 &

echo "🌐 Starting noVNC..."
websockify --web=/usr/share/novnc/ 6900 localhost:5900 &

echo "🚀 Starting Flask web..."
python3 main.py
