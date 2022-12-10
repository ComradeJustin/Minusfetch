
try: 
    import psutil
    import cpuinfo
    import platform
    import socket
    import os
    import distro

    from prompt_toolkit.application import Application
    import prompt_toolkit.formatted_text 
    from prompt_toolkit.key_binding import KeyBindings
    from prompt_toolkit.layout import (
        FormattedTextControl,
        HSplit,
        Layout,
         VSplit,
        Window,
        WindowAlign,
    )
    import prompt_toolkit.layout.dimension
    from prompt_toolkit.widgets import Dialog, Label
    import time
    import tkinter as tk
    import urllib.request
except:
    print("Get the Requirements")



def get_curr_screen_geometry():

    root = tk.Tk()
    root.update_idletasks()
    root.attributes('-fullscreen', True)
    root.state('iconic')
    geometry = root.winfo_geometry()
    root.destroy()
    return geometry
# Code shamelessly stolen from https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python/56913005#56913005


resolution = str(get_curr_screen_geometry())
ip = str(urllib.request.urlopen('https://ident.me').read().decode('utf8'))
PyVers= 'Python '+str(platform.python_version())


user = str(os.getenv('username')).upper()
os = platform.platform()

Uptime = time.time() - psutil.boot_time()
Time_elapsed = str(round(Uptime/60/60, 2)) + ' Hours'
#Gets Uptime


#Checks for Linux Distro if there is any
if os.upper().__contains__('windows'.upper()): 
    oshead = 'Windows'
    distro = 'No Linux'
elif os.upper().__contains__('linux'.upper()): 
    oshead = 'Linux'
    distro = str(distro.linux_distribution())
else: 
    oshead = 'MACOS'
    distro =  'No Linux'




def main():
    # Key bindings.
    kb = KeyBindings()

    @kb.add("c-c")
    def _(event):
        "Quit when control-c is pressed."
        event.app.exit()

    Usingcpu = str(cpuinfo.get_cpu_info()['brand_raw'])
    
    Rammain = str(int(psutil.virtual_memory().total/1000/1000))+"MB"

    Ram = str(int(psutil.virtual_memory().available/1000/1000))+"MB"
    Hostname = socket.gethostname()
    lbreak = '\n'
    osInfo = lbreak+  f'{Usingcpu}'+ lbreak+oshead+' '+platform.uname().release+lbreak+Ram+"/"+Rammain+lbreak+Hostname+lbreak+distro+lbreak+PyVers+lbreak+Time_elapsed+lbreak+resolution+lbreak+ip
    info = lbreak+ "CPU:" +lbreak+"Current OS:"+lbreak+"Memory:"+lbreak+"Hostname:"+lbreak+"Linux Distro:"+lbreak+'PythonVersion:'+lbreak+"Time started:"+lbreak+" Resolution:"+lbreak+"Public IP:"
    
    text_area = Label(text=osInfo, align=WindowAlign.RIGHT, dont_extend_height=False)
    Using = Label(info, align=WindowAlign.RIGHT, dont_extend_height=False)
    Logo = Label(Windowlogo, align=WindowAlign.CENTER, dont_extend_height=False)

    dialog_body = HSplit(
        [
            
            Label("Press control-c to quit.",
                align=WindowAlign.CENTER,
            ),
            VSplit(
                [   
                    Logo,
                    Using,
                    text_area,
                ],
                
            ),
            
        ]
    )

    application = Application(
        layout=Layout(
            container=Dialog(
                title=f"Welcome to {oshead}! {user}'",
                body=dialog_body,
                with_background=True,

            ),
            focused_element=Using,
        ),
        full_screen=True,

        key_bindings=kb,
    )
    application.run()

if os.upper().__contains__('windows'.upper()): Windowlogo = """                   .oodMMMMMMMMMMMMM
       ..oodMMM  MMMMMMMMMMMMMMMMMMM
 oodMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 `^^^^^^MMMMMMM  MMMMMMMMMMMMMMMMMMM
       ````^^^^  ^^MMMMMMMMMMMMMMMMM
                      ````^^^^^^MMMM"""
elif os.upper().__contains__('linux'.upper()): Windowlogo = """         _nnnn_
        dGGGGMMb
       @p~qp~~qMb
       M|@||@) M|
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--' hjm"""
else: Windowlogo = """                         
                      .888
                    .8888'
                   .8888'
                   888'
                   8'
      .88888888888. .88888888888.
   .8888888888888888888888888888888.
 .8888888888888888888888888888888888.
.&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
`%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.
 `00000000000000000000000000000000000'
  `000000000000000000000000000000000'
   `0000000000000000000000000000000'
     `###########################'
    `#######################'
         `#########''########'  """


#Windowlogo = ANSI()
   

if __name__ == "__main__":
    main()