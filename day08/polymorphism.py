class Backend:
    def role(self):
        print("Handles server-side logic")


class Frontend:
    def role(self):
        print("Handles UI and client-side logic")


def show_role(employee):
    employee.role()


show_role(Backend())
show_role(Frontend())
