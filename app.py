import gradio as gr
from src.converter import NumberToFrenchConverter

def convert_number(number):
    """Convert number to French using NumberToFrenchConverter."""
    converter = NumberToFrenchConverter()
    try:
        return converter.convert(number)
    except ValueError as e:
        return str(e)

# Gradio interface
def gradio_app():
    """Create a simple Gradio app."""
    gr.Interface(fn=convert_number, 
                 inputs="number", 
                 outputs="text", 
                 title="Number to French Converter", 
                 description="Enter a number and get its French word equivalent."
    ).launch()

if __name__ == "__main__":
    gradio_app()
