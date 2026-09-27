from PyQt6.QtWidgets import QTreeView
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import QDir


class FileTree(QTreeView):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.model = QFileSystemModel()

        root_path = QDir.currentPath()
        self.model.setRootPath(root_path)

        self.setModel(self.model)

        self.setRootIndex(self.model.index(root_path))

        self.setAnimated(True)
        self.setIndentation(20)
        self.setSortingEnabled(True)
        self.setColumnHidden(1, True)
        self.setColumnHidden(2, True)
        self.setColumnHidden(3, True)