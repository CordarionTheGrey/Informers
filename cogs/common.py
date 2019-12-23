import textwrap

import cog


def reindent(level, text):
    head, eol, tail = text.partition('\n')
    return head + textwrap.indent(eol + tail, "    " * level).replace('\n', "\n\n") if eol else text


def write(text):
    assert text.lstrip().startswith("..\n")
    cog.out(textwrap.dedent(text)[3:])
