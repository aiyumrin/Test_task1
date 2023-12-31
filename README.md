# Оценка статистической значимости признаков при определении моделью количества углов комнат

## Описание данных

- **mean, max, min** - среднее, максимум и минимум углов отклонения между полом и потолком;
- **floor_mean, floor_max, floor_min** - среднее, максимум и минимум углов отклонения между полом и опорной плоскостью;
- **ceiling_mean, ceiling_max, ceiling_min** - среднее, максимум и минимум углов отклонения между потолком и опорной плоскостью;
- **Gt_corners** - истинное количество углов в комнате;
- **Rb_corners** - количество углов, найденных моделью;

\* *(Значения углов отклонения представлены в градусах)*

## Постановка задачи

Необходимо оценить статистическую значимость признаков при определении моделью количества углов в комнате.

## Требования к выполнению

- Создать проект в idea, pycharm или vscode;
- Создать файл requirements.txt и виртуальную среду;
- Создать класс для рисования графиков;
- Создать функцию «draw_plots» которая:
  - читает json-файл, переданный в качестве параметра, как DataFrame pandas
  - рисует график для сравнения разных столбцов
  - сохраняет графики в папке под названием «plots»
  - возвращает пути ко всем графикам
- Создать блокнот jupyter с именем Notebook.ipynb в корневом каталоге для вызова и визуализации графиков;
- Опубликовать проект на github.
