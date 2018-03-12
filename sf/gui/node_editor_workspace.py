import wx
import images

class NodeEditorWorkspace(wx.Notebook):
	def __init__(self, *args, **kwargs):
		super(NodeEditorWorkspace, self).__init__(*args, **kwargs)
		self.create_page()
		self.set_page_background()
		self.Show(True)

	def create_page(self):
		"""
		Creates NodeView Workspace and CodeView Workspace
		"""
		global nodeview
		# TODO: add scrollbars to NodeView
		# See VSCROLL and HSCROLL, style=wx.VSCROLL | wx.HSCROLL
		nodeview = wx.Window(self)
		self.AddPage(nodeview, "Node View")

		codeview = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		self.AddPage(codeview, "Code View")

	def set_page_background(self):
		"""
		Clears background colour with specified image bitmap
		"""
		self.bg_bmp = images.GridBG.GetBitmap()
		# Set background image to NodeView Workspace only
		self.GetPage(self.FindPage(nodeview)).Bind(
			wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground
			)

	def OnEraseBackground(self, evt):
		"""
		Redraw whole bitmap when zoom/pan/scrolling is enabled
		"""
		dc = evt.GetDC()

        # tile the background bitmap
		try:
			sz = self.GetClientSize()
		except RuntimeError:#close main window
			return
		w = self.bg_bmp.GetWidth()
		h = self.bg_bmp.GetHeight()
		x = 0

		while x < sz.width:
			y = 0

			while y < sz.height:
				dc.DrawBitmap(self.bg_bmp, x, y)
				y = y + h

			x = x + w