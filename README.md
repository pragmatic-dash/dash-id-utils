# Dash ID Utils

## Install

```bash
pip install dash-id-utils
```

## Usage

```python
from dash import html, ALL, callback


class AnnotatedImageListSidebar(html.Div):
    class slots:
        id = DashIDGenerator(page="session", type="view", name="image-list")
        image = DashIDGenerator(page="session", type="view", name="image")

    def __init__(self, items, **kwargs):
        self.items = items
        super().__init__(self.render(), id=self.slots.id.get_identifier(), **kwargs)        


    def render(self):
        return [
            html.Img(src=item.url, id=self.slots.image.get_identifier(item.id))
            for item in items
        ]

@callback(
    [...]
    AnnotatedImageListSidebar.slots.image.get_input("n_clicks", ALL),
)
def x(all_n_clicks):
    ...

@callback(
    [
        AnnotatedImageListSidebar.slots.id.get_output("children"),
    ]
    ...
)
def y(...):
    ...
```