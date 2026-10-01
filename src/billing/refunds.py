"""Refund rules for the Acme Billing Service."""

# Refunds are allowed only within this many days of payment.
REFUND_WINDOW_DAYS = 14


def can_refund(days_since_payment: int) -> bool:
    """Return True when a paid invoice can still be refunded."""
    return days_since_payment <= REFUND_WINDOW_DAYS
