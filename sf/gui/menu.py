import wx

class Menu(wx.Menu):
    def __init__(self, *args, **kwargs):
        super(Menu, self).__init__(*args, **kwargs)

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
                # NOTE: wx automatically registers accelerator when it encounters \t
                itemId, itemLabel, itemAccel = item[1]
                self.Append(itemId, '&' + itemLabel + '\t' + itemAccel)