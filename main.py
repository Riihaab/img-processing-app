from flask import Flask, request, send_file
from flask_pymongo import PyMongo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

app.config[
    'MONGO_URI'] = 'mongodb+srv://admin:tD7qQCDUGEXyMtX@cluster0.k2yqj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
mongo = PyMongo(app)

image_row_model = mongo.db.row_model


@app.route('/resize_image_and_save_to_db', methods=['POST'])
def resize_image_and_save_to_db():
    image_row_model.delete_many({})
    df = pd.read_csv('templates/img.csv')
    df = df.iloc[:, :151]
    image_data = df.to_dict('records')
    image_row_model.insert_many(image_data)
    return {'status': "ok"}


@app.route('/generate_image_frame', methods=['POST'])
def generate_image_frame():
    depth_min = float(request.args.get('depth_min', '0'))
    depth_max = float(request.args.get('depth_max', '10000'))

    data = list(image_row_model.find({'depth': {
        '$gte': depth_min, '$lte': depth_max
    }}, {'_id': False, 'depth': False}))
    data = [list(obj.values()) for obj in data]
    np_array = np.array(data)
    np_array = (np_array - np.min(np_array)) / (np.max(np_array) - np.min(np_array))
    plt.imsave('templates/frame.png', np_array, cmap='Greys')
    return send_file('templates/frame.png', mimetype='image/gif')


if __name__ == '__main__':
    app.run(port=5005, debug=True)
