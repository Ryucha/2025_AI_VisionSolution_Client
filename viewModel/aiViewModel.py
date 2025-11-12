from PySide6.QtCore import QObject, Slot, Property, Signal
from service import AIService
import os


class AIViewModel(QObject):
    selectedFileChanged = Signal()

    def __init__(self, service: AIService):
        super().__init__()

        self._service = service
        # 서비스의 시그널을 ViewModel의 시그널과 연결
        self._service.selectedFileChanged.connect(self.selectedFileChanged)

    @Property(str, notify=selectedFileChanged)
    def selectedFile(self):
        return self._service.get_selected_file_path()
    
    @Property(str, notify=selectedFileChanged)
    def selectedAITypeFile(self):
        return self._service.get_selected_ai_type_file_path()

    @Slot(str)
    def loadAIModel(self, file_url: str):
        self._service.set_selected_ai_file_path(file_url)
        self._service.save_ai_model()
        
    @Slot(str)
    def loadAITypeModel(self, file_url: str):
        self._service.set_selected_ai_type_file_path(file_url)
        self._service.save_ai_model()