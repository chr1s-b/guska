import wx

TITLE = "guska"


class MyApp(wx.App):

    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        self.frame = wx.Frame(None, wx.ID_ANY, title=TITLE)
        self.panel = wx.Panel(self.frame, wx.ID_ANY)
        self.frame.Show(True)
        return


if __name__ == "__main__":
    app = MyApp(redirect=False)
    app.MainLoop()
