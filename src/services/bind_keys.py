def bind_keys_to_widgets(window):
    """This function specifies keys to be binded with specific widgets."""

    window.bind_class("Button", "<Return>", invoke_binding)
    window.bind_class("Text", "<Tab>", invoke_binding)
    window.bind_class("Text", "<Shift-Tab>", invoke_binding)

def invoke_binding(window):
    """This function invokes the aforementined key bindings."""

    window.widget.invoke()

def focus_next_widget(event):
    """This function handles focusing when moving with <Tab>.
    Required only by tkinter's textbox widget."""

    event.widget.tk_focusNext().focus()

def focus_previous_widget(event):
    """This function handles focusing when moving with <Tab>.
    Required only by tkinter's textbox widget."""

    event.widget.tk_focusPrev().focus()
