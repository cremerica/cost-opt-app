from flask import Flask
import threading

app = Flask(__name__)

memory_load = []
cpu_running = False
cpu_thread = None

def cpu_worker():
    global cpu_running
    while cpu_running:
        # Simulate CPU load
        sum(i for i in range(100000))

@app.route('/')
def hello():
    return 'Hello, World! Memory load: {}, CPU running: {}'.format(len(memory_load), cpu_running)

@app.route('/increase_memory')
def increase_memory():
    memory_load.append([0] * 1000000)  # ~4MB
    return 'Memory increased. Current load: {}'.format(len(memory_load))

@app.route('/decrease_memory')
def decrease_memory():
    if memory_load:
        memory_load.pop()
    return 'Memory decreased. Current load: {}'.format(len(memory_load))

@app.route('/increase_cpu')
def increase_cpu():
    global cpu_running, cpu_thread
    if not cpu_running:
        cpu_running = True
        cpu_thread = threading.Thread(target=cpu_worker)
        cpu_thread.daemon = True
        cpu_thread.start()
    return 'CPU load increased'

@app.route('/decrease_cpu')
def decrease_cpu():
    global cpu_running
    cpu_running = False
    return 'CPU load decreased'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)