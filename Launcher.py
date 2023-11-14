# This license applies only to THIS FILE and files compiled from it.
# Copyright (c) 2023, Radium-bit
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     # Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     # Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     # Neither the name of the Radium-bit nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE RADIUM-BIT AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE RADIUM-BIT AND CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.}}

import os
import re
import locale
from tkinter import messagebox
def Start():
    language,_=locale.getdefaultlocale()
    tsklist="tasklist"
    callAria2=r"start .\aria2\aria2c.exe --conf=.\aria2\aria2.conf"
    callAriaNG_Native=r"start .\AriaNg_Native.exe"
    ProcessInfo=os.popen(tsklist).read()
    if re.search("aria2",ProcessInfo)==None:
        if re.search("AriaNg",ProcessInfo)==None:
          try:
            os.popen(callAria2)
            os.popen(callAriaNG_Native)
            # print("StartALL")
          except Exception as e:
              if language.startswith('zh'):
                  messagebox.showwarning("启动失败，请检查路径",{e})
              else:
                  messagebox.showwarning("Startup failed, please check the path",{e})

        else:
            try:
              os.popen(callAria2)
              # print("StartCore")
            except Exception as e:
                if language.startswith('zh'):
                    messagebox.showwarning("启动失败，请检查路径", {e})
                else:
                    messagebox.showwarning("Startup failed, please check the path",{e})
    else:
        if re.search("AriaNg",ProcessInfo)==None:
            try:
              os.popen(callAriaNG_Native)
              # print("StartGUI")
            except Exception as e:
                if language.startswith('zh'):
                    messagebox.showwarning("启动失败，请检查路径", {e})
                else:
                    messagebox.showwarning("Startup failed, please check the path",{e})
        else:
            # print("ALL HAS BEEN STARTED")
            if language.startswith('zh'):
              messagebox.showwarning("注意","已经在运行\n请勿重复运行！")
            else:
              messagebox.showwarning("Note", "Already running\nDo not run again!")

Start()