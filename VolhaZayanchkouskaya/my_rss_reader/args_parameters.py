#!/usr/bin/env python
import argparse


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Pure Python command-line RSS reader.")
        self.parser.add_argument("source", help="RSS URL", nargs="?", type=str)
        self.parser.add_argument("--version", help="Print version info", action="version", version="Version 1.0")
        self.parser.add_argument("--verbose", help="Outputs verbose status messages", action="store_true")
        self.parser.add_argument("--limit", help="Limits news topics if this parameter is provided", type=int)
        self.parser.add_argument("--json", help="Print result as JSON in stdout", action="store_true")
        self.parser.add_argument("--date", help="Print news of provided date in YYYYMMDD format", type=str)
        self.parser.add_argument("--to_html", help="Convert news to HTML-format", action="store_true")
        self.parser.add_argument("--to_pdf", help="Convert news to PDF-format", action="store_true")

    def print_help(self):
        """Print help message"""
        self.parser.print_help()

    def get_args(self) -> argparse.Namespace:
        """Initialize parser args"""
        return self.parser.parse_args()

