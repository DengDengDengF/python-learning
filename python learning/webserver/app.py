from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
import time

app = Flask(__name__)
CORS(app)  # 可选：允许所有域访问此应用的所有路由


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({
        'received': data
    })


@app.route('/api/add', methods=['GET'])
def add():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({
        'result': a + b
    })


# sse流传输
message = "Hello, this is a stream message!"
message_sent = False


@app.route('/stream')
def stream():
    global message_sent

    def generate():
        global message_sent
        if not message_sent:
            for char in message:
                yield f"data: {char}\n\n"
                time.sleep(0.1)  # 模拟延迟
            message_sent = True
        else:
            yield f"data: \n\n"  # 消息发送完毕后发送空消息

    return Response(generate(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)
