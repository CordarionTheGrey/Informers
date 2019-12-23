import textwrap

import cog
import yaml


def reindent(level, text):
    head, eol, tail = text.partition('\n')
    return head + textwrap.indent(eol + tail, "    " * level).replace('\n', "\n\n") if eol else text


def write(text):
    assert text.lstrip().startswith("..\n")
    cog.out(textwrap.dedent(text)[3:])


def write_informer(*, desc, title, expr, mode=""):
    write(f"""\
    ..
    .. list-table::
        :stub-columns: 1
        :widths: 1 50

        * - Описание
          - {reindent(3, desc)}
        * - Заголовок
          - ``{title}``
        * - Выражение
          - ``{expr}``
    """)
    if not mode:
        return
    write(f"""\
    ..
        * - Тип
          - ``{mode}``
    """)


def write_informers(yaml_source):
    for informer in yaml.safe_load(yaml_source):
        write_informer(**informer)
