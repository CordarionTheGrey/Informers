# CSS для подземных карт

По моему скромному мнению, расцветка карты подземелий, оставшаяся еще от оригинального Godville UI+,
вырвиглазна до невозможности. С теми, кому она тоже доставляет неудобства, хочу поделиться
альтернативной, которая не так выбивается из стиля чистого Годвилля.

<details><summary>Скриншоты</summary>

[![Скриншот 1][pic-1]][log-1][![Скриншот 2][pic-2]][log-2]  
[![Скриншот 3][pic-3]][log-3][![Скриншот 4][pic-4]][log-4]  
[![Скриншот 5][pic-5]][log-5][![Скриншот 6][pic-6]][log-6]

</details>

[log-1]: https://gdvl.tk/duels/log/6fcbe
[log-2]: https://gv.erinome.net/duels/log/cjpte
[log-3]: https://gv.erinome.net/duels/log/fjrnjh4am
[log-4]: https://gv.erinome.net/duels/log/h212fqb0u
[log-5]: https://gdvl.tk/duels/log/28edl
[log-6]: https://gv.erinome.net/duels/log/2xclyluqn
[pic-1]: https://i.imgur.com/32Eqohe.png
[pic-2]: https://i.imgur.com/U2N91J2.png
[pic-3]: https://i.imgur.com/uJkh1Ij.png
[pic-4]: https://i.imgur.com/NKqkR3K.png
[pic-5]: https://i.imgur.com/NFTAIKo.png
[pic-6]: https://i.imgur.com/c00Dp3A.png


## Описание

Вся подсветка разбита на несколько независимых частей: если какие-то не нравятся, просто не берите
их. Скриншоты выше сделаны в режиме «всё включено».

Чтобы «установить», зайдите в «[Настройки UI+][ui-settings]» и вставьте выбранные коды в поле
«Пользовательский CSS» внизу. К сожалению, хроникохранилища не имеют доступа к настройкам Годвилля.
Чтобы в них тоже всё работало, откройте какой-нибудь лог (скрины кликабельны, например), прокрутите
его в самый низ, нажмите кнопку «CSS» и вставьте туда тоже.

*Примечание:* Эта раскраска не работает с ночной темой Годвилля, потому что я не пользуюсь этой
темой. Если кому-то надо&nbsp;— скажите, доделаю.

[ui-settings]: https://godville.net/user/profile#ui_settings


## Код

<details><summary>Дверь</summary>

Помечает клетку входа символом двери вместо буквы «В», которая была на традиционных картах.

```css
/* Дверь (начало). */
body:not(.th_nightly) .map_exit_pos_ru::before,
body:not(.th_nightly) .map_exit_pos_en::before {
    display: none;
}

body:not(.th_nightly) .map_exit_pos_ru,
body:not(.th_nightly) .map_exit_pos_en {
    color: #555;
}
/* Дверь (конец). */
```

</details>
<details><summary>Подсказки</summary>

Перекрашивает стрелки и термометры обратно в чёрный цвет.

```css
/* Подсказки (начало). */
body:not(.th_nightly) .dmc.pointerMarker {
    color: #555;
}
/* Подсказки (конец). */
```

</details>
<details><summary>Зона клада</summary>

Не понимаю, зачем заливать полкарты красным. Следующий код заменяет красные пометки на курсив,
а оранжевые (термодинамика)&nbsp;— на курсив с уменьшенным шрифтом.

```css
/* Зона клада (начало). */
body:not(.th_nightly) .dmc.pointerMatched,
body:not(.th_nightly) .dmc.pointerMatchedThermo,
body:not(.th_nightly) .dmc.map_pos.pointerMatched,
body:not(.th_nightly) .dmc.map_pos.pointerMatchedThermo {
    color: #555;
}

.dmc.pointerMatched,
.dmc.pointerMatchedThermo {
    font-style: italic;
}

.dmc.pointerMatchedThermo:not(.map_pos) {
    font-size: 0.7em;
}
/* Зона клада (конец). */
```

</details>
<details><summary>Точки</summary>

Заменяет вопросики, в которых гарантированно нет стенок, точками (особенно удобно при просмотре
чужих логов и живых трансляций). В зоне клада ставятся курсивные проколотые точки. В неточной зоне
(термодинамика)&nbsp;— маленькие точки.

