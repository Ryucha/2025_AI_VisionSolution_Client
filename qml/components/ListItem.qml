import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Rectangle {
    property string no: "번호"
    property string result: "결과"
    property string confidence: "신뢰도"
    property string time: "시간"

    height: 40
    width: parent.width
    color: "transparent"
    
    RowLayout {
        anchors.fill: parent
        anchors.leftMargin: 16
        anchors.rightMargin: 16
        spacing: 10
        
    
        Text {
            Layout.fillWidth: true
            Layout.preferredWidth: 1
            text: parent.parent.no
            color: Colors.text_white
            font.pointSize: 20
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            elide: Text.ElideRight
        }

        Text {
            Layout.fillWidth: true
            Layout.preferredWidth: 2
            text: parent.parent.result
            color: Colors.text_white
            font.pointSize: 20
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            elide: Text.ElideRight
        }

        Text {
            Layout.fillWidth: true
            Layout.preferredWidth: 2
            text: parent.parent.confidence
            color: Colors.text_white
            font.pointSize: 20
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            elide: Text.ElideRight
        }

        Text {
            Layout.fillWidth: true
            Layout.preferredWidth: 2
            text: parent.parent.time
            color: Colors.text_white
            font.pointSize: 20
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            elide: Text.ElideRight
        }
    }
}