def bind_keys_to_widgets(window):
    window.bind_class("Button", "<Return>", invoke_binding)
    window.bind_class("Text", "<Tab>", invoke_binding)
    window.bind_class("Text", "<Shift-Tab>", invoke_binding)

def invoke_binding(window):
    window.widget.invoke()

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()

def focus_previous_widget(event):
    event.widget.tk_focusPrev().focus()
