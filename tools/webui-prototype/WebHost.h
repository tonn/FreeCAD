#pragma once

#include <QObject>
#include <QVariant>
#include <QJsonObject>

class WebHost : public QObject
{
    Q_OBJECT
public:
    explicit WebHost(QObject *parent = nullptr);

    Q_INVOKABLE QVariant getDocuments();
    Q_INVOKABLE QVariant createObject(const QVariant &params);

signals:
    void selectionChanged(const QVariant &payload);
    void objectCreated(const QVariant &info);

private:
    int m_nextId{1};
};
