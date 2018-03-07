import wx

from menu import Menu
import event_handler as SFEvt

class MenuBar(wx.MenuBar):
    def __init__(self, *args, **kwargs):
        super(MenuBar, self).__init__(*args, **kwargs)
        # allocate all custom ids (if any) before using them
        self.register_ids()
        self.create()

    def register_ids(self):
        """
        Assigns new unique ids to user-defined(custom) ids.
        The custom ids generated here are always outside the range of wx stock ids, to avoid conflicts.
        """
        self.ID_NewWindow = wx.ID_HIGHEST + 1

    def create(self):
        """
        Creates and attaches the menubar to the main application window.
        """
        self.fileMenu = Menu()
        ITEM_LIST = [
            # [stockItem: bool, stockID or separator or (newItem: tuple)]
            [True, wx.ID_NEW],
            [False, (self.ID_NewWindow, 'New Window', 'Ctrl+Shift+N')],
            [True, wx.ID_OPEN],
            [True, wx.ID_SAVE],
            [True, wx.ID_SAVEAS],
            [True, wx.ID_SEPARATOR],
            [True, wx.ID_EXIT]
        ]
        self.fileMenu.add_items(ITEM_LIST)

        self.editMenu = Menu()
        ITEM_LIST = [
            [True, wx.ID_UNDO],
            [True, wx.ID_REDO],
            [True, wx.ID_SEPARATOR],
            [True, wx.ID_CUT],
            [True, wx.ID_COPY],
            [True, wx.ID_PASTE]
        ]
        self.editMenu.add_items(ITEM_LIST)

        self.helpMenu = Menu()
        ITEM_LIST = [
            [True, wx.ID_ABOUT],
            [True, wx.ID_HELP]
        ]
        self.helpMenu.add_items(ITEM_LIST)

        self.Append(self.fileMenu, '&File')
        self.Append(self.editMenu, '&Edit')
        self.Append(self.helpMenu, '&Help')

    # process events "after" menu is added to the bar
    def bind_events(self):
        """
        Assigns every menu item to its appropriate event handlers.
        """
        self.GetFrame().Bind(wx.EVT_MENU, SFEvt.OnNewWindow, id=self.ID_NewWindow)
        self.GetFrame().Bind(wx.EVT_MENU, SFEvt.OnQuit, id=wx.ID_EXIT)
        self.GetFrame().Bind(wx.EVT_MENU, SFEvt.OnAbout, id=wx.ID_ABOUT)