#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio


async def slow_operation(future):
    await asyncio.sleep(1)

    # Make the future done and set its result.
    future.set_result('Future is done !')


def get_result(future):
    print(future.result())
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # Future - Represents the result of an asynchronous computation.
    # future = asyncio.Future()
    future = loop.create_future()

    asyncio.ensure_future(slow_operation(future))

    # Future.add_done_callback() method to describe explicitly the control flow.

    # loop.run_until_complete(future)
    # print(future.result())

    future.add_done_callback(get_result)

    loop.run_forever()
    loop.close()


# https://docs.python.org/3/library/asyncio-eventloop.html#futures
# https://docs.python.org/3/library/asyncio-task.html#future