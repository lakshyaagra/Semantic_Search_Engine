import streamlit as st

from config import collection
from search import semantic_search

st.set_page_config(
    page_title="Semantic Search Engine",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 Semantic Search Engine")

st.write(
    "Search your knowledge base using natural language."
)

if collection.count() == 0:
    st.warning(
        "No documents found. Run `python ingest.py` first."
    )
    st.stop()

# Get available source filenames
stored_data = collection.get(
    include=["metadatas"]
)

sources = sorted({
    metadata["source"]
    for metadata in stored_data["metadatas"]
    if metadata and "source" in metadata
})

selected_source = st.selectbox(
    "Filter by source",
    ["All"] + sources
)

query = st.text_input(
    "What do you want to search?"
)

top_k = st.slider(
    "Number of results",
    min_value=1,
    max_value=10,
    value=3
)

if st.button("Search", type="primary"):

    if not query.strip():
        st.warning("Please enter a search query.")

    else:
        with st.spinner("Searching documents..."):

            results = semantic_search(
                query=query,
                top_k=top_k,
                source=selected_source
            )

        if not results:
            st.info("No matching documents found.")

        else:
            st.subheader(
                f"Found {len(results)} matching chunks"
            )

            for i, result in enumerate(results, start=1):

                with st.container(border=True):

                    st.markdown(
                        f"**Result {i}**"
                    )

                    st.write(result["text"])

                    st.caption(
                        f"Source: {result['metadata']['source']}"
                    )

                    st.caption(
                        f"Chunk: {result['metadata']['chunk_index']}"
                    )

                    st.caption(
                        f"Distance: {result['distance']:.4f}"
                    )