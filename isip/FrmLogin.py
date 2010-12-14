import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class FrmLogin(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._lblTitle = System.Windows.Forms.Label()
		self._lblName = System.Windows.Forms.Label()
		self._lblPwd = System.Windows.Forms.Label()
		self._txtName = System.Windows.Forms.TextBox()
		self._txtPwd = System.Windows.Forms.TextBox()
		self._btnLogin = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# lblTitle
		# 
		self._lblTitle.Font = System.Drawing.Font("黑体", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 134)
		self._lblTitle.Location = System.Drawing.Point(12, 20)
		self._lblTitle.Name = "lblTitle"
		self._lblTitle.Size = System.Drawing.Size(264, 23)
		self._lblTitle.TabIndex = 0
		self._lblTitle.Text = "综合信息管理系统"
		self._lblTitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblName
		# 
		self._lblName.Font = System.Drawing.Font("黑体", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 134)
		self._lblName.Location = System.Drawing.Point(54, 67)
		self._lblName.Name = "lblName"
		self._lblName.Size = System.Drawing.Size(57, 23)
		self._lblName.TabIndex = 1
		self._lblName.Text = "用户："
		# 
		# lblPwd
		# 
		self._lblPwd.Font = System.Drawing.Font("黑体", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 134)
		self._lblPwd.Location = System.Drawing.Point(54, 99)
		self._lblPwd.Name = "lblPwd"
		self._lblPwd.Size = System.Drawing.Size(57, 23)
		self._lblPwd.TabIndex = 2
		self._lblPwd.Text = "密码："
		# 
		# txtName
		# 
		self._txtName.Font = System.Drawing.Font("黑体", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 134)
		self._txtName.Location = System.Drawing.Point(117, 65)
		self._txtName.Name = "txtName"
		self._txtName.Size = System.Drawing.Size(100, 26)
		self._txtName.TabIndex = 3
		self._txtName.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# txtPwd
		# 
		self._txtPwd.Font = System.Drawing.Font("黑体", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 134)
		self._txtPwd.Location = System.Drawing.Point(117, 97)
		self._txtPwd.Name = "txtPwd"
		self._txtPwd.PasswordChar = "#"
		self._txtPwd.Size = System.Drawing.Size(100, 26)
		self._txtPwd.TabIndex = 4
		self._txtPwd.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# btnLogin
		# 
		self._btnLogin.Font = System.Drawing.Font("黑体", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 134)
		self._btnLogin.Location = System.Drawing.Point(117, 145)
		self._btnLogin.Name = "btnLogin"
		self._btnLogin.Size = System.Drawing.Size(75, 23)
		self._btnLogin.TabIndex = 5
		self._btnLogin.Text = "登录"
		self._btnLogin.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.AcceptButton = self._btnLogin
		self.ClientSize = System.Drawing.Size(288, 194)
		self.Controls.Add(self._btnLogin)
		self.Controls.Add(self._txtPwd)
		self.Controls.Add(self._txtName)
		self.Controls.Add(self._lblPwd)
		self.Controls.Add(self._lblName)
		self.Controls.Add(self._lblTitle)
		self.Font = System.Drawing.Font("黑体", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 134)
		self.MaximizeBox = False
		self.Name = "MainForm"
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.Text = "系统登录"
		self.ResumeLayout(False)
		self.PerformLayout()

