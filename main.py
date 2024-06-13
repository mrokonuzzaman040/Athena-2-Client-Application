from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.uix.label import Label


class DashboardScreen(Screen):
    pass


class DataUploadScreen(Screen):
    def open_file_selector(self):
        self.clear_widgets()
        filechooser = FileChooserListView(size_hint=(1, 0.8))
        upload_button = Button(
            text="Upload",
            size_hint=(1, 0.1),
            on_press=lambda x: self.upload(filechooser.path, filechooser.selection),
        )
        back_button = Button(
            text="Back", size_hint=(1, 0.1), on_press=lambda x: self.load_default_view()
        )
        self.add_widget(filechooser)
        self.add_widget(upload_button)
        self.add_widget(back_button)

    def load_default_view(self):
        self.clear_widgets()
        layout = self.ids["default_layout"]
        self.add_widget(layout)

    def upload(self, path, filename):
        if filename:
            # Implement your upload logic here
            print(f"Uploading {filename} from {path}")


class DataProcessingScreen(Screen):
    pass


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(DataUploadScreen(name="data_upload"))
        sm.add_widget(DataProcessingScreen(name="data_processing"))
        return sm


if __name__ == "__main__":
    MainApp().run()
