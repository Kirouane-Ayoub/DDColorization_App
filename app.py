from gradio_imageslider import ImageSlider
import gradio as gr
from generate import generate

with gr.Blocks() as demo:
    with gr.Row():
      with gr.Column():
          image = gr.Image(type='filepath')
          button = gr.Button()
      output_image = ImageSlider(show_label=False, type="filepath", interactive=False)
    button.click(fn=generate, inputs=[image], outputs=[output_image])

demo.queue().launch(inline=False, share=True, debug=True)