import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "components"

Rectangle {
    color: "transparent"

    ColumnLayout {
        width : parent.width
        height: parent.height
        Item {
            Layout.fillWidth: true
            Layout.preferredHeight: childrenRect.height

            SwitchToggle {
                width: parent.width
                text: "트래킹"
            }
        }

        Item {
            Layout.fillWidth: true
            Layout.preferredHeight: childrenRect.height

            SwitchToggle {
                width: parent.width
                text: "검출 박스 표시"
            }
        }

        Item {
            Layout.fillWidth: true
            Layout.preferredHeight: childrenRect.height
            
            SwitchToggle {
                width: parent.width
                text: "타이머 모드" 
            }
        }

        Item {
            Layout.fillWidth: true
            Layout.preferredHeight: childrenRect.height

            SwitchToggle {
                width: parent.width
                text: "실시간"
                checked: cameraVM.isLive
                onToggled: cameraVM.live_toogle_changed(checked)
                

            }
        }

        Item {
            Layout.fillWidth: true
            Layout.fillHeight: true
        }

    }
}