import gradio as gr
from search import search_candidates

# Gradio Interface
iface = gr.Interface(
    fn=search_candidates,
    inputs="text",
    outputs="text",
    title="Recruiter Pro Code Assistant",
    description="Enter resume criteria to search for candidates."
)

if __name__ == "__main__":
    iface.launch()
