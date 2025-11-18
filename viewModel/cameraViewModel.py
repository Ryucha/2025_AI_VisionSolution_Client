from PySide6.QtCore import QObject, Slot, Property, Signal, QTimer
from provider.cameraImageProvider import CameraImageProvider
from service import *


class CameraViewModel(QObject):
    previewChanged = Signal()
    toggleChanged = Signal()
    openImageDialog = Signal()

    def __init__(
        self,
        provider: CameraImageProvider,
        camera_service: CameraService,
        file_image_service: FileImageService,
    ):
        super().__init__()

        self.count = 0
        self._provider = provider
        self._camera_service = camera_service
        self._file_image_service = file_image_service
        self.image_path = None

        ## 시그널 슬롯 장착
        self._camera_service.previewUpdatedSignal.connect(self.updatePreview)
        self._camera_service.isLiveChanged.connect(self.toggleChanged)
        self._file_image_service.imageLoadedSignal.connect(self.updateFileImage)

    @Property(str, notify=previewChanged)
    def previewImage(self):
        self.count += 1
        return "image://camera/" + str(self.count)

    @Property(bool, notify=toggleChanged)
    def isLive(self):
        return self._camera_service.get_is_live()

    @Slot(object)
    def updatePreview(self, image):
        if self.isLive:
            self._provider.image = image.copy()
            self.previewChanged.emit()

    @Slot(bool)
    def live_toogle_changed(self, checked: bool):
        print("CameraViewModel - live_toogle_changed : ", checked)
        self._camera_service.set_is_live(checked)
        self.toggleChanged.emit()

    @Slot()
    def click_camera_image(self):
        if not self.isLive:
            print("CameraViewModel - click_camera_image")
            self.openImageDialog.emit()

    @Slot(str)
    def load_image(self, file_url: str):
        print("CameraViewModel - load_image : ", file_url)
        self.image_path = file_url
        self._file_image_service.load_image_from_file(file_url)

    @Slot(object)
    def updateFileImage(self, image):
        print("CameraViewModel - updateFileImage Slot called")
        self._provider.image = image.copy()
        self.previewChanged.emit()
