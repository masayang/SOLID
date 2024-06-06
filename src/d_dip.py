class EmailSenderInterface:
    def send_email(self, recipient, subject, body):
        pass


class EmailSender(EmailSenderInterface):
    def send_email(self, recipient, subject, body):
        print(f"Sending email to {recipient}: {subject} - {body}")


class Newsletter:
    def __init__(self):
        self.subscribers = []
        self.email_sender: EmailSenderInterface

    def subscribe(self, email):
        self.subscribers.append(email)

    def notify_subscribers(self, article):
        for subscriber in self.subscribers:
            self.email_sender.send_email(
                subscriber,
                f"Here is a new article: {article.title}",
                article.body,
            )


class Article:
    def __init__(self, title, body):
        self.title = title
        self.body = body


if __name__ == "__main__":
    from datetime import datetime


    newsletter = Newsletter()
    newsletter.subscribe("johndoe@example.com")
    newsletter.subscribe("janedoe@example.com")

    email_sender = EmailSender()
    newsletter.email_sender = email_sender

    article = Article(f"Article {datetime.now().strftime('%Y%m%d-%H%M')}", "This is a pen")
    newsletter.notify_subscribers(article)