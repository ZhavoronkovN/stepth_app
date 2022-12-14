import QtQuick
import QtQuick.Controls
import com.logic

ApplicationWindow {
    id: root
    width: 640
    height: 480
    visible: true
    title: qsTr("")
    property string mainColor: "#e6e8e6"
    property string secondColor: "#7de2d1"
    property string actionColor: "#339989"
    property string textColor: "#131515"
    property string secondTextColor: "#2b2c28"
    property double rootOpacity: 1
    color: mainColor
    Rectangle {
        id: rectImage
        anchors {
            left: parent.left
            right: parent.right
            top: parent.top
        }
        height : parent.height  - Math.max(parent.height * 0.2, 300)
        color: root.mainColor
        opacity: root.rootOpacity
        Image {
            id: image_view
            anchors.fill: parent

            fillMode: Image.PreserveAspectFit
            smooth: true
            cache: false
            source: "image://myprovider/"
            function reloadImage() {
                console.log("Updating image...")
                var oldSource = source
                source = ""
                source = oldSource
            }
        }
    }

    Flickable {
        height: rectImage.height
        width: 50
        anchors.top: parent.top
        anchors.right: parent.right
        boundsMovement: Flickable.StopAtBounds
        contentHeight: colButtons.height
        Column {
            id: colButtons
            MyButton {
                icon: "assets/icons/aperture.svg"
                mainColor: root.secondColor
                hoverColor: root.mainColor
                pressedColor: root.actionColor
                action: () => controlsStack.replace(controlBlockImageComp)
            }
            MyButton {
                icon: "assets/icons/mountain.svg"
                mainColor: root.secondColor
                hoverColor: root.mainColor
                pressedColor: root.actionColor
                action: () => controlsStack.replace(controlBlockDepthComp)
            }
            MyButton {
                icon: "assets/icons/flower.svg"
                mainColor: root.secondColor
                hoverColor: root.mainColor
                pressedColor: root.actionColor
                action: () => controlsStack.replace(controlBlockMaskComp)
            }
            MyButton {
                icon: "assets/icons/paint_roll.svg"
                mainColor: root.secondColor
                hoverColor: root.mainColor
                pressedColor: root.actionColor
                action: () => controlsStack.replace(controlBlockPixComp)
            }
            MyButton {
                icon: "assets/icons/curve.svg"
                mainColor: root.secondColor
                hoverColor: root.mainColor
                pressedColor: root.actionColor
            }
        }
    }
    Flickable {
        id: flickControls
        anchors.top : rectImage.bottom
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        boundsMovement: Flickable.StopAtBounds
        contentHeight: controlsStack.currentItem.height + 5
        Rectangle {
            anchors.top: parent.top
            width: parent.width
            height: 5
            color: root.actionColor
        }

        Rectangle {
            id: rectControls
            anchors.topMargin: 5
            anchors.fill: parent
            color: root.mainColor
            opacity: root.rootOpacity
            StackView {
                id: controlsStack
                anchors {
                    left : parent.left
                    right : parent.right
                    top : parent.top
                }
                initialItem: controlBlockImageComp
            }
        }
    }
    Component {
        id: controlBlockImageComp
        ControlBlockImage {
            mainColor: root.mainColor
            secondColor: root.secondColor
            actionColor: root.actionColor
            mainTextColor : root.textColor
            additionalTextColor : root.secondTextColor
            onImageLoadReplace: (path) => logic.loadMainImage(path)
            onImageLoadAdd: (path) => logic.loadImageAdd(path)
        }
    }
    Component {
        id: controlBlockDepthComp
        ControlBlockDepth {
            mainColor: root.mainColor
            secondColor: root.secondColor
            actionColor: root.actionColor
            mainTextColor : root.textColor
            additionalTextColor : root.secondTextColor
            onDepthLoad: (path) => logic.loadDepth(path)
            onDepthLoadAdd: (path) => logic.loadDepthFromAdd(path)
            onDepthShow: (show) => logic.showDepth(show)
            onDepthInvert: () => logic.invertDepth()
            onDepthSelect: (t) => logic.depthSelect(t)
            onDepthSelectSlice: (f,t) => logic.depthSelectSlice(f, t)
        }
    }
    Component {
        id: controlBlockMaskComp
        ControlBlockMask {
            mainColor: root.mainColor
            secondColor: root.secondColor
            actionColor: root.actionColor
            mainTextColor : root.textColor
            additionalTextColor : root.secondTextColor
            onMaskLoad: (path) => logic.loadMask(path)
            onMaskShow: (show) => logic.showMask(show)
            onMaskInvert: () => logic.invertMask()
        }
    }
    Component {
        id: controlBlockPixComp
        ControlBlockPixels {
            mainColor: root.mainColor
            secondColor: root.secondColor
            actionColor: root.actionColor
            mainTextColor : root.textColor
            additionalTextColor : root.secondTextColor
            onImageModified: (preview, brightness, contrast, sharpness) => logic.modifyImage(preview, brightness, contrast, sharpness)
        }
    }
    Logic {
        id: logic
        onUpdateImage: image_view.reloadImage()
    }
}
