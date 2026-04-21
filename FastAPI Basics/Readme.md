# FastAPI Basics

In this section we will cover the basics of FastAPI.

## Why FastAPI ?

**Basic Terminology**:

1. API : Application Programming inteface -refers to web applications using HTTP protocols to transit structured data.

2. Web Applicaiton: Applicaiton that serves traffic over the web.

3. Web Framework : Software framework that helps build web appications.


FastAPI is a framework that helps us in creating API that are fast using Python.

**Key Features**:

1. Fast : very high perfomance

2. Low code and easy to learn: Python annotations and type hints.

3. Roboust: Production ready code with autodoc

4. Standards based : based on the OpenAI and JSON schema.


**Building our first web application with FastAPI**:

1. Install FastAPI

In the terminal run the below command:
```
pip install fastapi 
```

2.  Create your **main.py**:

Create a file called main.py and type the following code:
```
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message":"Hello World"}

```

3. Run the Server

In the terminal run the following command:
```
fastapi run dev main.py
```