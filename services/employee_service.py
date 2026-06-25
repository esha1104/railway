import sqlite3

DB_PATH = "database/railway_pf.db"

def get_salary_history(employee_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            month,
            year,
            gross_salary,
            net_salary
        FROM salary_history
        WHERE employee_id = ?
        ORDER BY year DESC, month DESC
    """, (employee_id,))

    rows = cursor.fetchall()

    conn.close()

    return rows
def get_pf_transactions(employee_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            month,
            year,
            contribution,
            interest_credited,
            balance_after_credit
        FROM pf_transactions
        WHERE employee_id = ?
        ORDER BY year DESC, month DESC
    """, (employee_id,))

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_connection():
    return sqlite3.connect(DB_PATH)


def get_employee_greeting_info(employee_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            employee_id,
            name,
            designation,
            department,
            city_classification,
            date_of_joining,
            pay_level      
        FROM employees
        WHERE employee_id = ?
    """, (employee_id,))

    employee = cursor.fetchone()

    conn.close()

    return employee


def get_salary_structure(employee_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM salary_structure
        WHERE employee_id = ?
    """, (employee_id,))

    salary = cursor.fetchone()

    conn.close()

    return salary


def get_pf_details(employee_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM pf_account
        WHERE employee_id = ?
    """, (employee_id,))

    pf = cursor.fetchone()

    conn.close()

    return pf