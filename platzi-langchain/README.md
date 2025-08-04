# LangChain Chatbot Training Course

This repository contains training materials and practical examples for learning how to use LangChain to create customized chatbots. The course covers the fundamentals of building intelligent conversational systems using LangChain's powerful framework for developing applications with large language models.

**Course Content Based On:** [LangChain Course from Platzi](https://platzi.com/cursos/langchain-chatbots/)

## Initial Setup

### 1. Create Conda Environment

First, create and activate a conda environment using the provided `environment.yml` file:

```bash
# Create the environment
conda env create -f environment.yml

# Activate the environment
conda activate platzi-langchain
```

### 2. Install and Setup Ollama

Ollama is required for running local language models. Follow these steps to install and configure it:

#### Install Ollama with Homebrew (macOS)

```bash
# Install Ollama
brew install ollama

# Start Ollama service
brew services start ollama
```

#### Verify Ollama Installation

Check that Ollama service is running by visiting: [http://localhost:11434/](http://localhost:11434/)

You should see a message like "Ollama is running" if everything is working correctly.

#### Managing Ollama Service

```bash
# Start Ollama service
brew services start ollama

# Stop Ollama service
brew services stop ollama

# Restart Ollama service
brew services restart ollama

# Check service status
brew services list | grep ollama
```

#### Download Required Models

After Ollama is running, download the required models:

```bash
# Download the embedding model
ollama pull all-minilm

# Download the chat model
ollama pull llama3.2:1b
```
