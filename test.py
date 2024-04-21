import os
import streamlit as st
import shodan

# Access Shodan API key from environment variable
SHODAN_API_KEY = os.getenv("PtN9TbVWjbJi9TDl0CvAs3sf707aoi3n")

# Create Shodan API object
api = shodan.Shodan(SHODAN_API_KEY)

# Function to search using Shodan API
def search_shodan(search_syntax):
    try:
        # Perform search using Shodan API
        results = api.search(search_syntax)
        return results['matches']
    except shodan.APIError as e:
        st.error(f"Error: {e}")

# Main function to run the Streamlit app
def main():
    st.title('Search Tool')

    # User input section
    search_syntax = st.text_input('Enter Shodan Search Syntax')

    # Search button
    if st.button('Search'):
        # Check if search syntax is provided
        if search_syntax:
            # Perform Shodan search and display results
            search_results = search_shodan(search_syntax)
            if search_results:
                # Display search results
                st.write("Search Results from Shodan:")
                for result in search_results:
                    st.write(result)
            else:
                st.write("No results found.")
        else:
            st.warning('Please enter a search syntax')

if __name__ == "__main__":
    main()
