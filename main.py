import logging.config
from threading import Thread

import psutil
import wx
import yaml
from scapy.all import *

from Frames import NMAPScanFrame
from Frames import PSFrame
from Frames import arpSpoofingFrame
from Frames import dataintegrtityFrame
from Frames import encryptDecryptFrame
from Frames import mainFrame
from Frames import passwordCheckerFrame
from Frames import passwordGenFrame
from Frames import webNetworkScanFrame
from Frames import webScanFrame
from Frames import webScannerFrame
from Frames import zipFrame
from Password_Checker import check as passwordCheck
from Password_Generator import generate as passwordGenerate
from arp_spoofing import ArpSpoofing
from brute_force_attack import ZipPwdCracker
from data_integrity import DI
from encrypt_decrypt import main as AES
from network_scanner import NetworkScanner
from web_scanner import WebScanner

EVT_RESULT_NET_SCAN_ID = wx.NewId()
EVT_RESULT_PORT_SCAN_ID = wx.NewId()
EVT_RESULT_FIND_ADMIN_ID = wx.NewId()


class GUI(mainFrame, passwordCheckerFrame, passwordGenFrame, arpSpoofingFrame, zipFrame, webScannerFrame,
          webNetworkScanFrame, NMAPScanFrame, PSFrame, webScanFrame, dataintegrtityFrame):

    def __init__(self, parent):
        mainFrame.__init__(self, parent)
        self.passwordCheckerFrame = None
        self.passwordGenFrame = None
        self.encryptDecryptFrame = None
        self.arpSpoofingFrame = None
        self.zipFrame = None
        self.webScannerFrame = None
        self.webNetworkScanFrame = None
        self.NMAPScanFrame = None
        self.PSFrame = None
        self.webScanFrame = None
        self.dataintegrtityFrame = None
        self.arpSpoofingThread = None
        with open("conf/logging.yml", 'r') as config_file:
            config_dict = yaml.load(config_file)
        logging.config.dictConfig(config_dict)
        self.logger = logging.getLogger(__name__)

    def btnActionExit(self, event):
        exit()

    # ----------------------------------------------------------#
    def btnActionPasswordCheck(self, event):
        password = self.passwordCheckerFrame.inpPass.GetValue()
        result = passwordCheck(password)
        self.passwordCheckerFrame.lblResult.SetLabel(result)
        self.passwordCheckerFrame.Layout()

    def btnActionPasswordChecker(self, event):
        self.passwordCheckerFrame = passwordCheckerFrame(None)
        self.passwordCheckerFrame.Bind(wx.EVT_BUTTON, self.btnActionPasswordCheck)
        self.passwordCheckerFrame.Show()

    # ----------------------------------------------------------#
    def btnActionPasswordGenerate(self, event):

        length = int(self.passwordGenFrame.inpLength.GetValue())

        CL = self.passwordGenFrame.ckCL.GetValue()
        SL = self.passwordGenFrame.ckSL.GetValue()
        NO = self.passwordGenFrame.ckNum.GetValue()
        SC = self.passwordGenFrame.ckSC.GetValue()

        # print(CL,SL)

        result = passwordGenerate(length, SL, CL, NO, SC)

        self.passwordGenFrame.inpResult.SetValue(result)

    def btnActionPasswordGenerator(self, event):
        self.passwordGenFrame = passwordGenFrame(None)
        self.passwordGenFrame.Bind(wx.EVT_BUTTON, self.btnActionPasswordGenerate)
        self.passwordGenFrame.Show()
        pass

    # ----------------------------------------------------------#
    def btnActionDecrypt(self, event):
        fileToDencrypt = self.encryptDecryptFrame.pikDecryptFile.GetPath()
        key = self.encryptDecryptFrame.inpDecKey.GetValue()

        # print(key)

        extension = os.path.splitext(fileToDencrypt)[1]

        # print(extension)

        # exit()

        with open(fileToDencrypt, "r") as f:
            data = f.read()

            encryptedData = AES(key).decrypt(data)

            newfilename = str(fileToDencrypt).replace(extension, "_decrypted_" + extension)
            with open(newfilename, "w") as ef:
                ef.write(encryptedData)

                self.encryptDecryptFrame.lblResult.SetLabel(
                    "File has been Decrypted and stored in " + newfilename)
                self.encryptDecryptFrame.Layout()

    def btnActionEncrypt(self, event):
        fileToEcncrypt = self.encryptDecryptFrame.pikEncryptFile.GetPath()
        key = self.encryptDecryptFrame.inpEncKey.GetValue()

        # encrypt_file(key,fileToEcncrypt)

        # ae= AES2(str(key)).encrypt_file(fileToEcncrypt,fileToEcncrypt+"00")

        # encryptf("1234",fileToEcncrypt)
        # exit()
        # print(key)

        extension = os.path.splitext(fileToEcncrypt)[1]

        try:
            with open(fileToEcncrypt, "r") as f:
                data = str(f.read())
        except:
            with open(fileToEcncrypt, "rb") as f:
                data = str(f.read())

        encryptedData = AES(key).encrypt(data)

        newfilename = str(fileToEcncrypt).replace(extension, "_Encrypted_" + extension)

        try:
            with open(newfilename, "w") as ef:
                ef.write(encryptedData)
        except:
            with open(newfilename, "wb") as ef:
                ef.write(encryptedData)

        self.encryptDecryptFrame.lblResult.SetLabel("File has been Encrypted and stored in " + newfilename)
        self.encryptDecryptFrame.Layout()

    def btnActionOpenAES(self, event):
        self.encryptDecryptFrame = encryptDecryptFrame(None)
        self.encryptDecryptFrame.btnEncrypt.Bind(wx.EVT_BUTTON, self.btnActionEncrypt)
        self.encryptDecryptFrame.btnDecrypt.Bind(wx.EVT_BUTTON, self.btnActionDecrypt)
        self.encryptDecryptFrame.Show()
        pass

    # ----------------------------------------------------------#

    def btnOpenZIP(self, event):
        self.zipFrame = zipFrame(None)
        self.zipFrame.btnAttack.Bind(wx.EVT_BUTTON, self.btnActionZIPAttach)
        self.zipFrame.btnAttack2.Bind(wx.EVT_BUTTON, self.btnActionBruteForceAttach)
        self.zipFrame.Show()

    def btnActionZIPAttach(self, event):
        zipFile = self.zipFrame.pikZiipFile.GetPath()
        dictFile = self.zipFrame.pikDictFile.GetPath()

        re = ZipPwdCracker().dictionary_attack(zipFile, dictFile)
        self.zipFrame.lblResult.SetLabel(re)
        self.zipFrame.Layout()

    def btnActionBruteForceAttach(self, event):
        zipFile = self.zipFrame.pikZiipFile.GetPath()
        dictFile = self.zipFrame.pikDictFile.GetPath()

        passLen = self.zipFrame.inpPassLen.GetValue() or 4

        re = ZipPwdCracker().brute_force_attack(zipFile, int(passLen))
        self.zipFrame.lblResult.SetLabel(str(re))
        self.zipFrame.Layout()

    # ----------------------------------------------------------#

    def btnOpenAdmin(self, event):
        self.webScannerFrame = webScannerFrame(None)
        self.webScannerFrame.btnScan.Bind(wx.EVT_BUTTON, self.btnActionScan)
        self.webScannerFrame.Show()

    def btnActionScan(self, event):

        url = self.webScannerFrame.inpURL.GetValue()
        self.Connect(-1, -1, EVT_RESULT_FIND_ADMIN_ID, self.on_find_admin_result)
        find_admin_thread = FindAdminThread(self, site=url)
        find_admin_thread.start()

    def on_find_admin_result(self, event):
        links = event.data
        allLinks = ""
        if not links or len(links) < 1:
            allLinks = "No result"
        else:
            for link in links:
                allLinks += link + "\n"

        self.webScannerFrame.lblResult.SetLabel(str(allLinks))
        self.webScannerFrame.Layout()

    # ----------------------------------------------------------#

    def btnOpenARP(self, event):
        self.arpSpoofingFrame = arpSpoofingFrame(None)
        self.arpSpoofingFrame.btnActionAttack.Bind(wx.EVT_BUTTON, self.btnActionAttach)
        self.arpSpoofingFrame.btnStop.Bind(wx.EVT_BUTTON, self.btnActionStop)
        self.arpSpoofingFrame.Show()

    def btnActionAttach(self, event):

        inpVictomIP = self.arpSpoofingFrame.inpVictomIP.GetValue()
        inpVictomMAC = self.arpSpoofingFrame.inpVictomMAC.GetValue()
        inpRouterIP = self.arpSpoofingFrame.inpRouterIP.GetValue()

        self.arpSpoofingFrame.btnStop.Enable()
        self.arpSpoofingFrame.btnActionAttack.Disable()

        self.arpSpoofingThread = ArpSpoofing(inpVictomIP, inpVictomMAC, gateway_ip=inpRouterIP)
        self.arpSpoofingThread.start()

    def btnActionStop(self, event):
        self.arpSpoofingFrame.btnStop.Disable()
        self.arpSpoofingFrame.btnActionAttack.Enable()
        self.arpSpoofingThread.stop()

    # ----------------------------------------------------------#

    def btnOpenNetworkScan(self, event):
        self.webNetworkScanFrame = webNetworkScanFrame(None)
        self.webNetworkScanFrame.btnScan.Bind(wx.EVT_BUTTON, self.btnActionNetworkScan)
        self.webNetworkScanFrame.Show()

    def btnActionNetworkScan(self, event):
        self.Connect(-1, -1, EVT_RESULT_NET_SCAN_ID, self.on_net_scan_result)
        netScanThread = NetScanThread(self)
        netScanThread.start()

    def on_net_scan_result(self, event):
        """Show Result status."""
        if event.data is None:
            # Thread aborted (using our convention of None return)
            self.webNetworkScanFrame.lblResult.SetLabel('Computation aborted')
        else:
            # Process results here
            current = self.webNetworkScanFrame.lblResult.GetLabel()
            self.webNetworkScanFrame.lblResult.SetLabel(
                current + "\nIP: " + str(event.data[0]) + "\tMAC: " + str(event.data[1]))
            self.webNetworkScanFrame.Layout()

    # Thread class that executes processing
    # ----------------------------------------------------------#

    def btnOpenNMAPScan(self, event):
        self.NMAPScanFrame = NMAPScanFrame(None)
        self.NMAPScanFrame.btnScan.Bind(wx.EVT_BUTTON, self.btnActionNMAPScan)
        self.NMAPScanFrame.Show()

    def btnActionNMAPScan(self, event):
        # self.NMAPScanFrame.lblResult.SetLabel("Please wait..")
        # self.NMAPScanFrame.Layout()

        self.Connect(-1, -1, EVT_RESULT_PORT_SCAN_ID, self.on_port_scan_result)
        hostname = self.NMAPScanFrame.inpIP.GetValue()
        port_scan_thread = PortScanThread(self, host=hostname)
        port_scan_thread.start()

    def on_port_scan_result(self, event):
        current = self.NMAPScanFrame.lblResult.GetLabel()

        self.NMAPScanFrame.lblResult.SetLabel(current + "\n" + str(event.data))
        self.NMAPScanFrame.Layout()

    # ----------------------------------------------------------#
    def btnOpenPSFrame(self, event):
        self.PSFrame = PSFrame(None)
        self.PSFrame.btnAttack.Bind(wx.EVT_BUTTON, self.btnActionPSAttack)
        self.PSFrame.btnStop.Bind(wx.EVT_BUTTON, self.btnActionPSStop)
        self.PSFrame.Show()

    def btnActionPSAttack(self, event):
        proc = subprocess.Popen(["python3 " + os.getcwd() + "/Packet_Sniff.py"],
                                shell=True,
                                stdin=None, stdout=None, stderr=None, close_fds=True)

        f = open(os.getcwd() + "/pid.txt", "w", encoding="utf-8")
        f.write(str(proc.pid))
        f.close()

        self.PSFrame.btnStop.Enable()
        self.PSFrame.btnAttack.Disable()

        self.PSFrame.lblResult.SetLabel("Working...")
        self.PSFrame.Layout()

    def btnActionPSStop(self, event):
        self.PSFrame.btnStop.Disable()
        self.PSFrame.btnAttack.Enable()

        f = open(os.getcwd() + "/pid.txt", "r", encoding="utf-8")
        pid = f.read()
        f.close()

        if int(pid.strip()) > 0:
            try:
                print("Kill process:", pid)
                p = psutil.Process(int(pid))
                p.terminate()
                p.kill()
            except BaseException as error:
                print(error)

        self.PSFrame.lblResult.SetLabel("Check packet_sniff.txt for results")
        self.PSFrame.Layout()

    # ----------------------------------------------------------#

    def btnOpenWebScan(self, event):
        self.webScanFrame = webScanFrame(None)
        self.webScanFrame.btnScan.Bind(wx.EVT_BUTTON, self.btnActionWebScan)
        self.webScanFrame.Show()

    def btnActionWebScan(self, event):

        url = self.webScanFrame.inpURL.GetValue()
        info = WebScanner().whois(url)

        if not "http://" in url and not "https://" in url:
            url = "http://" + url
        # self.webScanFrame.lblResult.SetLabel(str(info))
        self.webScanFrame.txtResult.SetValue(str(info))
        self.webScanFrame.Layout()

    # ----------------------------------------------------------#

    def btnOpenDIFrame(self, event):
        self.dataintegrtityFrame = dataintegrtityFrame(None)
        self.dataintegrtityFrame.btnScan.Bind(wx.EVT_BUTTON, self.btnActionDIScan)
        self.dataintegrtityFrame.Show()

    def btnActionDIScan(self, event):

        sha1 = self.dataintegrtityFrame.inpURL.GetValue()
        file = self.dataintegrtityFrame.pikFile.GetPath()

        re = DI(file, sha1)

        self.dataintegrtityFrame.txtResult.SetValue(str(re))
        self.dataintegrtityFrame.Layout()

    # ----------------------------------------------------------#


class ResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""

    def __init__(self, even_id, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(even_id)
        self.data = data


class NetScanThread(Thread):
    def __init__(self, notify_window):
        Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = False

    def run(self):
        NetworkScanner().ping_sweep_async(callback=self.on_host_online)
        wx.PostEvent(self._notify_window, ResultEvent(EVT_RESULT_NET_SCAN_ID, "DONE"))

    def on_host_online(self, host):
        wx.PostEvent(self._notify_window, ResultEvent(EVT_RESULT_NET_SCAN_ID, host))


class PortScanThread(Thread):
    def __init__(self, notify_window, host):
        Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = False
        self._host = host

    def run(self):
        NetworkScanner().scan_ports_async(self._host, callback=self.on_port_open)
        wx.PostEvent(self._notify_window, ResultEvent(EVT_RESULT_PORT_SCAN_ID, "DONE"))

    def on_port_open(self, port):
        wx.PostEvent(self._notify_window, ResultEvent(EVT_RESULT_PORT_SCAN_ID, port))


class FindAdminThread(Thread):
    def __init__(self, notify_window, site):
        Thread.__init__(self)
        self._notify_window = notify_window
        self._site = site

    def run(self):
        links = WebScanner().find_admin(self._site)
        wx.PostEvent(self._notify_window, ResultEvent(EVT_RESULT_FIND_ADMIN_ID, links))


app = wx.App()
frame = GUI(None)
frame.Show()
# frame.Maximize()

app.MainLoop()
