import QtQuick
import QtQuick.Window
import QtWebEngine

Window {
    width: 1024/2
    height: 768/2
    visible: true
    title: "HealthyRecipes"
    WebEngineView {
        anchors.fill: parent
        url: "http://localhost:8156"
    }
}
