# Transformer Model App

Welcome to the Transformer Model App! This app is deployed using Streamlit and integrates various state-of-the-art transformer models to provide multiple text processing functionalities including text generation, question & answering, sentiment analysis, text summarization, and text translation.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
  - [Chatbot](#chatbot)
  - [Question & Answering](#question-answering)
  - [Sentiment Analysis](#sentiment-analysis)
  - [Text Summarization](#summarization)
  - [Text Translation](#translation)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Introduction

This app leverages the power of transformer models to perform various text processing tasks. It is deployed using Streamlit, making it easy to use through a web interface. The home page includes a welcome animation to enhance user experience.

## Features

### Chatbot
- **Model Used**: `mistralai/Mistral-7B-Instruct-v0.2`
- **Description**: Engage in interactive conversations with the Mistral-based chatbot. It generates human-like responses and can be used for casual chatting or specific queries.

### Question & Answering
- **Model Used**: `deepset/roberta-base-squad2`
- **Description**: Ask any question and get precise answers from the model. It uses a RoBERTa model fine-tuned on the SQuAD2 dataset to provide accurate answers based on the given context.

### Sentiment Analysis
- **Model Used**: `distilbert/distilbert-base-uncased-finetuned-sst-2-english`
- **Description**: Analyze the sentiment of any text input. This module uses a DistilBERT model fine-tuned on the SST-2 dataset to classify the sentiment as positive or negative.

### Summarization
- **Model Used**: `facebook/bart-large-cnn`
- **Description**: Summarize long pieces of text into concise summaries. The BART model is utilized to generate summaries that capture the essence of the original content.

### Translation
- **Model Used**: `google/t5-small`
- **Description**: Translate text from one language to another using the T5 model by Google. This module supports multiple language translations for various use cases.

## Installation

To run this app locally, follow these steps:

1. Clone the repository from the GitHub link provided.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Run the Streamlit app using the appropriate command.

## Usage

Once the app is running, open your web browser and navigate to the local server address provided by Streamlit to access the app. The home page will greet you with a welcome animation. You can then navigate to different modules using the sidebar.

Each module provides a simple interface to interact with the respective model:
- **Chatbot**: Type your message and get a response from the chatbot.
- **Question & Answering**: Input a question and a context, and receive an answer.
- **Sentiment Analysis**: Enter text to determine its sentiment.
- **Text Summarization**: Provide text to get a summarized version.
- **Text Translation**: Input text and select the target language for translation.

## Credits

This app is built using the following open-source models and technologies:
- [Streamlit](https://streamlit.io/)
- [Mistral](https://huggingface.co/mistral)
- [deepset/roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2)
- [distilbert/distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)
- [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)
- [google/t5-small](https://huggingface.co/google/t5-small)

We hope you find this app useful for your text processing needs. If you encounter any issues or have suggestions for improvement, please feel free to open an issue on the GitHub repository. Enjoy!
