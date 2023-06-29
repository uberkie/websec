from attr import dataclass, field


@dataclass
class DHCPRelay:
    name: str
    interface: str
    dhcp_server: str
    delay_threshold: str = None
    local_address: str = None
    add_relay_info: bool = False
    disabled: bool = False
    invalid: bool = field(on_setattr=None, default=None)
    id: str = field(on_setattr=None, default=None)

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return not self.disabled
