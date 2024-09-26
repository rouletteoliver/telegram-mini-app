from flask import Flask, request, jsonify

app = Flask(__name__)

# Хранилище состояния кошелька, здесь будет храниться информация о подключении
wallet_status = {
    "connected": False,
    "wallet_address": ""
}

# Эндпоинт для получения состояния подключения
@app.route('/get_wallet_status', methods=['GET'])
def get_wallet_status():
    return jsonify(wallet_status)

# Эндпоинт для обновления состояния подключения
@app.route('/update_wallet_status', methods=['POST'])
def update_wallet_status():
    data = request.json
    wallet_status['connected'] = data.get('connected', False)
    wallet_status['wallet_address'] = data.get('wallet_address', "")
    return jsonify({"message": "Status updated successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
