
from database.db_connection import DBConnection
from database.create_tables import CreateTables
from services.department_history_service import DepartmentHistoryService
from services.employee_service import EmployeeService
from services.department_service import DepartmentService
from services.fact_table_service import FactTableService

def main():
    db = DBConnection(host='localhost', user='root', password='Yoda1801', database='adventureworks')
    conn = db.connect()
    cursor = conn.cursor()

    # Criar tabelas
    CreateTables.create_tables(cursor)

    # Extrair e inserir funcionários
    employees = EmployeeService.fetch_employees()
    EmployeeService.insert_employees(cursor, employees)

    # Extrair e inserir departamentos
    departments = DepartmentService.fetch_departments()
    DepartmentService.insert_departments(cursor, departments)
    
    

    # Salvar alterações
    conn.commit()
    
    for employee in employees:
        employee_id = employee.employeeId
        department_histories = DepartmentHistoryService.fetch_department_history(employee_id)
        DepartmentHistoryService.insert_department_histories(cursor, employee_id, department_histories)
        
    
     # Salvar alterações
    conn.commit()

    # Inserir dados na tabela de fatos
    department_histories = DepartmentHistoryService.get_department_histories(cursor)
    FactTableService.insert_fact_data(cursor, department_histories, employees)
    
     # Salvar alterações
    conn.commit()

    # Fechar a conexão
    cursor.close()
    db.close(conn)

if __name__ == "__main__":
    main()
