from attr import dataclass
from typing import List

from ros._base import BaseProp
from . import UpdateChannel


@dataclass
class Update:
    channel: UpdateChannel
    installed_version: str
    latest_version: str = None
    status: str = None
    section: int = None


class UpdateModule(BaseProp[Update]):
    def cancel(self):
        self.ros.post_as(f"{self.filename}/cancel", None)

    def check_for_updates(self) -> Update:
        return self.ros.post_as(f"{self.filename}/check-for-updates", List[Update])

    def download(self):
        self.ros.post_as(f"{self.filename}/download", None)

    def install(self):
        self.ros.post_as(f"{self.filename}/install", None)

    def set(self, channel: UpdateChannel):
        return super().set(channel=channel)
