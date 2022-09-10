class Todo():
    def __init__(self, name, owner, is_important=False, is_done=False):
        self.name = name
        self.owner = owner
        self.is_important = is_important
        self.is_done = is_done

    def toggle_is_important(self):
        self.is_important = not self.is_important

    def toggle_is_done(self):
        self.is_done = not self.is_done


todo_1 = Todo("go shopping", "isaac")
todo_2 = Todo("feed felix", "adam", True, True)

todo_1.toggle_is_important()
todo_2.toggle_is_done()

print(todo_1.__dict__)
print(todo_2.__dict__)