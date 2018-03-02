import wx

from menu_bar import SFMenuBar

class SFWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(SFWindow, self).__init__(*args, **kwargs)
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

        self.SetTitle("Shader Flow")
        self.Show()