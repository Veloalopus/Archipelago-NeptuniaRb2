import asyncio
import struct
from typing import List, Tuple
from pymem import pymem
from pymem.process import module_from_name
from CommonClient import logger
from . import offsets



class Rb2MemoryInterface():
    """Rb2MemoryInterface allows for reading and writing to the Rb2 game memory"""


    