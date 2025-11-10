from __future__ import annotations
from PySide6.QtCore import QObject, Signal, Slot, Property, QTimer

class Backend(QObject):
    
    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)
        