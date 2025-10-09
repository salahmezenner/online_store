"""Utility helpers for the checkout application."""

import logging
from typing import Iterable

import requests
from django.conf import settings

logger = logging.getLogger(__name__)


def format_order_message(order, items: Iterable[str]) -> str:
    """Build a human-readable WhatsApp message for an order."""
    customer_name = f"{order.first_name} {order.last_name}".strip()
    lines = [
        f"New order #{order.id}",
        f"Customer: {customer_name}" if customer_name else "Customer: (not provided)",
        f"Phone: {order.phone_number}",
        f"Address: {order.address}",
    ]
    if order.city:
        lines.append(f"City: {order.city}")
    lines.append("Items:")
    if items:
        lines.extend(items)
    else:
        lines.append("(No order items recorded)")
    total_cost = order.get_total_cost()
    lines.append(f"Total: ${total_cost:.2f}")
    return "\n".join(lines)


def send_whatsapp_message(phone_number: str, message: str) -> None:
    """Send a WhatsApp message using the Meta Cloud API.

    This helper expects two Django settings to be configured:
    ``WHATSAPP_PHONE_NUMBER_ID`` and ``WHATSAPP_ACCESS_TOKEN``. If either is
    missing, the message will not be sent but a warning will be logged instead.
    """

    phone_number_id = getattr(settings, "WHATSAPP_PHONE_NUMBER_ID", None)
    access_token = getattr(settings, "WHATSAPP_ACCESS_TOKEN", None)

    if not phone_number_id or not access_token:
        logger.warning(
            "WhatsApp credentials are not configured. Set WHATSAPP_PHONE_NUMBER_ID and "
            "WHATSAPP_ACCESS_TOKEN to enable notifications."
        )
        return

    url = f"https://graph.facebook.com/v17.0/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "text",
        "text": {"body": message},
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        logger.error("Failed to send WhatsApp notification: %s", exc)
