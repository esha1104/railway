import re


def detect_intent(text):

    text = text.lower().strip()

    salary_keywords = [
        "salary",
        "payslip",
        "pay slip",
        "salary details",
        "show salary",
        "view salary"
    ]

    salary_history_keywords = [
        "salary history",
        "past salary",
        "salary record",
        "previous salary"
    ]

    pf_keywords = [
        "pf",
        "provident fund",
        "pf details",
        "pf balance"
    ]

    pf_history_keywords = [
        "pf history",
        "pf transaction",
        "pf records",
        "pf statement"
    ]

    hr_keywords = [
        "hr",
        "human resource",
        "contact hr",
        "hr contact"
    ]

    restart_keywords = [
        "restart",
        "start over",
        "reset",
        "new session"
    ]

    if any(word in text for word in salary_history_keywords):
        return "salary_history"

    if any(word in text for word in pf_history_keywords):
        return "pf_history"

    if any(word in text for word in salary_keywords):
        return "salary"

    if any(word in text for word in pf_keywords):
        return "pf"

    if any(word in text for word in hr_keywords):
        return "hr"

    if any(word in text for word in restart_keywords):
        return "restart"

    return "unknown"