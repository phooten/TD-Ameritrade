/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionCase_1;
    QAction *actionCase_2;
    QWidget *centralwidget;
    QTextEdit *textEdit;
    QPushButton *pushButton;
    QMenuBar *menubar;
    QMenu *menuName_of_the_window;
    QMenu *menuDrop_down_menu;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(800, 600);
        actionCase_1 = new QAction(MainWindow);
        actionCase_1->setObjectName("actionCase_1");
        actionCase_2 = new QAction(MainWindow);
        actionCase_2->setObjectName("actionCase_2");
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        textEdit = new QTextEdit(centralwidget);
        textEdit->setObjectName("textEdit");
        textEdit->setGeometry(QRect(10, 10, 221, 31));
        pushButton = new QPushButton(centralwidget);
        pushButton->setObjectName("pushButton");
        pushButton->setGeometry(QRect(10, 40, 131, 32));
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 800, 22));
        menuName_of_the_window = new QMenu(menubar);
        menuName_of_the_window->setObjectName("menuName_of_the_window");
        menuDrop_down_menu = new QMenu(menubar);
        menuDrop_down_menu->setObjectName("menuDrop_down_menu");
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuName_of_the_window->menuAction());
        menubar->addAction(menuDrop_down_menu->menuAction());
        menuDrop_down_menu->addAction(actionCase_1);
        menuDrop_down_menu->addAction(actionCase_2);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        actionCase_1->setText(QCoreApplication::translate("MainWindow", "Case 1", nullptr));
        actionCase_2->setText(QCoreApplication::translate("MainWindow", "Case 2", nullptr));
        textEdit->setHtml(QCoreApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter ticker symbol here...</p></body></html>", nullptr));
        pushButton->setText(QCoreApplication::translate("MainWindow", "Confirm Ticker", nullptr));
        menuName_of_the_window->setTitle(QCoreApplication::translate("MainWindow", "Name of the window.", nullptr));
        menuDrop_down_menu->setTitle(QCoreApplication::translate("MainWindow", "Drop down menu.", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
