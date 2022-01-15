from flask import Flask, jsonify, request
from flask_cors import CORS



# configuration
DEBUG = True

VCENTER = [
    {   'id': '1',
        'vCenter': 'VDA1',
        'MachineName': 'Server2012',
        'MachineOpt': 'Windows',
        'ToolStatus': 'PoweredOn',
        'UserName':'John'


    },
      { 'id': '1',
        'vCenter': 'VDA1',
        'MachineName': 'Linux',
        'MachineOpt': 'Linux',
        'ToolStatus': 'OffLine',
        'UserName':'Jim'


    }]
    
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Get Books
@app.route('/vsphere', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        VCENTER.append({
            'id': post_data.get('id'),
            'vCenter': post_data.get('vCenter'),
            'MachineName': post_data.get('MachineName'),
            'MachineOpt': post_data.get('MachineOpt'),
            'ToolStatus': post_data.get('ToolStatus'),
            'UserName': post_data.get('UserName')
        })
    else:
        response_object['vcenters'] = VCENTER
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
