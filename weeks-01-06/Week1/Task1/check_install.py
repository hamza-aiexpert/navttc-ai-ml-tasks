# Checks that the libraries required by the course are installed.
import importlib, shutil, sys

print("Python:", sys.version.split()[0])
packages = ["numpy", "pandas", "matplotlib", "seaborn", "sklearn", "torch", "tensorflow", "nltk", "spacy"]
for name in packages:
    try:
        mod = importlib.import_module(name)
        print(f"[OK]        {name:12s} {getattr(mod, '__version__', '')}")
    except ImportError:
        print(f"[MISSING]   {name:12s} -> pip install {'scikit-learn' if name == 'sklearn' else name}")

for tool in ["conda", "code", "pycharm", "pycharm-community", "pycharm.sh"]:
    print(f"{tool:18s}", shutil.which(tool) or "not found on PATH")
