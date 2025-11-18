import QtQuick.Dialogs

FileDialog {
    property string  selectFile: ""
    title: "이미지 파일 선택"
    nameFilters: [ "Image Files (*.png *.jpg *.jpeg *.bmp)", "All Files (*)" ]
    onAccepted: {
        selectFile = fileUrls[0]
    }
}