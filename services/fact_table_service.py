
class FactTableService:
    @staticmethod
    def create_fact_table(cursor):
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employee_department_fact (
                factId INT PRIMARY KEY AUTO_INCREMENT,
                employeeId INT,
                departmentId INT,
                department VARCHAR(100),
                departmentGroup VARCHAR(100),
                startDate DATE,
                endDate DATE,
                vacationHours INT,
                sickLeaveHours INT,
                isActive BOOLEAN,
                FOREIGN KEY (employeeId) REFERENCES employees(employeeId),
                FOREIGN KEY (department) REFERENCES departments(department)
            )
        ''')

    @staticmethod
    def insert_fact_data(cursor, department_histories, employees):
        for history in department_histories:
            for emp in employees:
                if emp.employeeId == history.employeeId:
                    cursor.execute('''
                        INSERT INTO employee_department_fact (employeeId, department, departmentGroup, 
                                                              startDate, endDate, vacationHours, sickLeaveHours, isActive)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ''', (
                        emp.employeeId, history.department, history.departmentGroup,
                        history.startDate, history.endDate, emp.vacationHours, emp.sickLeaveHours, emp.isActive
                    ))
