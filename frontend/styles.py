import streamlit as st

def apply_custom_styles():
    st.markdown(
        """
        <style>
        /* Global Typography & Palette */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        
        /* Main Layout Margins */
        .main .block-container {
            padding-top: 2.5rem;
            padding-bottom: 6rem;
            max-width: 850px;
        }
        
        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            border-right: 1px solid rgba(128, 128, 128, 0.1);
        }
        
        section[data-testid="stSidebar"] .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Suggestion card style */
        .suggestion-card {
            background-color: var(--secondary-background-color);
            border: 1px solid rgba(128, 128, 128, 0.1);
            border-radius: 12px;
            padding: 1.25rem;
            margin-bottom: 1rem;
            transition: all 0.2s ease;
        }
        
        .suggestion-card:hover {
            border-color: var(--primary-color);
            transform: translateY(-2px);
        }
        
        .suggestion-title {
            font-weight: 600;
            font-size: 0.95rem;
            color: var(--text-color);
            margin-bottom: 0.25rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .suggestion-desc {
            font-size: 0.85rem;
            color: var(--text-color);
            opacity: 0.75;
            line-height: 1.4;
        }
        
        /* Card Styling for Ingestion Deck in Sidebar */
        .ingestion-deck {
            background-color: var(--secondary-background-color);
            border: 1px solid rgba(128, 128, 128, 0.1);
            border-radius: 12px;
            padding: 1.25rem;
            margin-top: 1rem;
            margin-bottom: 1.5rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
