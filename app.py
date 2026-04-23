import streamlit as st
from ui.layout import main_layout
from ui.styles import apply_custom_styles

def main():
    # Cấu hình trang chuyên nghiệp
    st.set_page_config(
        page_title="MangaOCR Pipeline",
        page_icon="📖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Áp dụng theme và CSS tùy chỉnh
    apply_custom_styles()
    
    # Khởi chạy giao diện chính
    main_layout()

if __name__ == "__main__":
    main()
