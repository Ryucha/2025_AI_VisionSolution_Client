import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType

from viewModel import *
from provider.cameraImageProvider import CameraImageProvider
from provider.rectPainter import RectPainter
from service import *
from repository import *
import resources_rc


class App:
    def __init__(self) -> None:
        self.qt_app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        
        ##Register Components
        qmlRegisterType(RectPainter, "widgets", 1, 0, "RectPainter")

        ##Repository
        self.ai_path_repository = AIPathRepository()

        ## Providers
        self.camera_image_provider = CameraImageProvider()

        ## Services
        self.ai_service = AIService(ai_path_repository=self.ai_path_repository)
        self.camera_service = CameraService()
        self.file_image_service = FileImageService()

        ## ViewModels
        self.ai_view_model = AIViewModel(
            service=self.ai_service, camera_image_provider=self.camera_image_provider
        )

        self.camera_view_model = CameraViewModel(
            provider=self.camera_image_provider,
            camera_service=self.camera_service,
            file_image_service=self.file_image_service,
        )

        self.engine.addImageProvider("camera", self.camera_image_provider)
        self.engine.rootContext().setContextProperty("aiVM", self.ai_view_model)
        self.engine.rootContext().setContextProperty("cameraVM", self.camera_view_model)

        self.engine.load(QUrl("qrc:/qml/Main.qml"))

    def run(self) -> int:
        return self.qt_app.exec()
