from PyQt6.QtWidgets import QFileDialog
from ui.editor import Editor
from charset_normalizer import from_bytes


class Manager:
    def __init__(self):
        super().__init__()
        self.last_file_path: str = ""

    def _save_file(self, text: str, path: str) -> None:
        try:
            with open(self.last_file_path, "w", encoding='utf-8', errors='ignore') as save_file:
                save_file.write(text)
        except PermissionError:
            print("Нет полномочий для изменения файла")

    def save(self, text: str):
        if self.last_file_path == "":
            self.save_as(text)
            return

        self._save_file(text, self.last_file_path)

    def save_as(self, text: str) -> None:
        file = QFileDialog.getSaveFileName(
            parent = None,
            caption = "Сохранить как",
            directory = "c:\\",
            filter = "All (*)",
        )
        fileName = file[0]

        if fileName:
            self._save_file(text, fileName)
            self.last_file_path = fileName

    def open_file(self, editor:Editor):
        file = QFileDialog.getOpenFileName(
            parent = None,
            caption = "Открыть файл",
            directory = "c:\\",
            filter = "All (*)"
        )
        file_path: str = file[0]

        if file_path:
            text: str = self.open(file_path)
            editor.setText(text)

    def open(self, path:str) -> str:
        file_encoding: str = self._get_encoding(path)
        with open(path, "r", encoding=file_encoding, errors="ignore") as open_file:
            print(f"open: {path}")
            text = open_file.read()
            self.last_file_path = path
            return text

    def new_file(self, editor:Editor) -> None:
        self.last_file_path = ""
        editor.setText("")

    def open_folder(self) -> str:
        folder = QFileDialog.getExistingDirectory(
            parent = None,
            caption = "Открыть папку",
            directory = "C:\\"
        )

        if folder:
            return folder
        return "C:\\"

    def _get_encoding(self, path:str) -> str:
        with open(path, "rb") as open_file:
            byte_data = open_file.read(6000)
            result = from_bytes(byte_data)
            best_match = result.best()

            if best_match:
                return best_match.encoding

            return "utf-8"