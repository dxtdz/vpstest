FROM dorowu/ubuntu-desktop-lxde-vnc:focal

USER root
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Ho_Chi_Minh

# Cập nhật + cài Python 3.12
RUN apt update && apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt update && apt install -y python3.12 python3.12-venv python3.12-distutils python3-pip && \
    ln -sf /usr/bin/python3.12 /usr/bin/python3 && \
    pip3 install --no-cache-dir flask psutil flask-socketio eventlet && \
    mkdir -p /app

# Copy Flask app và script
COPY main.py /app/main.py
COPY start.sh /app/start.sh
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN chmod +x /app/start.sh

# Expose ports: noVNC (6080) + Flask (8080)
EXPOSE 8080 6080

CMD ["/app/start.sh"]
