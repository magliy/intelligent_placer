## Постановка задачи
Имеется фотография с нарисованным многоугольником и каким-то количеством объектов. Требуется по фотографии определить поместятся ли предметы в имеющуюся фигуру. Предметы помещаются, если их можно расположить таким образом, чтобы никакая часть предметов не выходит за границы многоугольника

## Требования 
* Программа получает на вход путь до изображения со всеми объектами и нарисованным на листе многоугольником 
* Программа должна возвращаться true-в случае, если предметы помещаются в многоугольник. В противном случае - false. 
* Ответ выводится в стандартный поток вывода

### Общие требования
* Многоугольник выпуклый и имеет не более 7 вершин; нарисован темным маркером на белом листе бумаги и сфотографирован вместе с объектами; линии многоугольника имеют примерно одинаковую ширину.
* Все объекты заранее известны. Объекты полностью расположены на фотографии и их части не выходят за края; не перекрывают друг друга частично или полностью; располагаются ровно под листом с многоугольником и не выходят за его края; находятся на одной фотографии единожды, повторения не допускаются.
* Поверхность, на фоне которой делаются фотографии светлая и ровная, без рельефа.
* Объектив камеры должен располагаться перпендикулярно нормали к фотографируемой поверхности. Расстояние до предметов не более 50 сантиметров. Объекты хорошо освещены и имеют четкие границы, фотография не смазанная и без засветов. Фотографии вертикально ориентированы, соотношение сторон 9:16. Фотографии цветные, не допускается цветовая коррекция: наложение фильтров, изменение яркости, контрастности, цветов и тд.

## Изображения
[Исходные данные](https://github.com/magliy/intelligent_placer/tree/develop/Objects/Objects)

## Тесты
[Многоугольник занимает все простанство листа. Представлены все 10 объектов. Все объекты помещаются в многоугольник](https://github.com/magliy/intelligent_placer/blob/develop/Tests/yes%5C1.jpg)

Ответ: true

[Достаточно маленький мнгоугольник. Единственный объект помещается внутрь](https://github.com/magliy/intelligent_placer/blob/develop/Tests/Tests/YuRdUHiVX4.jpeg)

Ответ: true

[Многоугольник имеет максимальное количество углов. Объект помещается только в однои положении с очень маленькой вариабельностью угла](https://github.com/magliy/intelligent_placer/blob/develop/Tests/yes%5C8.jpg)

Ответ: true

[Маленький многоугольник. Не влезает ни один объект](https://github.com/magliy/intelligent_placer/blob/develop/Tests/Tests/7Dyjds5hmAA.jpeg)

Ответ: false

[На первый взгляд кажется, что объекты должны поместиться, но это не так](https://github.com/magliy/intelligent_placer/blob/develop/Tests/Tests/MCveEMRm7q8.jpeg)

Ответ: false

[В отдельных конфигурациях объекты влезают в многоульник, но не все вместе](https://github.com/magliy/intelligent_placer/blob/develop/Tests/Tests/G4T7Ge8sxMk.jpeg)

Ответ: false

