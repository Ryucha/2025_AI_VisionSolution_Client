import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15


Rectangle {
    id: root
    property string text: "Switch"
    property bool checked: false
    signal toggled(bool checked)
    height: 60
    color: "transparent"
    
    RowLayout {
        anchors.fill: parent
        spacing: 10

        Text {
            Layout.leftMargin: 16
            Layout.fillWidth: true
            text: root.text
            color: Colors.text_white
            font.pointSize: 24
            verticalAlignment: Text.AlignVCenter
        }

        Switch {
            Layout.rightMargin: 16
            id: toggleSwitch
            checked: root.checked
            onCheckedChanged: root.toggled(checked)
        }
    }
}