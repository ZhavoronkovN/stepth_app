import QtQuick
import QtCore
import QtQuick.Controls
import QtQuick.Dialogs

Column {
    id: root
    property string mainColor
    property string secondColor
    property string actionColor
    signal maskLoad(string path)
    signal maskShow(bool show)
    signal maskInvert()
    height : 11 * 40
    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        text: "Load mask"
        action: () => {
                    fileDialog.action = () => root.maskLoad(
                        String(fileDialog.selectedFile).substr(7))
                    fileDialog.open()
                }
    }
    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        toggle : true
        text: "Show mask"
        action: (show) => root.maskShow(show)
    }
    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        text: "Reset mask"
    }
    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        text: "Invert mask"
        action: ()=>root.maskInvert()
    }

    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        text: "Load and add to current"
    }

    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        text: "Load and remove from current"
    }

    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        text: "Load and intersect"
    }
    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        text: "Save mask to file"
    }

    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        text: "Load image and add to current by mask"
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
