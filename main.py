from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        return Label(text='Mera AI Agent App tayar hai!')

if __name__ == '__main__':
    MainApp().run()
