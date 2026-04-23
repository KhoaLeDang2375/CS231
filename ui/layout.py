import streamlit as st
from ui.components import render_header, render_pipeline_flow, render_step_details
from services.data_loader import load_mock_results

def main_layout():
    # 1. Sidebar - Controls & Navigation
    st.sidebar.title("MangaOCR v2.1")
    st.sidebar.markdown("---")
    
    model = st.sidebar.selectbox("Recognition Model", 
        ["MangaOCR v2.1 (Fast)", "MangaOCR High-Res", "Tesseract"])
    
    st.sidebar.subheader("Controls")
    show_boxes = st.sidebar.toggle("Show Bounding Boxes", value=True)
    conf_mask = st.sidebar.slider("Confidence Mask", 0.0, 1.0, 0.5)
    
    st.sidebar.markdown("---")
    st.sidebar.info("Kernel: Python 3.10 (Kaggle P100)")

    # 2. Main Content
    render_header()
    
    # Pipeline Flow Visualizer
    render_pipeline_flow()
    
    # Load Data (Simulating Kaggle Output)
    data = load_mock_results()
    
    # Layout with Sidebar-like info on the right
    col_main, col_stats = st.columns([2, 1], gap="large")
    
    with col_main:
        render_step_details(data, show_boxes)
        
    with col_stats:
        st.caption("KAGGE OUTPUT FEED")
        st.code(str(data['raw_json'])[:300] + "...", language="json")
        
        with st.container(border=True):
            st.write("### Pipeline Summary")
            st.progress(0.85, text="85% - Recognition Phase")
            st.write("**File:** `scan_v01.jpg`")
            st.write("**Inference:** `242ms`")
            
    st.divider()
    st.caption("© 2026 Manga Engineering | v2.1.0-STABLE")
