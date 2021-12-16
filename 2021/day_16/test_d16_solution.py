"""Test day 16 solution"""
import pytest
from d16_solution import hex_to_bin, part_1, part_2


@pytest.mark.parametrize(
    "hex_str,expected",
    [
        ("D2FE28", "110100101111111000101000"),
        ("38006F45291200", "00111000000000000110111101000101001010010001001000000000"),
    ],
)
def test_hex_to_bin(hex_str, expected):
    assert hex_to_bin(hex_str) == expected


@pytest.mark.parametrize(
    "hex_str,expected",
    [
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ],
)
def test_part_1(hex_str, expected):
    assert part_1(hex_str) == expected


@pytest.mark.parametrize(
    "hex_str,expected",
    [
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ],
)
def test_part_2(hex_str, expected):
    assert part_2(hex_str) == expected
