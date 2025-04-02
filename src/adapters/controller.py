from adapters.data_loader import DataLoader

class Controller:
    def __init__(self, bucket_name, file_key):
        """Initialize the Controller with data loader."""
        self.data_loader = DataLoader(bucket_name, file_key)

    def process_operations(self, operations):
        """
        Executes the requested operations and returns results.

        Args:
            operations (list): List of operations to perform.

        Returns:
            dict: Results of each operation.
        """
        results = {}

        if "employee_growth" in operations:
            results["employee_growth"] = self.data_loader.load_and_process_employee_growth()

        if "employee_growth_by_role" in operations:
            results["employee_growth_by_role"] = self.data_loader.load_and_process_employee_growth_by_role()

        if "top_next_employers" in operations:
            results["top_next_employers"] = self.data_loader.load_and_process_top_next_employers()

        if "yoy_growth" in operations:
            results["yoy_growth"] = self.data_loader.load_and_process_yoy_growth()

        return results
