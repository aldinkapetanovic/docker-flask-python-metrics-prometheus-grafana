from flask import Flask, Response
from prometheus_client import Gauge, generate_latest
import requests

app = Flask(__name__)

# Define Prometheus metrics
website_up_metric = Gauge('website_up', 'Website availability (1=up, 0=down)')
response_time_metric = Gauge('response_time_seconds', 'Website response time in seconds')

@app.route('/metrics')
def metrics():
    website_status, response_time = check_website_status()

    # Set Prometheus metrics values
    website_up_metric.set(int(website_status))
    response_time_metric.set(response_time)

    # Generate Prometheus exposition format
    metrics_data = generate_latest()

    return Response(metrics_data, mimetype='text/plain')

def check_website_status():
    try:
        response = requests.get('http://google.com')
        return response.status_code == 200, response.elapsed.total_seconds()
    except Exception as e:
        return False, None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
