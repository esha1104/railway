from datetime import datetime

def get_welcome_message():
    return (
        "Hello! Welcome to the **BLW Employee Self-Service Portal**. 🙏\n\n"
        "I'm your personal assistant at **Banaras Locomotive Works**.\n\n"
        "I can help you with:\n"
        "- 💰 Monthly salary slip & deduction details\n"
        "- 🏦 Provident Fund information\n"
        "- 📞 HR contact details\n\n"
        "To get started, please tell me your **Employee ID**."
    )

def employee_dashboard_html(employee):

    return (
    employee_dashboard_html({
        "name": employee[1],
        "employee_id": employee[0],
        "designation": employee[2],
        "department": employee[3],
        "grade": employee[6],
        "city_class": employee[4],
        "date_of_joining": employee[5]
    }),
    True,
    [
        "Salary Details",
        "Salary History",
        "PF Details",
        "PF History",
        "HR Contact"
    ]
    ) 

def fmt(n: int) -> str:
    return "₹{:,}".format(n)

def greeting() -> str:
    h = datetime.now().hour
    return "Good morning" if h < 12 else "Good afternoon" if h < 17 else "Good evening"

def payslip_html(emp: dict) -> str:
    gross = emp["gross"]
    net = emp["net"]
    ded = (
        emp["pf"] +
        emp["income_tax"] +
        emp["esi"] +
        emp["other"]
    )
    month = datetime.now().strftime("%B %Y")
    ded_rows = "<tr><td>Provident Fund (12% of Basic)</td><td class='ded'>−" + fmt(emp['pf']) + "</td></tr>"
    if emp["income_tax"] > 0:
        ded_rows += "<tr><td>Income Tax (TDS)</td><td class='ded'>−" + fmt(emp['income_tax']) + "</td></tr>"
    if emp["esi"] > 0:
        ded_rows += "<tr><td>ESI Deduction</td><td class='ded'>−" + fmt(emp['esi']) + "</td></tr>"
    if emp["other"] > 0:
        ded_rows += "<tr><td>Other Deductions</td><td class='ded'>−" + fmt(emp['other']) + "</td></tr>"
    return (
        '<div class="payslip">'
        '<div class="ps-top">'
        '<div>'
        '<div class="ps-name">' + emp['name'] + '</div>'
        '<div class="ps-sub">' + emp['designation'] + ' &nbsp;·&nbsp; ' + emp['department'] + ' &nbsp;·&nbsp; ' + emp['grade'] + '</div>'
        '</div>'
        '<div class="ps-badge">📅 ' + month + '</div>'
        '</div>'
        '<div class="ps-body">'
        '<div class="ps-sect-lbl">EARNINGS</div>'
        '<table class="pst">'
        '<tr><td>Basic Pay</td><td class="earn">' + fmt(emp['basic']) + '</td></tr>'
        '<tr><td>Dearness Allowance (DA)</td><td class="earn">' + fmt(emp['da']) + '</td></tr>'
        '<tr><td>House Rent Allowance (HRA)</td><td class="earn">' + fmt(emp['hra']) + '</td></tr>'
        '<tr><td>Transport Allowance (TA)</td><td class="earn">' + fmt(emp['ta']) + '</td></tr>'
        '<tr class="tot-row"><td><strong>Gross Salary</strong></td><td class="earn"><strong>' + fmt(gross) + '</strong></td></tr>'
        '</table>'
        '<div class="ps-sect-lbl" style="margin-top:14px;">DEDUCTIONS</div>'
        '<table class="pst">'
        + ded_rows +
        '<tr class="tot-row"><td><strong>Total Deductions</strong></td><td class="ded"><strong>−' + fmt(ded) + '</strong></td></tr>'
        '</table>'
        '<div class="net-box">'
        '<span class="net-lbl">💳 &nbsp;Net Salary Credited</span>'
        '<span class="net-amt">' + fmt(net) + '</span>'
        '</div>'
        '</div>'
        '<div class="ps-foot">'
        '🏦 &nbsp;A/C: <strong>' + emp['account_no'] + '</strong> &nbsp;·&nbsp; ' + emp['bank'] +
        ' &nbsp;&nbsp;|&nbsp;&nbsp; Employer PF Contribution: <strong>' + fmt(emp['pf_employer']) + '</strong>'
        '</div>'
        '</div>'
    )

