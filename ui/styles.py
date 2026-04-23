import streamlit as st
from config.settings import THEME_COLORS

def apply_custom_styles():
    # Defensive script for fetch override issues (common with tunnels like localtunnel)
    st.markdown("""
        <script>
        (function() {
            try {
                const descriptor = Object.getOwnPropertyDescriptor(window, 'fetch');
                if (descriptor && !descriptor.writable && !descriptor.set) {
                    const originalDefineProperty = Object.defineProperty;
                    Object.defineProperty = function(obj, prop, descriptor) {
                        if (obj === window && prop === 'fetch') return obj;
                        return originalDefineProperty.apply(this, arguments);
                    };
                }
            } catch (e) {}
        })();
        </script>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <style>
        /* Card-like borders and shadows */
        .stBlock {{
            border: 1px solid {THEME_COLORS['outline_variant']};
            border-radius: 8px;
            padding: 1rem;
            background-color: {THEME_COLORS['surface']};
        }}
        
        /* Professional typography */
        h1, h2, h3 {{
            font-family: 'Inter', sans-serif;
            color: {THEME_COLORS['on_surface']};
        }}
        
        /* Custom Button */
        div.stButton > button {{
            background-color: {THEME_COLORS['primary']};
            color: white;
            border-radius: 4px;
            border: none;
            padding: 0.5rem 1rem;
            font-weight: 600;
        }}
        
        /* Sidebar dark theme like Professional Polish */
        [data-testid="stSidebar"] {{
            background-color: #0f172a;
            color: white;
        }}
        [data-testid="stSidebar"] * {{
            color: #94a3b8 !important;
        }}
        </style>
    """, unsafe_allow_html=True)
