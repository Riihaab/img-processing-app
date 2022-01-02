# How to run the app

To run the app locally:
- pip3 install -r requirements.txt
- python3 main.py

To run the app with docker:
- docker build -t img-processing-app
- docker run -p 5005:5005 img-processing-app



-------------------------------


# Services

The app is deployed on Heroku under the domain name: img-processing-app.herokuapp.com

- Resize & save image to db
```
    method: POST
    endpoint: https://img-processing-app.herokuapp.com/resize_image_and_save_to_db
    body: {}
    headers: {}
```
- Request image frames based on depth_min and depth_max
```
    method: POST
    endpoint: https://img-processing-app.herokuapp.com/generate_image_frame?depth_min=<min_depth_value>&depth_max=<max_depth_value>
    body: {}
    headers: {}
```
