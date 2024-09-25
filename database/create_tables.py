
class CreateTables:
    
    @staticmethod
    def create_tables(cursor):
        # Criação das tabelas de funcionários, departamentos e histórico de departamentos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                employeeId INT PRIMARY KEY,
                nationalIdnumber VARCHAR(50),
                loginId VARCHAR(100),
                organizationLevel INT,
                jobTitle VARCHAR(100),
                birthDate DATE,
                maritalStatus VARCHAR(10),
                gender VARCHAR(10),
                hireDate DATE,
                isSalaried BOOLEAN,
                vacationHours INT,
                sickLeaveHours INT,
                isActive BOOLEAN,
                modifiedDate DATE
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS departments (
                departmentId INT PRIMARY KEY,
                name VARCHAR(100),
                groupName VARCHAR(100),
                modifiedDate DATE
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS departmentHistories (
                employeeId INT,
                department VARCHAR(100),
                departmentGroup VARCHAR(100),
                shift VARCHAR(50),
                startDate DATE,
                endDate DATE,
                modifiedDate DATE,
                FOREIGN KEY (employeeId) REFERENCES employees(employeeId)
            )
        ''')

        # Criação da tabela de fatos
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
                FOREIGN KEY (departmentId) REFERENCES departments(departmentId)
            )
        ''')
