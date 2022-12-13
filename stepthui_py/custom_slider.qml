import QtQuick

Slider{
        id: root
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
