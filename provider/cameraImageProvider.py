from PySide6.QtQuick import QQuickImageProvider


class CameraImageProvider(QQuickImageProvider):

    def __init__(self):
        super().__init__(QQuickImageProvider.Image)
        self.image = None

    def requestImage(self, id, size, requestedSize):
        if self.image is None:
            return None

        return self.image
