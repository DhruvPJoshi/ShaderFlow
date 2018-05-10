import wx 
import gl_renderer as glr
import OpenGL.GL

class Window3D(wx.MiniFrame):
    def __init__(self, *arg, **kwargs):
        super(Window3D, self).__init__(*arg, **kwargs)
        self.init_3d_view()
        
    
    def init_3d_view(self):
        # adjust size and initial position of the render view 
        self.parent = self.GetParent()
        self.size_rect = self.parent.GetRect()
        width = self.size_rect.GetWidth()/2.1
        height = self.size_rect.GetHeight()/2
        self.SetSize(width, height)
        self.SetPosition(self.size_rect.GetBottomRight()-wx.Point(width, height))

        self.canvas = glr.GLRender(self, size=self.GetSize()) 
        OpenGL.GL.glClearColor(0.5, 0.5, 0.5, 1.0)
        OpenGL.GL.glClear(OpenGL.GL.GL_COLOR_BUFFER_BIT)
        self.canvas.SwapBuffers()
        self.Show()