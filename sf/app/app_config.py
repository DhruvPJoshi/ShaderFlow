import wx

class AppConfig(wx.App):
    def __init__(self, *args, **kwargs):
        super(AppConfig, self).__init__(*args, **kwargs)
        self.configure()

    def configure(self):
        self.SetAppDisplayName("Shader Flow")

    def OnExit(self):
        self.ExitMainLoop()
        self.Destroy()
        return True