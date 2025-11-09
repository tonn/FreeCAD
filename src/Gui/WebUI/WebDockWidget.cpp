#include "WebDockWidget.h"
#ifdef BUILD_WITH_WEBUI
#include <QVBoxLayout>
#include <QWebEngineView>
#include <QWebChannel>
#include "WebHost.h"
#endif

namespace Gui {

WebDockWidget::WebDockWidget(QWidget *parent)
    : QWidget(parent)
{
#ifdef BUILD_WITH_WEBUI
    auto *lay = new QVBoxLayout(this);
    lay->setContentsMargins(0,0,0,0);
    m_view = new QWebEngineView(this);

    auto *channel = new QWebChannel(m_view->page());
    auto *host = new WebHost(this);
    channel->registerObject(QStringLiteral("backend"), host);
    m_view->page()->setWebChannel(channel);

    m_view->setUrl(QUrl("qrc:/webui/index.html"));
    lay->addWidget(m_view);
#else
    Q_UNUSED(parent);
#endif
}

WebDockWidget::~WebDockWidget() = default;

} // namespace Gui
