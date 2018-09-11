#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
symbol.sym_name

Dictionary mapping the numeric values of the constants defined in this
module back to name strings, allowing more human-readable representation
of parse trees to be generated.
"""

import symbol


def symbol_sym_name():
    for key, value in symbol.sym_name.items():
        print(key, value)

    # 256 single_input
    # 257 file_input
    # 258 eval_input
    # 259 decorator
    # 260 decorators
    # 261 decorated
    # 262 async_funcdef
    # 263 funcdef
    # 264 parameters
    # 265 typedargslist
    # 266 tfpdef
    # 267 varargslist
    # 268 vfpdef
    # 269 stmt
    # 270 simple_stmt
    # 271 small_stmt
    # 272 expr_stmt
    # 273 annassign
    # 274 testlist_star_expr
    # 275 augassign
    # 276 del_stmt
    # 277 pass_stmt
    # 278 flow_stmt
    # 279 break_stmt
    # 280 continue_stmt
    # 281 return_stmt
    # 282 yield_stmt
    # 283 raise_stmt
    # 284 import_stmt
    # 285 import_name
    # 286 import_from
    # 287 import_as_name
    # 288 dotted_as_name
    # 289 import_as_names
    # 290 dotted_as_names
    # 291 dotted_name
    # 292 global_stmt
    # 293 nonlocal_stmt
    # 294 assert_stmt
    # 295 compound_stmt
    # 296 async_stmt
    # 297 if_stmt
    # 298 while_stmt
    # 299 for_stmt
    # 300 try_stmt
    # 301 with_stmt
    # 302 with_item
    # 303 except_clause
    # 304 suite
    # 305 test
    # 306 test_nocond
    # 307 lambdef
    # 308 lambdef_nocond
    # 309 or_test
    # 310 and_test
    # 311 not_test
    # 312 comparison
    # 313 comp_op
    # 314 star_expr
    # 315 expr
    # 316 xor_expr
    # 317 and_expr
    # 318 shift_expr
    # 319 arith_expr
    # 320 term
    # 321 factor
    # 322 power
    # 323 atom_expr
    # 324 atom
    # 325 testlist_comp
    # 326 trailer
    # 327 subscriptlist
    # 328 subscript
    # 329 sliceop
    # 330 exprlist
    # 331 testlist
    # 332 dictorsetmaker
    # 333 classdef
    # 334 arglist
    # 335 argument
    # 336 comp_iter
    # 337 comp_for
    # 338 comp_if
    # 339 encoding_decl
    # 340 yield_expr
    # 341 yield_arg

if __name__ == '__main__':
    symbol_sym_name()


# reference
# https://docs.python.org/3/library/symbol.html