```css
/* Точки (начало). */
body:not(.th_nightly) .dmc.notAWall {
    color: transparent;
}

body:not(.th_nightly) .dmc.notAWall::before {
    display: block;
    text-align: center;
    font-weight: bold;
    color: #7E7E7E;
    content: "•";
}

body:not(.th_nightly) .dmc.notAWall.pointerMatched::before {
    font-weight: normal;
    color: #555;
    content: "⚬";
}

body:not(.th_nightly) .dmc.notAWall.pointerMatchedThermo::before {
    font-size: 1em;
    font-style: normal;
    color: #111;
    content: "·";
}
/* Точки (конец). */
```

Если вы хотите размечать зону клада красным/оранжевым цветом, **вместо** кода выше возьмите этот.

```css
/* Цветные точки (начало). */
.dmc.notAWall::before {
    display: block;
    text-align: center;
    font-weight: bold;
    content: "•";
}

.dmc.notAWall:not(.pointerMatched):not(.pointerMatchedThermo)::before {
    color: #7E7E7E;
}
/* Цветные точки (конец). */
```

</details>
<details><summary>Сокровищница</summary>

При входе в сокровищницу красит значок золотисто-оранжевым.

```css
/* Сокровищница (начало). */
.dmc.treasureChest {
    color: #BF8500 !important;
}

.dmc.treasureChest:not(.dmh) {
    background: none;
}

.dmc.treasureChest:not(.dmh).dmv {
    background: rgba(25, 155, 220, 0.07);
}

.dmc.treasureChest:not(.dmh).dmv:hover {
    background: rgba(25, 155, 220, 0.2);
}
/* Сокровищница (конец). */
```

</details>
<details><summary>Ярлычки</summary>

Как оказалось, я не воспринимаю целиком закрашенные клетки как проходимые. Поэтому уголки. Пробовал
пару других форм (полоски по краям, цветной кружок в центре)&nbsp;— неудобно.

Первые пару дней было трудно определять, какой уголок к какой клетке относится (особенно если их
несколько рядом), потом освоился.

