from app.app_config import AppConfig
from gui.main_window import Window as SFWindow

def main():
    SFApp = AppConfig()
    SFWindow(None, title=SFApp.GetAppDisplayName())
    SFApp.MainLoop()