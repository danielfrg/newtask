import os
import wx
import win32con
from mail import Mailer
from settings import SettingsForm
from settings import Settings


class MainFrame(wx.Frame):
    def __init__(self):
        super(MainFrame, self).__init__(None, title="New Task",
                            style=wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX)

        self.file = 'settings.cfg'
        self.settings = Settings(self.file)

        # Icon
        icon = wx.Icon("images/task.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        #
        self.createControls()
        self.bindEvents()
        self.doLayout()
        self.SetSizeWH(400, 100)
        self.Centre()
        self.Show(True)

    # ==============================================================================================
    # ====================================== UI
    # ==============================================================================================
    def createControls(self):
        self.panel = wx.Panel(self)
        self.txtTask = wx.TextCtrl(self.panel, 0, 'New Task', style=wx.TE_PROCESS_ENTER)

        bmp = wx.Bitmap("images/settings.png", wx.BITMAP_TYPE_ANY)
        self.btnSettings = wx.BitmapButton(self.panel, id=wx.ID_ANY, bitmap=bmp,
                                            size=(bmp.GetWidth() + 10, bmp.GetHeight() + 10))

        self.lblDummy = wx.StaticText(self.panel, size=(170, 300))
        self.btnCancel = wx.Button(self.panel, label='Cancel [esc]', size=(90, 26))
        self.btnSend = wx.Button(self.panel, label='Send [enter]', size=(90, 26))

    def doLayout(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Line 1
        vbox.Add(self.txtTask, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Line 2
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.btnSettings)
        hbox2.Add(self.lblDummy)
        hbox2.Add(self.btnCancel)
        hbox2.Add(self.btnSend)
        vbox.Add(hbox2, flag=wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Main
        self.panel.SetSizer(vbox)

    # ==============================================================================================
    # ====================================== EVENTS
    # ==============================================================================================

    def bindEvents(self):
        self.txtTask.Bind(wx.EVT_KEY_UP, self.OnKeyUP)
        self.txtTask.Bind(wx.EVT_TEXT_ENTER, self.onSend)

        self.btnSettings.Bind(wx.EVT_BUTTON, self.onOpenSettings)
        self.btnSend.Bind(wx.EVT_BUTTON, self.onSend)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.onCancel)

        wx.EVT_CLOSE(self, self.onClose)  # triggered when the app is closed

        self.registerHotkey()
        self.registerMinimizeToTray()

    def onSend(self, event):
        self.mailer = Mailer(self.settings.getEmail(), self.settings.getPassword())
        toaddr = self.settings.getEmailTo()
        subject = self.txtTask.GetValue()

        self.onMinimize(None)
        self.txtTask.SetValue("")

        self.mailer.sendMail(toaddr, subject, "")  # Send at the end to close faster the window

    def onCancel(self, event):
        self.txtTask.SetValue("")
        self.onMinimize(None)

    def onOpenSettings(self, event):
        SettingsForm(self, self.file)

    def onClose(self, event):
        self.tbIcon.RemoveIcon()  # remove the systemtray icon when the program closes
        os._exit(1)

    def OnKeyUP(self, event):
        keyCode = event.GetKeyCode()
        if keyCode == wx.WXK_ESCAPE:
                self.ToggleShow(None)

    # ==============================================================================================
    # ====================================== HOTKEYS
    # ==============================================================================================

    def registerHotkey(self):
        self.hotKeyId = wx.NewId()
        print self.RegisterHotKey(
                        self.hotKeyId,  # a unique ID for this hotkey
                        win32con.MOD_WIN,  # the modifier key
                        win32con.VK_DELETE)  # the key to watch for
        self.Bind(wx.EVT_HOTKEY, self.handleHotKey, id=self.hotKeyId)

    def handleHotKey(self, evt):
        self.ToggleShow(None)

    # ==============================================================================================
    # ====================================== MINIMIZE TO TRAY
    # ==============================================================================================

    def registerMinimizeToTray(self):
        self.tbIcon = wx.TaskBarIcon()
        icon = wx.Icon("images/task.ico", wx.BITMAP_TYPE_ICO)
        self.tbIcon.SetIcon(icon, "Tasks")

        wx.EVT_TASKBAR_LEFT_DCLICK(self.tbIcon, self.ToggleShow)  # left click
        wx.EVT_TASKBAR_LEFT_UP(self.tbIcon, self.ToggleShow)  # double left click
        wx.EVT_TASKBAR_RIGHT_UP(self.tbIcon, self.ToggleShow)  # single left click

        self.Bind(wx.EVT_ICONIZE, self.onMinimize)  # binding for minimizing

    def onMinimize(self, event):
        self.Hide()  # this removes it from the taskbar so it only appears in the system tray

    def ToggleShow(self, event):
        if self.IsShown():
            self.Hide()
        else:
            self.Show()
            self.Restore()  # take it out of the taskbar (otherwise it'll be shown but still minimized, which is awkward)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
