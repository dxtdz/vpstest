from flask import Flask, render_template_string, request
import os, subprocess, psutil

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Ubuntu VPS - noVNC</title>
<style>
body { background: #0d1117; color: #e6edf3; font-family: sans-serif; text-align:center; }
a,button { background:#238636; color:white; border:none; padding:10px 20px; border-radius:6px; cursor:pointer; }
iframe { border:none; width:100%; height:600px; border-radius:10px; }
input { width:80%; padding:8px; margin:8px; border-radius:5px; border:1px solid #444; background:#161b22; color:white; }
</style>
</head>
<body>
<h2>🧠 Ubuntu VPS 24.04 (Python Ready)</h2>
<p>🔑 VNC Password: <b>123456</b></p>
<p><a href="/vnc">🖥️ Open Desktop (noVNC)</a></p>
<hr>
<h3>💻 Bash Console</h3>
<form method="POST" action="/run">
<input name="cmd" placeholder="Enter bash command..." autocomplete="off"/>
<button type="submit">Run</button>
</form>
<pre style="text-align:left;width:90%;margin:auto;background:#161b22;padding:10px;border-radius:6px;">{{output}}</pre>
<hr>
<h4>System Info</h4>
<p>CPU: {{cpu}}% | RAM: {{ram}}% | Disk: {{disk}}%</p>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML, output='', cpu=psutil.cpu_percent(), ram=psutil.virtual_memory().percent, disk=psutil.disk_usage('/').percent)

@app.route('/run', methods=['POST'])
def run_cmd():
    cmd = request.form.get('cmd', '')
    try:
        result = subprocess.getoutput(cmd)
    except Exception as e:
        result = str(e)
    return render_template_string(HTML, output=result, cpu=psutil.cpu_percent(), ram=psutil.virtual_memory().percent, disk=psutil.disk_usage('/').percent)

@app.route('/vnc')
def vnc():
    return '<iframe src="http://localhost:6900/vnc.html?autoconnect=true" width="100%" height="800px"></iframe>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
