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
        url: "http://0.0.0.0:8156/index.html"
    }
}
