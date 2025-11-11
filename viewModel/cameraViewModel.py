from PySide6.QtCore import QObject, Slot, Property, Signal, QTimer
from provider.cameraImageProvider import CameraImageProvider
from service import CameraService


class CameraViewModel(QObject):
    previewChanged = Signal()

    def __init__(self, provider: CameraImageProvider, service: CameraService):
        super().__init__()

        self.count = 0
        self._provider = provider
        self._service = service

        ## 시그널 슬롯 장착
        self._service.previewUpdatedSignal.connect(self.updatePreview)

    @Property(str, notify=previewChanged)
    def previewImage(self):
        self.count += 1
        return "image://camera/" + str(self.count)

    @Slot(object)
    def updatePreview(self, image):
        self._provider.image = image.copy()
        self.previewChanged.emit()
