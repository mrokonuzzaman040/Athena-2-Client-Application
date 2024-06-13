from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView

class DashboardScreen(Screen):
    pass

class DataUploadScreen(Screen):
    def open_file_selector(self):
        # Add a file chooser for selecting files
        filechooser = FileChooserListView()
        self.add_widget(filechooser)

class DataProcessingScreen(Screen):
    pass

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(DataUploadScreen(name='data_upload'))
        sm.add_widget(DataProcessingScreen(name='data_processing'))
        return sm

if __name__ == '__main__':
    MainApp().run()
