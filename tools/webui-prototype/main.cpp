#include <QApplication>
#include <QMainWindow>
#include <QWebEngineView>
#include <QWebChannel>
#include "WebHost.h"

int main(int argc, char **argv)
{
    QApplication app(argc, argv);

    QMainWindow wnd;
    wnd.setWindowTitle("FreeCAD WebUI PoC");
    wnd.resize(1100, 700);

    auto *view = new QWebEngineView(&wnd);

    // WebChannel setup
    auto *channel = new QWebChannel(view->page());
    auto *host = new WebHost();
    channel->registerObject(QStringLiteral("backend"), host);
    view->page()->setWebChannel(channel);

    // Load embedded SPA
    view->setUrl(QUrl("qrc:/webui/index.html"));
    wnd.setCentralWidget(view);
    wnd.show();

    return app.exec();
}
