.. [[[cog
    import generator
    generator.write_informers(r"""
    - desc: >-
        Гласовый. Срабатывает в поле в перерывах между сражениями с монстрами — тогда, когда можно
        что-нибудь погласить.
      title: Бой окончен
      expr: >-
        !gv.currentMonster && !gv.voiceCooldown && gv.mileStones >= (gv.isForecast("gvroads") ? 1
        : 3) && !gv.isGoingBack && !gv.isFishing && !gv.isTrading && gv.health && gv.questName
        !~ " \\((?:выполнено|отменено)\\)" && gv.godpower >= 5
    """)
    ]]]
.. list-table::
    :stub-columns: 1
    :widths: 1 50

    * - Описание
      - Гласовый. Срабатывает в поле в перерывах между сражениями с монстрами — тогда, когда можно что-нибудь погласить.
    * - Заголовок
      - ``Бой окончен``
    * - Выражение
      - ``!gv.currentMonster && !gv.voiceCooldown && gv.mileStones >= (gv.isForecast("gvroads") ? 1 : 3) && !gv.isGoingBack && !gv.isFishing && !gv.isTrading && gv.health && gv.questName !~ " \\((?:выполнено|отменено)\\)" && gv.godpower >= 5``
.. [[[end]]] (checksum: f23da20501a611593d4f7c19794f992d)
