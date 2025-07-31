# FastAPI on AWS Lambda with Mangum

This is a minimal starter project for deploying a FastAPI application as a serverless function on AWS Lambda.

## 🚀 Quick Start

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run Locally:**
    Use `uvicorn` to run the development server. The command points to the `main.py` file and the `app` instance within it.
    ```bash
    uvicorn main:app --reload
    ```
    You can now access the API at `http://127.0.0.1:8000` and the auto-generated docs at `http://127.0.0.1:8000/docs`.

## 📦 Deployment to AWS Lambda

To deploy this application, you need to package it into a zip file along with its dependencies and upload it to AWS Lambda.

1.  **Install dependencies into a package directory:**
    ```bash
    pip install -r requirements.txt --target ./package
    ```

2.  **Copy your application code into the package:**
    ```bash
    cp main.py ./package/
    ```

3.  **Create a zip archive from the package contents:**
    ```bash
    cd package
    zip -r ../deployment.zip .
    cd ..
    ```

4.  **Upload to AWS Lambda:**
    - Create a new Lambda function in the AWS console with a Python runtime.
    - Upload the `deployment.zip` file you just created.
    - Set the function's **Handler** configuration to `main.handler`. This tells Lambda to use the `handler` object created by Mangum in your `main.py` file as the entry point.
    - Configure a trigger, such as an API Gateway, to make your function accessible via a public HTTP endpoint.

That's it! Your FastAPI application is now running serverlessly on AWS Lambda.
