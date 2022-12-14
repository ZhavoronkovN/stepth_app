import QtQuick
import QtCore
import QtQuick.Controls
import QtQuick.Dialogs

Column {
    id: root
    property string mainColor
    property string secondColor
    property string actionColor
    property string mainTextColor
    property string additionalTextColor
    signal depthLoad(string path)
    signal depthLoadAdd(string path)
    signal depthInvert
    signal depthShow(bool show)
    signal depthSelect(int type)
    signal depthSelectSlice(int from, int to)
    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        mainTextColor: root.mainTextColor
        additionalTextColor: root.additionalTextColor
        text: "Load depth"
        action: () => {
                    fileDialog.action = () => root.depthLoad(
                        String(fileDialog.selectedFile).substr(7))
                    fileDialog.open()
                }
    }

    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        mainTextColor: root.mainTextColor
        additionalTextColor: root.additionalTextColor
        text: "Load depth from additional image"
        action: () => {
                    fileDialog.action = () => root.depthLoadAdd(
                        String(fileDialog.selectedFile).substr(7))
                    fileDialog.open()
                }
    }

    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        mainTextColor: root.mainTextColor
        additionalTextColor: root.additionalTextColor
        text: "Invert depth"
        action: () => root.depthInvert()
    }

    Row {
        height : 40
        width : parent.width
        MyTextButton {
            height: 40
            width: parent.width / 2
            mainColor: root.mainColor
            hoverColor: root.secondColor
            pressedColor: root.actionColor
            mainTextColor: root.mainTextColor
            additionalTextColor: root.additionalTextColor
            text: "Select foreground"
            action : () => root.depthSelect(1)
        }

        MyTextButton {
            height: 40
            width: parent.width / 2
            mainColor: root.mainColor
            hoverColor: root.secondColor
            pressedColor: root.actionColor
            mainTextColor: root.mainTextColor
            additionalTextColor: root.additionalTextColor
            text: "Select background"
            action : () => root.depthSelect(2)
        }
    }

    Row {
        height : 40
        width : parent.width
        MyTextButton {
            height: 40
            width: parent.width / 3
            mainColor: root.mainColor
            hoverColor: root.secondColor
            pressedColor: root.actionColor
            mainTextColor: root.mainTextColor
            additionalTextColor: root.additionalTextColor
            text: "Select foreground"
            action : () => root.depthSelect(3)
        }

        MyTextButton {
            height: 40
            width: parent.width / 3
            mainColor: root.mainColor
            hoverColor: root.secondColor
            pressedColor: root.actionColor
            mainTextColor: root.mainTextColor
            additionalTextColor: root.additionalTextColor
            text: "Select middleground"
            action : () => root.depthSelect(4)
        }

        MyTextButton {
            height: 40
            width: parent.width / 3
            mainColor: root.mainColor
            hoverColor: root.secondColor
            pressedColor: root.actionColor
            mainTextColor: root.mainTextColor
            additionalTextColor: root.additionalTextColor
            text: "Select background"
            action : () => root.depthSelect(5)
        }
    }

    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        mainTextColor: root.mainTextColor
        additionalTextColor: root.additionalTextColor
        toggle : true
        text: "Show depth"
        action: (show) => root.depthShow(show)
    }

    Row {
        width : parent.width
        height : 40
        Label {
            width : parent.width * 0.05
            height : parent.height
            text : Math.round(parseFloat(depthSlider.first.value))
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }
        RangeSlider{
                id: depthSlider
                width : parent.width * 0.7
                height : parent.height
                from : 0
                to : 255
                second.value : to

                first.handle: Rectangle {
                    x: depthSlider.leftPadding + depthSlider.first.visualPosition * (depthSlider.availableWidth - width)
                    y: depthSlider.topPadding + depthSlider.availableHeight / 2 - height / 2
                    implicitWidth: 10
                    implicitHeight: depthSlider.height
                    color: root.actionColor
                }

                second.handle: Rectangle {
                    x: depthSlider.leftPadding + depthSlider.second.visualPosition * (depthSlider.availableWidth - width)
                    y: depthSlider.topPadding + depthSlider.availableHeight / 2 - height / 2
                    implicitWidth: 10
                    implicitHeight: depthSlider.height
                    color: root.actionColor
                    radius : 10
                }



                background: Rectangle{
                    x: depthSlider.leftPadding
                    y: depthSlider.topPadding + depthSlider.availableHeight/2 - height /2
                    width: depthSlider.availableWidth

                    implicitHeight: 4
                    height: implicitHeight
                    radius: 2

                    Rectangle{
                        id: section1
                        height: parent.height
                        width: depthSlider.first.visualPosition*parent.width
                        color : root.mainColor
                    }

                    Rectangle{
                        id: section2
                        x: depthSlider.first.visualPosition * parent.width
                        height: parent.height
                        width: depthSlider.second.visualPosition*parent.width -x
                        color :root.secondColor
                    }

                    Rectangle{
                        id: section3
                        x: depthSlider.second.visualPosition * parent.width
                        height: parent.height
                        width: parent.width -x
                        color : root.mainColor
                    }
                }
            }
        Label {
            width : parent.width * 0.05
            height : parent.height
            text : Math.round(parseFloat(depthSlider.second.value))
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }
        MyTextButton {
            height : 40
            width : parent.width * 0.2
            mainColor: root.mainColor
            hoverColor: root.secondColor
            pressedColor: root.actionColor
            mainTextColor: root.mainTextColor
            additionalTextColor: root.additionalTextColor
            text: "Select slice"
            action : () => root.depthSelectSlice(Math.round(parseFloat(depthSlider.first.value)), Math.round(parseFloat(depthSlider.second.value)))
        }
    }

    MyTextButton {
        height: 40
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        mainTextColor: root.mainTextColor
        additionalTextColor: root.additionalTextColor
        text: "Save depth to file"
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
