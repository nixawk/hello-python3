#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import typing

from urllib.parse import urlparse
from mitmproxy import (
    http,
    ctx
)

class ReplaceHost(object):

    def load(self, loader):
        loader.add_option(
            name = "src_target",
            typespec = typing.Optional[str],
            default = "",
            help = "Set src target",
        )

        loader.add_option(
            name = "dst_target",
            typespec = typing.Optional[str],
            default = "",
            help = "Set dst target",
        )

    def request(self, flow: http.HTTPFlow):
        # redirect to different host
        src_target = ctx.options.src_target
        dst_target = ctx.options.dst_target

        # If no dst_target, raise an exception
        if not dst_target:
            raise Exception("[*] --set dst_target=example.com")

        # If no src_target, replace all src_targets with dst_target.
        if not src_target:
            flow.request.host = dst_target
        else:
            if flow.request.pretty_host.lower() == src_target.lower():
                flow.request.host = dst_target
                ctx.log.info("[*] ReplaceHost: %s -> %s" % (src_target, dst_target))


class TamperURI(object):

    def request(self, flow: http.HTTPFlow):
        # redirect to different host

        src_uri = flow.request.path
        dst_uri = urlparse(src_uri).path

        flow.request.path = dst_uri
        ctx.log.info("[*] TransferURI: %s -> %s" % (src_uri, dst_uri))


class ReturnResponse(object):
        def response(self, flow: http.HTTPFlow):
            for k, v in flow.response.headers.items():
                ctx.log.info("[*] ResponseHeaders: %s = %s" % (k ,v))

            # flow.response = http.HTTPResponse.make(
            #       418, b"This is a test message",
            # )


addons = [
    ReplaceHost(),
    TamperURI(),
    ReturnResponse(),
]

# mitmproxy -s replacehost.py --set src_target=localhost --set dst_target=apache.org
# [mitmproxy mode] : console.view.eventlog

# https://github.com/mitmproxy/mitmproxy/tree/master/mitmproxy/addons
# https://github.com/mitmproxy/mitmproxy/blob/master/mitmproxy/http.py
# https://github.com/mitmproxy/mitmproxy/blob/master/mitmproxy/net/http/response.py
# https://docs.mitmproxy.org/stable/addons-options/