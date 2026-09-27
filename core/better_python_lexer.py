import re
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.Qsci import QsciScintilla, QsciLexerPython


class QsciBetterPythonLexer(QsciLexerPython):
    def __init__(self, parent=None):
        super().__init__(parent)

        custom_key