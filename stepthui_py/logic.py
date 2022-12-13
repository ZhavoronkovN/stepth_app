from PySide6.QtCore import QObject, Slot, Signal, QByteArray
from PySide6.QtQuick import QQuickImageProvider
from PySide6.QtQml import QmlElement
from PySide6.QtGui import *
from stepth_client import StepthClient

class MyImageProvider(QQuickImageProvider):
        def __init__(self):
            super(MyImageProvider, self).__init__(QQuickImageProvider.Image)
            self.image = QImage()

        def set_image_raw(self, raw_data):
            print("Setting new image")
            self.data = raw_data
            self.image = QImage.fromData(QByteArray(self.data))

        def requestImage(self, id, size, requested_size):
            print(f"Requested image id = {id}, size = {size}, req_size = {requested_size}")
            size = self.image.size()
            return self.image

image_provider = MyImageProvider()

QML_IMPORT_NAME = "com.logic"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class Logic(QObject):
    updateImage = Signal()
    def __init__(self, parent = None):
        super(Logic, self).__init__(parent)
        self.client = StepthClient()

    @Slot(result=bool)
    def checkServerConnected(self):
        return self.client.check_connected()

    @Slot(str, result=bool)
    def loadMainImage(self, path):
        loaded_image = self.client.load_image(path)
        if loaded_image is not None:
            image_provider.set_image_raw(loaded_image)
            self.updateImage.emit()
            return True
        return False

    @Slot(str, result=bool)
    def loadImageAdd(self, path):
        loaded_image = self.client.load_image_to_current(path)
        if loaded_image is not None:
            image_provider.set_image_raw(loaded_image)
            self.updateImage.emit()
            return True
        return False

    @Slot(str, result=bool)
    def loadDepth(self, path):
        return self.client.load_depth(path)

    @Slot(str, result=bool)
    def loadDepthFromAdd(self, path):
        return self.client.load_depth_from_additional(path)

    @Slot(bool, result=bool)
    def showDepth(self, enabled):
        loaded_image = self.client.show_depth(enabled)
        if loaded_image is not None:
            image_provider.set_image_raw(loaded_image)
            self.updateImage.emit()
            return True
        return False

    @Slot(bool, result=bool)
    def showMask(self, enabled):
        loaded_image = self.client.show_mask(enabled)
        if loaded_image is not None:
            image_provider.set_image_raw(loaded_image)
            self.updateImage.emit()
            return True
        return False

    @Slot(int, result=bool)
    def depthSelect(self, type):
        return self.client.select_depth(type)

    @Slot(int, int, result=bool)
    def depthSelectSlice(self, f, t):
        return self.client.select_depth(0, f, t)

    @Slot(result=bool)
    def invertDepth(self):
        return self.client.invert_depth()

    @Slot(result=bool)
    def invertMask(self):
        return self.client.invert_mask()

    @Slot(bool,int,int,int, result=bool)
    def modifyImage(self, preview, brightness, contrast, sharpness):
        loaded_image = self.client.modify_image(preview, brightness, contrast, sharpness)
        if loaded_image is not None:
            image_provider.set_image_raw(loaded_image)
            self.updateImage.emit()
            return True
        return False

