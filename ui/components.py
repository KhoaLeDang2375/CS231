import streamlit as st

def render_header():
    st.title("MangaOCR Pipeline Dashboard")
    st.markdown("Visualize detection, cropping, and orientation results from Kaggle Notebooks.")

def render_pipeline_flow():
    steps = ["Upload", "Detect", "Crop", "Correct", "OCR"]
    cols = st.columns(len(steps))
    for i, step in enumerate(steps):
        with cols[i]:
            # Highlight first step as complete
            is_active = "✅" if i == 0 else "⚪"
            st.button(f"{is_active} {step}", key=f"step_{i}", use_container_width=True)

def render_step_details(data, show_boxes):
    tab1, tab2, tab3, tab4 = st.tabs(["1. Detection", "2. Cropping", "3. Correction", "4. Results"])
    
    with tab1:
        st.image(data['detection_img'], caption="Detection results with boxes" if show_boxes else "Raw source")
        
    with tab2:
        st.write("### Segmented Chips")
        cols = st.columns(4)
        for i, crop in enumerate(data['crops'][:4]):
            cols[i % 4].image(crop, use_container_width=True)
            
    with tab3:
        col_a, col_b = st.columns(2)
        col_a.image(data['correction']['before'], caption="Before (Skewed)")
        col_b.image(data['correction']['after'], caption="After (Deskewed)")
        
    with tab4:
        for res in data['results']:
            with st.expander(f"{res['id']} - Conf: {res['conf']}%", expanded=True):
                c1, c2 = st.columns([1, 4])
                c1.image(res['img'])
                c2.success(res['text'])
