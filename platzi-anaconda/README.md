# Python Virtual Environment Guide for macOS

## Introduction

Project is based on Platzi's comprehensive [Curso de Entornos Virtuales con Anaconda y Jupyter](https://platzi.com/cursos/anaconda-jupyter) course. It provides hands-on experience with Python data science tools and environments.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Creating a Virtual Environment](#creating-a-virtual-environment)
- [Activating the Virtual Environment](#activating-the-virtual-environment)
- [Installing Packages](#installing-packages)
- [Conda Channels](#conda-channels)
  - [Default Channels](#default-channels)
  - [Using Specific Channels](#using-specific-channels)
- [Listing Installed Packages](#listing-installed-packages)
- [Creating Requirements File](#creating-requirements-file)
- [CookieCutter: Project Templating Tool](#cookiecutter-project-templating-tool)
  - [What is CookieCutter](#what-is-cookiecutter)
  - [Benefits of Using CookieCutter](#benefits-of-using-cookiecutter)
  - [Installing CookieCutter](#installing-cookiecutter)
  - [Using CookieCutter](#using-cookiecutter)
- [Deactivating the Virtual Environment](#deactivating-the-virtual-environment)
- [Deleting a Virtual Environment](#deleting-a-virtual-environment)
- [Cleaning Cache](#cleaning-cache)
- [Installing and Running Jupyter Notebook](#installing-and-running-jupyter-notebook)
- [Jupyter Notebook Magic Commands](#jupyter-notebook-magic-commands)
  - [Common Magic Commands](#common-magic-commands)
  - [Example Usage](#example-usage)
- [Working with Git and Jupyter Notebooks - nbdime](#working-with-git-and-jupyter-notebooks---nbdime)
  - [Installing nbdime](#installing-nbdime)
  - [Git Integration Setup](#git-integration-setup)
  - [Common nbdime Commands](#common-nbdime-commands)
  - [Example Usage](#example-usage-1)
  - [Best Practices for Notebooks and Git](#best-practices-for-notebooks-and-git)
- [Best Practices](#best-practices)

## Prerequisites

Make sure you have Python 3 installed on your macOS system. You can check by running:
```bash
python3 --version
```

For conda environments, make sure you have Anaconda or Miniconda installed. You can check by running:
```bash
conda --version
```

## Creating a Virtual Environment

```bash
# Using python3 venv / Using conda
python3 -m venv your_env_name / conda create --name your_env_name python=3.11
```

## Activating the Virtual Environment

```bash
# For python3 venv / For conda environments
source your_env_name/bin/activate / conda activate your_env_name
```

When activated, you'll see the environment name in parentheses at the beginning of your terminal prompt:
```bash
(myproject_env) username@MacBook-Pro:~/your-project$
```

## Installing Packages

```bash
# For python3 venv / For conda environments
pip install package_name / conda install package_name
```

These packages will be installed only in the virtual environment, keeping them separate from your system's global Python installation.

## Conda Channels

Conda channels are repositories where packages are stored. When you install a package, conda searches through configured channels to find it.

### Default Channels

- **default**: The main Anaconda repository maintained by Anaconda Inc., contains curated packages
- **conda-forge**: Community-driven channel with the largest collection of packages, often more up-to-date

### Using Specific Channels

```bash
# Install from conda-forge channel
conda install -c conda-forge package_name

# Install from default channel (explicitly)
conda install -c defaults package_name

# Add conda-forge as a permanent channel (recommended)
conda config --add channels conda-forge

# Set channel priority (conda-forge first, then defaults)
conda config --set channel_priority strict
```

## Listing Installed Packages

```bash
# For python3 venv / For conda environments
pip list / conda list
```

## Creating Requirements File

```bash
# For python3 venv environments
pip freeze > requirements.txt
pip install -r requirements.txt

# For conda environments
conda env export > environment.yml
conda env create -f environment.yml
```

## CookieCutter: Project Templating Tool

### What is CookieCutter

CookieCutter is a command-line utility that creates projects from project templates (called "cookiecutters"). It's particularly useful for data science projects as it helps you start with a well-organized, standardized project structure that follows best practices.

### Benefits of Using CookieCutter

1. **Consistent Project Structure**: Ensures all your projects follow the same organization pattern
2. **Best Practices Built-in**: Templates include industry-standard folder structures and configurations
3. **Time Saving**: No need to manually create directories, files, and boilerplate code
4. **Customizable**: Templates can be customized with project-specific information during creation
5. **Version Control Ready**: Templates often include `.gitignore`, `README.md`, and other VCS essentials
6. **Reproducible Research**: Standardized structure makes it easier to share and reproduce work
7. **Team Collaboration**: Everyone on the team uses the same project structure

### Installing CookieCutter

```bash
# Using pip (venv) / Using conda
pip install cookiecutter / conda install -c conda-forge cookiecutter-data-science
```

### Using CookieCutter

Once installed, you can create a new data science project using the Cookiecutter Data Science template:

```bash
ccds
```

The `ccds` command is a convenient shortcut specifically for the Cookiecutter Data Science template when installed through conda-forge.

## Deactivating the Virtual Environment

To deactivate the virtual environment and return to your system's global Python environment, simply run:

```bash
deactivate
```

The environment name will disappear from your terminal prompt, indicating you're back to the global environment.

## Deleting a Virtual Environment

```bash
# For python3 venv environments
deactivate && rm -rf your_env_name

# For conda environments
conda deactivate && conda env remove --name your_env_name
```

**Warning:** This action is irreversible. Make sure you have a `requirements.txt` file or `environment.yml` file saved before deleting the environment.

## Cleaning Cache

```bash
# For python3 venv environments
pip cache purge
rm -rf ~/.cache/pip

# For conda environments
conda clean --all
conda clean --packages  # Clean only package cache
conda clean --index-cache  # Clean only index cache
```

## Installing and Running Jupyter Notebook

```bash
# For python3 venv / For conda environments
pip install jupyter / conda install jupyter

# Launch Jupyter Notebook (same for both)
jupyter notebook
```

The notebook will open in your default web browser at `http://localhost:8888`.

## Jupyter Notebook Magic Commands

Magic commands are special commands in Jupyter Notebook that provide additional functionality. There are two types:

- **Line magic (`%`)**: Affects only the line where it's used
- **Cell magic (`%%`)**: Affects the entire cell

### Common Magic Commands

- `%run`: Executes an external Python script
- `%time`: Measures execution time of a single line of code
- `%timeit`: Measures average execution time of a line of code over multiple runs
- `%matplotlib inline`: Displays matplotlib plots inline within the notebook
- `%pwd`: Shows the current working directory
- `%ls`: Lists files in the current directory
- `%who`: Shows active variables in the notebook
- `%writefile`: Writes cell content to a file
- `%reset`: Removes all variables from the namespace
- `%lsmagic`: Shows a complete list of available magic commands

### Example Usage

```python
# Time a single execution
%time sum(range(100))

# Time multiple executions for average
%timeit sum(range(100))

# Write cell content to a file
%%writefile script.py
print("Hello, World!")

# Reset all variables
%reset
```

## Working with Git and Jupyter Notebooks - nbdime

**nbdime** (Notebook Diff and Merge) is a tool that provides better diff and merge functionality for Jupyter notebooks when working with Git. Since notebooks are JSON files, regular Git diff shows unreadable changes, but nbdime provides a clean, visual comparison.

### Installing nbdime

```bash
# Using pip / Using conda
pip install nbdime / conda install nbdime
```

### Git Integration Setup

To integrate nbdime with Git for automatic notebook diffing and merging:

```bash
# Enable nbdime for Git
nbdime config-git --enable --global

# To disable later (optional)
nbdime config-git --disable --global
```

### Common nbdime Commands

- `nbdiff`: Shows differences between two notebook files in a readable format
- `nbmerge`: Merges notebook files with conflict resolution
- `nbdiff-web`: Opens a web-based visual diff viewer for notebooks
- `nbmerge-web`: Opens a web-based visual merge tool for resolving conflicts
- `nbshow`: Displays notebook content in the terminal
- `nbstripout`: Removes output cells from notebooks (useful for Git)

### Example Usage

```bash
# Compare two notebook versions
nbdiff notebook_v1.ipynb notebook_v2.ipynb

# Open web-based diff viewer
nbdiff-web notebook_v1.ipynb notebook_v2.ipynb

# Merge notebooks with conflict resolution
nbmerge base.ipynb local.ipynb remote.ipynb

# Strip output from notebook before committing
nbstripout notebook.ipynb
```

### Best Practices for Notebooks and Git

1. **Use nbstripout** to remove outputs before committing to keep repositories clean
2. **Configure Git hooks** to automatically strip outputs on commit
3. **Use nbdiff-web** for reviewing notebook changes in pull requests
4. **Commit notebooks frequently** with meaningful commit messages

## Best Practices

1. **Always activate your virtual environment** before working on your project
2. **Use descriptive names** for your virtual environments
3. **Keep a requirements.txt file** to track your project dependencies
4. **Don't commit the virtual environment folder** to version control (add it to `.gitignore`)
