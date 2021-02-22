# QTpcinfo
Persistent QT5 window to display Datetime (yyyy-mm-dd Day hh:mm:ss) CPU% RAM% and network bandwidth.

Do note that this is always on the top window by default and it will be persistent even during watching the movies. Actually, that was one of my requirement, if it annoys you then comment line 58 and uncomment line 59

To change the text size line 102

To changecolor line 107 (default is Qt.cyan)

The only external requirement is Pyqt5 library <pip install pyqt5>

Why this tool?
I made this application because I wanted a full-screen experience like Linux without an annoying toolbar at the bottom which mostly needed only to check the current date and time. Besides I occasionally want to see whether there is any application hogging the system resources or consuming the bandwidth. Most Linux Flavours (usually XFCE4) allow you to customize the width of the toolbar so it wouldn't block the entire horizontal line of your desktop. But in Windows, there is no such option. There is only auto-hide toolbar option but that means no date and time display. And on top of that Windows default DateTime format is something I don't like. So to solve this just made a single application to display all the information I needed without blocking the desktop real estate. Also wanted to learn Pyqt5 so thought this will be a fun project, like any other Python project it took less time than expected, just import some library & bam!  

It looks something like this 
![image](https://user-images.githubusercontent.com/28746824/108650638-ffa0e780-74e5-11eb-8df8-136c279c3992.png)


I have added the bat file (change the folder path in bat file accordingly), if you want to launch the notification window on restart then press window + R, write "shell:startup" enter and a new folder will pop-up, paste the given batch file into that folder.

For Linux use qtpcinfo.sh 

Maybe in the future I will add the stock ticker in the display window, the problem is additional dependency and sites tend to change the design a lot.
