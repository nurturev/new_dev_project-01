import json
from application.agent_facade import AgentFacade
from utils.logger import logger

def lambda_handler(event, context):
    """
    AWS Lambda entry point.

    Args:
        event (dict): The AWS Lambda event.
        context: The AWS Lambda context.

    Returns:
        dict: The response object.
    """
    try:
        # Extract bucket_name and file_key from environment variables
        bucket_name = config.S3_BUCKET_NAME
        file_key = config.S3_FILE_KEY

        # Extract operations from event
        body = json.loads(event.get("body", "{}"))
        operations = body.get("operations", [])

        facade = AgentFacade(bucket_name, file_key)
        result = facade.process_request({"operations": operations})

        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }

    except Exception as e:
        logger.error(f"Lambda error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
