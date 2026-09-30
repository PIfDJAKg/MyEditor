from PyQt6.Qsci import *
from PyQt6.QtGui import QFont, QColor, QFontDatabase
from pathlib import Path


class Editor(QsciScintilla):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.editorFont = QFont("consolas", 12) # Зададим базовый размер

        self.lexer = QsciLexerPython()
        self.lexer.setDefaultFont(self.editorFont)

        self.setText(
            "class MyClass:\n"
            "    def __init__(self):\n"
            "        self.active = True\n\n"
            "    def check_data(self, data):\n"
            "        if not data or len(data) == 0:\n"
            "            print('Пусто!')\n"
            "            return False\n"
            "        \n"
            "        count = int(data[0])\n"
            "        return True"
        )

        self.setLexer(self.lexer)
        self.setUtf8(True)
        
        self.setMarginType(0, QsciScintilla.MarginType.NumberMargin)
        self.setMarginWidth(0, "0000")
        self.setIndentationsUseTabs(False)
        self.setTabWidth(4)
        self.setIndentationWidth(4)
        self.setAutoIndent(True)  

        self.configure_colors()

    def set_custom_font(self, path:str) -> None:
        font_id = QFontDatabase.addApplicationFont(path)

        if font_id == -1:
            print(f"Ошибка: не удалось загрузить файл шрифта \"{path}\"")
            font_family = "Consolas"
        else:
            font_families = QFontDatabase.applicationFontFamilies(font_id)
            font_family = font_families[0]

        custom_font = QFont(font_family, 14)
        self.lexer.setFont(custom_font)

    def configure_colors(self):
        # Палитра из QDarkStyleSheet
        BG_COLOR = QColor("#19232D")       # Главный фон
        TEXT_COLOR = QColor("#F0F0F0")     # Главный текст
        MARGIN_BG = QColor("#232E3A")      # Фон панели номеров строк
        MARGIN_FG = QColor("#788D9C")      # Цвет самих номеров строк
        CARET_BG = QColor("#2C3B4D")       # Цвет подсветки текущей строки

        self.SendScintilla(QsciScintilla.SCI_STYLESETBACK, 32, BG_COLOR)
        self.SendScintilla(QsciScintilla.SCI_STYLESETFORE, 32, TEXT_COLOR)
        
        self.lexer.setDefaultPaper(BG_COLOR)
        self.lexer.setDefaultColor(TEXT_COLOR)

        for style_id in range(128):
            self.lexer.setPaper(BG_COLOR, style_id)

        self.SendScintilla(QsciScintilla.SCI_STYLECLEARALL)


        self.setCaretLineBackgroundColor(CARET_BG)
        self.setCaretLineVisible(True)
        self.setCaretForegroundColor(TEXT_COLOR)

        self.setMarginBackgroundColor(0, MARGIN_BG)

        self.SendScintilla(QsciScintilla.SCI_STYLESETFORE, 33, MARGIN_FG)


        self.lexer.setColor(QColor("#1EA8FC"), QsciLexerPython.Keyword)
        self.lexer.setFont(QFont("Consolas", 12, QFont.Weight.Bold), QsciLexerPython.Keyword)

        self.lexer.setColor(QColor("#546E7A"), QsciLexerPython.Comment)

        self.lexer.setColor(QColor("#FFB65C"), QsciLexerPython.SingleQuotedString)
        self.lexer.setColor(QColor("#FFB65C"), QsciLexerPython.DoubleQuotedString)

        self.lexer.setColor(QColor("#FF5370"), QsciLexerPython.Number)

        self.lexer.setColor(QColor("#C3E88D"), QsciLexerPython.ClassName)
        self.lexer.setColor(QColor("#C3E88D"), QsciLexerPython.FunctionMethodName)
        
        self.lexer.setColor(QColor("#C792EA"), QsciLexerPython.Decorator)