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
            on_text_validate: print(self.text)
        Label:
            text: "Enter Password"
        TextInput:
            hint_text: "Enter Password Here"
            multiline: False
            on_text_validate: print(self.text)
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


class HomeScreen(Screen):
    pass


class LoginScreen(Screen):
    def find_username(self, obj):
        pass


class RegisterScreen(Screen):
    def add_username(self, obj):
        with open("login_info.txt", "a+") as f:
            f.write("username: " + obj + "\n")

    def add_password(self, obj):
        with open("login_info.txt", "a") as f:
            f.write("password: " + obj + "\n")


class LoginApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="Home"))
        sm.add_widget(LoginScreen(name="Login"))
        sm.add_widget(RegisterScreen(name="Register"))
        return sm


loginapp = LoginApp()
loginapp.run()
