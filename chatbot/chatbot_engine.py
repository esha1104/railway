import streamlit as st

from datetime import datetime

from services.auth_service import verify_pin
from services.employee_data_service import build_employee_profile
from services.employee_service import (
    get_employee_greeting_info,
    get_salary_structure,
    get_pf_details,
    get_salary_history
)
from services.employee_service import get_pf_transactions
from services.nlp_service import detect_intent
from services.response_service import (
    employee_dashboard_html,
    payslip_html,
    greeting,
    fmt
)



def generate_response(user_input: str):
    """Returns (content: str, is_html: bool, chips: list[str])"""
    raw   = user_input.strip()
    phase = st.session_state.phase

    

    if phase == "awaiting_id":
        emp_id = raw.strip().upper()
        employee = get_employee_greeting_info(emp_id)
        if not employee:
            return (
                f"❌ Employee ID {emp_id} not found.",
                False,
                []
            )
        st.session_state.emp_id = emp_id
        st.session_state.phase = "service_selection"
        st.session_state.employee = employee
        return (
            f"""
            ### 👋 Welcome {employee[1]}

           🏢 **Department:** {employee[3]}

           💼 **Designation:** {employee[2]}

           📊 **Pay Level:** {employee[6]}

           📍 **City Classification:** {employee[4]}

            📅 **Date of Joining:** {employee[5]}

            What would you like to access?
            """,
            False,
            [
                "Salary Details",
                "Salary History",
                "PF Details",
                "PF History",
                "HR Contact"
            ]
        )
    
    if phase == "service_selection":
        intent = detect_intent(raw)
        if intent == "salary":
            st.session_state.requested_service = "salary"
            st.session_state.phase = "awaiting_pin"

            return (
                "🔐 Please enter your 4-digit PIN to access Salary Details.",
                False,
                []
            )
        elif intent == "pf":
            st.session_state.requested_service = "pf"
            st.session_state.phase = "awaiting_pin"

            return (
                "🔐 Please enter your 4-digit PIN to access PF Details.",
                False,
                []
            )
        elif intent == "hr":
            return (
                "📞 BLW HR Contact\n\n0542-2501234",
                False,
                ["Salary Details", "PF Details"]
            )
        elif intent == "salary_history":
            st.session_state.requested_service = "salary_history"
            st.session_state.phase = "awaiting_pin"
            return (
                "🔐 Please enter your 4-digit PIN to access Salary History.",
                False,
                []
            )
        elif intent == "pf_history":
            st.session_state.requested_service = "pf_history"
            st.session_state.phase = "awaiting_pin"
            return (
                "🔐 Please enter your 4-digit PIN to access PF History.",
                False,
                []
            )
        else:
            return (
                "Sorry, I couldn't understand your request.",
                True,
                [
                    "Salary Details",
                    "Salary History",
                    "PF Details",
                    "PF History",
                    "HR Contact"
                ]
            )

           
    # Step 3: Verify PIN against real database
    if phase == "awaiting_pin":
        pin = raw.strip()
        emp_id = st.session_state.get("emp_id", "")

        auth_result = verify_pin(
            emp_id,
            pin
        )

        if not auth_result["success"]:

            message = auth_result["message"]

            if "Employee Not Found" in message:

                st.session_state.phase = "awaiting_id"

                return (
                    f"❌ Employee ID **{emp_id}** not found.\n\n"
                    "Please re-enter your correct Employee ID.",
                    False,
                    []
                )

            if "Locked" in message:

                

                return (
                    "🔒 " + message,
                    False,
                    ["Start Over"]
                )

            return (
                f"⚠️ {message}",
                False,
                []
            )

        emp = build_employee_profile(emp_id)
        if not emp:
            return (
                "Unable to retrieve employee information.", False,[]
            )
        requested_service = st.session_state.get("requested_service")
        st.session_state.last_emp = emp
        st.session_state.phase = "done"
        
        if requested_service == "salary":
            return (
                payslip_html(emp),
                True,
                ["View Salary Again", "Salary History", "PF Info", "PF History", "Contact HR", "Start Over"]
            )
        if requested_service == "salary_history":
            history = get_salary_history(st.session_state.emp_id)
            response = (
                "**📊 Salary History**\n\n"
                "| Month | Gross Salary | Net Salary |\n"
                "|---|---|---|\n"
            )
            month_names = [
                "", "Jan", "Feb", "Mar", "Apr",
                "May", "Jun", "Jul", "Aug",
                "Sep", "Oct", "Nov", "Dec"
            ]
            for row in history:
                response += (
                    f"| {month_names[row[0]]} {row[1]} | "
                    f"{fmt(int(row[2]))} | "
                    f"{fmt(int(row[3]))} |\n"
                )
                return (
                    response,
                    False,
                    [
                        "View Salary Again",
                        "Salary History",
                        "PF Info",
                        "PF History",
                        "Contact HR",
                        "Start Over"
                    ]
                )
        
        
        
        if requested_service == "pf":
            return (
                "**🏦 Your Provident Fund Account**\n\n"
                f"Monthly Contribution: {fmt(emp['pf_monthly'])}\n\n"
                f"Employer Contribution: {fmt(emp['pf_employer'])}\n\n"
                f"Total PF Balance: {fmt(emp['pf_balance'])}\n\n"
                f"Last Updated: {emp['pf_last_updated']}",
                False,["View Salary Again", "Salary History", "PF History", "Contact HR", "Start Over"]
            )
        if requested_service == "pf_history":
            transactions = get_pf_transactions(st.session_state.emp_id)
            response = (
                "**🏦 PF Transaction History**\n\n"
                "| Month | Contribution | Interest | Balance |\n"
                "|---|---|---|---|\n"
            )
            month_names = [
                "",
                "Jan", "Feb", "Mar", "Apr",
                "May", "Jun", "Jul", "Aug",
                "Sep", "Oct", "Nov", "Dec"
            ]
            for row in transactions:
                response += (
                    f"| {month_names[row[0]]} {row[1]} "
                    f"| {fmt(int(row[2]))} "
                    f"| {fmt(int(row[3]))} "
                    f"| {fmt(int(row[4]))} |\n"
                )
                return (
                    response,
                    False,
                    [
                        "View Salary Again",
                        "Salary History",
                        "PF Info",
                        "PF History",
                        "Contact HR",
                        "Start Over"
                    ]
                )


        # Post-login options
    if phase == "done":
        intent = detect_intent(raw)

        if intent == "salary_history":
            history = get_salary_history(
                st.session_state.emp_id
            )

            response = (
                "**📊 Salary History**\n\n"
                "| Month | Gross Salary | Net Salary |\n"
                "|---|---|---|\n"
            )

            month_names = [
                "", "Jan", "Feb", "Mar", "Apr",
                "May", "Jun", "Jul", "Aug",
                "Sep", "Oct", "Nov", "Dec"
            ]

            for row in history:
                month = month_names[row[0]]
                response += (
                    f"| {month} {row[1]} | "
                    f"{fmt(int(row[2]))} | "
                    f"{fmt(int(row[3]))} |\n"
                )

            return (
                response,
                False,
                [
                    "View Salary Again",
                    "Salary History",
                    "PF Info",
                    "PF History",
                    "Contact HR",
                    "Start Over"
                ]
            )

        if intent == "pf_history":
            transactions = get_pf_transactions(
                st.session_state.emp_id
            )

            response = (
                "**🏦 PF Transaction History**\n\n"
                "| Month | Contribution | Interest | Balance |\n"
                "|---|---|---|---|\n"
            )

            month_names = [
                "",
                "Jan", "Feb", "Mar", "Apr",
                "May", "Jun", "Jul", "Aug",
                "Sep", "Oct", "Nov", "Dec"
            ]

            for row in transactions:
                response += (
                    f"| {month_names[row[0]]} {row[1]} "
                    f"| {fmt(int(row[2]))} "
                    f"| {fmt(int(row[3]))} "
                    f"| {fmt(int(row[4]))} |\n"
                )

            return (
                response,
                False,
                [
                    "View Salary Again",
                    "Salary History",
                    "PF Info",
                    "Contact HR",
                    "Start Over"
                ]
            )

        if intent == "salary":
            emp = st.session_state.last_emp
            if emp:
                return (
                    payslip_html(emp),
                    True,
                    [
                        "PF Info",
                        "Salary History",
                        "PF History",
                        "Contact HR",
                        "Start Over"
                    ]
                )

        if intent == "pf":
            emp = st.session_state.last_emp
            if emp:
                return (
                    "**🏦 Your Provident Fund Account**\n\n"
                    "| Detail | Amount |\n|---|---|\n"
                    "| Your Monthly Contribution (12%) | " + fmt(emp["pf_monthly"]) + " |\n"
                    "| Employer Contribution (12%) | " + fmt(emp["pf_employer"]) + " |\n"
                    "| **Total PF Balance** | **" + fmt(emp["pf_balance"]) + "** |\n"
                    "| Last Updated | " + emp["pf_last_updated"] + " |\n\n"
                    "📞 PF Helpline: **1800-118-005** *(toll free)*\n"
                    "🌐 epfindia.gov.in",
                    False,
                    [
                        "View Salary Again",
                        "Salary History",
                        "PF History",
                        "Contact HR",
                        "Start Over"
                    ]
                )

        if intent == "hr":
            return (
                "**📞 BLW HR / Personnel Department**\n\n"
                "📞 **0542-2501234**\n\n"
                "📧 hr@blw.indianrailways.gov.in\n\n"
                "🏢 Personnel Branch, BLW Campus, Varanasi – 221005\n\n"
                "⏰ Mon – Sat | 9:00 AM – 5:30 PM",
                False,
                [
                    "View Salary Again",
                    "Salary History",
                    "PF Info",
                    "PF History",
                    "Start Over"
                ]
            )

        if intent == "restart":
            st.session_state.phase = "awaiting_id"
            st.session_state.user_name = None
            st.session_state.attempts = 0
            st.session_state.last_emp = None
            st.session_state.emp_id = None
            st.session_state.employee = None

            return (
                greeting() + " again! 🙏 Please tell me your **Employee ID** to begin.",
                False,
                []
            )

        return (
            "I can help you with your **salary slip**, **Salary History**, **PF balance**, **PF History**, or **HR contacts**.",
            False,
            [
                "View Salary Again",
                "Salary History",
                "PF Info",
                "PF History",
                "Contact HR",
                "Start Over"
            ]
        )
    return ("I didn't understand that. Please try again.", False, [])
    