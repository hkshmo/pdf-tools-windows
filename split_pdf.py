import sys
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox
from pdf2image import convert_from_path
from PyPDF2 import PdfReader, PdfWriter
import threading


class PDFSplitterApp(tk.Tk):
    def __init__(self, pdf_file, poppler_dir):
        super().__init__()
        self.title("Разделение PDF")
        self.geometry("400x180")

        # Получаем размер экрана и размер окна
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 400
        window_height = 180

        # Вычисляем координаты для расположения окна в центре экрана
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Устанавливаем координаты окна
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        self.resizable(False, False)

        self.pdf_file = Path(pdf_file)
        self.poppler_dir = Path(poppler_dir)

        # Вставляем лейбл
        self.progress_label = tk.Label(self, text="Выберите формат разделения...")
        self.progress_label.pack(pady=10)

        # Кнопки для выбора формата
        self.split_to_pdf_button = tk.Button(
            self, text="Разделить на PDF", command=self.split_to_pdf
        )
        self.split_to_pdf_button.pack(pady=5, padx=20, fill=tk.X)

        self.split_to_jpg_button = tk.Button(
            self, text="Разделить на JPG", command=self.split_to_jpg
        )
        self.split_to_jpg_button.pack(pady=5, padx=20, fill=tk.X)

        # Прогресс-бар
        self.progress = ttk.Progressbar(
            self, orient="horizontal", length=350, mode="determinate"
        )
        self.progress.pack(pady=10)

        self.after(100, self.start_split)

    def start_split(self):
        """Метод, который вызывается после старта программы"""
        pass  # Будет вызван метод в зависимости от кнопки

    def split_to_pdf(self):
        """Разделить на PDF страницы"""
        threading.Thread(target=self.split_pdf, daemon=True).start()

    def split_to_jpg(self):
        """Разделить на JPG страницы"""
        threading.Thread(target=self.split_jpg, daemon=True).start()

    def split_pdf(self):
        """Разделить PDF на отдельные страницы (PDF)"""
        output_dir = self.pdf_file.parent / self.pdf_file.stem
        output_dir.mkdir(exist_ok=True)

        try:
            reader = PdfReader(str(self.pdf_file))
            total = len(reader.pages)
        except Exception as e:
            self.after(0, lambda: self.show_error(str(e)))
            return

        self.after(0, lambda: self.progress.configure(maximum=total))

        for i, page in enumerate(reader.pages, start=1):
            writer = PdfWriter()
            writer.add_page(page)

            output_file = output_dir / f"{self.pdf_file.stem}_стр{i}.pdf"
            with open(output_file, "wb") as f:
                writer.write(f)

            self.after(0, lambda i=i: self.update_progress(i, total))

        self.after(0, lambda: self.finish(total, output_dir))

    def split_jpg(self):
        """Разделить PDF на изображения (JPG)"""
        output_dir = self.pdf_file.parent / self.pdf_file.stem
        output_dir.mkdir(exist_ok=True)

        try:
            pages = convert_from_path(
                self.pdf_file, dpi=200, poppler_path=str(self.poppler_dir)
            )
        except Exception as e:
            self.after(0, lambda: self.show_error(str(e)))
            return

        total = len(pages)
        self.after(0, lambda: self.progress.configure(maximum=total))

        for i, page in enumerate(pages, start=1):
            output_file = output_dir / f"{self.pdf_file.stem}_стр{i}.jpg"
            page.save(output_file, "JPEG")
            page.close()
            self.after(0, lambda i=i: self.update_progress(i, total))

        self.after(0, lambda: self.finish(total, output_dir))

    def update_progress(self, i, total):
        """Обновить прогресс-бар"""
        self.progress["value"] = i
        self.progress_label["text"] = f"Обработка страницы {i}/{total}"

    def show_error(self, msg):
        """Показать сообщение об ошибке"""
        messagebox.showerror("Ошибка при обработке PDF", msg)
        self.destroy()
        sys.exit(1)

    def finish(self, total, output_dir):
        """Окончание процесса с выводом сообщения"""
        messagebox.showinfo(
            "Готово",
            f"PDF разделён на {total} страниц.\nФайлы сохранены в:\n{output_dir}",
        )
        self.destroy()
        sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Ошибка", "Не выбран PDF-файл.")
        sys.exit(1)

    pdf_file = sys.argv[1]

    # Путь к Poppler (папка poppler рядом с exe)
    if getattr(sys, "_MEIPASS", False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).parent
    poppler_path = base_path / "poppler" / "Library" / "bin"

    app = PDFSplitterApp(pdf_file, poppler_path)
    app.mainloop()
