import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "components"

Rectangle {
    color: "transparent"

    AIDialog {
        id: aiDialog
        onAccepted: {
            aiVM.loadAIModel(aiDialog.selectedFile)
        }
    }

    AIDialog {
        id: aiTypeDialog
        onAccepted: {
            aiVM.loadAITypeModel(aiTypeDialog.selectedFile)
        }
    }

    ColumnLayout {
        width: parent.width
        spacing: 10
        Item {
            Layout.fillWidth: true
            Layout.preferredHeight: childrenRect.height
            
            Text {
                text: "양품"
                font.pixelSize: 48
                anchors.centerIn: parent
                color: Colors.green
                font.weight: Font.ExtraBold
            }
        }

        Item {
            Layout.fillWidth: true
            Layout.preferredHeight: childrenRect.height            
            Text {
                text: "98%"
                font.pixelSize: 24
                anchors.centerIn: parent
                color: Colors.text_white
                font.weight: Font.Bold
            }
        }

        Item {
            Layout.fillWidth: true
            Layout.preferredHeight: childrenRect.height            
            Layout.leftMargin: 16
            Layout.rightMargin: 16
            Text {
                text: "모델 : " + aiVM.selectedFile
                font.pixelSize: 24
                color: Colors.text_white
                font.weight: Font.Bold
            }
        }

        Item {
            Layout.fillWidth: true
            Layout.preferredHeight: childrenRect.height            
            Layout.leftMargin: 16
            Layout.rightMargin: 16
            Text {
                text: "분석 유형 모델 : " + aiVM.selectedAITypeFile
                font.pixelSize: 24
                color: Colors.text_white
                font.weight: Font.Bold
            }
        }

        Item {
            Layout.fillWidth: true
            Layout.preferredHeight: childrenRect.height            
            Layout.leftMargin: 16
            Layout.rightMargin: 16
            Layout.topMargin: 10
            Layout.bottomMargin: 10
            RowLayout {
                width: parent.width
                spacing: 10

                DefaultButton {
                    Layout.fillWidth: true
                    Layout.preferredHeight: 80
                    text: "객체 모델 선택"
                    onClicked: {
                        aiDialog.open()
                    }
                }

                DefaultButton {
                    Layout.fillWidth: true
                    Layout.preferredHeight: 80
                    text: "분석 모델 선택"
                    onClicked: aiTypeDialog.open()
                }
            }
        }

        Item {
            Layout.fillWidth: true
            Layout.preferredHeight: childrenRect.height            
            Layout.leftMargin: 16
            Layout.rightMargin: 16
            Text {
                text: "FPS : 30.0"
                font.pixelSize: 20
                color: Colors.text_white
                font.weight: Font.Bold
            }
        }

        Item {
            Layout.fillWidth: true
            Layout.preferredHeight: childrenRect.height            
            Layout.leftMargin: 16
            Layout.rightMargin: 16
            Text {
                text: "처리 시간 : 33ms"
                font.pixelSize: 20
                color: Colors.text_white
                font.weight: Font.Bold
            }
        }
    }
}