import os
import wx
import win32con
from mail import Mailer

class MainFrame(wx.Frame):
	def __init__(self):
		super(MainFrame, self).__init__(None, title="New Task",
			style= wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX)

		self.initUI()
		self.SetSizeWH(400, 100)
		self.Centre()
		self.Show(True)
		wx.EVT_CLOSE(self, self.onClose) # triggered when the app is closed

		icon = wx.Icon("checkmark.ico", wx.BITMAP_TYPE_ICO)
		self.SetIcon(icon)

		#
		self.initMailer()
		self.registerHotkey()
		self.registerMinimizeToTray()


	# ==============================================================================================
	# ====================================== UI
	# ==============================================================================================

	def initUI(self):
		panel = wx.Panel(self)

		vbox = wx.BoxSizer(wx.VERTICAL)

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		self.txtTask = wx.TextCtrl(panel, -1, 'New Task', style=wx.TE_PROCESS_ENTER)
		self.txtTask.Bind(wx.EVT_KEY_UP, self.OnKeyUP)
		self.txtTask.Bind(wx.EVT_TEXT_ENTER, self.sendTask)
		vbox.Add(self.txtTask, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		#

		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		bmp = wx.Bitmap("settings.png", wx.BITMAP_TYPE_ANY)
		#btnSettings = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp, size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
		#distros = ['Ubuntu', 'Arch', 'Fedora', 'Debian', 'Mint']
		#cbServices = wx.ComboBox(panel, size=(170, 300), choices=distros, style=wx.CB_READONLY)
		lblDummy = wx.StaticText(panel, size=(196, 300))
		btnCancel = wx.Button(panel, label='Cancel [esc]', size=(90, 26))
		btnCancel.Bind(wx.EVT_BUTTON, self.cancelTask)
		btnSend = wx.Button(panel, label='Send [enter]', size=(90, 26))
		btnSend.Bind(wx.EVT_BUTTON, self.sendTask)

		#hbox2.Add(btnSettings)
		#hbox2.Add(cbServices, flag=wx.EXPAND)
		hbox2.Add(lblDummy)
		hbox2.Add(btnCancel)
		hbox2.Add(btnSend)
		vbox.Add(hbox2, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		panel.SetSizer(vbox)

	def sendTask(self, event):
		#toaddr = 'df.rodriguez143@gmail.com'
		toaddr = 'task@producteev.com'
		subject = self.txtTask.GetValue()

		self.onMinimize(None)
		self.txtTask.SetValue("")

		self.mailer.sendMail(toaddr, subject, '') # Send at the end to close faster the window

	def cancelTask(self, event):
		self.txtTask.SetValue("")
		self.onMinimize(None)

	def OnKeyUP(self, event):
		keyCode = event.GetKeyCode()
		if keyCode == wx.WXK_ESCAPE:
				self.ToggleShow(None)

	def onClose(self, event):
		self.tbIcon.RemoveIcon() # remove the systemtray icon when the program closes
		os._exit(1)

	# ==============================================================================================
	# ====================================== MAILER
	# ==============================================================================================

	def initMailer(self):
		self.mailer = Mailer('YOUR_MAIL', 'YOUR_PASSWORD')

	# ==============================================================================================
	# ====================================== HOTKEYS
	# ==============================================================================================

	def registerHotkey(self):
		self.hotKeyId = wx.NewId()
		print self.RegisterHotKey(
						self.hotKeyId, #a unique ID for this hotkey
						win32con.MOD_WIN, #the modifier key
						win32con.VK_DELETE) #the key to watch for
						#win32con.VK_INSERT) #the key to watch for
		self.Bind(wx.EVT_HOTKEY, self.handleHotKey, id=self.hotKeyId)

	def handleHotKey(self, evt):
		self.ToggleShow(None)

	# ==============================================================================================
	# ====================================== MINIMIZE TO TRAY
	# ==============================================================================================

	def registerMinimizeToTray(self):
		self.tbIcon = wx.TaskBarIcon()
		icon = wx.Icon("checkmark.ico", wx.BITMAP_TYPE_ICO)
		self.tbIcon.SetIcon(icon, "Tasks")

		wx.EVT_TASKBAR_LEFT_DCLICK(self.tbIcon, self.ToggleShow) # left click
		wx.EVT_TASKBAR_LEFT_UP(self.tbIcon, self.ToggleShow) # double left click
		wx.EVT_TASKBAR_RIGHT_UP(self.tbIcon, self.ToggleShow) # single left click

		self.Bind(wx.EVT_ICONIZE, self.onMinimize) # binding for minimizing

	def onMinimize(self, event):
		self.Hide() # this removes it from the taskbar so it only appears in the system tray

	def ToggleShow(self, event):
		if self.IsShown():
			self.Hide()
		else:
			self.Show()
			self.Restore() # take it out of the taskbar (otherwise it'll be shown but still minimized, which is awkward)



if __name__ == "__main__":
	app = wx.App(False)
	frame = MainFrame()
	app.MainLoop()
