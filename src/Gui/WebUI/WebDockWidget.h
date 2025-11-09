#pragma once

#include <QWidget>

QT_BEGIN_NAMESPACE
class QWebEngineView;
QT_END_NAMESPACE

namespace Gui {

class WebDockWidget : public QWidget
{
    Q_OBJECT
public:
    explicit WebDockWidget(QWidget *parent = nullptr);
    ~WebDockWidget() override;

private:
    QWebEngineView *m_view{nullptr};
};

} // namespace Gui
