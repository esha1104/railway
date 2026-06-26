import sqlite3
import bcrypt
from datetime import datetime, timedelta

DB_PATH = "database/railway_pf.db"

MAX_FAILED_ATTEMPTS = 3
LOCKOUT_DURATION_MINUTES = 2


def get_connection():
    return sqlite3.connect(DB_PATH)


def log_login_attempt(employee_id, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO login_audit
        (
            employee_id,
            login_time,
            status
        )
        VALUES (?, ?, ?)
    """, (
        employee_id,
        datetime.now().isoformat(),
        status
    ))

    conn.commit()
    conn.close()


def get_failed_attempts(employee_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT status
        FROM login_audit
        WHERE employee_id = ?
        ORDER BY id DESC
        LIMIT ?
    """, (
        employee_id,
        MAX_FAILED_ATTEMPTS
    ))

    rows = cursor.fetchall()

    conn.close()

    count = 0

    for row in rows:

        if row[0] == "FAILED":
            count += 1
        else:
            break

    return count


def is_locked_out(employee_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT login_time, status
        FROM login_audit
        WHERE employee_id = ?
        ORDER BY id DESC
        LIMIT ?
    """, (
        employee_id,
        MAX_FAILED_ATTEMPTS
    ))

    rows = cursor.fetchall()

    conn.close()

    if len(rows) < MAX_FAILED_ATTEMPTS:
        return False, 0

    for row in rows:
        if row[1] != "FAILED":
            return False, 0

    latest_failure_time = datetime.fromisoformat(
        rows[0][0]
    )

    unlock_time = (
        latest_failure_time
        + timedelta(
            minutes=LOCKOUT_DURATION_MINUTES
        )
    )

    if datetime.now() < unlock_time:

        minutes_remaining = max(
            1,
            int(
                (
                    unlock_time
                    - datetime.now()
                ).total_seconds() / 60
            )
        )

        return True, minutes_remaining

    return False, 0


def verify_pin(employee_id, entered_pin):

    locked, minutes_remaining = is_locked_out(
        employee_id
    )

    if locked:

        return {
            "success": False,
            "message":
            f"Account Locked. Try again in {minutes_remaining} minute(s)."
        }

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT pin_hash
        FROM employees
        WHERE employee_id = ?
    """, (employee_id,))

    result = cursor.fetchone()

    conn.close()

    if result is None:

        return {
            "success": False,
            "message": "Employee Not Found"
        }

    stored_hash = result[0]

    is_valid = bcrypt.checkpw(
        entered_pin.encode(),
        stored_hash.encode()
    )

    if is_valid:

        log_login_attempt(
            employee_id,
            "SUCCESS"
        )

        return {
            "success": True,
            "message": "Login Successful"
        }

    else:

        log_login_attempt(
            employee_id,
            "FAILED"
        )

        failed_attempts = get_failed_attempts(
            employee_id
        )

        remaining = max(
            0,
            MAX_FAILED_ATTEMPTS
            - failed_attempts
        )

        if remaining == 0:

            return {
                "success": False,
                "message":
                f"Account Locked for {LOCKOUT_DURATION_MINUTES} minutes."
            }

        return {
            "success": False,
            "message":
            f"Invalid PIN. {remaining} attempts remaining."
        }