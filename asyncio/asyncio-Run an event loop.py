#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio


# AbstractEventLoop
# AbstractEventLoopPolicy
# BaseEventLoop
# DefaultEventLoopPolicy
# Event
# SelectorEventLoop
# base_events
# events
# get_event_loop
# get_event_loop_policy
# new_event_loop
# selector_events
# set_event_loop
# set_event_loop_policy
# unix_events

async def greeting(loop):
    if loop.is_running():  # Returns running status of event loop.
        print("hello asyncio")
        loop.stop()        # Stop running the event loop


loop = asyncio.get_event_loop()
loop.run_until_complete(greeting(loop))
loop.close()               # Close the event loop. The loop must not be running.

if loop.is_closed():       # Returns True if the event loop was closed
    print("loop is closed")


# https://docs.python.org/3/library/asyncio-eventloop.html#run-an-event-loop