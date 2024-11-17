from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def process_request():
    if request.method == 'GET':
        tenant_id = request.args.get('tenant_id')
        domofon_id = request.args.get('domofon_id')
        apartment_id = request.args.get('apartment_id')
        
    elif request.method == 'POST':
        data = request.json
        tenant_id = data.get('tenant_id') if data else None
        domofon_id = data.get('domofon_id') if data else None
        apartment_id = data.get('apartment_id') if data else None
        
    if not domofon_id or not tenant_id or not apartment_id:
        return jsonify({'message': 'Missing arguments, tenant_id, domofon_id and apartment_id are required'}), 400
    
    return jsonify({'message': 'Request processed successfully'}), 200

if __name__ == '__main__':
    app.run(debug=False, port=4123, host="0.0.0.0")
