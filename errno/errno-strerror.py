#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module makes available standard errno system symbols. The value of each
symbol is the corresponding integer value. The names and descriptions are
borrowed from linux/include/errno.h.



01            EPERM Operation not permitted
02           ENOENT No such file or directory
03            ESRCH No such process
04            EINTR Interrupted system call
05              EIO Input/output error
06            ENXIO Device not configured
07            E2BIG Argument list too long
08          ENOEXEC Exec format error
09            EBADF Bad file descriptor
10           ECHILD No child processes
11          EDEADLK Resource deadlock avoided
12           ENOMEM Cannot allocate memory
13           EACCES Permission denied
14           EFAULT Bad address
15          ENOTBLK Block device required
16            EBUSY Resource busy
17           EEXIST File exists
18            EXDEV Cross-device link
19           ENODEV Operation not supported by device
20          ENOTDIR Not a directory
21           EISDIR Is a directory
22           EINVAL Invalid argument
23           ENFILE Too many open files in system
24           EMFILE Too many open files
25           ENOTTY Inappropriate ioctl for device
26          ETXTBSY Text file busy
27            EFBIG File too large
28           ENOSPC No space left on device
29           ESPIPE Illegal seek
30            EROFS Read-only file system
31           EMLINK Too many links
32            EPIPE Broken pipe
33             EDOM Numerical argument out of domain
34           ERANGE Result too large
35           EAGAIN Resource temporarily unavailable
36      EINPROGRESS Operation now in progress
37         EALREADY Operation already in progress
38         ENOTSOCK Socket operation on non-socket
39     EDESTADDRREQ Destination address required
40         EMSGSIZE Message too long
41       EPROTOTYPE Protocol wrong type for socket
42      ENOPROTOOPT Protocol not available
43  EPROTONOSUPPORT Protocol not supported
44  ESOCKTNOSUPPORT Socket type not supported
45          ENOTSUP Operation not supported
46     EPFNOSUPPORT Protocol family not supported
47     EAFNOSUPPORT Address family not supported by protocol family
48       EADDRINUSE Address already in use
49    EADDRNOTAVAIL Can't assign requested address
50         ENETDOWN Network is down
51      ENETUNREACH Network is unreachable
52        ENETRESET Network dropped connection on reset
53     ECONNABORTED Software caused connection abort
54       ECONNRESET Connection reset by peer
55          ENOBUFS No buffer space available
56          EISCONN Socket is already connected
57         ENOTCONN Socket is not connected
58        ESHUTDOWN Can't send after socket shutdown
59     ETOOMANYREFS Too many references: can't splice
60        ETIMEDOUT Operation timed out
61     ECONNREFUSED Connection refused
62            ELOOP Too many levels of symbolic links
63     ENAMETOOLONG File name too long
64        EHOSTDOWN Host is down
65     EHOSTUNREACH No route to host
66        ENOTEMPTY Directory not empty
67         EPROCLIM Too many processes
68           EUSERS Too many users
69           EDQUOT Disc quota exceeded
70           ESTALE Stale NFS file handle
71          EREMOTE Too many levels of remote in path
72          EBADRPC RPC struct is bad
73     ERPCMISMATCH RPC version wrong
74     EPROGUNAVAIL RPC prog. not avail
75    EPROGMISMATCH Program version wrong
76     EPROCUNAVAIL Bad procedure for program
77           ENOLCK No locks available
78           ENOSYS Function not implemented
79           EFTYPE Inappropriate file type or format
80            EAUTH Authentication error
81        ENEEDAUTH Need authenticator
82          EPWROFF Device power is off
83          EDEVERR Device error
84        EOVERFLOW Value too large to be stored in data type
85         EBADEXEC Bad executable (or shared library)
86         EBADARCH Bad CPU type in executable
87       ESHLIBVERS Shared library version mismatch
88        EBADMACHO Malformed Mach-o file
89        ECANCELED Operation canceled
90            EIDRM Identifier removed
91           ENOMSG No message of desired type
92           EILSEQ Illegal byte sequence
93          ENOATTR Attribute not found
94          EBADMSG Bad message
95        EMULTIHOP EMULTIHOP (Reserved)
96          ENODATA No message available on STREAM
97          ENOLINK ENOLINK (Reserved)
98            ENOSR No STREAM resources
99           ENOSTR Not a STREAM
100           EPROTO Protocol error
101            ETIME STREAM ioctl timeout
102       EOPNOTSUPP Operation not supported on socket
103        ENOPOLICY Policy not found
"""

import os
import errno


all_error_codes = errno.errorcode
for errno_num in sorted(all_error_codes):
    print(
        "%02d %16s %s" % (
            errno_num, all_error_codes[errno_num], os.strerror(errno_num)
        )
    )


# https://docs.python.org/3/library/errno.html
