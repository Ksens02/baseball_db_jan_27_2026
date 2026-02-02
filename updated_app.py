import gradio as gr

# def f(x):
#     return x**2



# with gr.Blocks() as iface:
#     number = gr.Number(label = "Type in a number.")
#     square = gr.Number(label = "This is the square of that number.")
#     number.change(fn = f, inputs = [number] , outputs = [square])

def f(x,y):
    return x+y



# with gr.Blocks() as iface:
#     x = gr.Number(label = "Type in x.")
#     y = gr.Number(label = "Type in y.")
#     sum = gr.Number(label = "This is the sum of those numbers.")
#     x.change(fn = f, inputs = [x,y], outputs = [sum])
#     y.change(fn = f, inputs = [x,y], outputs = [sum])

with gr.Blocks() as iface:
    with gr.Row():
        with gr.Column():
            x = gr.Number(label = "Type in x")
            y = gr.Number(label = "Type in y")
        with gr.Column():
            sum = gr.Number(label = "This is the sum of the two numbers")
    
    x.change(fn = f, inputs = [x,y], outputs = [sum])
    y.change(fn = f, inputs = [x,y], outputs = [sum])

    

iface.launch()