# Master's Thesis LaTeX

This repository contains the LaTeX code for generating my master's thesis project, titled: **Remote sensing of coastal environments**, submitted in partial satisfaction of the requirements for the degree Master of Science in Media Arts and Technology at University of California, Santa Barbara.

## 🏗️ How to Build

### 1. Install LaTeX (macOS)
This project requires a working LaTeX environment. On macOS:

```bash
brew install --cask mactex
echo 'export PATH="/Library/TeX/texbin:$PATH"' >> ~/.zprofile
source ~/.zprofile
```

### 2. Compile main.pdf

directly

```bash
./build.sh
```

or with latexmk

```bash
latexmk -pdf main.tex
```

### 3. Clean build files

```bash
latexmk -c
```

## 📦 Required LaTeX Packages
This project uses the following LaTeX packages (installed automatically if using MacTeX or TeX Live full):

- graphicx
- fancyhdr
- titling
- setspace
- hyperref
- cleveref

If using a minimal install, install these manually with tlmgr:

```bash
sudo tlmgr install graphicx fancyhdr titling setspace hyperref cleveref
```

## 🐍 Python Virtual Environment
To create a virtual environment and install required packages to enable use of Python scripts in maps folder:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📄 License
This project is released under the MIT License. You are free to reuse, modify, and distribute.

## 📬 Contact

For questions or collaboration, feel free to reach out via GitHub.