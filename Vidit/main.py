import re
import mysql.connector
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineAvatarListItem
from kitchen_sink.libs.baseclass import list_items

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.factory import Factory
from kivymd.toast.kivytoast.kivytoast import toast
from kivy.animation import Animation
from kivymd.theming import ThemeManager
from kivy.properties import ObjectProperty, StringProperty
import time
Builder.load_string(""" 

#:import utils kivy.utils 
""")

class ContentNavigationDrawer(BoxLayout):
    pass


class NavigationItem(OneLineAvatarListItem):
    icon = StringProperty()

class get_data:

    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="vidit")
        mycursor = mydb.cursor()
        f = open("current_user.txt", "r")
        r = (str(f.read()),)
        sql = "select * from users where email = %s"
        mycursor.execute(sql,r)
        data = mycursor.fetchone()
        email = data[0]
        name = data[1]
        number = data[2]
        # self.ids.uname.text=str(name)

    except BaseException as error:
        print('An exception occurred: {}'.format(error))

class ViditApp(MDApp):
    def __init__(self, **kwargs):
         self.title = "VIDIT"
         self.sm = ScreenManager()
         super().__init__(**kwargs)

    data = get_data()
    total = 0
    def animate_card(self,widget):
        anim=Animation(pos_hint={"center_y": 0.5}, duration=2)
        anim.start(widget)

    def animate_background(self, widget):
        anim = Animation(size_hint_y= 1) + Animation(size_hint_y = 0.6)
        anim.start(widget.ids.bx)

    def registeruser(self,remail,rname,rcontact,rpassword,rcpassword):
        self.remail=str(remail)
        self.rname=str(rname)
        self.rcontact=str(rcontact)
        self.rpassword=str(rpassword)
        self.rcpassword = str(rcpassword)
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        if (re.search(regex, remail) == None or len(rpassword) < 6):
            toast("Invalid ID or Password...", duration=2)
        if (rpassword != rcpassword):
            toast("Password and Confirm Password are Different...", duration=2)
        if (remail=='' or rname=='' or rcontact=='' or rpassword=='' or rcpassword==''):
            toast("Please fill all the field...", duration=2)
        else:
            try:
                mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="vidit")
                mycursor = mydb.cursor()
                sql = "SELECT name FROM users WHERE email = %s"
                remail = (str(remail),)
                mycursor.execute(sql, remail)
                result = mycursor.fetchone()
                if(result):
                    toast("Email already Registered...", duration=2)
                else:
                    sql = "INSERT INTO users (email,name,contact_no,password) VALUES (%s, %s, %s, %s)"
                    val = (str(remail[0]),str(rname),str(rcontact),str(rpassword))
                    mycursor.execute(sql, val)
                    mydb.commit()
                    toast("Registered Successfully...", duration=2)
            except BaseException as error:
                print('An exception occurred: {}'.format(error))

    def checkuser(self,femail,fpassword):
        self.femail=str(femail)
        self.fpassword=str(fpassword)
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if (re.search(regex, femail) == None or len(fpassword)< 6):
            toast("Invalid ID or Password...", duration=2)
        else:
            try:
                mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="vidit")
                mycursor = mydb.cursor()
                sql = "SELECT password FROM users WHERE email = %s"
                femail = (str(femail),)
                mycursor.execute(sql, femail)
                dpassword = mycursor.fetchone()

                if(dpassword):
                    if (dpassword[0] == fpassword):
                        toast("Login Successfully...", duration=2)
                        f = open("current_user.txt", "w")
                        f.write(femail[0])
                        f.close()
                        self.sm.current="screen3"

                    else:
                        toast("Please Enter Valid Id and Password...", duration=2)

                else:
                    toast("Please Register Your Account...", duration=2)
            except BaseException as error:
                print('An exception occurred: {}'.format(error))


    def build(self):
        self.sm.add_widget(LoginScreen(name='screen1'))
        self.sm.add_widget(RegisterationScreen(name='screen2'))
        self.sm.add_widget(MenuScreen(name='screen3'))
        self.sm.add_widget(QScreen1(name='Qscr1'))
        self.sm.add_widget(QScreen2(name='Qscr2'))
        self.sm.add_widget(QScreen3(name='Qscr3'))
        self.sm.add_widget(QScreen4(name='Qscr4'))
        self.sm.add_widget(QScreen5(name='Qscr5'))
        self.sm.add_widget(QScreen6(name='Qscr6'))
        self.sm.add_widget(QScreen7(name='Qscr7'))
        self.sm.add_widget(QScreen8(name='Qscr8'))
        self.sm.add_widget(QScreen9(name='Qscr9'))
        self.sm.add_widget(QScreen10(name='Qscr10'))
        return self.sm

class LoginScreen(Screen):
    pass

class RegisterationScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class QScreen1(Screen):
    pass

class QScreen2(Screen):
    pass

class QScreen3(Screen):
    pass

class QScreen4(Screen):
    pass

class QScreen5(Screen):
    pass

class QScreen6(Screen):
    pass

class QScreen7(Screen):
    pass

class QScreen8(Screen):
    pass

class QScreen9(Screen):
    pass

class QScreen10(Screen):
    pass


class Manager(ScreenManager):

    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)
    q_screen_one = ObjectProperty(None)
    q_screen_two = ObjectProperty(None)
    q_screen_three = ObjectProperty(None)
    q_screen_two = ObjectProperty(None)
    q_screen_five = ObjectProperty(None)
    q_screen_six = ObjectProperty(None)
    q_screen_seven = ObjectProperty(None)
    q_screen_eight = ObjectProperty(None)
    q_screen_nine = ObjectProperty(None)
    q_screen_ten = ObjectProperty(None)

if __name__ == "__main__":

    ViditApp().run()
