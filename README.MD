# Projeto ETL: Extração de Dados da API AdventureWorks e Armazenamento no MySQL

## Endpoints Utilizados

- **Endpoint de Funcionários**: 
  - URL: `https://demodata.grapecity.com/adventureworks/api/v1/employees`
- **Endpoint de Histórico de Departamento**: 
  - URL: `https://demodata.grapecity.com/adventureworks/api/v1/employees/{id}/departmentHistories`
- **Endpoint de Departamentos**: 
  - URL: `https://demodata.grapecity.com/adventureworks/api/v1/departments`

## Requisitos

- Python 3.10 ou superior
- MySQL Server
- Bibliotecas Python:
  - `requests`: Para realizar requisições HTTP à API.
  - `mysql-connector-python`: Para conectar-se ao MySQL e manipular o banco de dados.

Instale as dependências com:

```bash
pip install -r requirements.txt

Como Executar

    Clone este repositório.
    Configure a conexão ao banco de dados MySQL no arquivo database.py (se necessário).
    Execute o arquivo main.py:

bash

python main.py

O programa irá extrair os dados dos funcionários, seus históricos de departamento e os departamentos, e inserir no banco de dados MySQL.
Estrutura do Banco de Dados

O banco de dados criado segue a estrutura de tabela de fatos e dimensões, com as seguintes tabelas:

    employees: Contém os dados básicos de cada funcionário.
    departments: Contém os dados dos departamentos da empresa.
    department_histories: Contém o histórico de departamentos de cada funcionário.

