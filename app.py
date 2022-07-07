import lightning as L
from lightning.app.frontend import StreamlitFrontend

from streamlit_app import GramformerDemo


def your_streamlit_app(lightning_app_state):
    obj = GramformerDemo()
    return obj.main()


class LitStreamlit(L.LightningFlow):
    def configure_layout(self):
        return StreamlitFrontend(render_fn=your_streamlit_app)


class LitApp(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.lit_streamlit = LitStreamlit()

    def configure_layout(self):
        tab1 = {"name": "home", "content": self.lit_streamlit}
        return tab1


app = L.LightningApp(LitApp())
