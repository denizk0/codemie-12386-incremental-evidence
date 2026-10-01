"""Invoice totals for the Acme Billing Service."""

from dataclasses import dataclass, field

# Standard VAT rate applied to every invoice line (raised to 21% on 2026-10-01).
VAT_RATE = 0.21


@dataclass
class InvoiceLine:
    description: str
    unit_price: float
    quantity: int = 1

    @property
    def net(self) -> float:
        return round(self.unit_price * self.quantity, 2)


@dataclass
class Invoice:
    number: str
    customer: str
    lines: list[InvoiceLine] = field(default_factory=list)

    def net_total(self) -> float:
        return round(sum(line.net for line in self.lines), 2)

    def vat(self) -> float:
        return round(self.net_total() * VAT_RATE, 2)

    def gross_total(self) -> float:
        return round(self.net_total() + self.vat(), 2)
