import importlib.metadata
import os
import signal
import time

import pynecone as pc


class State(pc.State):
    v: str = ""
    slow: bool = False

    @pc.var
    def slow_v(self) -> str:
        if self.slow:
            time.sleep(0.5)
        return repr(self.v)


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading(State.slow_v, font_size="2em"),
            pc.input(value=State.v, on_change=State.set_v),
            pc.hstack(pc.text("Slow?"), pc.checkbox(value=State.slow, on_change=State.set_slow)),
        ),
        padding_top="10%",
    )


app = pc.App(state=State)
app.add_page(index)
app.compile()
