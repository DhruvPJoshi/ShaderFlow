def OnNewWindow(evt):
    """
    Creates a totally new window instance.
    """
    from ..main_app import main
    main()

def OnQuit(evt):
    """
    Exits the current window instance.
    """
    menuObj = evt.GetEventObject()
    evt.Skip()
    menuObj.GetWindow().Close()

def OnAbout(evt):
    """
    Displays general application information.
    """
    import wx
    from wx.lib.wordwrap import wordwrap
    from wx.adv import AboutDialogInfo, AboutBox

    aboutInfo = AboutDialogInfo()
    aboutInfo.Name = "Shader Flow"
    aboutInfo.Version = "v0.0.1"
    aboutInfo.Copyright = "(c) 2018 Unick Developers"
    aboutInfo.Description = wordwrap(
        "Shader Flow gives the freedom to an artist from writing tedious graphic shader codes. Instead, it provides an easier approach - to create graphic shaders visually.", 480, wx.ClientDC(evt.GetEventObject().GetWindow()), margin=10
    )
    aboutInfo.SetWebSite("https://github.com/DhruvPJoshi/ShaderFlow")
    aboutInfo.Developers = [
        "Dhruv Joshi",
        "Pruthvirajsinh Parmar",
        "Breej Vania",
        "Deep Desai"
    ]
    AboutBox(aboutInfo)