import streamlit as st  # Import Streamlit library for building the web application
from duckduckgo_search import DDGS  # Import DDGS for searching DuckDuckGo
from datetime import datetime  # Import datetime for fetching the current date
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Load environment variables from a .env file (if needed)
load_dotenv()
MODEL = "llama3.2"  # Placeholder for the model name, currently not used in this code

# Initialize DuckDuckGo search client
ddgs = DDGS()

# Function to search the web for the given query
def search_web(query):
    print(f"Searching the web for {query}...")  # Log the search query to the console
    
    # Get the current date for more recent search results
    current_date = datetime.now().strftime("%Y-%m")
    # Perform a web search using DuckDuckGo
    results = ddgs.text(f"{query} {current_date}", max_results=10)  # Get top 10 results
    
    if results:  # Check if any results were found
        news_results = ""  # Initialize an empty string to hold formatted results
        # Iterate through the results and format them
        for result in results:
            news_results += f"**Title**: {result['title']}\n**URL**: {result['href']}\n**Description**: {result['body']}\n\n"
        return news_results.strip()  # Return the formatted results
    else:
        return f"Could not find news results for '{query}'."  # Return a message if no results were found

# Function to analyze and synthesize search results
def analyze_results(results):
    # For demonstration purposes, return results as-is
    return f"Analyzed and synthesized results:\n{results}"

# Function to format results into an article
def format_article(analyzed_data):
    return f"# Generated Article\n\n{analyzed_data}"  # Format the analyzed data as a markdown article

# Main workflow function
def run_workflow(query):
    # Step 1: Web search
    raw_results = search_web(query)  # Call search_web to get raw results
    
    # Step 2: Analyze results
    analyzed_data = analyze_results(raw_results)  # Call analyze_results to process the raw results
    
    # Step 3: Format into article
    article = format_article(analyzed_data)  # Call format_article to generate the final article
    
    return article  # Return the formatted article

# Streamlit app
def main():
    # Set the page configuration for the Streamlit app
    st.set_page_config(page_title="Internet Research Assistant 🔎", page_icon="🔎")
    st.title("Internet Research Assistant 🔎")  # Set the title of the app

    # Initialize session state for query and article
    if 'query' not in st.session_state:  # Check if query is in session state
        st.session_state.query = ""  # Initialize query state
    if 'article' not in st.session_state:  # Check if article is in session state
        st.session_state.article = ""  # Initialize article state

    # Search query input field
    query = st.text_input("Enter your search query:", value=st.session_state.query)  # Get user input for the query

    # Generate article when button is clicked
    if st.button("Generate Article") and query:  # Check if the button is clicked and a query is provided
        with st.spinner("Generating article..."):  # Show a loading spinner while processing
            article = run_workflow(query)  # Run the workflow to generate the article
            st.session_state.query = query  # Update session state with the current query
            st.session_state.article = article  # Store the generated article in session state

    # Display the article if it exists
    if st.session_state.article:  # Check if an article is available
        st.markdown(st.session_state.article)  # Render the article as markdown

# Entry point of the application
if __name__ == "__main__":
    main()  # Call the main function to run the Streamlit app
