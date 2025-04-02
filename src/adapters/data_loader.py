from core.employee_growth import EmployeeGrowth
from core.employee_growth_by_role import EmployeeGrowthByRole
from core.top_next_employers import TopNextEmployers
from core.yoy_growth import YoYGrowth
import pandas as pd

class DataLoader:
    def __init__(self, raw_data):
        """Initialize with raw data"""
        self.raw_data = raw_data

    def load_and_process_employee_growth(self):
        """Process employee growth data."""
        return EmployeeGrowth(self.raw_data).process_employee_growth()

    def load_and_process_employee_growth_by_role(self):
        """Process employee growth by role."""
        return EmployeeGrowthByRole(self.raw_data).process_employee_growth_by_role()

    def load_and_process_top_next_employers(self):
        """Process top next employers data."""
        return TopNextEmployers(self.raw_data).calculate_top_next_employers()

    def load_and_process_yoy_growth(self):
        """Process YoY growth data."""
        return YoYGrowth(self.raw_data).calculate_yoy_growth()
