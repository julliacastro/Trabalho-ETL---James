from models.employee import Employee
from services.api_service import ApiService

class EmployeeService:
    @staticmethod
    def fetch_employees():
        employees_data = ApiService.fetch_data('https://demodata.grapecity.com/adventureworks/api/v1/employees')
        employees = []
        for emp in employees_data:
            employees.append(Employee(
                emp['employeeId'], emp['nationalIdnumber'], emp['loginId'], emp['organizationLevel'],
                emp['jobTitle'], emp['birthDate'], emp['maritalStatus'], emp['gender'], emp['hireDate'],
                emp['isSalaried'], emp['vacationHours'], emp['sickLeaveHours'], emp['isActive'], emp['modifiedDate']
            ))
        return employees

    @staticmethod
    def insert_employees(cursor, employees):
        for emp in employees:
            cursor.execute('''
                INSERT INTO employees (employeeId, nationalIdnumber, loginId, organizationLevel, jobTitle,
                                       birthDate, maritalStatus, gender, hireDate, isSalaried, vacationHours,
                                       sickLeaveHours, isActive, modifiedDate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                emp.employeeId, emp.nationalIdnumber, emp.loginId, emp.organizationLevel, emp.jobTitle,
                emp.birthDate, emp.maritalStatus, emp.gender, emp.hireDate, emp.isSalaried, emp.vacationHours,
                emp.sickLeaveHours, emp.isActive, emp.modifiedDate
            ))
