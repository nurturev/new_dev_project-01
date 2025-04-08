import json
from application.lambda_input_handler import extract_input_from_lambda
from adapters.controller import Controller

def lambda_handler(event, context):
    try:
        user_input = extract_input_from_lambda(event)
        controller = Controller()
        result = controller.route(user_input)
        return {
            "statusCode": 200,
            "body": json.dumps({"result": result})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
