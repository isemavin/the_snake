# the snake
---
Snake («Питон», «Удав», «Червяк») - компьютерная игра, в которой игрок управляет «головой» растущей линии («змеи»). Первые подобные игры возникли в 1970-х годах. Цель игры съесть как можно больше яблок, появляющихся на экране. Каждый раз, когда змея съедает яблоко, она становится длиннее, что усложняет дальнейший процесс игры. Змея при этом должна избегать столкновений с собственным телом.

---

### Game Features:
* Игрок управляет телом змеи, состоящей изначально из 1 части (головы), с клавиатуры при помощи стрелок: ←Влево, →Вправо, ↑Вверх, ↓Вниз.
* Змейка собирает яблоки на экране, которые появляются случайно. Благодаря этому змейка увеличивается в размерах. 
* Змейка "разбивется" при столкновении со своим "хвостом" и игра начинается с начала. 
---

### How it works:
#### 1. Класс GameObject:
##### Атрибуты:
* __position__ — позиция объекта на игровом поле. 
* __body_color__ — цвет объекта.
##### Методы:
* __init__ — инициализирует базовые атрибуты объекта, такие как его позиция и цвет.
* __draw__ — это абстрактный метод, который предназначен для переопределения в дочерних классах.
#### 2. Класс Apple, наследуется от GameObject:
##### Атрибуты:
* __body_color__ — цвет яблока.
* __position__ — позиция яблока на игровом поле. Яблоко появляется в случайном месте на игровом поле.
##### Методы:
* __init__ — задаёт цвет яблока и устанавливает начальную позицию яблока.
* __randomize_position__ — устанавливает случайное положение яблока на игровом поле — задаёт атрибуту position новое значение. Координаты выбираются так, чтобы яблоко оказалось в пределах игрового поля.
* __draw__ — отрисовывает яблоко на игровой поверхности.
#### 3. Класс Snake, наследуется от GameObject:
##### Атрибуты:
* __length__ — длина змейки. Изначально змейка имеет длину 1.
* __positions__ — список, содержащий позиции всех сегментов тела змейки. Начальная позиция — центр экрана.
* __direction__ — направление движения змейки. По умолчанию змейка движется вправо.
* __next_direction__ — следующее направление движения, которое будет применено после обработки нажатия клавиши.
* __body_color__ — цвет змейки.
##### Методы:
* __init__ — инициализирует начальное состояние змейки.
* __update_direction__ — обновляет направление движения змейки.
* __move__ — обновляет позицию змейки (координаты каждой секции), добавляя новую голову в начало списка __positions__ и удаляя последний элемент, если длина змейки не увеличилась.
* __draw__ — отрисовывает змейку на экране, затирая след 
* __get_head_position__ — возвращает позицию головы змейки (первый элемент в списке __positions__).
* __reset__ — сбрасывает змейку в начальное состояние после столкновения с собой.

#### Функции:
__handle_keys__ — обрабатывает нажатия клавиш, чтобы изменить направление движения змейки.