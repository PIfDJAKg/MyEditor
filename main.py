import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QSplitter,
)
from PyQt6.QtCore import Qt, QModelIndex
from PyQt6.QtGui import QFileSystemModel
import qdarkstyle

from ui.editor import Editor
from ui.file_tree import FileTree
from ui.menu_bar import MenuBar
from core.file_manager import Manager


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IDE")
        self.resize(1080, 720)
        self.setMinimumSize(1080, 720)

        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.setCentralWidget(self.splitter)

        self.editor = Editor(self)

        self.file_tree = FileTree(self)
        self.file_tree.doubleClicked.connect(self.open_file_in_tree)
        self.file_tree.setMaximumWidth(int((self.size().width() / 10) * 3))

        self.splitter.addWidget(self.file_tree)
        self.splitter.addWidget(self.editor)

        self.file_manager = Manager()
        self.connect_menu_bar()

    def connect_menu_bar(self) -> None:
        self.menu_bar.save_as_action.triggered.connect(
            lambda save_as: self.file_manager.save_as(self.editor.text())
        )
        self.menu_bar.open_folder_action.triggered.connect(
            lambda open_foulder: self.file_tree.set_path(self.file_manager.open_folder())
        )
        self.menu_bar.save_action.triggered.connect(
            lambda save: self.file_manager.save(self.editor.text())
        )
        self.menu_bar.open_file_action.triggered.connect(
            lambda open_file: self.file_manager.open_file(self.editor)
        )
        self.menu_bar.new_file_action.triggered.connect(
            lambda new_file: self.file_manager.new_file(self.editor)
        )
        self.menu_bar.close_editor_action.triggered.connect(
            self.close
        )

    def resizeEvent(self, event):
        super().resizeEvent(event)

        self.on_resize()

    def on_resize(self):
        self.file_tree.setMaximumWidth(int((self.size().width() / 10) * 2))

    def open_file_in_tree(self, index: QModelIndex) -> None:
        tree_model: QFileSystemModel = self.file_tree.model
        if not tree_model.isDir(index):
            file_path = tree_model.filePath(index)
            text:str = self.file_manager.open(file_path)
            self.editor.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyqt6"))
    ide = Main()
    ide.show()
    sys.exit(app.exec())