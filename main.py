from flask import Flask, render_template_string
from flask_socketio import SocketIO, emit
import subprocess

app = Flask(__name__)
socketio = SocketIO(app)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>Ubuntu Web VPS</title>
  <style>
    body { background: #0d1117; color: #e6edf3; font-family: monospace; text-align: center; }
    iframe { width: 90%; height: 600px; border: 2px solid #222; border-radius: 10px; }
    #term { width: 90%; height: 200px; background: #000; color: #0f0; overflow-y: scroll; margin: 20px auto; padding: 10px; border-radius: 10px; text-align: left; }
    input { width: 90%; padding: 10px; border-radius: 10px; border: none; outline: none; background: #161b22; color: #fff; }
  </style>
</head>
<body>
  <h1>💻 Ubuntu VPS (Python 3.12)</h1>
  <iframe src="http://localhost:6080/vnc.html" title="Ubuntu Desktop"></iframe>
  <h3>Bash Console:</h3>
  <div id="term"></div>
  <input id="cmd" placeholder="Nhập lệnh Bash ở đây..." autocomplete="off"/>
  <script src="https://cdn.socket.io/4.0.1/socket.io.min.js"></script>
  <script>
    const socket = io();
    const term = document.getElementById('term');
    const input = document.getElementById('cmd');
    input.addEventListener('keydown', e => {
      if (e.key === 'Enter') {
        socket.emit('command', input.value);
        input.value = '';
      }
    });
    socket.on('output', data => {
      term.innerHTML += data + "\\n";
      term.scrollTop = term.scrollHeight;
    });
  </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@socketio.on('command')
def handle_command(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        result = e.output
    emit('output', result)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
