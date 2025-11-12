import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "components"

ApplicationWindow {
    visible: true
    width: 1280
    height: 1024
    title: qsTr("AI 비전 솔루션")

    Rectangle {
        anchors.fill: parent
        color: Colors.background
    }

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 36
        spacing: 24
        
        Text {
            text: "AI 검사"
            font.pointSize: 36
            color: Colors.text_white
            horizontalAlignment: Text.AlignHCenter
            Layout.alignment: Qt.AlignTop
        }

        RowLayout {
            Layout.fillWidth: true
            spacing: 20

            ColumnLayout {
                Layout.preferredWidth: 3
                spacing: 10

                Item {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    Layout.preferredHeight: 1

                    Camera {
                        anchors.fill: parent
                    }
                }

                Item {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    Layout.preferredHeight: 1

                    RowLayout {
                        anchors.fill: parent
                        spacing: 10

                        Item {
                            Layout.fillWidth: true
                            Layout.fillHeight: true

                            Rectangle {
                                anchors.fill: parent
                                color: "red"
                            }
                        }

                        Item {
                            Layout.fillWidth: true
                            Layout.fillHeight: true

                            ToggleBox {
                                width: parent.width
                                height: parent.height
                            }
                        }
                    }   
                }
            }

            ColumnLayout {
                Layout.preferredWidth: 2
                spacing: 24

                Item {
                    Layout.fillWidth: true
                    Layout.preferredHeight: childrenRect.height


                    RightUp {
                        height: childrenRect.height
                        width: parent.width                       

                    }
                }

                Item {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    
                    RightDown {
                        width: parent.width
                        height: parent.height
                    }
                }
            }
        }
    }
}
