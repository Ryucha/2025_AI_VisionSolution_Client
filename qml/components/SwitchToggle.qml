import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15


Rectangle {
    property string text: "Switch"
    height: 60
    color: "transparent"
    
    RowLayout {
        anchors.fill: parent
        spacing: 10

        Text {
            Layout.leftMargin: 16
            Layout.fillWidth: true
            text: parent.parent.text
            color: Colors.text_white
            font.pointSize: 24
            verticalAlignment: Text.AlignVCenter
        }

        Switch {
            Layout.rightMargin: 16
            id: toggleSwitch
            checked: false
        }
    }
}