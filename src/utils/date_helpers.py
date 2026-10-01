"""Due-date helpers for the Acme Billing Service."""

from datetime import date, timedelta

# Payment terms: invoices are due this many days after issue.
PAYMENT_TERMS_DAYS = 30


def due_date(issued_on: date) -> date:
    """Return the date an invoice issued on ``issued_on`` is due."""
    return issued_on + timedelta(days=PAYMENT_TERMS_DAYS)


def days_until_due(issued_on: date, today: date) -> int:
    """Return how many days are left until the invoice is due (negative when overdue)."""
    return (due_date(issued_on) - today).days
