# Task 1 - Installation

Required: Anaconda3, PyTorch, TensorFlow 2.0 (or later), VSCode, PyCharm.

## 1. Anaconda3
- Download the installer for your OS: https://www.anaconda.com/download
- Windows/macOS: run the graphical installer (choose "Just Me").
- Linux: `bash Anaconda3-<version>-Linux-x86_64.sh`, then restart the terminal.
- Verify: `conda --version`

## 2. Create an environment (recommended)
```
conda create -n aiml python=3.10 -y
conda activate aiml
conda install numpy pandas matplotlib seaborn scikit-learn jupyter -y
```

## 3. PyTorch (CPU build; pick the GPU build at https://pytorch.org/get-started/locally/)
```
pip install torch torchvision torchaudio
```
Verify: `python -c "import torch; print(torch.__version__)"`

## 4. TensorFlow
```
pip install tensorflow
```
Verify: `python -c "import tensorflow as tf; print(tf.__version__)"`

## 5. VSCode
- Download: https://code.visualstudio.com/
- Install the "Python" and "Jupyter" extensions, then select the `aiml` interpreter
  (Ctrl+Shift+P -> "Python: Select Interpreter").
- Linux (Debian/Ubuntu): `sudo apt install ./code_*.deb`

## 6. PyCharm
- Download Community Edition: https://www.jetbrains.com/pycharm/download/
- Linux: `sudo snap install pycharm-community --classic`
- Settings -> Project -> Python Interpreter -> Add -> Conda Environment -> existing `aiml`.

## 7. Verify everything
Run `python check_install.py` (included in this folder) and take a screenshot as proof of completion.
