import wx

import event_handler as SFEvt

class SFMenuBar(wx.MenuBar):
    def __init__(self, *args, **kwargs):
        super(SFMenuBar, self).__init__(*args, **kwargs)
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
        self.fileMenu = SFMenu()
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

        self.editMenu = SFMenu()
        ITEM_LIST = [
            [True, wx.ID_UNDO],
            [True, wx.ID_REDO],
            [True, wx.ID_SEPARATOR],
            [True, wx.ID_CUT],
            [True, wx.ID_COPY],
            [True, wx.ID_PASTE]
        ]
        self.editMenu.add_items(ITEM_LIST)

        self.helpMenu = SFMenu()
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


class SFMenu(wx.Menu):
    def __init__(self, *args, **kwargs):
        super(SFMenu, self).__init__(*args, **kwargs)

    def add_items(self, items):
        """
        Extracts the menu items and adds them to it.
        If the menu item is a custom one, then registers its accelerator (aka shortcut/key-combination).
        """
        for item in items:
            if item[0]:
                # it's a wx stock item
                if item[1] == wx.ID_SEPARATOR:
                    self.AppendSeparator()
                    continue
                self.Append(item[1])
            else:
                # it's a custom item
                # TODO: register the new accelerator
                itemId, itemLabel, itemAccel = item[1]
                self.Append(itemId, '&' + itemLabel + '\t' + itemAccel)