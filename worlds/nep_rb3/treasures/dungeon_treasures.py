from typing import Optional, ClassVar, Dict, Set
import ast
import asyncio
import colorama
import os
import pymem
from pathlib import Path
import time

from ..Rb3MemoryInterface import Rb3MemoryInterface
from ..offsets import *

class VirtuaForestSafeZoneTreasures():
    treasure_count = 4
    treasure_1 = 0b00001000
    treasure_2 = 0b00010000
    treasure_3 = 0b00100000
    treasure_4 = 0b01000000
    treasure_bytes = 0x89D
    byte = None

    def get_treasure(self, treasureID):
        logger.info("the treasure function was called with {treasureID}")

        logger.info("byte was set as {self.byte}")
        if treasureID == 1:
            return self.treasure_1 & self.byte
        
        if treasureID == 2:
            return self.treasure_2 & self.byte
        
        if treasureID == 3:
            return self.treasure_3 & self.byte
        
        if treasureID == 4:
            return self.treasure_4 & self.byte
        
class StationAreaTreasures():
    treasure_count = 4
    treasure_bytes_1 = SAVE_START + 0x89E
    treasure_bytes_2 = SAVE_START + 0x89F
    treasure_1 = 0b00100000
    treasure_2 = 0b01000000
    treasure_3 = 0b10000000
    treasure_4 = 0b00000001
    byte_1 = None
    byte_2 = None

    def get_treasure(self, treasureID):
        self.byte_1 = Rb3MemoryInterface._read_byte(self.treasure_bytes_1)
        self.byte_2 = Rb3MemoryInterface._read_byte(self.treasure_bytes_2)

        if treasureID == 1:
            return self.treasure_1 & self.byte_1
        
        if treasureID == 2:
            return self.treasure_2 & self.byte_1
        
        if treasureID == 3:
            return self.treasure_3 & self.byte_1
        
        if treasureID == 4:
            return self.treasure_4 & self.byte_2
