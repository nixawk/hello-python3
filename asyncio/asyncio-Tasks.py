#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio


def greeting(welcome):
    print(welcome)


async def say(what, when):
    await asyncio.sleep(when)
    print(what)


async def main(loop):

    # Schedule the execution of a coroutine object: wrap it in a future.
    # Return a Task object. Third-party event loops can use their own subclass
    # of Task for interoperability. In this case, the result type is a subclass
    # of Task.

    # create_task was added in Python 3.4.2. Use async() function to support
    # also older Python versions.

    loop.create_task(say('first hello', 2))
    loop.create_task(say('second hello', 1))

    # Set a task factory that will be used by AbstractEventLoop.create_task().
    # If factory is None, the default task factory will be set.
    # If factory is callable, it should have a signature matching(loop, coro),
    # where loop will be a reference to the active event loop, coro will be
    # a coroutine object. The callable must return an asyncio.Future compatible
    # object.

    loop.set_task_factory(greeting('third hello'))

    # Return a task factory, or None if the default one is in use.
    # print(loop.get_task_factory())

    await asyncio.sleep(5)  # wait tasks finishes.


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))

# Note that this example will never terminate, as the loop is asked
# to run_forever.
# loop.run_forever()

loop.close()


# http://asyncio.readthedocs.io/en/latest/hello_world.html#creating-tasks