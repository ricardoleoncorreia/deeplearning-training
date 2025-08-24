# LangChain for LLM Application Development

## Introduction

This project is based on DeepLearning.AI's comprehensive [LangChain for LLM Application Development](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/) course. It provides hands-on experience with building Large Language Model (LLM) applications using the LangChain framework.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Environment Setup](#environment-setup)
  - [Creating a Virtual Environment](#creating-a-virtual-environment)
  - [Activating the Virtual Environment](#activating-the-virtual-environment)
- [Course Modules](#course-modules)
- [Installing Dependencies](#installing-dependencies)
- [Getting Help](#getting-help)

## Prerequisites

Make sure you have Python 3.8+ installed on your macOS system. You can check by running:
```bash
python3 --version
```

For conda environments, make sure you have Anaconda or Miniconda installed:
```bash
conda --version
```

## Environment Setup

### Creating a Virtual Environment

```bash
# Using conda
conda create --name deeplearningai-langchain python=3.13
```

### Activating the Virtual Environment

```bash
# Activate the conda environment
conda activate deeplearningai-langchain
```

## Course Modules

This project covers the following key areas of LangChain development:

1. **Models, Prompts and Parsers** - Understanding LLM models, crafting effective prompts, and parsing outputs
2. **Memory** - Implementing conversation memory for chatbots and interactive applications
3. **Chains** - Building sequential operations and complex workflows
4. **Question Answering** - Creating Q&A systems over documents and knowledge bases
5. **Evaluation** - Testing and evaluating LLM application performance
6. **Agents** - Building autonomous agents that can use tools and make decisions

## Installing Dependencies

```bash
# Install from environment.yml
conda env create -f environment.yml
conda activate deeplearningai-langchain
```

### Getting Help

- Check the [LangChain Documentation](https://python.langchain.com/)
- Visit the [LangChain GitHub Repository](https://github.com/langchain-ai/langchain)

--------

