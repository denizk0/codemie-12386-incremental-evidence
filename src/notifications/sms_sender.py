"""Payment reminder SMS notifications."""

REMINDER_DAYS_BEFORE_DUE = 3


def build_payment_reminder(invoice_number: str, phone: str, days_left: int) -> dict | None:
    """Build the SMS reminder, or None when it is not time to remind yet."""
    if days_left != REMINDER_DAYS_BEFORE_DUE:
        return None
    return {
        "to": phone,
        "text": f"Acme: invoice {invoice_number} is due in {days_left} days.",
    }
