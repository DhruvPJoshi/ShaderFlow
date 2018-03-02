import wx

from gui.main_window import SFWindow

def main():
    SFApp = wx.App()
    SFWindow(None)
    SFApp.MainLoop()

if __name__ == '__main__':
    main()