import sys
import time
import threading
import itertools
from termcolor import colored


class Spinner:
    """Spinner class to show a circular animation."""

    def __init__(self, message="Loading"):
        self.stop_running = threading.Event()
        self.spinner = itertools.cycle(["|", "/", "-", "\\"])
        self.message = message

    def start(self):
        """Start the spinner animation in a separate thread."""
        self.thread = threading.Thread(target=self.spin, daemon=True)
        self.thread.start()

    def spin(self):
        """Run the spinner animation."""
        while not self.stop_running.is_set():
            sys.stdout.write(
                f"\r{colored(self.message,'magenta')} {next(self.spinner)}")
            sys.stdout.flush()
            time.sleep(0.1)

    def stop(self):
        """Stop the spinner animation."""
        self.stop_running.set()
        self.thread.join()
        sys.stdout.write("\r" + " " * len(self.message) + "\r")
        sys.stdout.flush()
