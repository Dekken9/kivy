import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from chat import get_response
# Your existing code here (import statements, model loading, etc.)

class ChatApp(App):
    def build(self):
        self.main_layout = BoxLayout(orientation='vertical')

        self.output_label = Label(text="Let's chat!", size_hint_y=0.8)
        self.input_text = TextInput(size_hint_y=0.1)
        self.send_button = Button(text='Send', size_hint_y=0.1)
        self.send_button.bind(on_press=self.send_message)

        self.main_layout.add_widget(self.output_label)
        self.main_layout.add_widget(self.input_text)
        self.main_layout.add_widget(self.send_button)

        return self.main_layout

    def send_message(self, instance):
        user_input = self.input_text.text
        if user_input.lower() == 'quit':
            App.get_running_app().stop()
            return

        response = get_response(user_input)
        self.output_label.text += f"\nYou: {user_input}\nBot: {response}\n"
        self.input_text.text = ""

if __name__ == "__main__":
    ChatApp().run()