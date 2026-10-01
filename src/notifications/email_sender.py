"""Invoice e-mail notifications (legacy SMTP relay)."""

SMTP_RELAY_HOST = "smtp-relay.acme.example"
SENDER = "billing@acme.example"


def build_invoice_email(invoice_number: str, customer_email: str, gross_total: float) -> dict:
    """Build the e-mail sent when an invoice is issued."""
    return {
        "from": SENDER,
        "to": customer_email,
        "subject": f"Your Acme invoice {invoice_number}",
        "body": f"Invoice {invoice_number} is ready. Amount due: {gross_total:.2f} EUR.",
        "relay": SMTP_RELAY_HOST,
    }
