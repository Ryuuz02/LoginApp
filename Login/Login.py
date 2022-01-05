import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

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
        Label:
            text: "Enter Password"
        TextInput:
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
        Label:
            text: "Register Password"
        TextInput:
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
    pass


class RegisterScreen(Screen):
    pass


class LoginApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="Home"))
        sm.add_widget(LoginScreen(name="Login"))
        sm.add_widget(RegisterScreen(name="Register"))
        return sm


loginapp = LoginApp()
loginapp.run()
