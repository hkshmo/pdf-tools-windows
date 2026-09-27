# PDF Tools for Windows

Небольшие программы для работы с PDF в Windows.

## Скачать готовую программу

Скачайте последнюю версию здесь:

[Скачать PDF Tools for Windows](https://github.com/hkshmo/pdf-tools-windows/releases/latest)

В разделе `Assets` выберите:

- `merge_pdf.exe`
- `split_pdf.exe`

## Установка в меню "Отправить"

После скачивания программы сами не появляются в контекстном меню. Их нужно один
раз положить в постоянную папку и создать ярлыки в меню Windows `Отправить`.

1. Создайте папку:

```text
C:\PDF Tools
```

2. Положите в эту папку оба скачанных файла:

- `merge_pdf.exe`
- `split_pdf.exe`

3. Нажмите `Win + R`.

4. Введите:

```text
shell:sendto
```

5. В открывшейся папке создайте ярлыки на программы:

- ярлык на `C:\PDF Tools\merge_pdf.exe` назовите `Объединить в PDF`;
- ярлык на `C:\PDF Tools\split_pdf.exe` назовите `Разделить PDF`.

После этого пункты появятся в контекстном меню:

```text
Правая кнопка мыши -> Отправить -> Объединить в PDF
Правая кнопка мыши -> Отправить -> Разделить PDF
```

## English quick start

PDF Tools for Windows is a small set of Windows utilities for merging PDF files
and splitting PDF pages into PDF or JPG files.

Download the latest release here:

[Download PDF Tools for Windows](https://github.com/hkshmo/pdf-tools-windows/releases/latest)

From `Assets`, download:

- `merge_pdf.exe`
- `split_pdf.exe`

Create this folder:

```text
C:\PDF Tools
```

Move both `.exe` files into that folder.

To add the tools to the Windows `Send to` menu:

1. Press `Win + R`.
2. Enter:

```text
shell:sendto
```

3. In the opened folder, create shortcuts to:

- `C:\PDF Tools\merge_pdf.exe`
- `C:\PDF Tools\split_pdf.exe`

After that, select your files, right-click them, and use:

```text
Send to -> merge_pdf
Send to -> split_pdf
```

## Как пользоваться

У программ нет главного окна, которое нужно открывать отдельно. Они работают с
файлами, которые вы передаете им из Windows.

Используйте один из способов:

- выделите файлы, нажмите правой кнопкой мыши и выберите `Отправить`;
- перетащите PDF или изображения мышкой прямо на нужный `.exe`-файл.

`merge_pdf.exe` принимает несколько PDF или изображений и объединяет их в один
PDF. `split_pdf.exe` принимает один PDF и разделяет его на отдельные PDF-страницы
или JPG-картинки.

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

Разделение в JPG работает сразу, без дополнительных установок.

## Сборка для Windows

Запустите:

```powershell
.\build_windows.ps1
```

Готовые файлы появятся в папке `dist`:

- `merge_pdf.exe`
- `split_pdf.exe`

## Быстрая проверка

После установки можно выделить файлы, нажать правой кнопкой мыши и выбрать:

```text
Отправить -> Объединить в PDF
```

или:

```text
Отправить -> Разделить PDF
```

Для объединения можно выделить несколько PDF или изображений. Для разделения
нужно отправлять один PDF-файл.

## Участие в разработке

Если хотите улучшить программу, сделайте fork репозитория и отправьте pull
request. Исправления ошибок, предложения и улучшения приветствуются.

Папки `.venv`, `build`, `dist` и временные файлы не публикуются в GitHub.
