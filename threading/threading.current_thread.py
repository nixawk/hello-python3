#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import logging


logging.basicConfig(level=logging.INFO, format="%(threadName)s: %(message)s")
log = logging.getLogger(__file__)


def worker(num):
    """thread worker function"""
    # print("%s: %d" % (threading.current_thread().getName(), num))

    """
    Most programs do not use print to debug. The logging module supports embedding the thread name
    in every log message using the formatter code %(threadName)s. Including thread names in log messages makes it
    possible to trace those messages back to their source

    logging is also thread-safe, so messages from different threads are kept distinct in the output.
    """
    log.info(num)


if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()