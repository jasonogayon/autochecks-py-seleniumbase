from pages.todos import Todos
from seleniumbase import BaseCase
import random



class TestsTodos(BaseCase):


    def test_can_add_a_single_todo(self):
        # Go to ToDoMVC React Page
        Todos.load(self)

        # Add a Todo
        todo = 'a sample todo'
        Todos.addTodo(self, todo)

        # Check that Todo is Added
        self.assert_element_visible(f'//li[.="{todo}"]')

        # Check that Number of Items Left is Correct
        self.assert_exact_text("1 item left", Todos.spanTodoCount)


    def test_can_add_multiple_todos(self):
        # Go to ToDoMVC React Page
        Todos.load(self)

        # Add Multiple Todos
        todos = [ 'todo #1', 'todo #2', 'todo #3' ]
        for todo in todos:
            Todos.addTodo(self, todo)

        # Check that All Todos are Added
        for todo in todos:
            self.assert_element_visible(f'//li[.="{todo}"]')

        # Check that Number of Items Left is Correct
        self.assert_exact_text(f'{len(todos)} items left', Todos.spanTodoCount)


    def test_can_remove_a_todo(self):
        # Go to ToDoMVC React Page
        Todos.load(self)

        # Add a Todo
        todo = 'a sample todo'
        Todos.addTodo(self, todo)

        # Remove Todo
        Todos.removeTodo(self, todo)

        # Check that Todo is Removed
        self.assert_element_not_visible(f'//li[.="{todo}"]')
        self.assert_element_not_visible(Todos.spanTodoCount)


    def test_can_edit_a_todo(self):
        if self.data != 'CI':
            # Go to ToDoMVC React Page
            Todos.load(self)

            # Add a Todo
            todo = 'todo X'
            Todos.addTodo(self, todo)

            # Edit Todo
            newTodo = 'todo Y'
            Todos.editTodo(self, todo, newTodo)

            # Check that Todo is Updated
            self.assert_element_visible(f'//li[.="{newTodo}"]')
            self.assert_element_not_visible(f'//li[.="{todo}"]')
            self.assert_exact_text("1 item left", Todos.spanTodoCount)


    def test_can_mark_a_todo_as_completed_or_active(self):
        # Go to ToDoMVC React Page
        Todos.load(self)

        # Add a Todo
        todo = 'a sample todo'
        Todos.addTodo(self, todo)

        # Check that Todo is Active by Default
        todoEl = f'//li[.="{todo}"]'
        self.assert_attribute_not_present(todoEl,'class', 'completed')

        # Mark Todo as Completed
        Todos.markAsCompletedOrActive(self, todo)

        # Check that Todo is Marked as Completed
        self.assert_attribute(todoEl,'class', 'completed')

        # Mark Todo as Active
        Todos.markAsCompletedOrActive(self, todo)

        # Check that Todo is Marked as Active
        self.assert_attribute_not_present(todoEl,'class', 'completed')


    def test_can_mark_all_todos_as_completed_or_active(self):
        # Go to ToDoMVC React Page
        Todos.load(self)

        # Add Multiple Todos
        todos = [ 'todo #1', 'todo #2', 'todo #3' ]
        for todo in todos:
            Todos.addTodo(self, todo)

        # Check that All Todos are Active by Default
        for todo in todos:
            todoEl = f'//li[.="{todo}"]'
            self.assert_attribute_not_present(todoEl,'class', 'completed')

        # Mark All Todos as Completed
        Todos.markAllAsCompletedOrActive(self)

        # Check that All Todos are Marked as Completed
        for todo in todos:
            todoEl = f'//li[.="{todo}"]'
            self.assert_attribute(todoEl,'class', 'completed')

        # Mark All Todos as Active
        Todos.markAllAsCompletedOrActive(self)

        # Check that All Todos are Marked as Active
        for todo in todos:
            todoEl = f'//li[.="{todo}"]'
            self.assert_attribute_not_present(todoEl,'class', 'completed')


    def test_todo_input_has_a_placeholder_value_of_what_needs_to_be_done(self):
        # Go to ToDoMVC React Page
        Todos.load(self)

        # Check Todo Input Placeholder Text
        input = Todos.inputNewTodo
        self.wait_for_element_visible(input)
        self.assert_attribute(input,'placeholder', 'What needs to be done?')


    def test_can_view_completed_or_active_todos(self):
        # Go to ToDoMVC React Page
        Todos.load(self)

        # Add Multiple Todos
        todos = [ 'todo #1', 'todo #2', 'todo #3' ]
        for todo in todos:
            Todos.addTodo(self, todo)

        # Mark a Single Todo as Completed
        randomTodo = random.choice(todos)
        Todos.markAsCompletedOrActive(self, randomTodo)

        # View Only Completed Todos and Check that Only One Todo is Visible
        Todos.viewCompletedToDos(self, True)
        self.assert_element_visible(f'//li[.="{randomTodo}"]')

        active = todos[:]
        active.remove(randomTodo)

        for todo in active:
            self.assert_element_not_visible(f'//li[.="{todo}"]')

        # View Only Active Todos and Check that the Other Todos are Visible
        Todos.viewCompletedToDos(self, False)
        self.assert_element_not_visible(f'//li[.="{randomTodo}"]')

        for todo in active:
            self.assert_element_visible(f'//li[.="{todo}"]')


    def test_adding_a_todo_from_the_completed_page_adds_the_todo_but_will_not_display_from_there(self):
        # Go to ToDoMVC React Page
        Todos.load(self)

        # Add Multiple Todos
        todos = [ 'todo #1', 'todo #2', 'todo #3' ]
        for todo in todos:
            Todos.addTodo(self, todo)

        # View Only Completed Todos
        Todos.viewCompletedToDos(self, True)

        # Add a Todo
        todo = 'an active todo'
        Todos.addTodo(self, todo)

        # Check that Todo is Not Displayed in the Page
        self.assert_element_not_visible(f'//li[.="{todo}"]')

        # Check that Number of Items Left is Correct
        self.assert_exact_text(f'{len(todos) + 1} items left', Todos.spanTodoCount)

        # View Only Active Todos and Check that the Todo is There
        Todos.viewCompletedToDos(self, False)
        self.assert_element_visible(f'//li[.="{todo}"]')
