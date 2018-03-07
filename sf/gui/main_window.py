import wx

from menu_bar import MenuBar as SFMenuBar

class Window(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.init_ui()

    def init_ui(self):
        """
        Creates and initializes the main working area.
        """
        # cover the whole desktop, except the taskbar
        self.SetSize(wx.ClientDisplayRect())

        menuBar = SFMenuBar()
        self.SetMenuBar(menuBar)
        menuBar.bind_events()

        self.Show()