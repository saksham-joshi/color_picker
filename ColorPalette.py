from PyQt5.QtWidgets import QColorDialog , QApplication , QWidget , QPushButton , QTextEdit
from PyQt5.QtGui import QIcon , QFont
from sys import exit,argv

class Main :

    def __init__(this) :
        this.app = QApplication(argv)
        this.icon = QIcon("icon.png")
        this.screen_dim = this.app.primaryScreen().size()
        this.button_font = QFont("Acknowledgement",pointSize=10)

        this.widget = QWidget()
        this.widget.setWindowTitle("Color Palette")
        this.widget.setFixedSize(297,232)
        this.widget.setWindowIcon(this.icon)
        ##f2ffff
        this.widget.setStyleSheet('''
            background-color:cyan;
        ''')

        this.color_list_frame = QWidget()
        this.colordialog = QColorDialog(this.widget)
        this.color_name_list_setup()

        def show_color_dialog() :
            this.colordialog.show()

        this.button = QPushButton(this.icon," Show",this.widget)
        this.button.setGeometry(74 ,37,150,75)
        this.button.setFont(this.button_font)
        this.button.setStyleSheet('''
        QPushButton{
            border-radius:10px;
            background-color:black;
            color:cyan;
        }
        QPushButton::hover{
            background-color:#000050;
        }
        QPushButton::pressed{
            background-color:cyan;
            color:black;
        }
        ''')
        this.button.pressed.connect(show_color_dialog)

        def color_list_btn_pressed() :
            this.color_list_frame.show()
        this.color_list_btn = QPushButton("Color List",this.widget)
        this.color_list_btn.setGeometry(74,120,150,75)
        this.color_list_btn.setFont(this.button_font)
        this.color_list_btn.pressed.connect(color_list_btn_pressed)
        this.color_list_btn.setStyleSheet('''
        QPushButton{
            border-radius:10px;
            background-color:black;
            color:cyan;
        }
        QPushButton::hover{
            background-color:#000050;
        }
        QPushButton::pressed{
            background-color:cyan;
            color:black;
        }
        ''')

        this.widget.show()
        exit(this.app.exec_())

    def color_name_list_setup(this) :
        this.color_list_frame.setFixedSize(this.screen_dim.width()//4 , this.screen_dim.height()-100)
        this.color_list_frame.setWindowTitle("Color Palette")
        this.color_list_frame.setWindowIcon(this.icon)
        lst = this.colordialog.customColor(1).colorNames()
        st = ""
        textedit = QTextEdit( "Available color names :\n"+st ,this.color_list_frame)
        textedit.setFixedSize(this.color_list_frame.width() , this.color_list_frame.height())
        textedit.setReadOnly(True)
        textedit.setStyleSheet('''
            background-color:black;
            color:cyan;
            font-family:Verdana;
            font-weight:bold;
            font-size:18px;
        ''')
        for i in range(lst.__len__()):
            textedit.append(str(i+1)+". "+lst[i]+" .")

if __name__ == "__main__" :
    Main()
