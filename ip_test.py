from flask import Flask
import requests

app = Flask(__name__)

@app.route('/get_ip', methods=['GET'])
def get_ip():
    try:
        response = requests.get('https://ifconfig.me')
        return f"Vercel's outgoing IP address is: {response.text}", 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
