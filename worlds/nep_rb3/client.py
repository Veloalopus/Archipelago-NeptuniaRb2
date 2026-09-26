from typing import Optional, ClassVar, Dict, Set
import ast
import asyncio
import colorama
import os
import pymem
from pathlib import Path
import time

from CommonClient import (
    CommonContext,
    get_base_parser,
    logger,
    server_loop,
    gui_enabled,
)
from MultiServer import mark_raw
from NetUtils import ClientStatus
from Utils import get_intended_text
from worlds.AutoWorld import World

from .Rb3MemoryInterface import Rb3MemoryInterface
from .treasures.dungeon_treasures import *

from .names import InternalItemIDs

from . import DropTables

class Rb3Context(CommonContext):
    """Hyperdimension Neptunia ReBirth3 Game Context"""
    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        super().__init__(server_address, password)
        self.game = "Hyperdimension Neptunia Re;Birth3 V GENERATION"
        self.items_handling = 0b001  # only items from other worlds
        self.location_name_to_ap_id = None
        self.location_ap_id_to_name = None
        self.item_name_to_ap_id = None
        self.item_ap_id_to_name = None
        self.rb3_interface = Rb3MemoryInterface()

        self.seed_name = None

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def make_gui(self):
        ui = super().make_gui()
        ui.base_title = "Hyperdimension Neptunia Re;Birth3 V GENERATION Client"
        return ui
    
    def client_received_initial_server_data(self):
        return(self.slot)
    
    async def wait_for_initial_connection(self):
        if self.client_received_initial_server_data():
            return
        
        logger.info("Waiting for server connection")
        while not self.client_received_initial_server_data() and not self.exit_event_is_set():
            await asyncio.sleep(1)
        
        if not self.exit_event.is_set():
            await asyncio.sleep(1)
            assert self.slot_data

    

async def rb3_watcher(ctx: Rb3Context):
    """
    Client loop, watching the game process
    Handles game hook attachments, checking locations, giving items, etc.

    :Rb3Context ctx: The ReBirth3 Client context instance.
    """

    showed_connecting_message = False
    showed_connected_message = False

    while not ctx.exit_event.is_set():

        if not showed_connecting_message:
            logger.info("Waiting for Re;Birth3...")
            showed_connecting_message = True

        if ctx.rb3_interface.is_connected():
            if not showed_connected_message:
                logger.info("Connected to Re;Birth3")
                showed_connected_message = True

        await asyncio.sleep(0.25)
        if not ctx.rb3_interface.is_connected():
            await ctx.rb3_interface.connect(ctx.exit_event)

        while True:
            await asyncio.sleep(0.5)

            if not ctx.server:
                break

            if ctx.exit_event.is_set():
                break

            if ctx.slot is not None:
                #logger.info(f"Base pointer is {ctx.rb3_interface.rb3_basePointer}")
                #logger.info(f"Save data starts at {ctx.rb3_interface.rb3_savePointer}")

                logger.info(f"Inventory has {ctx.rb3_interface._current_item_count()} unique items")

                logger.info(f"Player currently has {ctx.rb3_interface._get_item_amount(ctx.rb3_interface._get_item_slot(InternalItemIDs.FRAGMENT_LIFE))} Life Fragments")

                ctx.rb3_interface.insert_drop_table(DropTables.testTreasure)
                

                for i in range(len(ctx.rb3_interface.vfszTreasureData)):
                    if ctx.rb3_interface.vfszTreasureFlags[i] == 0:
                        curTreasureData = ctx.rb3_interface.vfszTreasureData[i]
                        curTreasureByte = ctx.rb3_interface._read_byte(curTreasureData[0])
                        curTreasureBitmask = curTreasureData[1]
                        curTreasureFlag = curTreasureByte & curTreasureBitmask

                        if curTreasureFlag:
                            logger.info(f"Collected VFSZ Treasure ID: {i + 1}")
                            ctx.rb3_interface.vfszTreasureFlags[i] = 1

                for i in range(len(ctx.rb3_interface.stationAreaTreasureData)):
                    if ctx.rb3_interface.stationAreaTreasureFlags[i] == 0:
                        curTreasureData = ctx.rb3_interface.stationAreaTreasureData[i]
                        curTreasureByte = ctx.rb3_interface._read_byte(curTreasureData[0])
                        curTreasureBitmask = curTreasureData[1]
                        curTreasureFlag = curTreasureByte & curTreasureBitmask

                        if curTreasureFlag:
                            logger.info(f"Collected Station Area Treasure ID: {i + 1}")
                            ctx.rb3_interface.stationAreaTreasureFlags[i] = 1

        if ctx.exit_event.is_set():
            break
        if not ctx.server:
            continue

        await asyncio.sleep(1)
    

async def main(args):
    """
    Launch a client instance (threaded)
    """
    ctx = Rb3Context(args.connect, args.password)
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="Rb3 Server Loop")

    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()

    watcher = asyncio.create_task(
        rb3_watcher(ctx),
        name="Rb3 Progression Checking"
    )
    await ctx.exit_event.wait()
    await watcher
    await ctx.shutdown()

def launch(*args) -> None:
    """
    Launch a client instance (wrapper / args parser)
    """
    parser = get_base_parser(description="Hyperdimension Neptunia Re;Birth3 V GENERATION Client")
    parser.add_argument("--name", default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")
    args = parser.parse_args(args)

    if args.url:
        url = urllib.parse.urlparse(args.url)
        args.connect = url.netloc
        if url.username:
            args.name = urllib.parse.unquote(url.username)
        if url.password:
            args.password = urllib.parse.unquote(url.password)

    asyncio.run(main(args))
