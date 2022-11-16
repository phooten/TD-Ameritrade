#include "mainwindow.h"

#include <QApplication>

int main( int argc, char *argv[] )
{
    QApplication a( argc, argv );

    MainWindow w;
    w.show();

    // the connect implementation
    connect( exitButton, &QPushButton::clicked, qApp, &QApplication::quit );

    return a.exec();
}
