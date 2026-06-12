import asyncio
import streamlit as st
from api import send_rag_query_event, wait_for_run_output

def render_chat_canvas(top_k: int):
    # Initialize message history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Render chat history or Welcome screen
    if not st.session_state.messages:
        # Centered welcome view
        st.markdown("<h1 style='text-align: center; margin-top: 4rem; font-weight: 800; font-size: 3rem;'>🧠 DocuMind AI</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.15rem; margin-bottom: 3rem;'>Intelligent document indexing & context synthesis engine</p>", unsafe_allow_html=True)
        
        # Suggestion grid container
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                <div class="suggestion-card">
                    <div class="suggestion-title">📄 1. Ingest Documents</div>
                    <div class="suggestion-desc">Upload a PDF file using the sidebar panel. It will be instantly chunked and embedded in the Qdrant index.</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                """
                <div class="suggestion-card">
                    <div class="suggestion-title">💬 2. Synthesize Answers</div>
                    <div class="suggestion-desc">Ask anything about your document collection in the input below. Results will highlight semantic sources.</div>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
                if msg.get("sources"):
                    st.caption("🌐 Sources retrieved:")
                    with st.expander("📄 View Sources", expanded=False):
                        for src in msg["sources"]:
                            st.markdown(f"- `{src}`")

    # Chat input at absolute bottom
    if question := st.chat_input("Ask a question about your documents..."):
        # Append user question to history and render
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)
            
        # Generate assistant answer
        with st.chat_message("assistant"):
            with st.spinner("Processing question & synthesizing answer..."):
                # Fire-and-forget event to Inngest for observability/workflow
                event_id = asyncio.run(send_rag_query_event(question.strip(), int(top_k)))
                # Poll the local Inngest API for the run's output
                output = wait_for_run_output(event_id)
                answer = output.get("answer", "") or "(No answer)"
                sources = output.get("sources", [])
                
            st.markdown(answer)
            if sources:
                st.caption("🌐 Sources retrieved:")
                with st.expander("📄 View Sources", expanded=False):
                    for src in sources:
                        st.markdown(f"- `{src}`")
                        
            # Append assistant response to history
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "sources": sources
            })
