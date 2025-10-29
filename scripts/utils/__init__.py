"""
Shared utility functions for SweepGraph scripts.
"""

import logging
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.logging import RichHandler


def setup_logger(name: str, log_file: str = None) -> logging.Logger:
    """
    Set up a logger with Rich formatting and optional file output.

    Args:
        name: Logger name
        log_file: Optional path to log file

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.handlers = []  # Clear existing handlers

    # Rich console handler
    console_handler = RichHandler(
        rich_tracebacks=True,
        markup=True,
        show_time=True,
        show_path=False
    )
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)

    # File handler (if specified)
    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger


def get_timestamp() -> str:
    """Get timestamp for filenames (YYYYMMDD_HHMMSS)."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def get_date() -> str:
    """Get date string (YYYY-MM-DD)."""
    return datetime.now().strftime("%Y-%m-%d")


def get_datetime() -> str:
    """Get datetime string (YYYY-MM-DD HH:MM:SS)."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def print_banner(title: str, width: int = 70):
    """Print a styled banner."""
    console = Console()
    console.print()
    console.print("=" * width, style="bold blue")
    console.print(f"{title:^{width}}", style="bold white")
    console.print("=" * width, style="bold blue")
    console.print()
