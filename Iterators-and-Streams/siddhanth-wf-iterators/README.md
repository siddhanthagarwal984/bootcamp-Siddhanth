# siddhanth-wf-iterators

## 📌 Overview
This Python package demonstrates the usage of **iterators and generators** for efficient data processing. It includes functionalities such as:
- Basic iterators
- File reading iterators & generators
- Filtering and stream processing
- File processing pipelines
- Handling large files efficiently
- Exception handling in file operations
- Chaining multiple iterators

## 🚀 Installation
### 1️⃣ Install from TestPyPI
To install the package from **TestPyPI**, run:
```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps siddhanth-wf-iterators
```

### 2️⃣ Install Locally (Development Mode)
Clone the repository and install dependencies:
```bash
git clone https://github.com/your-repo/siddhanth-wf-iterators.git
cd siddhanth-wf-iterators
pip install -e .
```

---

## 🛠️ Usage
Run all iterators and generators from the `main.py` script:
```bash
python main.py
```

Example usage inside Python:
```python
from siddhanth_wf_iterators.basic_iterator import NumberIterator

for num in NumberIterator():
    print(num)
```

---

## ✅ Running Tests
Run all tests using `pytest`:
```bash
pytest tests/
```
Run a specific test:
```bash
pytest tests/test_pipeline.py
```

---

## 📦 Building and Publishing to TestPyPI
To build the package:
```bash
python -m build
```
To upload to **TestPyPI**:
```bash
python -m twine upload --repository testpypi dist/*
```

After uploading, install the package using:
```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps siddhanth-wf-iterators
```

---

## 🔧 Folder Structure
```
siddhanth-wf-iterators/
│── siddhanth_wf_iterators/  # Main package
│── tests/                   # Test suite
│── data/                    # Sample files
│── main.py                  # Entry point for running all features
│── pyproject.toml           # Packaging metadata
│── README.md                # Project documentation
│── requirements.txt         # Dependencies
│── dist/                    # Built package
│── build/                   # Temporary build files
```

---

## 📜 License
This project is licensed under the MIT License.

