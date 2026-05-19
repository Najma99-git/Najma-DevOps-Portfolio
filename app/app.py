from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route('/')
def hello():
    return "Welcome to Flask + Redis!"

@app.route('/count')
def count():
    r.incr('hits')
    return f"Visit count: {r.get('hits').decode('utf-8')}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
