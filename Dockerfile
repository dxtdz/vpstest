FROM dorowu/ubuntu-desktop-lxde-vnc:noble

USER root
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Ho_Chi_Minh

# Cập nhật và cài Python 3.12 sẵn (Ubuntu 24.04)
RUN apt update && apt install -y python3 python3-pip python3-venv && \
    pip3 install --no-cache-dir flask psutil flask-socketio eventlet && \
    mkdir -p /app

# Copy Flask app và script
COPY main.py /app/main.py
COPY start.sh /app/start.sh
COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN chmod +x /app/start.sh

EXPOSE 8080 6080

CMD ["/app/start.sh"]
