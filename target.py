from paramiko import SSHClient
from scp import SCPClient
import paramiko
import os
import socket
import subprocess


class Target:
    def __init__(self, hostname, uname, pword, num):
        self.hostname = hostname
        self.uname = uname
        self.pword = pword
        self.target_num = num
        self.ssh = None 
        self.is_open = False 
    def conn(self):
        #print("Opening SSH connection to target...")
        self.ssh = paramiko.SSHClient()#use ssh.exec_command("") to perform an action.
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.hostname, username=self.uname, password=self.pword)
        scp = SCPClient(self.ssh.get_transport())#don't call this, but use the above function instead.
        self.is_open = True
    #TODO: fix rm -rf bug
    def scpFiles(filename, recur=True):#call this with a filename and false if it is a single file
        ssh.exec_command("rm " + filename)
        scp.put(filename, recursive=recur)
    
    def close(self):
        self.is_open = False
        self.ssh.close()


