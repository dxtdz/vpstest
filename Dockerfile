FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Ho_Chi_Minh

# Cài gói cơ bản + Python + noVNC + desktop nhẹ
RUN apt update && apt upgrade -y && \
    apt install -y python3 python3-pip python3-venv \
    supervisor xfce4 xfce4-terminal novnc websockify x11vnc xvfb \
    net-tools sudo wget curl unzip git && \
    pip3 install --no-cache-dir flask psutil flask-socketio eventlet && \
    mkdir -p /root/.vnc

# Đặt mật khẩu VNC
RUN x11vnc -storepasswd 123456 /root/.vnc/passwd

# Copy file Flask app và script
COPY main.py /app/main.py
COPY start.sh /app/start.sh
COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN chmod +x /app/start.sh

EXPOSE 8080 5900 6900

CMD ["/app/start.sh"]
