import json
from adapters.controller import Controller
from utils.logger import logger

class AgentFacade:
    def __init__(self, bucket_name: str, file_key: str):
        """Initialize the Agent Facade with S3 details."""
        self.controller = Controller(bucket_name, file_key)

    def process_request(self, input_data):
        """
        Processes a request and calls the appropriate controller method.

        Args:
            input_data (dict): User input specifying which operations to perform.

        Returns:
            dict: Processed results or error messages.
        """
        try:
            requested_operations = input_data.get("operations", [])
            if not requested_operations:
                return {"error": "No operations specified"}

            # Delegate to Controller
            results = self.controller.process_operations(requested_operations)
            return {"status": "success", "results": results}

        except Exception as e:
            logger.error(f"Error processing request: {str(e)}")
            return {"status": "error", "message": str(e)}
