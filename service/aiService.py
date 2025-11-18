from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtWidgets import QFileDialog
from repository import AIPathRepository
import os
from ultralytics import YOLO
from PySide6.QtGui import QImage
import numpy as np


class AIService(QObject):
    selectedFileChanged = Signal()

    def __init__(self, ai_path_repository: AIPathRepository):
        super().__init__()
        self._selected_ai_file_path = ""
        self._selected_ai_type_file_path = ""
        self._ai_path_repository = ai_path_repository

        self.yolo_model = None
        self.efficientNet_model = None
        
        self.view_width = None
        self.view_height = None
        self.image_width = None
        self.image_height = None

        self.load_ai_model()

    def save_ai_model(self):
        self._ai_path_repository.save_model_path(
            self._selected_ai_file_path, self._selected_ai_type_file_path
        )

    def load_ai_model(self):
        self._ai_path_repository.load_model_path()
        self.set_selected_ai_file_path(self._ai_path_repository.model_path)
        self.set_selected_ai_type_file_path(self._ai_path_repository.type_model_path)

    def set_selected_ai_type_file_path(self, file_url: str):
        self._selected_ai_type_file_path = file_url
        if file_url.startswith('file:///'):
            file_url = file_url[8:]  # Remove 'file:///' prefix
        elif file_url.startswith('file://'):
            file_url = file_url[7:]  # Remove 'file://' prefix
            
        
        self.selectedFileChanged.emit()

    def set_selected_ai_file_path(self, file_url: str):
        self._selected_ai_file_path = file_url
        if file_url.startswith('file:///'):
            file_url = file_url[8:]  # Remove 'file:///' prefix
        elif file_url.startswith('file://'):
            file_url = file_url[7:]  # Remove 'file://' prefix
        
        self.yolo_model = YOLO(file_url)
        self.selectedFileChanged.emit()

    def set_selected_ai_type_file_path(self, file_url: str):
        self._selected_ai_type_file_path = file_url
        self.selectedFileChanged.emit()

    def get_selected_file_path(self) -> str:
        return (
            os.path.basename(self._selected_ai_file_path)
            if self._selected_ai_file_path
            else ""
        )

    def get_selected_ai_type_file_path(self) -> str:
        return (
            os.path.basename(self._selected_ai_type_file_path)
            if self._selected_ai_type_file_path
            else ""
        )

    def detect_objects(self, image):
        if self.yolo_model is not None:
            # QImage를 NumPy 배열로 변환
            if isinstance(image, QImage):
                image = image.convertToFormat(QImage.Format_RGB888)
                width = image.width()
                height = image.height()
                ptr = image.bits()
                arr = np.array(ptr).reshape(height, width, 3)
            else:
                arr = image

            results = self.yolo_model(arr, conf=0.50)
            return results, self.yolo_model.names
        else:
            print("AIService - YOLO model is not loaded.")
            return None, None
