# объединить_в_один_PDF.py
import sys
from pathlib import Path
from PIL import Image
from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import messagebox, simpledialog
import re

def natural_sort_key(s):
    """Естественная сортировка для имен файлов (img1, img2, img10)"""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', str(s))]

def combine_to_pdf(file_paths):
    temp_pdfs = []

    # сортировка файлов по естественному порядку
    file_paths.sort(key=natural_sort_key)

    for path_str in file_paths:
        path = Path(path_str)
        if not path.exists():
            continue

        ext = path.suffix.lower()

        if ext in [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif"]:
            im = Image.open(path).convert("RGB")
            temp_pdf = path.with_suffix(".temp.pdf")
            im.save(temp_pdf)
            temp_pdfs.append(temp_pdf)

        elif ext == ".pdf":
            temp_pdfs.append(path)

    if not temp_pdfs:
        tk.Tk().withdraw()
        messagebox.showerror("Ошибка", "Нет подходящих файлов для объединения (jpg/png/pdf).")
        return

    # --- Запрос имени итогового PDF ---
    root = tk.Tk()
    root.withdraw()
    output_name = simpledialog.askstring(
        "Сохранить как", 
        "Введите имя итогового PDF файла:",
        initialvalue="Объединенный_файл"
    )

    if not output_name:  # если пользователь отменил или оставил пустое
        messagebox.showinfo("Отмена", "Операция объединения отменена.")
        return

    output_name = output_name.strip()
    if not output_name.lower().endswith(".pdf"):
        output_name += ".pdf"

    output = Path(file_paths[0]).parent / output_name

    # --- Объединение PDF ---
    merger = PdfMerger()
    for pdf in temp_pdfs:
        merger.append(str(pdf))
    merger.write(output)
    merger.close()

    # удалить временные pdf, созданные из изображений
    for pdf in temp_pdfs:
        if pdf.name.endswith(".temp.pdf"):
            pdf.unlink(missing_ok=True)

    messagebox.showinfo("Готово", f"Создан файл:\n{output.name}")

if __name__ == "__main__":
    files = sys.argv[1:]
    if not files:
        tk.Tk().withdraw()
        messagebox.showerror("Ошибка", "Не выбраны файлы.")
        sys.exit(0)

    combine_to_pdf(files)
