from app import Init


class App(Init):
    def __init__(self):
        super(App, self).__init__()
        self.resources()

    def run(self):
        self.app.run(
            debug=True
        )


if __name__ == "__main__":
    App().run()
