# flask-serverless

Examples of deploying an ML model using serverless framework &amp; zappa into AWS lambda.


## Serverless Framework

Setup & installation.

```bash
npm install -g serverless
npm init
npm install --save-dev serverless-wsgi serverless-python-requirements
```

Run a python virtual environment.

Test running locally.

```bash
sls wsgi serve
```

Deploy lambda function with API gateway & cloudwatch.

```bash
sls deploy
```