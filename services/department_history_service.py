
import requests

from models.department_history import DepartmentHistory

class DepartmentHistoryService:
    @staticmethod
    def fetch_department_history(employee_id):
        url = f'https://demodata.grapecity.com/adventureworks/api/v1/employees/{employee_id}/departmentHistories'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return []

    @staticmethod
    def insert_department_histories(cursor, employee_id, department_histories):
        for history in department_histories:
            cursor.execute('''
                INSERT INTO departmenthistories (employeeId, department, departmentGroup, shift, startDate, endDate, modifiedDate)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (
                employee_id,
                history['department'],
                history['departmentGroup'],
                history['shift'],
                history['startDate'],
                history['endDate'] if history['endDate'] is not None else None,
                history['modifiedDate']
            ))         
            

    
    @staticmethod
    def get_department_histories(cursor):
        cursor.execute('''
                SELECT employeeId, department, departmentGroup, shift, startDate, endDate, modifiedDate
                FROM departmenthistories
            ''')
        rows = cursor.fetchall()
        return [DepartmentHistory(*row) for row in rows]
