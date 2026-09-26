# PDF Tools for Windows

Небольшие программы для работы с PDF в Windows.

## Возможности

- объединение нескольких PDF и изображений в один PDF;
- естественная сортировка файлов по имени;
- разделение PDF на отдельные страницы;
- сохранение страниц в PDF или JPG;
- сборка в самостоятельные `.exe`-файлы.

## Запуск из исходников

Требуется Python 3.10 или новее.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Объединение файлов:

```powershell
python merge_pdf.py файл1.pdf файл2.pdf изображение.jpg
```

Разделение PDF:

```powershell
python split_pdf.py документ.pdf
```

Для сохранения страниц в JPG нужен Poppler. Его можно положить в папку
`poppler\Library\bin` рядом со скриптом или добавить в `PATH`.

## Сборка для Windows

Без встроенного Poppler:

```powershell
.\build_windows.ps1
```

Со встроенным Poppler:

```powershell
.\build_windows.ps1 -PopplerPath "C:\путь\к\poppler"
```

Готовые файлы появятся в папке `dist`:

- `merge_pdf.exe`
- `split_pdf.exe`

Папки `.venv`, `build`, `dist` и временные файлы не публикуются в GitHub.
