from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def process_request():
    if request.method == 'GET':
        domofon_id = request.args.get('domofon_id')
        tenant_id = request.args.get('tenant_id')
    elif request.method == 'POST':
        data = request.json
        domofon_id = data.get('domofon_id') if data else None
        tenant_id = data.get('tenant_id') if data else None

    if not domofon_id or not tenant_id:
        return jsonify({'message': 'Both domofon_id and tenant_id are required'}), 400
    
    return jsonify({'message': 'Request processed successfully'}), 200

if __name__ == '__main__':
    app.run(debug=False)
