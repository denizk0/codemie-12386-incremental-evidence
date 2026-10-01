# Acme Billing Service (CodeMie 12386 sandbox)

Throwaway repository used to record evidence for **EPMCDME-12386: incremental indexing**
of CodeMie Git (code) datasources. Every file is small on purpose, so the backend log
shows exactly which paths an incremental run re-indexes, purges or skips.

## Layout

| Path | What it holds |
|---|---|
| `src/billing/invoice.py` | Invoice totals and the VAT rate |
| `src/billing/discounts.py` | Loyalty and volume discounts |
| `src/notifications/email_sender.py` | Invoice e-mails |
| `src/notifications/sms_sender.py` | Payment reminder SMS |
| `src/utils/date_helpers.py` | Due-date helpers |
| `tests/test_invoice.py` | Invoice unit tests |

Safe to delete after the recording.
