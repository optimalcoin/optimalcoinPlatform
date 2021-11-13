
    # Optimal Algorand Smart Contract Solutions: Increased Tax Efficiency Empowered by Blockchain Technology
    # Optimal token is a part of the the Optimal DApp
    # Note that this token is under development
    # Warning: This module is under the development, and therefore, it has not been controlled in terms of security issues
    
import algosdk #line:1
from cryptography .fernet import Fernet ,InvalidToken #line:3
from cryptography .hazmat .backends import default_backend #line:4
from cryptography .hazmat .primitives import hashes #line:5
from cryptography .hazmat .primitives .kdf .pbkdf2 import PBKDF2HMAC #line:6
class algoWallet :#line:9  
    
    def __init__ (O00O000O0O0OOO0O0 ,filename ="algoWallet"):#line:12
        ""#line:21
        O00O000O0O0OOO0O0 .walletFileName =filename #line:22
        O00O000O0O0OOO0O0 .internalWallet ={}#line:23
        try :#line:24
            O00O000O0O0OOO0O0 .importWallet (filename )#line:25
        except FileNotFoundError :#line:26
            O00O000O0O0OOO0O0 .exportWallet (filename )#line:27
    def setWalletFileName (O0OOOO0OO0OO00OO0 ,O00OOOOO0OOOO00O0 :str ):#line:34
        ""#line:40
        O0OOOO0OO0OO00OO0 .walletFileName =O00OOOOO0OOOO00O0 #line:41
    def importWallet (OOOO0O00OOOOO00O0 ,fileName :str =None ):#line:44
        ""#line:50
        import json #line:52
        if not fileName :#line:53
            fileName =OOOO0O00OOOOO00O0 .walletFileName #line:54
        OOOO0O00OOOOO00O0 .internalWallet =json .load (open (fileName ,'r'))#line:55
    def exportWallet (OO0O00O00OO0O0OO0 ,fileName :str =None ):#line:58
        ""#line:64
        import json #line:65
        if not fileName :#line:66
            fileName =OO0O00O00OO0O0OO0 .walletFileName #line:67
        with open (fileName ,'w')as OO0O00O0OO0O00O00 :#line:68
            json .dump (OO0O00O00OO0O0OO0 .internalWallet ,OO0O00O0OO0O00O00 ,indent =4 )#line:69
    def genAccount (O0O00OOO0O000OO00 ,OOOO00O00OOOOOO0O :str ,password :str =None ,pub_crypt :bool =False ):#line:72
        ""#line:80
        OOOOOO0OO0OOOO000 ,OO000OOO000O0OOO0 =algosdk .account .generate_account ()#line:82
        O0O00OOO0O000OO00 .makeAccount (OOOO00O00OOOOOO0O ,OOOOOO0OO0OOOO000 ,password ,pub_crypt )#line:83

