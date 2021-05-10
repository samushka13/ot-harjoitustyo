def bind_keys_to_widgets(window):
    """Specifies keys to be binded with specific widgets."""

    window.bind_class("Button", "<Return>", invoke_binding)
    window.bind_class("Text", "<Tab>", focus_next_widget)
    window.bind_class("Text", "<Shift-Tab>", focus_previous_widget)

def invoke_binding(window):
    """Invokes the key bindings spcified in bind_keys_to_widgets."""

    window.widget.invoke()

def focus_next_widget(event):
    """Handles focusing when moving with <Tab>.
    Required only by tkinter's textbox widget."""

    event.widget.tk_focusNext().focus()

def focus_previous_widget(event):
    """Handles focusing when moving with <Tab>.
    Required only by tkinter's textbox widget."""

    event.widget.tk_focusPrev().focus()
