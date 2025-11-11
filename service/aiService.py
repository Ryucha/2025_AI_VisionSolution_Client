from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtWidgets import QFileDialog
from repository import AIPathRepository
import os


class AIService(QObject):
    selectedFileChanged = Signal()

    def __init__(self, ai_path_repository: AIPathRepository):
        super().__init__()
        self._selected_file_path = ""
        self._ai_path_repository = ai_path_repository
        self.load_ai_model()

    def save_ai_model(self):
        self._ai_path_repository.save_model_path(self._selected_file_path)
        
    def load_ai_model(self):
        self._ai_path_repository.load_model_path()
        self.set_selected_file_path(self._ai_path_repository.model_path)

    def set_selected_file_path(self, file_url: str):
        self._selected_file_path = file_url
        self.selectedFileChanged.emit()

    def get_selected_file_path(self) -> str:
        return (
            os.path.basename(self._selected_file_path)
            if self._selected_file_path
            else ""
        )
