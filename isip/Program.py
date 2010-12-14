import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Windows.Forms import Application
import FrmLogin

Application.EnableVisualStyles()
form = FrmLogin.FrmLogin()
Application.Run(form)
