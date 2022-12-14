import QtQuick
import QtQuick.Controls

MouseArea {
    id : root
    width : parent.width
    height : 20
    cursorShape : Qt.PointingHandCursor
    property string mainColor : "white"
    property string hoverColor : "white"
    property string pressedColor : "white"
    property string mainTextColor : "black"
    property string additionalTextColor : "white"
    property string currentColor : mainColor
    property string text : "Button text"
    property var action: () => {}
    property bool toggle : false
    property bool toggled : false
    onEntered : { if (!toggled) currentColor = hoverColor }
    onExited : {if (!toggled) currentColor = mainColor }
    onClicked : {
        if (toggle) {
        toggled = ! toggled;
        if (toggled)
            currentColor = pressedColor;
        else
            currentColor = hoverColor;
        action(toggled)
        }
        else {
            currentColor = pressedColor;
            action();
            currentColor = mainColor;
        }
    }
    hoverEnabled : true

    Rectangle {
        id : rect
        anchors.fill : parent
        color : root.currentColor
        border.color : root.pressedColor
        border.width : 1
        Text {

            anchors.fill : parent
            horizontalAlignment : Text.AlignHCenter
            verticalAlignment : Text.AlignVCenter
            text : root.text
            color: root.currentColor === root.mainColor ? root.mainTextColor : root.additionalTextColor
        }
    }
}

