from models.department import Department
from services.api_service import ApiService

class DepartmentService:
    @staticmethod
    def fetch_departments():
        departments_data = ApiService.fetch_data('https://demodata.grapecity.com/adventureworks/api/v1/departments')
        departments = []
        for dept in departments_data:
            departments.append(Department(
                dept['departmentId'], dept['name'], dept['groupName'], dept['modifiedDate']
            ))
        return departments

    @staticmethod
    def insert_departments(cursor, departments):
        for dept in departments:
            cursor.execute('''
                INSERT INTO departments (departmentId, name, groupName, modifiedDate)
                VALUES (%s, %s, %s, %s)
            ''', (
                dept.departmentId, dept.name, dept.groupName, dept.modifiedDate
            ))
