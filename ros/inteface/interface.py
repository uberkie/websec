from attr import dataclass
from typing import Union

import cattrs
from cattrs import Converter
from typing import Union

# Define the structure hook
from cattrs.converters import NoneType


@dataclass
class Interface:
    mtu: Union[int, str]
    name: Union[str, None] = None
    running: Union[bool, None] = None
    rx_byte: Union[int, None] = None
    rx_drop: Union[int, None] = None
    rx_error: Union[int, None] = None
    rx_packet: Union[int, None] = None
    tx_byte: Union[int, None] = None
    tx_drop: Union[int, None] = None
    tx_error: Union[int, None] = None
    tx_packet: Union[int, None] = None
    tx_queue_drop: Union[int, None] = None
    type: Union[str, None] = None
    comment: Union[str, None] = None
    l2mtu: Union[int, None] = None
    mac_address: str = None
    default_name: Union[str, None] = None
    max_l2mtu: Union[int, None] = None
    slave: Union[bool, None] = None
    id: Union[str, None] = None
    actual_mtu: Union[int, None] = None
    disabled: Union[bool, None] = None
    fp_rx_byte: Union[int, None] = None
    fp_rx_packet: Union[int, None] = None

    fp_tx_byte: Union[int, None] = None
    fp_tx_packet: Union[int, None] = None
    link_downs: Union[int, None] = None

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return not self.disabled

