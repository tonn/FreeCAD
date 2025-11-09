#include "WebHost.h"
#include <QDebug>

WebHost::WebHost(QObject *parent)
    : QObject(parent)
{
}

QVariant WebHost::getDocuments()
{
    // Minimal stub: return a list with one dummy document
    QVariantList docs;
    QVariantMap d;
    d["id"] = QStringLiteral("doc-1");
    d["name"] = QStringLiteral("Untitled");
    docs << d;
    return docs;
}

QVariant WebHost::createObject(const QVariant &params)
{
    // Simple stub: increment id and emit objectCreated
    const int id = m_nextId++;
    QVariantMap info;
    info["objectId"] = QString::number(id);
    info["params"] = params;
    qDebug() << "WebHost::createObject" << params;
    emit objectCreated(info);
    // Return success
    QVariantMap res;
    res["status"] = QStringLiteral("ok");
    res["objectId"] = info["objectId"];
    return res;
}
