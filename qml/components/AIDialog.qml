import QtQuick.Dialogs

FileDialog {
    property string  selectFile: ""
    title: "모델 파일 선택"
    nameFilters: [ "ONNX Files (*.onnx)", "All Files (*)" ]
    onAccepted: {
        selectFile = fileUrls[0]
    }
    
}