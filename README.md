# Skin Disease Image Classification Using ResNet-50

## Introduction
This repository contains a project for classifying skin diseases using deep learning techniques. The model is built using ResNet-50, a popular convolutional neural network architecture, and leverages transfer learning for effective and efficient training. The trained model is then deployed as a Flask web application, containerized using Docker for easy deployment and scalability.

## Features
ResNet-50 Transfer Learning: Utilizes a pre-trained ResNet-50 model, fine-tuned to classify different types of skin diseases.
Docker Containerization: The Flask application and model are encapsulated in a Docker container for easy deployment on any platform.
Flask Web Application: Provides a simple and intuitive web interface where users can upload images and get predictions for skin disease classification.

## Installation and Setup
1. Clone the Repository
bash
Copy code
[(https://github.com/shelearnai/SkinImaegDeploy.git)]
cd SkinImaegDeploy
2. Set Up the Virtual Environment (Optional)
It's recommended to use a virtual environment to manage dependencies.

bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install Required Python Packages
Install the necessary Python packages using requirements.txt.

bash
Copy code
pip install -r requirements.txt
4. Build and Run the Docker Container
To build and run the Docker container, follow these steps:

## Build the Docker Image:

bash
Copy code
docker build -t skin-disease-classification .
Run the Docker Container:

bash
Copy code
docker run -p 5000:5000 skin-disease-classification
5. Access the Web Application
Once the Docker container is running, you can access the web application by navigating to http://localhost:5000 in your web browser. Upload an image of a skin condition to get a prediction.

## Usage
Upload an Image: Use the web interface to upload an image of the skin condition.
Get Prediction: The model will classify the image and provide the result along with the predicted class.
Explore Results: The result will be displayed on the web page, showing the classified skin disease type.
## Troubleshooting
Ensure Docker is properly installed and running on your system.
If you encounter issues with dependencies, ensure that the requirements.txt file has been fully installed in your environment.
If the web application does not start, check the Docker build logs for errors and ensure that all necessary files are included in the Docker build.
## Contributing
Contributions are welcome! If you have any improvements or bug fixes, feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

newly added
