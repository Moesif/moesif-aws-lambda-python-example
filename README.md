# Moesif AWS Lambda Example for Python

[Moesif](https://www.moesif.com) is an API analytics platform.
[moesif-aws-lambda-python](https://github.com/Moesif/moesif-aws-lambda-python)
is a middleware that logs API calls to Moesif for AWS Lambda.

This example is a Python application with Moesif's API analytics and monitoring integrated.

## How to run this example.

Create a new AWS Lambda function that is trigged by AWS API Gateway

Create a zip using following steps:
1. pip install --target ./package moesif_aws_lambda
2. cd package
3. zip -r9 ${OLDPWD}/function.zip .
4. cd $OLDPWD
5. zip -g function.zip lambda_function.py

Upload this zip, when prompted for handler, enter `lambda_function.lambda_handler`

You will also want to add an environment vairable `MOESIF_APPLICATION_ID` with the value being your 
application id from your Moesif account

Go to the URL for the API gateway such as https://XXXXXX.execute-api.us-west-2.amazonaws.com/default/my-test-function

The API Calls should show up in Moesif.
