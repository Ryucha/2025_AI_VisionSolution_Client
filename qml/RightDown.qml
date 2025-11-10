import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "components"

Rectangle {
    width : parent.width
    height: parent.height
    color: "transparent"
    border.color: Colors.text_white
    radius: 8

    ColumnLayout {
        width: parent.width
        height: parent.height
        spacing: 4

        Item {
            Layout.fillWidth: true
            Layout.preferredHeight: childrenRect.height

            ListItem {
                
            }
        }

        Item {
            Layout.fillWidth: true
            Layout.fillHeight: true

            ListView {
                anchors.fill: parent
                model: 30
                clip: true
                delegate: ListItem {
                    no: (index + 1).toString()
                    result: "양품"
                    confidence: "98%"
                    time: "12:34:56"
                }
            }
        }
    }
}