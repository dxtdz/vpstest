FROM dorowu/ubuntu-desktop-lxde-vnc:jammy

# Cài Python 3.12 và các công cụ cần thiết
RUN apt update && apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt update && apt install -y python3.12 python3.12-venv python3.12-distutils python3-pip && \
    ln -sf /usr/bin/python3.12 /usr/bin/python3 && \
    apt install -y sudo wget curl unzip git xfce4 xfce4-terminal x11vnc xvfb novnc websockify net-tools supervisor && \
    pip3 install --no-cache-dir -r /app/requirements.txt && \
    mkdir -p /app

WORKDIR /app
COPY . /app

EXPOSE 5000 6080
CMD ["supervisord", "-c", "/app/supervisord.conf"]