```css
/* Ярлычки (начало). */
body:not(.th_nightly) .dmc:not(.dmh).vault {
    background: linear-gradient(225deg, #00BDA6 18%, transparent 20%, transparent 80%, #00BDA6 82%);
    color: #008675;
}

body:not(.th_nightly) .dmc:not(.dmh).boss {
    background: linear-gradient(225deg, transparent 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).boss.dmv {
    background: linear-gradient(225deg, rgba(25, 155, 220, 0.07) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).boss.dmv:hover {
    background: linear-gradient(225deg, rgba(25, 155, 220, 0.2) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).boss.bonusGodpower {
    background: linear-gradient(225deg, #58BCE2 18%, transparent 20%, transparent 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).boss.bonusGodpower.dmv {
    background: linear-gradient(225deg, #58BCE2 18%, rgba(25, 155, 220, 0.07) 20%, rgba(25, 155, 220, 0.07) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).boss.bonusGodpower.dmv:hover {
    background: linear-gradient(225deg, #58BCE2 18%, rgba(25, 155, 220, 0.2) 20%, rgba(25, 155, 220, 0.2) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).boss.bonusHealth {
    background: linear-gradient(225deg, #18CE18 18%, transparent 20%, transparent 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).boss.bonusHealth.dmv {
    background: linear-gradient(225deg, #18CE18 18%, rgba(25, 155, 220, 0.07) 20%, rgba(25, 155, 220, 0.07) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).boss.bonusHealth.dmv:hover {
    background: linear-gradient(225deg, #18CE18 18%, rgba(25, 155, 220, 0.2) 20%, rgba(25, 155, 220, 0.2) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).boss.trapLowDamage {
    background: linear-gradient(225deg, #FF8282 18%, transparent 20%, transparent 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).boss.trapLowDamage.dmv {
    background: linear-gradient(225deg, #FF8282 18%, rgba(25, 155, 220, 0.07) 20%, rgba(25, 155, 220, 0.07) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).boss.trapLowDamage.dmv:hover {
    background: linear-gradient(225deg, #FF8282 18%, rgba(25, 155, 220, 0.2) 20%, rgba(25, 155, 220, 0.2) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bonusGodpower {
    background: linear-gradient(225deg, #58BCE2 18%, transparent 20%);
}

body:not(.th_nightly) .dmc:not(.dmh).bonusGodpower.dmv {
    background: linear-gradient(225deg, #58BCE2 18%, rgba(25, 155, 220, 0.07) 20%);
}

body:not(.th_nightly) .dmc:not(.dmh).bonusGodpower.dmv:hover {
    background: linear-gradient(225deg, #58BCE2 18%, rgba(25, 155, 220, 0.2) 20%);
}

body:not(.th_nightly) .dmc:not(.dmh).bonusHealth {
    background: linear-gradient(225deg, #18CE18 18%, transparent 20%);
}

body:not(.th_nightly) .dmc:not(.dmh).bonusHealth.dmv {
    background: linear-gradient(225deg, #18CE18 18%, rgba(25, 155, 220, 0.07) 20%);
}

body:not(.th_nightly) .dmc:not(.dmh).bonusHealth.dmv:hover {
    background: linear-gradient(225deg, #18CE18 18%, rgba(25, 155, 220, 0.2) 20%);
}

body:not(.th_nightly) .dmc:not(.dmh).trapUnknown {
    background: transparent;
}

body:not(.th_nightly) .dmc:not(.dmh).trapUnknown.dmv {
    background: rgba(25, 155, 220, 0.07);
}

body:not(.th_nightly) .dmc:not(.dmh).trapUnknown.dmv:hover {
    background: rgba(25, 155, 220, 0.2);
}

body:not(.th_nightly) .dmc:not(.dmh).trapMoveLoss {
    background: linear-gradient(225deg, #888888 18%, transparent 20%);
}

body:not(.th_nightly) .dmc:not(.dmh).trapMoveLoss.dmv {
    background: linear-gradient(225deg, #888888 18%, rgba(25, 155, 220, 0.07) 20%);
}

body:not(.th_nightly) .dmc:not(.dmh).trapMoveLoss.dmv:hover {
    background: linear-gradient(225deg, #888888 18%, rgba(25, 155, 220, 0.2) 20%);
}

body:not(.th_nightly) .dmc:not(.dmh).trapGold,
body:not(.th_nightly) .dmc:not(.dmh).trapTrophy {
    background: linear-gradient(225deg, #C8CE83 18%, transparent 20%);
}

body:not(.th_nightly) .dmc:not(.dmh).trapGold.dmv,
body:not(.th_nightly) .dmc:not(.dmh).trapTrophy.dmv {
    background: linear-gradient(225deg, #C8CE83 18%, rgba(25, 155, 220, 0.07) 20%);
}

body:not(.th_nightly) .dmc:not(.dmh).trapGold.dmv:hover,
body:not(.th_nightly) .dmc:not(.dmh).trapTrophy.dmv:hover {
    background: linear-gradient(225deg, #C8CE83 18%, rgba(25, 155, 220, 0.2) 20%);
}

body:not(.th_nightly) .dmc:not(.dmh).trapLowDamage,
body:not(.th_nightly) .dmc:not(.dmh).trapModerateDamage {
    background: linear-gradient(225deg, #FF8282 18%, transparent 20%);
}

body:not(.th_nightly) .dmc:not(.dmh).trapLowDamage.dmv,
body:not(.th_nightly) .dmc:not(.dmh).trapModerateDamage.dmv {
    background: linear-gradient(225deg, #FF8282 18%, rgba(25, 155, 220, 0.07) 20%);
}

body:not(.th_nightly) .dmc:not(.dmh).trapLowDamage.dmv:hover,
body:not(.th_nightly) .dmc:not(.dmh).trapModerateDamage.dmv:hover {
    background: linear-gradient(225deg, #FF8282 18%, rgba(25, 155, 220, 0.2) 20%);
}

body:not(.th_nightly) .dmc:not(.dmh).trapModerateDamage.trapTrophy {
    background: linear-gradient(225deg, #FF8282 18%, transparent 20%, transparent 80%, #C8CE83 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).trapModerateDamage.trapTrophy.dmv {
    background: linear-gradient(225deg, #FF8282 18%, rgba(25, 155, 220, 0.07) 20%, rgba(25, 155, 220, 0.07) 80%, #C8CE83 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).trapModerateDamage.trapTrophy.dmv:hover {
    background: linear-gradient(225deg, #FF8282 18%, rgba(25, 155, 220, 0.2) 20%, rgba(25, 155, 220, 0.2) 80%, #C8CE83 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint {
    background: linear-gradient(225deg, transparent 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.dmv {
    background: linear-gradient(225deg, rgba(25, 155, 220, 0.07) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.dmv:hover {
    background: linear-gradient(225deg, rgba(25, 155, 220, 0.2) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.bonusGodpower {
    background: linear-gradient(225deg, #58BCE2 18%, transparent 20%, transparent 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.bonusGodpower.dmv {
    background: linear-gradient(225deg, #58BCE2 18%, rgba(25, 155, 220, 0.07) 20%, rgba(25, 155, 220, 0.07) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.bonusGodpower.dmv:hover {
    background: linear-gradient(225deg, #58BCE2 18%, rgba(25, 155, 220, 0.2) 20%, rgba(25, 155, 220, 0.2) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.bonusHealth {
    background: linear-gradient(225deg, #18CE18 18%, transparent 20%, transparent 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.bonusHealth.dmv {
    background: linear-gradient(225deg, #18CE18 18%, rgba(25, 155, 220, 0.07) 20%, rgba(25, 155, 220, 0.07) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.bonusHealth.dmv:hover {
    background: linear-gradient(225deg, #18CE18 18%, rgba(25, 155, 220, 0.2) 20%, rgba(25, 155, 220, 0.2) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapUnknown {
    background: linear-gradient(225deg, transparent 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapUnknown.dmv {
    background: linear-gradient(225deg, rgba(25, 155, 220, 0.07) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapUnknown.dmv:hover {
    background: linear-gradient(225deg, rgba(25, 155, 220, 0.2) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapMoveLoss {
    background: linear-gradient(225deg, #888888 18%, transparent 20%, transparent 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapMoveLoss.dmv {
    background: linear-gradient(225deg, #888888 18%, rgba(25, 155, 220, 0.07) 20%, rgba(25, 155, 220, 0.07) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapMoveLoss.dmv:hover {
    background: linear-gradient(225deg, #888888 18%, rgba(25, 155, 220, 0.2) 20%, rgba(25, 155, 220, 0.2) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapGold,
body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapTrophy {
    background: linear-gradient(225deg, #C8CE83 18%, transparent 20%, transparent 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapGold.dmv,
body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapTrophy.dmv {
    background: linear-gradient(225deg, #C8CE83 18%, rgba(25, 155, 220, 0.07) 20%, rgba(25, 155, 220, 0.07) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapGold.dmv:hover,
body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapTrophy.dmv:hover {
    background: linear-gradient(225deg, #C8CE83 18%, rgba(25, 155, 220, 0.2) 20%, rgba(25, 155, 220, 0.2) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapLowDamage,
body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapModerateDamage {
    background: linear-gradient(225deg, #FF8282 18%, transparent 20%, transparent 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapLowDamage.dmv,
body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapModerateDamage.dmv {
    background: linear-gradient(225deg, #FF8282 18%, rgba(25, 155, 220, 0.07) 20%, rgba(25, 155, 220, 0.07) 80%, #FDBB25 82%);
}

body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapLowDamage.dmv:hover,
body:not(.th_nightly) .dmc:not(.dmh).bossHint.trapModerateDamage.dmv:hover {
    background: linear-gradient(225deg, #FF8282 18%, rgba(25, 155, 220, 0.2) 20%, rgba(25, 155, 220, 0.2) 80%, #FDBB25 82%);
}
/* Ярлычки (конец). */
```

Да, я знаю, о чём вы думаете. Нет, лишнего здесь нет, всё нужное.

На самом деле ярлыки&nbsp;— это диагональный градиент, ага.

</details>
<details><summary>Без раскраски в Творительной</summary>

В Творительной нет разнотипных ловушек и не нужно подсвечивать предупреждения о боссе по соседству.
Там нет необходимости красить вообще что-либо.

```css
/* Отмена раскраски в Творительной (начало). */
body:not(.th_nightly) .dmc.masterBossForge,
body:not(.th_nightly) .dmc.lesserBossForge,
body:not(.th_nightly) .dmc.trapForge,
body.th_nightly .dmc.masterBossForge,
body.th_nightly .dmc.lesserBossForge,
body.th_nightly .dmc.trapForge {
    background: transparent;
}

body:not(.th_nightly) .dmc.dmp,
body.th_nightly .dmc.dmp {
    background: rgba(25, 155, 220, 0.2);
}
/* Отмена раскраски в Творительной (конец). */
```

</details>
