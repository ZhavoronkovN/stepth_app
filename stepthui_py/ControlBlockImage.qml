import QtQuick
import QtCore
import QtQuick.Controls
import QtQuick.Dialogs

Column {
    id: root
    property string mainColor
    property string secondColor
    property string actionColor
    signal imageLoadReplace(string path)
    signal imageLoadAdd(string path)
    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        text: "Load image and replace"
        action: () => {
                    fileDialog.action = () => root.imageLoadReplace(
                        String(fileDialog.selectedFile).substr(7))
                    fileDialog.open()
                }
    }

    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        text: "Load image and add to current by mask"
        action: () => {
                    fileDialog.action = () => root.imageLoadAdd(
                        String(fileDialog.selectedFile).substr(7))
                    fileDialog.open()
                }
    }

    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        text: "Save image ignoring mask"
    }

    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        text: "Save image by mask"
    }

    FileDialog {
        id: fileDialog
        title: "Please choose an image"
        property var action
        nameFilters: ["Image files (*.jpg *.png *.jpeg)"]
        visible: false
        currentFolder: StandardPaths.standardLocations(
                           StandardPaths.PicturesLocation)[0]
        onAccepted: action()
    }
}
