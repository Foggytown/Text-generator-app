import reflex as rx
from backend import NGramGenerator
import time

class State(rx.State):
    """The app state."""

    prompt = ""
    num_words=""
    complete = False
    processing=False
    result=""
    finished_training=False
    training=False

    async def train_model(self):
        if self.training:
            return
        
        self.training=True
        yield
        def do_training():
            print("Starting training...")
            generator.train()
            print("Training finished!")
            return True
        
        trained = await rx.run_in_thread(do_training)
        
        self.finished_training=True

    async def get_new_words(self):
        """Get the image from the prompt."""
        if self.prompt == "":
            rx.window_alert("Prompt Empty")
        if self.num_words == "":
            rx.window_alert("Number of words empty Empty")

        self.processing, self.complete = True, False
        yield
        def do_suggestion():
            print("started suggesting")
            generated_words = generator.suggest(self.prompt, n_words=int(self.num_words), n_texts=1)
            print("suggesting finished")
            return generated_words
        generated_words=await rx.run_in_thread(do_suggestion)
        self.result=self.prompt[:-1]+' '+' '.join(generated_words)
        self.processing, self.complete = False, True

def index_main():
    return rx.center(
        rx.vstack(
            rx.heading("n-gram generation", font_size="1.5em"),
            rx.input(
                placeholder="Enter a prompt..",
                on_blur=State.set_prompt,
                width="25em",
            ),
            rx.input(
                placeholder="Enter how many words to generate",
                on_blur=State.set_num_words,
                width="25em",
            ),
            rx.button(
                "Generate new words",
                on_click=State.get_new_words,
                width="25em",
                loading=State.processing
            ),
            rx.cond(
                State.complete,
                rx.text(State.result)
            ),
            align="center",
        ),
        width="100%",
        height="100vh",
    )

def loading():
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.heading("Loading model", font_size="1.5em"),
                rx.spinner(size="3")
            ),
            rx.cond(
                    State.finished_training,
                    rx.button(
                        "go to the chat", on_click=rx.redirect("/chat"), width="100%",
                    ),
            ),
        ),
        width="100%",
        height="100vh",
        on_mount=State.train_model,
        )

print("starting")
generator=NGramGenerator()
app = rx.App()
app.add_page(loading, route="/")
app.add_page(index_main, route="/chat")

