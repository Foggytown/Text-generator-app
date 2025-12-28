import reflex as rx
from reflex_proj.backend import NGramGenerator

class State(rx.State):
    finished_loading=False
    loading=False

    async def load_model(self):
        if self.loading or self.finished_loading:
            return
        
        self.loading=True
        yield
        def load_model():
            print("Front end: starting loading generator...")
            generator.load(test=False)
            print("Front end: Loading finished!")
            return True
        
        self.finished_loading = await rx.run_in_thread(load_model)
        self.loading=False


def loading():
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.heading("Loading model", font_size="1.5em"),
                rx.cond(State.loading, rx.spinner(size="3"))
            ),
            rx.cond(
                    State.finished_loading,
                    rx.button(
                        "go to the chat", on_click=rx.redirect("/email"), width="100%",
                    ),
            ),
        ),
        width="100%",
        height="100vh",
        on_mount=State.load_model,
        )

class AutoCompleteState(rx.State):
    query: str = ""
    suffix: str = ""
    word_suggestions: list[str] = []
    full_suggestions: list[str] = []
    in_line_suggestion: str =""
    selected_index: int = -1
    show_suggestions: bool = False
    loading: bool = False

    def update_query(self, value: str) -> None:
        if not value.strip():
            self.word_suggestions = []
            self.full_suggestions = []
            self.show_suggestions = False
            self.selected_index = -1
            self.in_line_suggestion = ""
            return
        if value[-1]==" ":
            return
        
        self.loading = True
        self.show_suggestions = True
        
        self.query = value
        self.in_line_suggestion = ""

        backend_suggestions = self._fetch_from_backend(value)
        
        self.word_suggestions=[]
        self.full_suggestions = []
        cur_chars=len(self.query.split()[-1])
        for i in range(len(backend_suggestions)):
            self.word_suggestions.append(backend_suggestions[i][0])
            if len(backend_suggestions[i][0])!=cur_chars:
                backend_suggestions[i][0]=backend_suggestions[i][0][cur_chars:]
                self.full_suggestions.append(" ".join(backend_suggestions[i]))
            else:
                self.full_suggestions.append(" "+" ".join(backend_suggestions[i][1:]))
            
        self.selected_index = -1
        self.loading = False
        if not backend_suggestions:
            self.show_suggestions = False

    def _fetch_from_backend(self, query: str) -> list[list[str]]:
        return generator.suggest(self.query, n_words=2, n_texts=5, greedy=False)

    def select_suggestion(self, suggestion: str):
        if len(self.query.split())>1:
            self.query = " ".join(self.query.split()[:-1])+ " " + suggestion
        else:
            self.query=suggestion
        self.show_suggestions = False
        self.in_line_suggestion = " "+" ".join(self.in_line_suggestion.split()[1:])
        self.selected_index = -1

    def handle_key_down(self, key: str):
        if not self.show_suggestions:
            return

        if key == "ArrowDown":
            self.selected_index = min(self.selected_index + 1, len(self.word_suggestions) - 1)
        elif key == "ArrowUp":
            self.selected_index = max(self.selected_index - 1, -1)
        elif key == "Enter" and self.selected_index >= 0:
            self.select_suggestion(self.word_suggestions[self.selected_index])
        elif key == "Escape":
            self.show_suggestions = False
            self.selected_index = -1
            self.in_line_suggestion = ""

        if self.selected_index!=-1:
            self.in_line_suggestion=self.full_suggestions[self.selected_index]
            
    def clear_input(self):
        self.query = ""
        self.word_suggestions = []
        self.full_suggestions = []
        self.show_suggestions = False
        self.selected_index = -1
        self.in_line_suggestion = ""

def autocomplete_input():
    return rx.center(rx.vstack(
        rx.heading("Напишите свой эмейл, а мы вам поможем!", size="5"),
        rx.text("Начните вводить текст:", color="gray"),
        rx.box(
            rx.hstack(
                rx.box(
                    # два одинаковых окна поверх друг друга чтобы показывать серый текст
                    rx.input(
                        value=AutoCompleteState.query + AutoCompleteState.in_line_suggestion,
                        is_disabled=True,
                        color="#888888",
                        position="absolute",
                        z_index=1,
                        width="100%",
                        height="40px",
                        bg="black",
                        border_color="gray.200",
                        _focus={"border_color": "gray.200"},
                    ),
                    rx.input(
                        value=AutoCompleteState.query,
                        on_change=AutoCompleteState.update_query,
                        on_key_down=AutoCompleteState.handle_key_down,
                        placeholder="Введите текст для подсказок...",
                        size="2",
                        position="absolute",
                        z_index=2,
                        width="100%",
                        height="40px",
                        bg="transparent",
                        color="white",
                        border_color="gray.200",
                        _placeholder={"color": "gray.400"},
                        _focus={
                            "border_color": "#3b82f6",
                            "box_shadow": "0 0 0 1px #3b82f6",
                            "z_index": 2,
                        },
                    ),
                    position="relative",
                    height="40px",
                    width="100%",
                ),
                rx.cond(
                    AutoCompleteState.query,
                    rx.icon_button(
                        rx.icon("delete"),
                        on_click=AutoCompleteState.clear_input,
                        size="2",
                        variant="ghost",
                    ),
                ),
                width="100%",
            ),
            
            rx.cond(
                AutoCompleteState.show_suggestions,
                rx.card(
                    rx.vstack(
                        rx.cond(
                            AutoCompleteState.loading,
                            rx.hstack(
                                rx.spinner(size="2"),
                                rx.text("Загрузка...", size="2"),
                                padding="0.5em",
                            ),
                        ),
                        rx.foreach(
                            AutoCompleteState.word_suggestions,
                            lambda suggestion, idx: rx.cond(
                                idx == AutoCompleteState.selected_index,
                                rx.button(
                                    rx.text(suggestion, size="2"),
                                    on_click=lambda s=suggestion: AutoCompleteState.select_suggestion(s),
                                    width="100%",
                                    background_color="rgba(59, 130, 246, 0.1)",
                                    _hover={"background_color": "rgba(59, 130, 246, 0.2)"},
                                    padding="0.5em",
                                ),
                                rx.button(
                                    rx.text(suggestion, size="2"),
                                    on_click=lambda s=suggestion: AutoCompleteState.select_suggestion(s),
                                    width="100%",
                                    variant="ghost",
                                    padding="0.5em",
                                ),
                            ),
                        ),
                        spacing="0",
                        width="100%",
                    ),
                    margin_top="0.5em",
                    width="100%",
                    max_height="200px",
                    overflow_y="auto",
                    z_index=10,
                ),
            ),
            
            position="relative",
            width=["90vw", "60vw", "50vw", "40vw", "30vw"],
        ),
        spacing="2", align_items="start", padding="1em",
    ), width="100%", height="100vh",
    )


print("starting")
generator=NGramGenerator()
app = rx.App()
app.add_page(loading, route="/")
app.add_page(autocomplete_input, route="/email")


