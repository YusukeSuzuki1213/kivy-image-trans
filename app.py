from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class AppBox(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        layout = AppBox()
        return layout


if __name__ == '__main__':
    MyApp().run()