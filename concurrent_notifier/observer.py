class Observer:
    """Observer (Client) that waits for updates from the Server (Subject)."""

    def __init__(self, time_delay: int) -> None:
        self.time_delay = time_delay

    def update(self, event_data: str) -> None:
        """Client request when notified by the server."""
        # Implementation will be added later
        pass
