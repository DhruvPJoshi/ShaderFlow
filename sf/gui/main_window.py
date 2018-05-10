import wx

from menu_bar import MenuBar as SFMenuBar
from node_editor_workspace import NodeEditorWorkspace as SFNEW
from window_3d import Window3D 

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

        # setup node editing workspace
        nodeview = SFNEW(self)

        # setup 3D view
        view3d = Window3D(self, title='3D View', style= wx.CAPTION|wx.RESIZE_BORDER)

        self.Show()