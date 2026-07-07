from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def lookup_customer_profile(customer_id: str) -> dict[str, Any]:
    """Return a customer profile by customer ID from local mock data.

    Args:
        customer_id: Unique customer identifier to search for.

    Returns:
        The matching customer record as a dictionary, or an error dictionary
        when no matching customer exists.
    """
    customers = _load_json_data("customers.json")

    for customer in customers:
        if customer.get("customer_id") == customer_id:
            return customer

    return {"error": "Customer not found"}


def lookup_network_status(city: str) -> dict[str, Any]:
    """Return network status details for a city (case-insensitive match)."""
    network_records = _load_json_data("network.json")

    target_city = city.strip().lower()
    for record in network_records:
        if str(record.get("city", "")).strip().lower() == target_city:
            return record

    return {"error": "City not found"}


def lookup_knowledge(topic: str) -> dict[str, Any]:
    """Return a knowledge base article by topic (case-insensitive match)."""
    knowledge_records = _load_json_data("knowledge.json")

    target_topic = topic.strip().lower()
    for record in knowledge_records:
        if str(record.get("topic", "")).strip().lower() == target_topic:
            return record

    return {"error": "Knowledge article not found"}


def _load_json_data(filename: str) -> list[dict[str, Any]]:
    """Load and return records from a JSON file in the app/data directory."""
    data_path = Path(__file__).resolve().parent / "data" / filename
    with data_path.open("r", encoding="utf-8") as file:
        return json.load(file)
