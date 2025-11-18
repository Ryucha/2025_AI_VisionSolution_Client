from PySide6.QtCore import QObject, Slot, Property, Signal
from service import AIService
from provider.cameraImageProvider import CameraImageProvider
import os
import utils.aiParser as AIParser


class AIViewModel(QObject):
    selectedFileChanged = Signal()
    onDetectedObjects = Signal(object)

    def __init__(self, service: AIService, camera_image_provider: CameraImageProvider):
        super().__init__()

        self._service = service
        self._camera_image_provider = camera_image_provider
        self._service.selectedFileChanged.connect(self.selectedFileChanged)
        
        
        self._detect_objects = []

    @Property(str, notify=selectedFileChanged)
    def selectedFile(self):
        return self._service.get_selected_file_path()

    @Property(str, notify=selectedFileChanged)
    def selectedAITypeFile(self):
        return self._service.get_selected_ai_type_file_path()

    @Property(object, notify=onDetectedObjects)
    def detectedObjectsRects(self):
        return self._detect_objects
    
    @Slot(str)
    def loadAIModel(self, file_url: str):
        self._service.set_selected_ai_file_path(file_url)
        self._service.save_ai_model()

    @Slot(str)
    def loadAITypeModel(self, file_url: str):
        self._service.set_selected_ai_type_file_path(file_url)
        self._service.save_ai_model()
        
    @Slot(float, float)
    def view_size_update(self, width: float, height: float):
        self._view_width = width
        self._view_height = height

    @Slot()
    def detect_object(self):
        print("AIViewModel - detect_object called")
        image = self._camera_image_provider.image.copy()
        self._image_width = image.width()
        self._image_height = image.height()
        
        result, labels = self._service.detect_objects(image)
        
        results = AIParser.yolo_result_parser(result, labels)
        
        print("AIViewModel - Detection Results:")
        print(results)
        self.detect_objects.clear()
        for res in results:
            pass