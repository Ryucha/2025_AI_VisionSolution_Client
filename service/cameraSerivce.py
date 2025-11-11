from PySide6.QtCore import QObject, Slot, Signal, QTimer
from PySide6.QtGui import QImage
import numpy as np
from utils.camera import Camera


class CameraService(QObject):
    previewUpdatedSignal = Signal(object)

    def __init__(self):
        super().__init__()

        Camera()
        Camera().capture_callback.connect(self.camera_image_callback)
        Camera().startStream()

        self.preview_timer = QTimer(self)
        self.preview_timer.timeout.connect(self.emit_preview_update)
        self.preview_timer.start(33)

    @Slot(object)
    def camera_image_callback(self, image):
        self.capture_image = np.copy(image)

    def emit_preview_update(self):
        if hasattr(self, "capture_image"):
            q_image = QImage(
                self.capture_image.data,
                self.capture_image.shape[1],
                self.capture_image.shape[0],
                QImage.Format_Grayscale8,
            )

            self.previewUpdatedSignal.emit(q_image)
