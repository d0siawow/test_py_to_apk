from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class TestApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, I am Android app", halign="center")


TestApp().run()
