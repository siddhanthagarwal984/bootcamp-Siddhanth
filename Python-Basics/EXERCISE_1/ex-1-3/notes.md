# Notes for ex-1-3

## 1. Understanding of the Problem
This exercise focuses on packaging and publishing the "helloworld" library and its CLI to 
TestPyPI (dev-pypi). The goal is to make the CLI installable using `pip install`.

## 2. Approach Taken
- Configured a `pyproject.toml` file with dependencies.
- Used Poetry to package the project.
- Published the package to TestPyPI using:
    ```
    poetry publish --build -r testpypi
    ```
- Installed the package from TestPyPI and tested it.

## 3. LLMs Used and Their Content
ChatGPT 4 provided guidance on:
- How to configure Poetry for package management.
- Steps to publish to TestPyPI.
- Common issues when publishing packages.

## 4. Prompts and Responses
1. **How to build and publish to TestPyPI?**
    ```
    poetry build
    poetry publish -r testpypi
    ```
    You need a TestPyPI account. Use 
    ```
    poetry config repositories.testpypi https://test.pypi.org/legacy/
    ```
    to set up the repository. Publish to TestPyPI:
    ```
    poetry publish -r testpypi --username __token__ --password YOUR_API_TOKEN
    ```

2. **How to install from TestPyPI?**
    ```
    pip install --index-url https://test.pypi.org/simple/ --no-deps hello-cli
    ```
    Run the CLI as a command:
    ```
    hello John
    ```
    This should output:
    ```
    Hello, John!
    ```

3. **How to configure Poetry for package management?**
    ```
    poetry init
