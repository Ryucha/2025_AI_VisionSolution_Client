import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15



Button {
    text: "Button"
    height: 80
    contentItem: Text {
        text: parent.text
        font.pointSize: 24 
        color: Colors.text_white
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    background: Rectangle {
        radius: 8
        color: parent.down ? Colors.button_hover : Colors.button_normal
        border.color: Colors.button_border
    }
}