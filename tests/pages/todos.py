from re import T
from selenium.webdriver.common.keys import Keys



class Todos(object):

    url = "https://www.todomvc.com/examples/react/#/"

    buttonRemove = "//button[@class='destroy']"
    header = "//h1[.='todos']"
    inputNewTodo = "input.new-todo"
    inputEditTodo = "//input[contains(@class,'edit')]"
    linkAll = "//a[.='All']"
    linkActive = "//a[.='Active']"
    linkCompleted = "//a[.='Completed']"
    listTodos = "//ul[@class='todo-list']//li"
    spanTodoCount = "span.todo-count"
    toggleAll = "//label[@for='toggle-all']"
    toggleComplete = "//input[@class='toggle']"



    def load(self):
        self.maximize_window()
        self.open(Todos.url)
        self.wait_for_element_visible(Todos.header)


    def addTodo(self, text):
        input = Todos.inputNewTodo

        self.wait_for_element_visible(input)
        self.type(input, f'{text}\n')
        self.wait_for_attribute(input, "value", "")


    def removeTodo(self, text):
        todo = f'//li[.="{text}"]'
        buttonRemove = f'{todo}{Todos.buttonRemove}'

        self.wait_for_element_visible(todo)
        self.click(todo)
        self.wait_for_element_visible(buttonRemove)
        self.sleep(1)
        self.click(buttonRemove)
        self.wait_for_element_not_visible(buttonRemove)


    def editTodo(self, text, newText):
        todo = f'//li[.="{text}"]'

        self.wait_for_element_visible(todo)
        self.double_click(todo)
        inputEditTodo = self.wait_for_element_visible(Todos.inputEditTodo)
        inputEditTodo.send_keys(Keys.CONTROL, "a")
        inputEditTodo.send_keys(Keys.DELETE)
        inputEditTodo.send_keys(newText)
        inputEditTodo.send_keys(Keys.ENTER)


    def markAsCompletedOrActive(self, text):
        # Get the List of Todos as List of Todo Texts
        listEl = self.find_elements(Todos.listTodos)
        listText = []
        for el in listEl:
            listText.append(el.text)

        # Determine the Placement (Index) of the Todo from the List of Todos
        keys = []
        textIndex = listText.index(text) + 2
        for _ in range(textIndex):
            keys.append(Keys.TAB)
        keys.append(Keys.SPACE)

        # Click the New Todo Input
        inputNewTodo = self.wait_for_element_visible(Todos.inputNewTodo)
        inputNewTodo.click()

        # Because we are Unable to Click the Input.Toggle Element Properly
        # Use Tabs Key Press to Select the Todo
        # Then Use Space Key Press to Mark the Todo as Completed/Active
        inputNewTodo.send_keys(keys)


    def markAllAsCompletedOrActive(self):
        toggleAll = self.wait_for_element_visible(Todos.toggleAll)
        toggleAll.click()
        self.sleep(1)


    def viewCompletedToDos(self, completed):
        link = Todos.linkActive
        if completed == True:
            link = Todos.linkCompleted

        self.wait_for_element_visible(link)
        self.click(link)
        self.sleep(1)
