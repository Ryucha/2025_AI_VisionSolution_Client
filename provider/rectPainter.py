from PySide6.QtQuick import QQuickPaintedItem
from PySide6.QtGui import QPainter, QColor, QPen, QBrush
from PySide6.QtCore import Qt, Signal, Property, Slot, QRectF

class RectPainter(QQuickPaintedItem):
    rectUpdated = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._rects = []
    
    @Property(list, notify=rectUpdated)
    def rects(self):
        return self._rects
    
    @Slot(float, float, float, float)
    def addRect(self, x, y, width, height):
        """사각형 추가"""
        self._rects.append(QRectF(x, y, width, height))
        self.rectUpdated.emit()
        self.update()
    
    @Slot(int)
    def removeRect(self, index):
        """특정 인덱스의 사각형 제거"""
        if 0 <= index < len(self._rects):
            self._rects.pop(index)
            self.rectUpdated.emit()
            self.update()
    
    @Slot()
    def clearRects(self):
        """모든 사각형 초기화"""
        self._rects.clear()
        self.rectUpdated.emit()
        self.update()
    
    @Slot(list)
    def setRects(self, rects):
        """사각형 리스트를 한번에 설정"""
        self._rects = rects
        self.rectUpdated.emit()
        self.update()
    
    def paint(self, painter):
        """사각형들을 그리기"""
        painter.setRenderHint(QPainter.Antialiasing)
        
        pen = QPen(QColor(255, 0, 0), 2)
        painter.setPen(pen)
        
        for rect in self._rects:
            painter.drawRect(rect)
 
        