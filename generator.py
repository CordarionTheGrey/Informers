import textwrap

import cog
import yaml


def write(text):
    assert text.lstrip().startswith("..\n")
    cog.out(textwrap.dedent(text)[3:])


def write_informer(desc, title, expr, mode=""):
    write(f"""\
    ..
    .. list-table::
        :stub-columns: 1
        :widths: 1 50

        * - Описание
          - {desc}
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


def write_informers():
    with open("informers.yml", encoding="utf-8-sig") as f:
        for informer in yaml.safe_load(f):
            write_informer(**informer)
