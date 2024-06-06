'''
SRP: Single Responsibility Principle (単一責任の原則)
'''


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def send_notification(self, message):
        print(f"Sending mail to {self.name}(self.email): {message}")


class NotificationManager:
    def send_notification(self, user, message):
        user.send_notification(message)


if __name__ == "__main__":
    user = User("John", "john@test.com")
    nm = NotificationManager()
    nm.send_notification(user, "Hello!")