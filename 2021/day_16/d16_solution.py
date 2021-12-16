"""Day 16 solution"""
import math
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class PacketType(Enum):
    SUM = 0
    PRODUCT = 1
    MIN = 2
    MAX = 3
    LITERAL = 4
    GT = 5
    LT = 6
    EQ = 7


@dataclass
class Header:
    version_id: int
    type: PacketType


class Packet:
    EVAL_HANDLERS = {
        PacketType.SUM: sum,
        PacketType.PRODUCT: math.prod,
        PacketType.MIN: min,
        PacketType.MAX: max,
        PacketType.GT: lambda args: args[0] > args[1],
        PacketType.LT: lambda args: args[0] < args[1],
        PacketType.EQ: lambda args: args[0] == args[1],
    }

    def __init__(
        self,
        header: Header,
        value: Optional[int] = None,
        subpackets: Optional[list] = None,
    ):
        self.header = header
        self.value = value
        self.subpackets = subpackets or []

    def version_sum(self) -> int:
        return self.header.version_id + sum(
            subpacket.version_sum() for subpacket in self.subpackets
        )

    def eval(self) -> Optional[int]:
        if self.header.type == PacketType.LITERAL:
            return self.value

        return self.EVAL_HANDLERS[self.header.type](
            [subpacket.eval() for subpacket in self.subpackets]
        )


def hex_to_bin(hex_str: str) -> str:
    """Convert hex string to binary representation"""
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)


def shift_binary(data: str, num_bits: int) -> tuple[str, str]:
    bits = data[:num_bits]
    return bits, data[num_bits:]


def shift(data: str, num_bits: int) -> tuple[int, str]:
    bits = data[:num_bits]
    return int(bits, 2), data[num_bits:]


def parse_header(data: str) -> tuple[Header, str]:
    version_id, data = shift(data, 3)
    type_id, data = shift(data, 3)
    return Header(version_id, PacketType(type_id)), data


def parse_literal(data: str) -> tuple[int, str]:
    value = 0
    group_bit, data = shift(data, 1)

    while group_bit == 1:
        group, data = shift(data, 4)
        value = 16 * value + group
        group_bit, data = shift(data, 1)

    group, data = shift(data, 4)
    value = 16 * value + group
    return value, data


def parse_subpackets_by_length(data: str) -> tuple[list[Packet], str]:
    total_length, data = shift(data, 15)
    subpacket_data, data = shift_binary(data, total_length)
    subpackets = []

    while subpacket_data:
        subpacket, subpacket_data = parse_packet(subpacket_data)
        subpackets.append(subpacket)

    return subpackets, data


def parse_subpackets_by_count(data: str) -> tuple[list[Packet], str]:
    total_subpackets, data = shift(data, 11)
    subpackets = []

    for _ in range(total_subpackets):
        subpacket, data = parse_packet(data)
        subpackets.append(subpacket)

    return subpackets, data


def parse_packet(data: str) -> tuple[Packet, str]:
    header, data = parse_header(data)

    if header.type == PacketType.LITERAL:
        value, data = parse_literal(data)
        return Packet(header, value=value), data

    length_type_id, data = shift(data, 1)

    if length_type_id == 0:
        subpackets, data = parse_subpackets_by_length(data)
    else:
        subpackets, data = parse_subpackets_by_count(data)

    return Packet(header, subpackets=subpackets), data


def parse_transmission(hex_str: str):
    transmission = hex_to_bin(hex_str)
    packet, _ = parse_packet(transmission)
    return packet


def part_1(transmission_hex_str: str) -> int:
    transmission = parse_transmission(transmission_hex_str)
    return transmission.version_sum()


def part_2(transmission_hex_str: str) -> Optional[int]:
    transmission = parse_transmission(transmission_hex_str)
    return transmission.eval()


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        transmission_hex_str = input.read().strip()

    part_1_ans = part_1(transmission_hex_str)
    print(part_1_ans)

    part_2_ans = part_2(transmission_hex_str)
    print(part_2_ans)
