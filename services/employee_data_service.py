from services.employee_service import (
    get_employee_greeting_info,
    get_salary_structure,
    get_pf_details
)


def build_employee_profile(employee_id):

    emp = get_employee_greeting_info(employee_id)
    

    if not emp:
        return None

    salary = get_salary_structure(employee_id)
    pf = get_pf_details(employee_id)

    employee = {
        "employee_id": emp[0],
        "name": emp[1],
        "designation": emp[2],
        "department": emp[3],
        "city_class": emp[4],
        "date_of_joining": emp[5],

        "grade": f"Pay Level {emp[6]}",

        "basic": int(salary[1]) if salary else 0,
        "da": int(salary[3]) if salary else 0,
        "hra": int(salary[5]) if salary else 0,
        "ta": int(salary[6]) if salary else 0,

        "gross": int(salary[7]) if salary else 0,

        "pf": int(
            salary[1] * salary[8] / 100
        ) if salary else 0,

        "income_tax": int(salary[9]) if salary else 0,
        "esi": int(salary[10]) if salary else 0,
        "other": 0,

        "net": int(salary[11]) if salary else 0,

        "pf_monthly": int(pf[1]) if pf else 0,
        "pf_balance": int(pf[2]) if pf else 0,
        "pf_employer": int(pf[1]) if pf else 0,
        "pf_last_updated": pf[3] if pf else "-",

        "account_no": "XXXXXXXX" + employee_id[-4:],
        "bank": "State Bank of India"
    }

    return employee