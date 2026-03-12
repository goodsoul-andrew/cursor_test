# converter.py

Скрипт `converter.py` принимает путь к текстовому файлу, читает содержимое, преобразует в верхний регистр и записывает результат в новый файл **в той же папке** с суффиксом `_upper`.

## Требования

- Python 3 (подойдёт 3.8+)
- Только стандартная библиотека Python (внешние зависимости не используются)

## Использование

```bash
python3 converter.py /path/to/input.txt
```

После выполнения скрипт создаст файл:

- `/path/to/input.txt_upper`

И выведет путь к созданному файлу в stdout.

## Пример

```bash
echo "Hello, мир!" > sample.txt
python3 converter.py sample.txt
cat sample.txt_upper
```
