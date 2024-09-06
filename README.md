# LLM Project

## Overview

The **LLM Project** is a machine learning application designed to analyze text prompts and determine whether they are AI-generated or human-generated
This project leverages a fine-tuned language model to classify text inputs.

The primary goal of this project is to enhance my skills with LLMs. By developing and deploying a real-world application, I aim to:
- Deepen my understanding of machine learning models
- Explore the practical aspects of LLMs in a scalable environment 
- Improve my Python coding abilities

Additionally, I’ve also improved my JavaScript skills throughout the development of this project.

## Project Versions
There are 2 versions for this project:

### Local Development Branch (main)

- **Purpose**: This branch contains scripts and code for local development, including JavaScript and database integration.
- **Features**: Includes setup for running the application locally without the need for deployment costs.
- **Usage**: Ideal for development, testing, and running the application on your local machine.

### Streamlit Deployment (master)

- **Purpose**: This branch contains the Streamlit application code, which is intended for the deployed version of the project.
- **Features**: Provides a user-friendly web interface for interacting with the model and viewing predictions.
- **Deployment**: Use this branch to deploy the application to cloud platforms or other hosting services.

## Pre-requisites
- Python 3.12+
- Python libraries are listed in [`requirements.txt`](./requirements.txt)
- JavaScript dependencies are listed in [`package.json`](https://github.com/AxelPribadi/LLMProject/blob/main/client/package.json) (found in the main branch)

## Additional Notes
Dataset: [AI vs Human Text](https://www.kaggle.com/datasets/shanegerami/ai-vs-human-text)

Fine-Tuned LLM Model claims to be 99% accurate though it seems to be overtrained. 
This issue can be addressed by adjusting the learning rate and other hyperparameters.
