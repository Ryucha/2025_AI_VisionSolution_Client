import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Rectangle {
    anchors.fill: parent
    color: "black"
    
    Image {
        anchors.fill: parent
        source: cameraVM.previewImage
        cache: false
    }

    
}