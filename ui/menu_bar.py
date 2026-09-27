from PyQt6.QtWidgets import QMenuBar, QMenu
from PyQt6.QtGui import QAction


class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)

        self.file_menu = self.addMenu("File")

        self.new_file_action = QAction("New file", self)
        self.open_file_action = QAction("Open file", self)
        self.save_action = QAction("Save", self)
        self.save_as_action = QAction("Save as", self)
        self.close_file_action = QAction("Close file", self)
        self.close_editor_action = QAction("Close editor", self)

        self.file_menu.addAction(self.new_file_action)
        self.file_menu.addAction(self.open_file_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.save_as_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.close_file_action)
        self.file_menu.addAction(self.close_editor_action)


        self.edit_menu = self.addMenu("Edit")

        self.copy_action = QAction("Copy", self)
        self.paste_action = QAction("Paste", self)
        self.cut_action = QAction("Cut", self)
        self.undo_action = QAction("Undo", self)
        self.redo_action = QAction("Redo", self)

        self.edit_menu.addAction(self.copy_action)
        self.edit_menu.addAction(self.paste_action)
        self.edit_menu.addAction(self.cut_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.undo_action)
        self.edit_menu.addAction(self.redo_action)


        self.editor_menu = self.addMenu("Editor")

        self.settings_action = QAction("Settings", self)
        self.addons_action = QAction("Addons", self)
        self.highlight_action = QAction("Highlight", self)
        self.restart_action = QAction("Restart", self)
        self.about_action = QAction("About", self)

        self.editor_menu.addAction(self.settings_action)
        self.editor_menu.addAction(self.addons_action)
        self.editor_menu.addAction(self.highlight_action)
        self.editor_menu.addSeparator()
        self.editor_menu.addAction(self.restart_action)
        self.editor_menu.addAction(self.about_action)
