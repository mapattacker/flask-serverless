# flask-serverless

Examples of deploying an ML model using [Serverless Framework](https://www.serverless.com/) &amp; [Zappa](https://github.com/zappa/Zappa) into AWS lambda.

Zappa files
 * `zappa_settings.json`

Serverless files
 * `package-lock.json`
 * `package.json`
 * `serverless.yml`

## Zappa

Run a virtual environment using `venv`.

```bash
python -m venv venv
source venv/bin/activate
```

Install Zappa & Initiate.

```bash
pip install zappa
zappa init
```

Deploy & remove lambda function stack with API gateway & cloudwatch.

```bash
zappa deploy
zappa undeploy
```


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

Deploy & remove lambda function stack with API gateway & cloudwatch.

```bash
sls deploy
sls remove
```