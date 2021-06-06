
# Search
			elif Type == "editline":
				parent.Children[Index] = EditLine()
				parent.Children[Index].SetParent(parent)
				self.LoadElementEditLine(parent.Children[Index], ElementValue, parent)

# Add after

			elif Type == "editline_new":
				parent.Children[Index] = EditLineNew()
				parent.Children[Index].SetParent(parent)
				self.LoadElementEditLine(parent.Children[Index], ElementValue, parent)


# Search

		if value.has_key("secret_flag"):
			window.SetSecret(value["secret_flag"])

# Add after

		if value.has_key("info_msg"):
			window.SetInfoMessage(value["info_msg"])


# Search

	RegisterToolTipWindow("TEXT", TextLine)

# Add before

class EditLineNew(EditLine):
	def __init__(self):
		EditLine.__init__(self)

		self.backText = TextLine()
		self.backText.SetParent(self)
		self.backText.SetPosition(0,0)
		self.backText.SetFontColor(128,128,128)

	def __del__(self):
		EditLine.__del__(self)

	def SetInfoMessage(self, msg):
		self.backText.SetText(msg)

		if len(self.GetText()) > 0:
			self.backText.Hide()
		else:
			self.backText.Show()

	def OnIMEUpdate(self):
		EditLine.OnIMEUpdate(self)
		if len(self.GetText()) > 0:
			self.backText.Hide()
		else:
			self.backText.Show()
