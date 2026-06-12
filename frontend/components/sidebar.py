import asyncio
import time
import streamlit as st
from api import save_uploaded_pdf, send_rag_ingest_event

def render_sidebar():
    with st.sidebar:
        st.markdown("### 🗂️ Data Management")
        st.caption(
            "Upload your PDF documents. Ingested files are automatically processed, chunked, and stored in Qdrant Vector database."
        )
        
        st.markdown('<div class="ingestion-deck">', unsafe_allow_html=True)
        uploaded = st.file_uploader(
            "Upload a PDF file",
            type=["pdf"],
            accept_multiple_files=False
        )
        
        if uploaded is not None:
            with st.spinner("Ingesting PDF..."):
                path = save_uploaded_pdf(uploaded)
                asyncio.run(send_rag_ingest_event(path))
                time.sleep(0.3)
            st.success(f"Successfully processed:\n\n**{path.name}**")
            st.caption("The document is now chunked, embedded, and stored in Qdrant.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.divider()
        
        # Advanced settings grouped inside an expander at the bottom of the sidebar
        with st.expander("⚙️ Advanced Settings", expanded=False):
            top_k = st.slider(
                "How many chunks to retrieve?",
                min_value=1,
                max_value=20,
                value=5,
                step=1,
                help="Number of context segments to fetch from the database to answer your question."
            )
            
        st.divider()
        
        # Utility button to clear chat history
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            if "messages" in st.session_state:
                st.session_state.messages = []
            st.rerun()

    return top_k
