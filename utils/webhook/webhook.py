from flask import Flask, request, jsonify
from .handler_webhook import webhookHandler

core = Flask(__name__)

@core.route('/', methods=['GET', 'POST'])
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
    
    
    webhookHandler(tenant_id, domofon_id, apartment_id)
    
    return jsonify({'message': 'Request processed successfully'}), 200

if __name__ == '__main__':
    core.run(debug=False)
    #менять в main.py