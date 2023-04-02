import docker
from flask import Flask, render_template, request, Markup, redirect, url_for
import socket
from simpleicons.all import icons
app = Flask(__name__)

@app.route('/')
def index():
    client = docker.from_env()
    containers = client.containers.list()

    host_ip = socket.gethostbyname(socket.gethostname())
    
    container_info = []
    for container in containers:
        try:
            host_port = list(container.ports.values())[0][0]['HostPort']
        except (TypeError, IndexError):
            host_port = None
        if host_port:
            try:
                container_info.append({'name': container.name.split("_")[0], 'url': f'http://{host_ip}:{host_port}/', 'icon' : {'path': icons.get(container.name.split("_")[0].lower()).path,'color': icons.get(container.name.split("_")[0].lower()).hex}})
            except:
                container_info.append({'name': container.name.split("_")[0], 'url': f'http://{host_ip}:{host_port}/', 'icon' : {'path': 'M17.657 6.343a.999.999 0 0 0-1.414 0L12 10.586 7.757 6.343a.999.999 0 1 0-1.414 1.414L10.586 12l-4.243 4.243a.999.999 0 1 0 1.414 1.414L12 13.414l4.243 4.243a.999.999 0 1 0 1.414-1.414L13.414 12l4.243-4.243a.999.999 0 0 0 0-1.414z','color': 'FF0000'}})
    return render_template('index.html', container_info=container_info)
    

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        color = request.form['color']
        with open('static/style.css', 'w') as f:
            f.write('body { background-color: %s; }' % color)
        return redirect(url_for('index'))
    return render_template('settings.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
