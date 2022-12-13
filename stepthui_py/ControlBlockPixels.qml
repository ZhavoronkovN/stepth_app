import QtQuick
import QtCore
import QtQuick.Controls
import QtQuick.Dialogs

Column {
    id: root
    property string mainColor
    property string secondColor
    property string actionColor
    signal imageModified(bool preview, int brightness, int contrast, int sharpness)
    height : 200
    Row {
        width : parent.width
        height : 40
        Label {
            width : parent.width * 0.15
            height : parent.height
            text : "Brightness : "
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }
    Slider {
        id : sliderBrightness
        width : parent.width * 0.75
        height : parent.height
        horizontalPadding : 10
        from : -128.0
        to : 128.0
        stepSize : 1.0
        value : 0
        live : true
        snapMode : Slider.SnapAlways
            handle: Rectangle {
                x: sliderBrightness.leftPadding + sliderBrightness.visualPosition * (sliderBrightness.availableWidth - width)
                y: sliderBrightness.topPadding + sliderBrightness.availableHeight / 2 - height / 2
                color: root.actionColor
                implicitWidth: 10
                implicitHeight: sliderBrightness.height
                radius: 10
            }
    }
    Label {
        width : parent.width * 0.1
        height : parent.height
        text : sliderBrightness.value
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
    }
    }
    Row {
        width : parent.width
        height : 40
        Label {
            width : parent.width * 0.15
            height : parent.height
            text : "Contrast : "
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }
    Slider {
        id : sliderContrast
        width : parent.width * 0.75
        height : parent.height
        horizontalPadding : 10
        from : -20
        to : 20
        stepSize : 1.0
        value : 0
        live : true
        snapMode : Slider.SnapAlways
            handle: Rectangle {
                x: sliderContrast.leftPadding + sliderContrast.visualPosition * (sliderContrast.availableWidth - width)
                y: sliderContrast.topPadding + sliderContrast.availableHeight / 2 - height / 2
                color: root.actionColor
                implicitWidth: 10
                implicitHeight: sliderContrast.height
                radius: 10
            }
    }
    Label {
        width : parent.width * 0.1
        height : parent.height
        text : sliderContrast.value
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
    }
    }
    Row {
        width : parent.width
        height : 40
        Label {
            width : parent.width * 0.15
            height : parent.height
            text : "Sharpness : "
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }
    Slider {
        id : sliderSharpness
        width : parent.width * 0.75
        height : parent.height
        horizontalPadding : 10
        from : -10
        to : 10
        stepSize : 1.0
        value : 0
        live : true
        snapMode : Slider.SnapAlways
            handle: Rectangle {
                x: sliderSharpness.leftPadding + sliderSharpness.visualPosition * (sliderSharpness.availableWidth - width)
                y: sliderSharpness.topPadding + sliderSharpness.availableHeight / 2 - height / 2
                color: root.actionColor
                implicitWidth: 10
                implicitHeight: sliderSharpness.height
                radius: 10
            }
    }
    Label {
        width : parent.width * 0.1
        height : parent.height
        text : sliderSharpness.value
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
    }
    }
    Row {
        width : parent.width
        height : 40
        MyTextButton {
            height: 40
            width : parent.width/3
            mainColor: root.mainColor
            hoverColor: root.secondColor
            pressedColor: root.actionColor
            text: "Reset"
            action : () => root.imageModified(true, 0,0,0)
        }
    MyTextButton {
        height: 40
        width : parent.width/3
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        text: "Preview"
        action : () => root.imageModified(true, Math.round(sliderBrightness.value),Math.round(sliderContrast.value),Math.round(sliderSharpness.value))
    }
    MyTextButton {
        height: 40
        width : parent.width/3
        mainColor: root.mainColor
        hoverColor: root.secondColor
        pressedColor: root.actionColor
        text: "Apply"
        action : () => root.imageModified(false, Math.round(sliderBrightness.value),Math.round(sliderContrast.value),Math.round(sliderSharpness.value))
    }
    }
}
