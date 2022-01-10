from time import sleep

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput

kivy.require("2.0.0")

Builder.load_string("""
<HomeScreen>:
    GridLayout:
        cols: 2
        Button:
            text: "Login Here"
            on_press: root.manager.current = "Login"
        Button:
            text: "Register Here"
            on_press: root.manager.current = "Register"
<LoginScreen>:
    GridLayout:
        cols: 2
        Label:
            text: "Enter Username"
        TextInput:
            hint_text: "Enter Username Here"
            multiline: False
            on_text_validate: root.find_username(self.text)
        Label:
            text: "Enter Password"
        TextInput:
            hint_text: "Enter Password Here"
            multiline: False
            on_text_validate: root.find_password(self.text)
        Button:
            text: "Return To Home Screen"
            on_press: root.manager.current = "Home"
        Button:
            text: "Register Here"
            on_press: root.manager.current = "Register"
<RegisterScreen>:
    GridLayout:
        cols: 2
        Label:
            text: "Register Username"
        TextInput:
            hint_text: "Enter Username Here"
            multiline: False
            on_text_validate: root.add_username(self.text)
        Label:
            text: "Register Password"
        TextInput:
            hint_text: "Enter Password Here"
            multiline: False
            on_text_validate: root.add_password(self.text)
        Button:
            text: "Return To Home Screen"
            on_press: root.manager.current = "Home"
        Button:
            text: "Login Here"
            on_press: root.manager.current = "Login"

""")


def search_file(searched_text, login_type):
    with open("login_info.txt", "r") as f:
        with open("login_info.txt", "r") as g:
            file_length = len(g.read())
            g.seek(0)
            file_length += (len(g.readlines()) - 1)
        found = False
        while not found:
            next_line = f.readline()
            if next_line[0:8] == login_type:
                iterated_name = next_line[9:len(next_line) - 1]
                if searched_text.lower() == iterated_name.lower():
                    found = True
            if f.tell() == file_length:
                break
    return found


class HomeScreen(Screen):
    pass


class LoginScreen(Screen):
    def find_username(self, obj):
        found = search_file(obj, "username")
        if found:
            print("Found your Username")
        else:
            print("Invalid Username")

    def find_password(self, obj):
        found = search_file(obj, "password")
        if found:
            print("Found your Password")
        else:
            print("Invalid Password")


class RegisterScreen(Screen):
    def add_username(self, obj):
        found = search_file(obj, "username")
        if not found:
            with open("login_info.txt", "a+") as f:
                f.write("\nusername:" + obj)
        else:
            print("That username is already in use")

    def add_password(self, obj):
        found = search_file(obj, "password")
        if not found:
            with open("login_info.txt", "a+") as f:
                f.write("\npassword:" + obj)
        else:
            print("That username is already in use")


class LoginApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="Home"))
        sm.add_widget(LoginScreen(name="Login"))
        sm.add_widget(RegisterScreen(name="Register"))
        return sm


loginapp = LoginApp()
loginapp.run()
