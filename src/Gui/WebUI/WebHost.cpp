#include "WebHost.h"
#include <QDebug>

namespace Gui {

WebHost::WebHost(QObject *parent)
    : QObject(parent)
{
}

QVariant WebHost::getDocuments()
{
    QVariantList docs;
    QVariantMap d;
    d["id"] = QStringLiteral("doc-1");
    d["name"] = QStringLiteral("Untitled");
    docs << d;
    return docs;
}

QVariant WebHost::createObject(const QVariant &params)
{
    static int nextId = 1;
    const int id = nextId++;
    QVariantMap info;
    info["objectId"] = QString::number(id);
    info["params"] = params;
    qDebug() << "WebHost::createObject" << params;
    emit objectCreated(info);
    QVariantMap res;
    res["status"] = QStringLiteral("ok");
    res["objectId"] = info["objectId"];
    return res;
}

} // namespace Gui
