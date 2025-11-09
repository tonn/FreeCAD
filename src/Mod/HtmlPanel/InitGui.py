# SPDX-License-Identifier: LGPL-2.1-or-later

from PySide import QtCore, QtGui
import FreeCADGui, __main__


class HtmlPanelWorkbench(__main__.Workbench):
    """Very small workbench that provides a menu entry to show the HTML panel.
    The panel is implemented as a dock widget that contains a QTextBrowser.
    """
    Icon = "python"
    MenuText = "Html Panel"
    ToolTip = "Html Panel workbench"

    def __init__(self):
        self.mw = FreeCADGui.getMainWindow()
        self.dock = None
        self.menu = None
        self.item = []

    def Initialize(self):
        # Create a small menu and add an action to show the panel
        self.menu = QtGui.QMenu()
        self.menu.setTitle("Html Panel")
        action = self.menu.addAction("Show HTML Panel")
        QtCore.QObject.connect(action, QtCore.SIGNAL("triggered()"), self.showPanel)

        # Insert the menu into the main window's menu bar near the Windows menu
        bar = self.mw.menuBar()
        a = bar.actions()
        for i in a:
            if i.objectName() == "&Windows":
                break
        bar.insertMenu(i, self.menu)
        self.menu.menuAction().setVisible(True)

    def Activated(self):
        # lazy create the dock widget when the workbench is activated
        if self.dock is None:
            from HtmlPanel.Gui.HtmlPanel import createDock
            self.dock = createDock()
            self.mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dock)

    def Deactivated(self):
        # keep the dock around but hide it when deactivated
        if self.dock is not None:
            self.dock.hide()

    def showPanel(self):
        # show (or create) the dock and raise it
        if self.dock is None:
            from HtmlPanel.Gui.HtmlPanel import createDock
            self.dock = createDock()
            self.mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dock)
        self.dock.show()
        self.dock.raise_()


FreeCADGui.addWorkbench(HtmlPanelWorkbench)
