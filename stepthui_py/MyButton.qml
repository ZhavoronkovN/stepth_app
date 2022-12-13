import QtQuick
import QtQuick.Controls

MouseArea {
    id : root
    property int size : 50
    width : size
    height : size
    cursorShape : Qt.PointingHandCursor
    property string mainColor : "white"
    property string hoverColor : "white"
    property string pressedColor : "white"
    property string currentColor : mainColor
    property double targetOpacity : 0.6
    property string icon
    property var action: () => {}
    onEntered : {currentColor = hoverColor; opacity = 1}
    onExited : {currentColor = mainColor; opacity = targetOpacity}
    onClicked : {
        currentColor = pressedColor;
        action()
        currentColor = hoverColor;
    }
    hoverEnabled : true

    Rectangle {
        id : rect
        anchors.fill : parent
        color : root.currentColor
        border.color : root.pressedColor
        border.width : 1
        Image {
              anchors.fill : parent
              anchors.margins : 5
              fillMode: Image.PreserveAspectFit
              source: root.icon
              opacity : parent.opacity
        }
    }
}
