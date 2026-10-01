from src.billing.invoice import Invoice, InvoiceLine


def test_gross_total_includes_vat():
    invoice = Invoice(number="INV-1", customer="ACME-42", lines=[InvoiceLine("Support plan", 100.0)])

    assert invoice.net_total() == 100.0
    assert invoice.vat() == 21.0
    assert invoice.gross_total() == 121.0
