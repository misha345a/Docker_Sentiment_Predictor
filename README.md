## Docker Sentiment Predictor

![docker-flask-flair](https://user-images.githubusercontent.com/84154105/144725463-eab0531c-02cf-47ff-9c64-87409cca4b16.jpg)

This project deploys a simple sentiment prediction interface using Flask and Docker. <br>
Once a user enters a valid text input, sentiment is automatically predicted and displayed as POSITIVE or NEGATIVE along with the model's confidence score for that prediction.

<b>Update:</b><br>
The Docker image is now deployed to Heroku as well. <br>
You can check out the full web app using this link: <br>
http://flask-sentiment-predictor.herokuapp.com/

## Model
The text classification model is a pre-trained variation of BERT, which is downloaded and run using Flair - a powerful NLP library. 
This model has been trained on corpora from large sentiment datasets, including Amazon product reviews and movie reviews.

## Usage
Docker is used to package the application, as well as the necessary libraries, to avoid conflicting system requirements and dependencies for other users. 

The container image for this project can be pulled directly from Docker Hub. <br>
Once you have Docker installed and set up, simply run the following command in the terminal: <br>
```bash
docker run -dp 8000:8000 misha345a/flask_sentiment_predictor:latest
``` 

This will pull down the image from the registry and start the app. <br>

![Image](https://user-images.githubusercontent.com/84154105/144734190-f770b9a8-0606-45ed-a86b-47200d60b1e8.png)

Once complete, view the Flask app with your browser on http://localhost:8000/. <br>
If you are using Docker Toolbox, then you may have to visit the Toolbox VM’s private IP address instead. <br>
Most likely, this address will be http://192.168.99.100:8000/. And if not, check for the correct IP using the ```docker-machine ip``` command.

As an easy alternative, you can also run the image using the same command on Docker's playground environment: <br>
https://labs.play-with-docker.com/. A badge with the label 8000 will appear once the image is pulled. Click on it to launch the app.

## Demo
![Flask_App_Demonstration](https://user-images.githubusercontent.com/84154105/144725467-4b73b8be-d8d2-406f-aa3e-e952d416f2c3.gif)
