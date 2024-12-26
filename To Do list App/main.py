from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class TaskRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(TaskRecycleView, self).__init__(**kwargs)
        self.data = []

class ToDoListApp(App):
    def build(self):
        self.tasks = []
        self.completed_tasks = []

        layout = BoxLayout(orientation='vertical')

        self.task_input = TextInput(hint_text='Enter a new task', size_hint_y=None, height=40)
        layout.add_widget(self.task_input)

        self.add_task_button = Button(text='Add Task', size_hint_y=None, height=40)
        self.add_task_button.bind(on_press=self.add_task)
        layout.add_widget(self.add_task_button)

        self.task_list_view = TaskRecycleView()
        layout.add_widget(self.task_list_view)

        self.complete_task_button = Button(text='Complete Task', size_hint_y=None, height=40)
        self.complete_task_button.bind(on_press=self.complete_task)
        layout.add_widget(self.complete_task_button)

        self.show_completed_button = Button(text='Show Completed Tasks', size_hint_y=None, height=40)
        self.show_completed_button.bind(on_press=self.show_completed_tasks)
        layout.add_widget(self.show_completed_button)

        return layout

    def add_task(self, instance):
        task = self.task_input.text
        if task:
            self.tasks.append(task)
            self.task_list_view.data = [{'text': task} for task in self.tasks]
            self.task_input.text = ''

    def complete_task(self, instance):
        if self.tasks:
            completed_task = self.tasks.pop()
            self.completed_tasks.append(completed_task)
            self.task_list_view.data = [{'text': task} for task in self.tasks]

    def show_completed_tasks(self, instance):
        if self.completed_tasks:
            completed_tasks_str = '\n'.join(self.completed_tasks)
            popup = Popup(title='Completed Tasks', content=Label(text=completed_tasks_str), size_hint=(0.8, 0.8))
            popup.open()
        else:
            popup = Popup(title='Completed Tasks', content=Label(text='No tasks completed yet.'), size_hint=(0.8, 0.8))
            popup.open()

if __name__ == '__main__':
    ToDoListApp().run() 