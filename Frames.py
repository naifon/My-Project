# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version May 29 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 851,610 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTitle = wx.StaticText( self, wx.ID_ANY, u"Penetration Test Tools", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.lblTitle.Wrap( -1 )
		self.lblTitle.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer1.Add( self.lblTitle, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.ALL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )
		
		wSizer23 = wx.WrapSizer( wx.HORIZONTAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.lbl1 = wx.StaticText( self, wx.ID_ANY, u"Password Tools", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )
		self.lbl1.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer2.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnOne = wx.Button( self, wx.ID_ANY, u"Password Generator", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnOne, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnTwo = wx.Button( self, wx.ID_ANY, u"Password Checker", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnTwo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnThree = wx.Button( self, wx.ID_ANY, u"Brute Force Attack", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnThree, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lbl2 = wx.StaticText( self, wx.ID_ANY, u"Cryptography", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl2.Wrap( -1 )
		self.lbl2.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer2.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnFour = wx.Button( self, wx.ID_ANY, u"Integrity of Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnFour, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnFive = wx.Button( self, wx.ID_ANY, u"Encrypt/ Decrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnFive, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		wSizer23.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		wSizer24 = wx.WrapSizer( wx.HORIZONTAL )
		
		wSizer24.SetMinSize( wx.Size( 100,-1 ) ) 
		self.m_staticline41 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		wSizer24.Add( self.m_staticline41, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		wSizer23.Add( wSizer24, 1, wx.EXPAND, 5 )
		
		bSizer55 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.lbl4 = wx.StaticText( self, wx.ID_ANY, u"Data Collection", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl4.Wrap( -1 )
		self.lbl4.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer10.Add( self.lbl4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnSix = wx.Button( self, wx.ID_ANY, u"NMAP", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.btnSix, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnSeven = wx.Button( self, wx.ID_ANY, u"Network Scanner", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.btnSeven, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnEight = wx.Button( self, wx.ID_ANY, u"Web Information Scanner", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.btnEight, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lbl3 = wx.StaticText( self, wx.ID_ANY, u"ARP Spoofing", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )
		self.lbl3.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer10.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnNine = wx.Button( self, wx.ID_ANY, u"ARP Spoofing", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.btnNine, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline71 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline71, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lbl31 = wx.StaticText( self, wx.ID_ANY, u"Packet Sniffing", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl31.Wrap( -1 )
		self.lbl31.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer10.Add( self.lbl31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnTen = wx.Button( self, wx.ID_ANY, u"Packet Sniffing", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.btnTen, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline711 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline711, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lbl311 = wx.StaticText( self, wx.ID_ANY, u"Admin Panel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl311.Wrap( -1 )
		self.lbl311.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer10.Add( self.lbl311, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnTen1 = wx.Button( self, wx.ID_ANY, u"Admin Panel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.btnTen1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer55.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		
		wSizer23.Add( bSizer55, 0, wx.EXPAND|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer1.Add( wSizer23, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer11 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.m_staticline51 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		wSizer11.Add( self.m_staticline51, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer1.Add( wSizer11, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		wSizer1 = wx.WrapSizer( wx.HORIZONTAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnAbout = wx.Button( self, wx.ID_ANY, u"About", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btnAbout, 1, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		wSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnExit = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )
		
		
		wSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( wSizer1, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.LEFT, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnOne.Bind( wx.EVT_BUTTON, self.btnActionPasswordGenerator )
		self.btnTwo.Bind( wx.EVT_BUTTON, self.btnActionPasswordChecker )
		self.btnThree.Bind( wx.EVT_BUTTON, self.btnOpenZIP )
		self.btnFour.Bind( wx.EVT_BUTTON, self.btnOpenDIFrame )
		self.btnFive.Bind( wx.EVT_BUTTON, self.btnActionOpenAES )
		self.btnSix.Bind( wx.EVT_BUTTON, self.btnOpenNMAPScan )
		self.btnSeven.Bind( wx.EVT_BUTTON, self.btnOpenNetworkScan )
		self.btnEight.Bind( wx.EVT_BUTTON, self.btnOpenWebScan )
		self.btnNine.Bind( wx.EVT_BUTTON, self.btnOpenARP )
		self.btnTen.Bind( wx.EVT_BUTTON, self.btnOpenPSFrame )
		self.btnTen1.Bind( wx.EVT_BUTTON, self.btnOpenAdmin )
		self.btnExit.Bind( wx.EVT_BUTTON, self.btnActionExit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnActionPasswordGenerator( self, event ):
		event.Skip()
	
	def btnActionPasswordChecker( self, event ):
		event.Skip()
	
	def btnOpenZIP( self, event ):
		event.Skip()
	
	def btnOpenDIFrame( self, event ):
		event.Skip()
	
	def btnActionOpenAES( self, event ):
		event.Skip()
	
	def btnOpenNMAPScan( self, event ):
		event.Skip()
	
	def btnOpenNetworkScan( self, event ):
		event.Skip()
	
	def btnOpenWebScan( self, event ):
		event.Skip()
	
	def btnOpenARP( self, event ):
		event.Skip()
	
	def btnOpenPSFrame( self, event ):
		event.Skip()
	
	def btnOpenAdmin( self, event ):
		event.Skip()
	
	def btnActionExit( self, event ):
		event.Skip()
	

###########################################################################
## Class passwordCheckerFrame
###########################################################################

class passwordCheckerFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 646,419 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTitle = wx.StaticText( self, wx.ID_ANY, u"Password Checker", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.lblTitle.Wrap( -1 )
		self.lblTitle.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer11.Add( self.lblTitle, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline10, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer2 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Enter a Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		wSizer2.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.inpPass = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.inpPass, 0, wx.ALL, 5 )
		
		self.m_button34 = wx.Button( self, wx.ID_ANY, u"Check", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.m_button34, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( wSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer14.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lblResult = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblResult.Wrap( -1 )
		bSizer14.Add( self.lblResult, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer11.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button34.Bind( wx.EVT_BUTTON, self.btnActionPasswordCheck )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnActionPasswordCheck( self, event ):
		event.Skip()
	

###########################################################################
## Class passwordGenFrame
###########################################################################

class passwordGenFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 646,419 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTitle = wx.StaticText( self, wx.ID_ANY, u"Password Generator", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.lblTitle.Wrap( -1 )
		self.lblTitle.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer11.Add( self.lblTitle, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline10, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Password Options", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		bSizer11.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer5 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Length", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		wSizer5.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		self.inpLength = wx.TextCtrl( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer5.Add( self.inpLength, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( wSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.ckNum = wx.CheckBox( self, wx.ID_ANY, u"Numbers", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ckNum.SetValue(True) 
		bSizer21.Add( self.ckNum, 0, wx.ALL, 5 )
		
		self.ckCL = wx.CheckBox( self, wx.ID_ANY, u"Capital letters", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ckCL.SetValue(True) 
		bSizer21.Add( self.ckCL, 0, wx.ALL, 5 )
		
		self.ckSL = wx.CheckBox( self, wx.ID_ANY, u"Small Letters", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ckSL.SetValue(True) 
		bSizer21.Add( self.ckSL, 0, wx.ALL, 5 )
		
		self.ckSC = wx.CheckBox( self, wx.ID_ANY, u"Special characters", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ckSC.SetValue(True) 
		bSizer21.Add( self.ckSC, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer21, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer2 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.btnGenerate = wx.Button( self, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.btnGenerate, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( wSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer14.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.inpResult = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inpResult.SetMinSize( wx.Size( 200,-1 ) )
		
		bSizer14.Add( self.inpResult, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lblResult = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblResult.Wrap( -1 )
		bSizer14.Add( self.lblResult, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer11.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnGenerate.Bind( wx.EVT_BUTTON, self.btnActionPasswordGenerate )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnActionPasswordGenerate( self, event ):
		event.Skip()
	

###########################################################################
## Class encryptDecryptFrame
###########################################################################

class encryptDecryptFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 646,419 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTitle = wx.StaticText( self, wx.ID_ANY, u"Encrypt/ Decrypt", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.lblTitle.Wrap( -1 )
		self.lblTitle.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer11.Add( self.lblTitle, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline10, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer2 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Open file to encrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		wSizer2.Add( self.m_staticText19, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.pikEncryptFile = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file to encrypt", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		wSizer2.Add( self.pikEncryptFile, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.lbl1 = wx.StaticText( self, wx.ID_ANY, u"Key", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )
		wSizer2.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.inpEncKey = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.inpEncKey, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnEncrypt = wx.Button( self, wx.ID_ANY, u"Encrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.btnEncrypt, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer11.Add( wSizer2, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer21 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.m_staticText191 = wx.StaticText( self, wx.ID_ANY, u"Open file to decrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText191.Wrap( -1 )
		wSizer21.Add( self.m_staticText191, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.pikDecryptFile = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file to encrypt", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		wSizer21.Add( self.pikDecryptFile, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.lbl11 = wx.StaticText( self, wx.ID_ANY, u"Key", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl11.Wrap( -1 )
		wSizer21.Add( self.lbl11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.inpDecKey = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer21.Add( self.inpDecKey, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnDecrypt = wx.Button( self, wx.ID_ANY, u"Decrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer21.Add( self.btnDecrypt, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer11.Add( wSizer21, 0, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer14.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lblResult = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblResult.Wrap( -1 )
		bSizer14.Add( self.lblResult, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer11.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnEncrypt.Bind( wx.EVT_BUTTON, self.btnActionEncrypt )
		self.btnDecrypt.Bind( wx.EVT_BUTTON, self.btnActionDecrypt )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnActionEncrypt( self, event ):
		event.Skip()
	
	def btnActionDecrypt( self, event ):
		event.Skip()
	

###########################################################################
## Class zipFrame
###########################################################################

class zipFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 646,419 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTitle = wx.StaticText( self, wx.ID_ANY, u"Zip Bruce Force", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.lblTitle.Wrap( -1 )
		self.lblTitle.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer11.Add( self.lblTitle, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline10, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer2 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.fileZip = wx.StaticText( self, wx.ID_ANY, u"Choose zip file            ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fileZip.Wrap( -1 )
		wSizer2.Add( self.fileZip, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.pikZiipFile = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file to encrypt", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		wSizer2.Add( self.pikZiipFile, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer11.Add( wSizer2, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer21 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.fileDict = wx.StaticText( self, wx.ID_ANY, u"Choose Dictionary file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fileDict.Wrap( -1 )
		wSizer21.Add( self.fileDict, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.pikDictFile = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file to encrypt", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		wSizer21.Add( self.pikDictFile, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer11.Add( wSizer21, 0, wx.EXPAND, 5 )
		
		wSizer211 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.fileDi = wx.StaticText( self, wx.ID_ANY, u"Password Length         ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fileDi.Wrap( -1 )
		wSizer211.Add( self.fileDi, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.inpPassLen = wx.TextCtrl( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer211.Add( self.inpPassLen, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( wSizer211, 0, wx.EXPAND, 5 )
		
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline222 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer141.Add( self.m_staticline222, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAttack = wx.Button( self, wx.ID_ANY, u"Dictionray Attack", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.btnAttack, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnAttack2 = wx.Button( self, wx.ID_ANY, u"Brute Force Attack", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.btnAttack2, 0, wx.ALL, 5 )
		
		
		bSizer141.Add( bSizer42, 0, wx.ALIGN_CENTER, 5 )
		
		
		bSizer11.Add( bSizer141, 0, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer14.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lblResult = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblResult.Wrap( -1 )
		bSizer14.Add( self.lblResult, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer11.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnAttack.Bind( wx.EVT_BUTTON, self.btnActionAttack )
		self.btnAttack2.Bind( wx.EVT_BUTTON, self.btnActionBruteForceAttack )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnActionAttack( self, event ):
		event.Skip()
	
	def btnActionBruteForceAttack( self, event ):
		event.Skip()
	

###########################################################################
## Class arpSpoofingFrame
###########################################################################

class arpSpoofingFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 646,419 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTitle = wx.StaticText( self, wx.ID_ANY, u"ARP spoofing", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.lblTitle.Wrap( -1 )
		self.lblTitle.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer11.Add( self.lblTitle, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline10, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer2 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Victom IP Address     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		wSizer2.Add( self.m_staticText19, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.inpVictomIP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.inpVictomIP, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer11.Add( wSizer2, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer21 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.m_staticText191 = wx.StaticText( self, wx.ID_ANY, u"Victom MAC Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText191.Wrap( -1 )
		wSizer21.Add( self.m_staticText191, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.inpVictomMAC = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer21.Add( self.inpVictomMAC, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer11.Add( wSizer21, 0, wx.EXPAND, 5 )
		
		wSizer211 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.m_staticText1911 = wx.StaticText( self, wx.ID_ANY, u"Router IP Address     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1911.Wrap( -1 )
		wSizer211.Add( self.m_staticText1911, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.inpRouterIP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer211.Add( self.inpRouterIP, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer11.Add( wSizer211, 0, wx.EXPAND, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnActionAttack = wx.Button( self, wx.ID_ANY, u"Attack", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.btnActionAttack, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnStop = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnStop.Enable( False )
		
		bSizer32.Add( self.btnStop, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer32, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer14.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lblResult = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblResult.Wrap( -1 )
		bSizer14.Add( self.lblResult, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer11.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnStop.Bind( wx.EVT_BUTTON, self.btnActionStop )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnActionStop( self, event ):
		event.Skip()
	

###########################################################################
## Class webScannerFrame
###########################################################################

class webScannerFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 646,419 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.Admin = wx.StaticText( self, wx.ID_ANY, u"Admin Panel Finder", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.Admin.Wrap( -1 )
		self.Admin.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer11.Add( self.Admin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline10, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer2 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		wSizer2.Add( self.m_staticText19, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.inpURL = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		wSizer2.Add( self.inpURL, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer11.Add( wSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnScan = wx.Button( self, wx.ID_ANY, u"Scan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.btnScan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer11.Add( bSizer32, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer14.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lblResult = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblResult.Wrap( -1 )
		bSizer14.Add( self.lblResult, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer11.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnScan.Bind( wx.EVT_BUTTON, self.btnActionScan )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnActionScan( self, event ):
		event.Skip()
	

###########################################################################
## Class webNetworkScanFrame
###########################################################################

class webNetworkScanFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 646,419 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.Admin = wx.StaticText( self, wx.ID_ANY, u"Network Scanner", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.Admin.Wrap( -1 )
		self.Admin.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer11.Add( self.Admin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline10, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnScan = wx.Button( self, wx.ID_ANY, u"Scan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.btnScan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer11.Add( bSizer32, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer14.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lblResult = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblResult.Wrap( -1 )
		bSizer14.Add( self.lblResult, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer11.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnScan.Bind( wx.EVT_BUTTON, self.btnActionScan )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnActionScan( self, event ):
		event.Skip()
	

###########################################################################
## Class NMAPScanFrame
###########################################################################

class NMAPScanFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 646,419 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.Admin = wx.StaticText( self, wx.ID_ANY, u"NMAP", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.Admin.Wrap( -1 )
		self.Admin.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer11.Add( self.Admin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline10, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer2 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"IP Address     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		wSizer2.Add( self.m_staticText19, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.inpIP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		wSizer2.Add( self.inpIP, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnScan = wx.Button( self, wx.ID_ANY, u"Scan", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.btnScan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer11.Add( wSizer2, 0, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer14.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lblResult = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblResult.Wrap( -1 )
		bSizer14.Add( self.lblResult, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer11.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnScan.Bind( wx.EVT_BUTTON, self.btnActionNMAPScan )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnActionNMAPScan( self, event ):
		event.Skip()
	

###########################################################################
## Class webScanFrame
###########################################################################

class webScanFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 646,419 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.Admin = wx.StaticText( self, wx.ID_ANY, u"Web Information Scanner", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.Admin.Wrap( -1 )
		self.Admin.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer11.Add( self.Admin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline10, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer2 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		wSizer2.Add( self.m_staticText19, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.inpURL = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		wSizer2.Add( self.inpURL, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnScan = wx.Button( self, wx.ID_ANY, u"Scan", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer2.Add( self.btnScan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer11.Add( wSizer2, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer11.Add( bSizer32, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer14.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.txtResult = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP|wx.HSCROLL|wx.VSCROLL )
		bSizer14.Add( self.txtResult, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer11.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnScan.Bind( wx.EVT_BUTTON, self.btnActionWebScan )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnActionWebScan( self, event ):
		event.Skip()
	

###########################################################################
## Class dataintegrtityFrame
###########################################################################

class dataintegrtityFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 646,419 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.Admin = wx.StaticText( self, wx.ID_ANY, u"Data Integrity", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.Admin.Wrap( -1 )
		self.Admin.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer11.Add( self.Admin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline10, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer2 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"SHA255", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		wSizer2.Add( self.m_staticText19, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.inpURL = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		wSizer2.Add( self.inpURL, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer11.Add( wSizer2, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		wSizer21 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.fileZip = wx.StaticText( self, wx.ID_ANY, u"Choose file            ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fileZip.Wrap( -1 )
		wSizer21.Add( self.fileZip, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.pikFile = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file to encrypt", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		wSizer21.Add( self.pikFile, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer11.Add( wSizer21, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline221 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer141.Add( self.m_staticline221, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer141, 0, wx.EXPAND, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnScan = wx.Button( self, wx.ID_ANY, u"Check", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.btnScan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer11.Add( bSizer32, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer14.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lblResult = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblResult.Wrap( -1 )
		bSizer14.Add( self.lblResult, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_LEFT|wx.ALL|wx.LEFT, 5 )
		
		
		bSizer11.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnScan.Bind( wx.EVT_BUTTON, self.btnActionDIScan )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnActionDIScan( self, event ):
		event.Skip()
	

###########################################################################
## Class PSFrame
###########################################################################

class PSFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 646,419 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.Admin = wx.StaticText( self, wx.ID_ANY, u"Packet Sniffer", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.Admin.Wrap( -1 )
		self.Admin.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande" ) )
		
		bSizer11.Add( self.Admin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline10, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAttack = wx.Button( self, wx.ID_ANY, u"Sniff", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.btnAttack, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnStop = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnStop.Enable( False )
		
		bSizer32.Add( self.btnStop, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer32, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer14.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lblResult = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblResult.Wrap( -1 )
		bSizer14.Add( self.lblResult, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer11.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnAttack.Bind( wx.EVT_BUTTON, self.btnActionPSAttack )
		self.btnStop.Bind( wx.EVT_BUTTON, self.btnActionStop )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnActionPSAttack( self, event ):
		event.Skip()
	
	def btnActionStop( self, event ):
		event.Skip()
	

