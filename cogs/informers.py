import yaml

import common as com


def write_informer(*, desc, title, expr, mode=""):
    com.write(f"""\
    ..
    .. list-table::
        :stub-columns: 1
        :widths: 1 50

        * - Описание
          - {com.reindent(3, desc)}
        * - Заголовок
          - ``{title}``
        * - Условие
          - ``{expr}``
    """)
    if not mode:
        return
    com.write(f"""\
    ..
        * - Тип
          - ``{mode}``
    """)


def generate(yaml_source):
    for informer in yaml.safe_load(yaml_source):
        write_informer(**informer)
