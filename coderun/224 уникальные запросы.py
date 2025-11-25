#!/usr/bin/env python3
# single_file_hll.py
# Простая, но практичная HyperLogLog (64-bit) в одном файле.
# Реализовано: MurmurHash64A, add, merge, cardinality с small-range correction.
# Автор: адаптация для тебя.

import sys
import struct
import math

def murmur64a(key: bytes, seed: int = 0xadc83b19) -> int:
    """MurmurHash64A port (returns unsigned 64-bit int)."""
    m = 0xc6a4a7935bd1e995
    r = 47
    length = len(key)
    h = (seed & 0xFFFFFFFFFFFFFFFF) ^ ((length * m) & 0xFFFFFFFFFFFFFFFF)

    # body
    i = 0
    while i + 8 <= length:
        k = struct.unpack_from('<Q', key, i)[0]
        k = (k * m) & 0xFFFFFFFFFFFFFFFF
        k ^= (k >> r)
        k = (k * m) & 0xFFFFFFFFFFFFFFFF

        h ^= k
        h = (h * m) & 0xFFFFFFFFFFFFFFFF
        i += 8

    # tail
    tail = key[i:length]
    if tail:
        tail_val = 0
        for j in range(len(tail)):
            tail_val |= tail[j] << (j * 8)
        h ^= (tail_val & 0xFFFFFFFFFFFFFFFF)
        h = (h * m) & 0xFFFFFFFFFFFFFFFF

    # fmix64
    h ^= (h >> r)
    h = (h * 0xff51afd7ed558ccd) & 0xFFFFFFFFFFFFFFFF
    h ^= (h >> r)
    return h & 0xFFFFFFFFFFFFFFFF

def _rho(w: int, max_bits: int) -> int:
    """Number of leading zeros in w (within max_bits), plus 1."""
    if w == 0:
        return max_bits + 1    
    lz = max_bits - w.bit_length()
    return lz + 1

class HyperLogLog:
    def __init__(self, p: int = 14, seed: int = 0xadc83b19):
        """
        p: number of index bits (registers = 2^p). Typical p in [10..16].
        seed: hash seed.
        """
        assert 4 <= p <= 20, "p should be between 4 and 20"
        self.p = p
        self.m = 1 << p
        self.registers = [0] * self.m  # simple dense representation
        self.seed = seed
        # alpha_m constant depends on m
        if self.m == 16:
            self.alpha = 0.673
        elif self.m == 32:
            self.alpha = 0.697
        elif self.m == 64:
            self.alpha = 0.709
        else:
            self.alpha = 0.7213 / (1 + 1.079 / self.m)

    def _hash(self, value: str) -> int:
        return murmur64a(value.encode('utf-8'), seed=self.seed)

    def add(self, value: str):
        x = self._hash(value)
        idx = x >> (64 - self.p)                    # top p bits
        w = x & ((1 << (64 - self.p)) - 1)         # remaining bits
        rank = _rho(w, 64 - self.p)
        if rank > self.registers[idx]:
            self.registers[idx] = rank
            return True
        return False

    def merge(self, other: "HyperLogLog"):
        if self.p != other.p:
            raise ValueError("Can't merge HLL with different p")
        for i in range(self.m):
            if other.registers[i] > self.registers[i]:
                self.registers[i] = other.registers[i]

    def raw_estimate(self) -> float:
        """Raw HyperLogLog estimate (before corrections)."""
        inv_sum = 0.0
        for r in self.registers:
            inv_sum += 2.0 ** (-r)
        E = self.alpha * (self.m ** 2) / inv_sum
        return E

    def cardinality(self) -> int:
        """Estimate with small-range correction (linear counting)."""
        E = self.raw_estimate()
        # Count zero registers
        V = self.registers.count(0)
        # Small range correction (linear counting) when E is small
        if E <= (5.0 / 2.0) * self.m:
            if V != 0:
                H = self.m * math.log(self.m / V)
                return int(round(H))
            else:
                return int(round(E))
        # Large range correction (not implemented advanced bias correction here)
        return int(round(E))

# применяем готовый hll
def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())    
    h = HyperLogLog(p=14)
    for _ in range(n):
        s = input()
        h.add(s)
    print(h.cardinality())

if __name__ == "__main__":
    main()
