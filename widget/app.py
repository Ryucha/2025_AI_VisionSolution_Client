import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from .backend import Backend
import resources_rc

class App:
    def __init__(self) -> None:
        self.qt_app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        
        self.backend = Backend()
        self.engine.rootContext().setContextProperty("backend", self.backend)

        self.engine.load(QUrl("qrc:/qml/Main.qml"))
        
    def run(self) -> int:
        return self.qt_app.exec()