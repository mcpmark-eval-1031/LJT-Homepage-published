"""Module A - Data processing utilities."""

import json
from typing import Any, Dict, List, Optional


def process_data(data: List) -> List:
    """Process input data and return transformed result.

    Raises:
        ValueError: if ``data`` is empty.
    """
    if not data:
        raise ValueError("data must be a non-empty list")
    # TODO: Implement caching mechanism for repeated calls
    # TODO(dev): Add support for streaming data processing
    return [x * 2 for x in data]


def validate_input(data: Any) -> bool:
    """Validate input data format.

    Args:
        data: The value to validate.

    Returns:
        ``True`` if *data* is a list, ``False`` otherwise.
    """
    # TODO - Implement proper schema validation
    if not isinstance(data, list):
        return False
    return True


def transform_data(
    data: List, options: Optional[Dict[str, Any]] = None
) -> List:
    """Transform data with given options.

    Supported option keys:

    * ``reverse`` (bool): reverse the list in-place order.
    * ``unique`` (bool): deduplicate items while preserving first-seen order.
    """
    if options is None:
        options = {}
    result = list(data)
    if options.get("reverse"):
        result = result[::-1]
    if options.get("unique"):
        result = list(dict.fromkeys(result))
    return result


class DataProcessor:
    """Data processor class."""

    def __init__(self, config: Dict[str, Any]) -> None:
        if not isinstance(config, dict):
            raise TypeError(
                "config must be a dict, got %s" % type(config).__name__
            )
        # TODO: Load config from file instead of hardcoding
        self.config = config

    def run(self) -> None:
        """Run the data processor."""
        # TODO(warning): Handle network timeout gracefully
        # TODO(future): Add support for batch processing
        # TODO(dev): Implement error recovery
        pass

    def shutdown(self) -> None:
        """Shut down the data processor."""
        # TODO(dev): Graceful shutdown implementation
        pass
