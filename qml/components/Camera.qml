import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import widgets

Rectangle {
    anchors.fill: parent
    color: "black"
    
    onWidthChanged: {
        console.log("Size changed:", width, "x", height)
        aiVM.view_size_update(width, height)
    }
    
    onHeightChanged: {
        aiVM.view_size_update(width, height)
    }

    Connections {
        target: cameraVM
        function onOpenImageDialog() {
            imageDialog.open()
        }
    }

    ImageDialog {
        id: imageDialog
        onAccepted: {
            cameraVM.load_image(imageDialog.selectedFile)
        }       
    }
    
    Image {
        anchors.fill: parent
        source: cameraVM.previewImage
        cache: false
        fillMode: Image.PreserveAspectFit
    }

    MouseArea {
        anchors.fill: parent
        onClicked: {
            cameraVM.click_camera_image()
        }
    }
    RectPainter {
        anchors.fill: parent
    }


    
}