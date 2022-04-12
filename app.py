import string
import requests
from flask import Flask, redirect, render_template, request
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/new_pet', methods=['GET'])
def person():
    return render_template('new_pet.html')


@app.route('/pet_detail', methods=['POST'])
def pet_detail():
    api_url = "https://petstore.swagger.io/v2/pet"
    id = request.form['id']
    name = request.form['name']
    status = request.form['status']
    new_data = {
                    "id": id,
                    "category": {
                        "id": 0,
                        "name": "string"
                    },                    "name": name,
                    "photoUrls": [
                        "string"
                    ],
                    "tags": [
                        {
                            "id": 0,
                            "name": "string"
                        }
                    ],
                    "status": status
                }
    response = requests.post(api_url, json=new_data)
    return render_template('pet_detail.html', value=(id, name, status))


@app.route('/pet/', methods=['GET'])
def pets(status: str = "pending"):
    url2 = "https://petstore.swagger.io/v2/pet/findByStatus?status={0}".format(status)
    response = requests.get(url2)
    data_pets = [(i['id'], i['name'], i['status']) for i in response.json()]
    #print(data_pets)
    return render_template('pets.html', value=data_pets)


@app.route('/pet_update/<id_pet>', methods=['GET'])
def pet_update(id_pet):
    return render_template('pet_update.html', value=id_pet)


@app.route('/pet_update_detail', methods=['POST'])
def pet_update_detail():
    api_url_update = "https://petstore.swagger.io/v2/pet"
    id = request.form['id']
    name = request.form['name']
    status = request.form['status']
    update_data = {
                        "id": id,
                        "category": {
                            "id": 0,
                            "name": "string"
                        },
                        "name": name,
                        "photoUrls": [
                            "string"
                        ],
                        "tags": [
                            {
                                "id": 0,
                                "name": "string"
                            }
                        ],
                        "status": status
                    }
    response = requests.put(api_url_update, json=update_data)
    return render_template('pet_detail.html', value=(id, name, status))


@app.route('/pet_delete/<id_pet>', methods=['GET'])
def pet_delete(id_pet):
    api_url = "https://petstore.swagger.io/v2/pet/{0}".format(id_pet)
    response = requests.delete(api_url)
    return render_template('pet_detail.html', value="Delete successfully")

'''
@app.route("/stores")
def stores():
    return render_template('stores.html')
'''

@app.route('/new_store', methods=['GET'])
def new_store():
    return render_template('new_store.html')

@app.route('/store_detail', methods=['POST'])
def store_detail():
    api_url = "https://petstore.swagger.io/v2/store/order"
    id = request.form['id']
    petId = request.form['petId']
    quantity = request.form['quantity']
    shipDate = request.form['shipDate']
    status = request.form['status']
    complete = request.form['complete']
    new_data_store = {
                         "id": id,
                         "petId": petId,
                         "quantity": quantity,
                         "shipDate": shipDate,
                         "status": status,
                         "complete": complete
                     }
    response = requests.post(api_url, json=new_data_store)
    return render_template('store_detail.html', value=(id, petId, quantity, shipDate, status, complete))

@app.route('/stores')
def store():
    return render_template('stores.html', value=0)

@app.route('/stores_search', methods=['POST'])
def storess(): 
    id = request.form['search']
    if id:
        print(id)
    else:
        id=0
    
    rute = '/stores/{0}'.format(id)
    return redirect(rute)

@app.route('/stores/<id>', methods=['GET'])
def stores(id):
    url3 = "https://petstore.swagger.io/v2/store/order/{0}".format(id)
    response = (requests.get(url3))
    response_json = response.json()
    #od = list(response_json.values())
    data_stores = [(i) for i in response_json.values()]
    #print(data_stores)

    '''
    od = {
        "id": response_json['id'],
        "shipDate": response_json['shipDate']
    }
    print(od['id'])
    '''
    #data_stores = [(i['id'], i['petId'], i['quantity'], i['shipDate'], i['status'], i['complete']) for i in response.json()]
    return render_template("stores.html", value=data_stores)

@app.route('/store_delete/<id>', methods=['GET'])
def store_delete(id):
    api_url_delete = "https://petstore.swagger.io/v2/store/order/{0}".format(id)
    response = requests.delete(api_url_delete)
    return render_template('store_detail.html', value = "id: " + id + " Deleted successfully")

@app.route('/stores/inventory')
def store_inventory():
    api_uri_inventory = "https://petstore.swagger.io/v2/store/inventory"
    response = (requests.get(api_uri_inventory))
    data_json = response.json()
    data = [ (i) for i in data_json.items()]
    #print(data)
    return render_template('inventory.html', value=data)


'''
@app.route('/pet', methods=['GET'])
def pets(status: str = "pending"):
    url2 = "https://petstore.swagger.io/v2/pet/findByStatus?status={0}".format(status)
    response = requests.get(url2)
    data_pets = [(i['id'], i['name'], i['status']) for i in response.json()]
    return render_template('pets.html', value=data_pets)
'''


'''
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
'''
if __name__ == '__main__':
    app.run()






'''
id
petId
quantity
shipDate
status
complete
'''