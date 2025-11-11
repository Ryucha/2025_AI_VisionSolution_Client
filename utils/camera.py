import gxipy as gx
from PySide6.QtCore import QObject, Signal
import numpy as np


class Camera(QObject):
    _instance = None
    _initialized = False
    capture_callback = Signal(object)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        super().__init__()
        self._initialized = True

        self.device_manager = gx.DeviceManager()
        self.dev_num, self.dev_info_list = self.device_manager.update_device_list()

        if self.dev_num != 0:
            self.cam = self.device_manager.open_device_by_sn(
                self.dev_info_list[0].get("sn")
            )
            self.cam.data_stream[0].register_capture_callback(
                Camera.raw_capture_callback
            )

    def setWidth(self, width):
        value = self.cam.Width.get_range()

        if value["min"] <= width <= value["max"]:
            self.cam.Width.set(int(width / value["inc"]) * value["inc"])
        elif width < value["min"]:
            self.cam.Width.set(value["min"])
        elif width > value["max"]:
            self.cam.Width.set(value["max"])

    def setHeight(self, height):
        value = self.cam.Height.get_range()

        if value["min"] <= height <= value["max"]:
            self.cam.Height.set(int(height / value["inc"]) * value["inc"])
        elif height < value["min"]:
            self.cam.Height.set(value["min"])
        elif height > value["max"]:
            self.cam.Height.set(value["max"])

    def setExposureTime(self, exposure_time):
        value = self.cam.ExposureTime.get_range()

        if value["min"] <= exposure_time <= value["max"]:
            self.cam.ExposureTime.set(int(exposure_time))
        elif exposure_time < value["min"]:
            self.cam.ExposureTime.set(value["min"])
        elif exposure_time > value["max"]:
            self.cam.ExposureTime.set(value["max"])

    def getHeight(self):
        return self.cam.Height.get()

    def getExposureTime(self):
        return self.cam.ExposureTime.get()

    def getExposureTimeRange(self):
        return self.cam.ExposureTime.get_range()

    def getWidth(self):
        return self.cam.Width.get()

    def startStream(self):
        self.cam.stream_on()

    def stopStream(self):
        self.cam.stream_off()

    @staticmethod
    def raw_capture_callback(raw_data):
        image_data = raw_data.get_numpy_array()
        image_copy = np.copy(image_data)

        Camera().capture_callback.emit(image_copy)
