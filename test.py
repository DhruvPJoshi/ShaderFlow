#!/user/bin/env python

import wx
import wx.aui as aui

class ShaderFlowApp(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(ShaderFlowApp, self).__init__(*args, **kwargs)
        self.InitUI()

    def CreateTab(self, parent, title, style):
        tab = wx.TextCtrl(parent, style=style)
        parent.AddPage(tab, title)
        return tab

    def InitUI(self):
        self.CreateStatusBar(2)

        self.nb = aui.AuiNotebook(self)

        nodesTab = self.CreateTab(self.nb, "Nodes", wx.TE_MULTILINE)
        nodesTab.write("Add some nodes here...")

        renderTab = self.CreateTab(self.nb, "Renderer", wx.TE_MULTILINE)
        renderTab.write("Render something here...")
        renderTab.SetInitialSize(wx.Size(300, -1))

        self.Show()


def main():
    myApp = wx.App()
    ShaderFlowApp(None, -1, title='Shader Flow')
    myApp.MainLoop()


if __name__ == '__main__':
    main()