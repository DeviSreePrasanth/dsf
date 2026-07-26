from datetime import datetime, timezone


def get_utc_timestamp() -> str:
    """Return the current UTC time as an ISO 8601 string."""
    return datetime.now(timezone.utc).isoformat()


def clean_column_name(name: str) -> str:
    """Normalize a column name: lowercase, spaces to underscores, strip whitespace."""
    return name.strip().lower().replace(" ", "_")


def validate_non_empty(value: str, field_name: str) -> str:
    """Raise a ValueError if a required string field is empty."""
    if not value or not value.strip():
        raise ValueError(f"{field_name} cannot be empty")
    return value.strip()


def chunk_list(items: list, chunk_size: int) -> list:
    """Split a list into smaller lists of a given size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater")