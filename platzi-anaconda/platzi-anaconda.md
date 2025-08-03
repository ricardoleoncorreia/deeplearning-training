# Python Virtual Environment Guide for macOS

This guide explains how to create, activate, and deactivate Python virtual environments on macOS using both the `python3` command and `conda`.

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

### Using python3 venv

To create a virtual environment, use the following command:

```bash
python3 -m venv your_env_name
```

This will create a new directory with the environment name containing all the necessary files for the virtual environment.

### Using conda

```bash
conda create --name your_env_name python=3.11
```

## Activating the Virtual Environment

### For python3 venv environments

To activate the virtual environment on macOS, use:

```bash
source your_env_name/bin/activate
```

When activated, you'll see the environment name in parentheses at the beginning of your terminal prompt:
```bash
(myproject_env) username@MacBook-Pro:~/your-project$
```

### For conda environments

```bash
conda activate your_env_name
```

## Installing Packages

### For python3 venv environments

While your virtual environment is activated, you can install packages using pip:

```bash
pip install package_name
```

These packages will be installed only in the virtual environment, keeping them separate from your system's global Python installation.

### For conda environments

```bash
conda install package_name
```

## Listing Installed Packages

### For python3 venv environments

To see what packages are installed in your virtual environment:

```bash
pip list
```

### For conda environments

```bash
conda list
```

## Creating Requirements File

### For python3 venv environments

To save your project dependencies:

```bash
pip freeze > requirements.txt
```

To install dependencies from a requirements file:

```bash
pip install -r requirements.txt
```

### For conda environments

```bash
conda env export > environment.yml
conda env create -f environment.yml
```

## Deactivating the Virtual Environment

To deactivate the virtual environment and return to your system's global Python environment, simply run:

```bash
deactivate
```

The environment name will disappear from your terminal prompt, indicating you're back to the global environment.

## Deleting a Virtual Environment

### For python3 venv environments

To completely remove a virtual environment, you simply delete its directory. Make sure the environment is deactivated first:

```bash
# First, deactivate the environment if it's active
deactivate

# Then delete the environment directory
rm -rf your_env_name
```

### For conda environments

```bash
# First, deactivate the environment if it's active
conda deactivate

# Then remove the environment
conda env remove --name your_env_name
```

**Warning:** This action is irreversible. Make sure you have a `requirements.txt` file or `environment.yml` file saved before deleting the environment.

## Cleaning Cache

### For python3 venv environments

To clean pip cache and free up disk space:

```bash
# Clean pip cache
pip cache purge

# Remove pip cache directory
rm -rf ~/.cache/pip
```

### For conda environments

To clean conda cache:

```bash
# Clean all conda caches
conda clean --all

# Clean only package cache
conda clean --packages

# Clean only index cache
conda clean --index-cache
```

## Installing and Running Jupyter Notebook

### For python3 venv environments

After activating your virtual environment, install Jupyter Notebook:

```bash
# Activate your environment first
source your_env_name/bin/activate

# Install Jupyter Notebook
pip install jupyter

# Launch Jupyter Notebook
jupyter notebook
```

### For conda environments

After activating your conda environment, install Jupyter Notebook:

```bash
# Activate your environment first
conda activate your_env_name

# Install Jupyter Notebook
conda install jupyter

# Launch Jupyter Notebook
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
# Using pip
pip install nbdime

# Using conda
conda install nbdime
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
