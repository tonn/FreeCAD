# SPDX-License-Identifier: LGPL-2.1-or-later

from PySide import QtGui

# Try to import a QWebEngineView from available PySide bindings; fall back to QTextBrowser
QWebEngineView = None
try:
  # PySide2
  from PySide2.QtWebEngineWidgets import QWebEngineView  # type: ignore
  WEBENGINE_BINDING = "PySide2"
except Exception:
  try:
    # PySide6
    from PySide6.QtWebEngineWidgets import QWebEngineView  # type: ignore
    WEBENGINE_BINDING = "PySide6"
  except Exception:
    try:
      # Old PySide (if available)
      from PySide.QtWebEngineWidgets import QWebEngineView  # type: ignore
      WEBENGINE_BINDING = "PySide"
    except Exception:
      QWebEngineView = None
      WEBENGINE_BINDING = None


class HtmlPanelDock(QtGui.QDockWidget):
  def __init__(self, parent=None):
    super(HtmlPanelDock, self).__init__("HTML Panel", parent)
    self.setObjectName("HtmlPanelDock")

    container = QtGui.QWidget()
    layout = QtGui.QVBoxLayout(container)

    # Use QWebEngineView when available to get full HTML/CSS/JS support.
    if QWebEngineView is not None:
      try:
        self.browser = QWebEngineView(container)
        # Some bindings require loading HTML through setHtml on the page
        try:
          # PySide6/2 use setHtml on the view/page
          self.browser.setHtml(
            """
            <html>
              <head><meta charset='utf-8'><title>HTML Panel</title></head>
              <body>
              <h1>HTML Panel (QWebEngineView)</h1>
              <p>JavaScript is available in this view.</p>
              <script>console.log('Hello from QWebEngineView');</script>
              </body>
            </html>
            """
          )
        except Exception:
          # If setHtml isn't available on the view object, try the page()
          try:
            self.browser.page().setHtml(
              """
              <html><body><h1>HTML Panel (QWebEngineView)</h1></body></html>
              """
            )
          except Exception:
            pass
      except Exception:
        # If for some reason instantiation fails, fall back to QTextBrowser
        self.browser = QtGui.QTextBrowser(container)
    else:
      self.browser = QtGui.QTextBrowser(container)

    layout.addWidget(self.browser)

    self.setWidget(container)

    # If using QTextBrowser, give a simple fallback HTML message.
    if QWebEngineView is None:
      self.browser.setHtml(
        """
        <html>
          <head><meta charset='utf-8'><title>HTML Panel</title></head>
          <body>
          <h1>HTML Panel</h1>
          <p>This is a simple HTML-rendering panel (QTextBrowser). JavaScript is not supported.</p>
          </body>
        </html>
        """
      )

  def setHtml(self, html):
    """Replace the HTML shown in the panel."""
    try:
      if QWebEngineView is not None:
        # Prefer the view/page API when available
        try:
          self.browser.setHtml(html)
        except Exception:
          try:
            self.browser.page().setHtml(html)
          except Exception:
            # last resort: set via QText-like API if present
            if hasattr(self.browser, 'setHtml'):
              self.browser.setHtml(html)
      else:
        self.browser.setHtml(html)
    except Exception:
      # swallow errors to avoid breaking the host application; caller can log if desired
      pass

  def runJavaScript(self, code, resultCallback=None):
    """Run JavaScript in the page when QWebEngineView is available.

    resultCallback will be called with the JS return value (if supported).
    If WebEngine is not available this is a no-op.
    """
    if QWebEngineView is None:
      return None
    try:
      page = None
      try:
        page = self.browser.page()
      except Exception:
        page = None
      if page is not None:
        # runJavaScript accepts an optional callback in modern bindings
        try:
          page.runJavaScript(code, resultCallback)
        except TypeError:
          # older bindings might not support callback parameter
          page.runJavaScript(code)
          if resultCallback:
            # can't get result synchronously
            resultCallback(None)
    except Exception:
      return None


def createDock(parent=None):
  """Factory that returns a dock widget instance."""
  return HtmlPanelDock(parent)
