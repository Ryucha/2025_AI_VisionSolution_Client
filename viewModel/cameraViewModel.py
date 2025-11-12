from PySide6.QtCore import QObject, Slot, Property, Signal, QTimer
from provider.cameraImageProvider import CameraImageProvider
from service import CameraService


class CameraViewModel(QObject):
    previewChanged = Signal()
    toggleChanged = Signal()

    def __init__(self, provider: CameraImageProvider, service: CameraService):
        super().__init__()

        self.count = 0
        self._provider = provider
        self._service = service

        ## 시그널 슬롯 장착
        self._service.previewUpdatedSignal.connect(self.updatePreview)
        self._service.isLiveChanged.connect(self.toggleChanged)

    @Property(str, notify=previewChanged)
    def previewImage(self):
        self.count += 1
        return "image://camera/" + str(self.count)
    
    @Property(bool, notify=toggleChanged)
    def isLive(self):
        return self._service.get_is_live()

    @Slot(object)
    def updatePreview(self, image):
        self._provider.image = image.copy()
        self.previewChanged.emit()
        
    @Slot(bool)
    def live_toogle_changed(self, checked: bool):
        print("CameraViewModel - live_toogle_changed : ", checked)
        self._service.set_is_live(checked)
        self.toggleChanged.emit()
        
        
