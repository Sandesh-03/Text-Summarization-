# 📝 Text Summarization Application

![Python](https://img.shields.io/badge/Python-Backend-yellow?logo=python&style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

This repository contains a **Text Summarization Application** that leverages NLP techniques to summarize long pieces of text. The project includes a data ingestion pipeline and an organized logging system to track the data processing stages. ***Forked from the Krish Naik repository***

---

## 📜 Description

The **Text Summarization** application includes several stages such as **data ingestion**, **data extraction**, and **model training**. This project aims to simplify the process of summarizing large text files by providing an easy-to-use pipeline for training and testing NLP models.

Key features:
- **Data Ingestion Pipeline**: Downloads and extracts data from a given URL.
- **Text Processing**: Cleans and prepares the data for training.
- **Logging System**: Tracks each stage of the data processing and model training using logging.

---

## 🚀 Running Steps

### 🛠 Backend Setup

   1. **Clone the repository:**
      ```
      git clone https://github.com/Sandesh-03/Text-Summarization-/tree/main
      cd Text-Summarization-
      
      ```

  3. **Install the required Python dependencies:**
      ```
     pip install -r requirements.txt
      
      ```
  4. **Run The porject**
      ```
      python api.py
      
      ```
 The server will start running at http://127.0.0.1:5001.
 
---

## 📂 Project Structure

  ```
  root
├── src/                  # Source code
│   ├── textSummarizer/   # Main module for text summarization
│   │   ├── __init__.py   # Initialize package
│   │   ├── config/       # Configuration files for the project
│   │   │   └── configuration.py # Configuration manager
│   │   ├── components/   # Code components for processing data
│   │   │   ├── data_ingestion.py # Data ingestion logic
│   │   │   └── __init__.py
│   │   ├── logging/      # Logging configuration
│   │   ├── pipeline/     # Data processing pipeline
│   │   │   ├── stage_01_data_ingestion.py # Data ingestion pipeline
│   │   │   └── __init__.py
│   │   ├── constants/    # Constants used across the app
│   │   ├── entity/       # Data models
│   │   ├── utils/        # Utility functions for reading YAML, file handling
│   │   └── logging/__init__.py
│   ├── config.yaml       # Configuration YAML file for paths
├── app.py                # Main entry point for the application
├── main.py               # Script to run data ingestion pipeline
├── Dockerfile            # Docker configuration file
├── requirements.txt      # Python dependencies
├── setup.py              # Setup for packaging the project
└── params.yaml           # Parameter file for the application
  
  ```


---

## ✨ Features

- 🌐 Data Ingestion: Downloads and extracts data from a source URL.
- 🧠 Text Summarization: Future feature to implement text summarization algorithms.
- 🎨 Logging: Comprehensive logging at every stage of data processing to ensure transparency.
- 🔧 Pipeline: Modular pipeline for handling data ingestion, extraction, and model training.

