import wx
import os
from ConfigParser import SafeConfigParser

class SettingsForm(wx.Frame):

	def __init__(self, parent, file):
		wx.Frame.__init__(self, parent, wx.ID_ANY, title='Settings',
											style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
		self.settings = Settings(file)

		self.createControls()
		self.bindEvents()
		self.doLayout()

		self.CenterOnParent()
		#self.GetParent().Enable(False)
		self.Show(True)
		self.Raise()

	# ==============================================================================================
	# ====================================== UI
	# ==============================================================================================

	def createControls(self):
		self.panel = wx.Panel(self)

		self.lblEmail = wx.StaticText(self.panel, label="Email:", size = (55, 22))
		self.txtEmail = wx.TextCtrl(self.panel, value=self.settings.getEmail(), size = (200, 22))
		self.lblPassword = wx.StaticText(self.panel, label="Password:", size = (55, 22))
		self.txtPassword = wx.TextCtrl(self.panel, value=self.settings.getPassword(), style = wx.TE_PASSWORD, size = (200, 22))
		self.lblEmailTo = wx.StaticText(self.panel, label="Send to:", size = (55, 22))
		self.txtEmailTo = wx.TextCtrl(self.panel, value=self.settings.getEmailTo(), size = (200, 22))
		self.btnSave = wx.Button(self.panel, label="Save", size = (100, 26))
		self.btnCancel = wx.Button(self.panel, label="Cancel", size = (100, 26))

	def doLayout(self):
		icon = wx.Icon("images/settings.ico", wx.BITMAP_TYPE_ICO)
		self.SetIcon(icon)

		vbox = wx.BoxSizer(orient=wx.VERTICAL)

		# Prepare some reusable arguments for calling sizer.Add():
		expandOption = dict(flag=wx.EXPAND)
		noOptions = dict()
		emptySpace = (0, 0)

		# Line 1
		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		hbox1.Add(self.lblEmail, flag=wx.TOP, border=4)
		hbox1.Add(self.txtEmail)
		vbox.Add(hbox1, 0, wx.ALL|wx.EXPAND, 5)

		# Line 2
		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		hbox2.Add(self.lblPassword, flag=wx.TOP, border=4)
		hbox2.Add(self.txtPassword)
		vbox.Add(hbox2, 0, wx.BOTTOM|wx.LEFT|wx.RIGHT, 5)

		# Line 3
		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		hbox3.Add(self.lblEmailTo, flag=wx.TOP, border=4)
		hbox3.Add(self.txtEmailTo)
		vbox.Add(hbox3, 0, wx.BOTTOM|wx.LEFT|wx.RIGHT, 5)

		# Line Button
		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		hbox4.Add(self.btnCancel, 0, wx.ALL, 5)
		hbox4.Add(self.btnSave, 0, wx.ALL, 5)
		vbox.Add(hbox4, 0, wx.BOTTOM|wx.LEFT|wx.RIGHT|wx.CENTER, 5)

		# Main
		self.panel.SetSizer(vbox)
		vbox.Fit(self)

	# ==============================================================================================
	# ====================================== EVENTS
	# ==============================================================================================

	def bindEvents(self):
		self.btnSave.Bind(wx.EVT_BUTTON, self.onSave)
		self.btnCancel.Bind(wx.EVT_BUTTON, self.onCancel)

		wx.EVT_CLOSE(self, self.onClose) # triggered when the app is closed

	def onSave(self, event):
		self.settings.setEmail(self.txtEmail.GetValue())
		self.settings.setPassword(self.txtPassword.GetValue())
		self.settings.setEmailTo(self.txtEmailTo.GetValue())
		#self.GetParent().Enable(True)
		self.Destroy()

	def onCancel(self, event):
		#self.GetParent().Enable(True)
		self.Destroy()

	def onClose(self, event):
		#self.GetParent().Enable(True)
		self.Destroy()


# ==============================================================================================
# ====================================== SETTINGS
# ==============================================================================================

class Settings(object):
	def __init__(self, file):
		self.file = file
		if os.path.exists(file):
			self.config = SafeConfigParser()
			self.config.read(file)
		else:
			self.config = SafeConfigParser()
			self.config.read(file)
			self.config.add_section('General')
			self.setEmail("i.e. df.rodriguez143@gmail.com")
			self.setPassword("***")
			self.setEmailTo("i.e. c04cdcccd@nirvanahq.in")

			with open(file, 'wb') as configfile:
				self.config.write(configfile)


	def getEmail(self):
		return self.config.get('General', 'email')

	def setEmail(self, email):
		self.config.set('General', 'email', email)
		with open(self.file, 'wb') as configfile:
				self.config.write(configfile)

	def getPassword(self):
		return self.config.get('General', 'password')

	def setPassword(self, password):
		self.config.set('General', 'password', password)
		with open(self.file, 'wb') as configfile:
				self.config.write(configfile)

	def getEmailTo(self):
		return self.config.get('General', 'emailto')

	def setEmailTo(self, emailto):
		self.config.set('General', 'emailto', emailto)
		with open(self.file, 'wb') as configfile:
				self.config.write(configfile)

if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = SettingsForm(None, 'settings.cfg')
	app.MainLoop()
	#s = Settings('settings.cfg')