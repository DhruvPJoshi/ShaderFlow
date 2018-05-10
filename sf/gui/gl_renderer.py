import wx
import wx.glcanvas as glc

class GLRender(glc.GLCanvas):
    def __init__(self, *arg, **kwargs):
        super(GLRender, self).__init__(*arg, **kwargs)
        self.create_ctx()

    def create_ctx(self):
        self.ctx = glc.GLContext(self)
        self.SetCurrent(self.ctx)
        
