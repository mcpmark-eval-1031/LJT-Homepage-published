"""Helper utilities."""

import threading
from typing import Any

# Module-level lock serialises concurrent calls to format_output.
_fmt_lock = threading.Lock()


def format_output(result: Any, template: str = "{value}") -> str:
    """Format result for display.

    Args:
        result: The value to format.
        template: A Python :meth:`str.format`-compatible template string
            containing the placeholder ``{value}``.  Defaults to
            ``"{value}"``.

    Returns:
        The formatted string.

    Thread-safety:
        Calls are serialised via the module-level ``_fmt_lock``.
    """
    with _fmt_lock:
        return template.format(value=result)
