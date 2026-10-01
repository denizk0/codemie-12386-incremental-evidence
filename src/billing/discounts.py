"""Discount rules for the Acme Billing Service."""

# Customers with this many paid invoices get the loyalty discount.
LOYALTY_THRESHOLD = 10
LOYALTY_DISCOUNT = 0.05

# Orders of at least this many units get the volume discount.
VOLUME_THRESHOLD = 100
VOLUME_DISCOUNT = 0.08


def discount_rate(paid_invoices: int, units: int) -> float:
    """Return the best single discount rate for a customer order."""
    rates = [0.0]
    if paid_invoices >= LOYALTY_THRESHOLD:
        rates.append(LOYALTY_DISCOUNT)
    if units >= VOLUME_THRESHOLD:
        rates.append(VOLUME_DISCOUNT)
    return max(rates)
