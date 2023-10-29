import reflex as rx

class State(rx.State):
    """The app state."""
    def onclick(self):
        return rx.redirect("/selections")