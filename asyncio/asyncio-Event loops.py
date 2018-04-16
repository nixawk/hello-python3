#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio


async def greeting(loop, welcome):
    print(welcome)
    loop.stop()


class MyEventLoopPolicy(asyncio.DefaultEventLoopPolicy):

    async def do_something(self):
        print("This is my event loop policy")

    def get_event_loop(self):
        """Get the event loop.

        This may be None or an instance of EventLoop
        """

        loop = super().get_event_loop()

        # Do something with loop
        loop.create_task(self.do_something())

        return loop


if __name__ == '__main__':

    # The following functions are convenient shortcuts to accessing the methods
    # of the global policy. Note that this provides access to the default policy
    # ,unless an alternative policy was set by calling set_event_loop_policy()
    # earlier in the execution of the process.

    default_loop_policy = asyncio.get_event_loop_policy()
    print(type(default_loop_policy))

    # Mac OSX, default: asyncio.unix_events._UnixDefaultEventLoopPolicy

    # Equivalent to calling get_event_loop_policy().get_event_loop()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(greeting(loop, "1st - hello asyncio event loop"))
    loop.close()

    # Equivalent to calling get_event_loop_policy().new_event_loop()
    newloop = asyncio.new_event_loop()

    # Equivalent to calling get_event_loop_policy().set_event_loop()
    asyncio.set_event_loop(newloop)
    asyncio.ensure_future(greeting(newloop, "2nd - hello asyncio event loop"))
    newloop.run_forever()
    newloop.close()

    # Available event loops

    # asyncio currently provides two implementations of event loops:
    # SelectorEventLoop and ProactorEventLoop.

    # Access to the global loop policy
    asyncio.set_event_loop_policy(MyEventLoopPolicy())
    my_loop = asyncio.get_event_loop()
    my_loop.run_until_complete(
        greeting(my_loop, "3rd - hello asyncio event loop")
    )
    my_loop.close()


# https://docs.python.org/3/library/asyncio-eventloops.html