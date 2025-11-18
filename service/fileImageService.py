from PySide6.QtCore import QObject, Signal, Slot, QUrl
from PySide6.QtGui import QImage


class FileImageService(QObject):
    imageLoadedSignal = Signal(object)

    def __init__(self):
        super().__init__()

    @Slot(str)
    def load_image_from_file(self, file_path: str):
        # file:// URL을 로컬 경로로 변환
        if file_path.startswith("file://"):
            file_path = QUrl(file_path).toLocalFile()

        print(f"FileImageService - Loading image from: {file_path}")
        image = QImage(file_path)

        if not image.isNull():
            self.imageLoadedSignal.emit(image)
            print("FileImageService - Image loaded successfully")
        else:
            print("FileImageService - Failed to load image (image is null)")
