import threading  # noqa f401

from concurrent_notifier.observer import Observer


class Subject:
    """Subject (Server) responsible for notifying observers about updates."""

    def __init__(self, time_delay: int) -> None:
        self._observers = []
        self.time_delay = time_delay

    def add_observer(self, observer: Observer) -> None:
        """Add an observer (client)."""
        self._observers.append(observer)

    def run(self) -> None:
        """Run method"""
        # Implementation will be added later
        pass

    def notify_observers(self, event_data: str) -> None:
        """Notify all observers (clients) about an event."""
        # Implementation will be added later
        pass
