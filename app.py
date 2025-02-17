import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="ALIGNs: Psychometric Analysis",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for a refined, high-end design with updated sidebar text styling
st.markdown("""
    <style>
        /* Import Google Font (Poppins) for a modern look */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        /* Global styling */
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }
        body {
            background-color: #f4f7f9;
            color: #333;
        }

        /* Main content container styling */
        [data-testid="stAppViewContainer"] {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 2rem 3rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            margin: 2rem;
        }

        /* Title styling */
        .title {
            font-size: 48px;
            font-weight: 600;
            text-align: center;
            color: #222222;
            margin-bottom: 10px;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 10px;
        }
        .subtitle {
            font-size: 24px;
            font-weight: 300;
            text-align: center;
            margin-bottom: 30px;
            color: #666666;
        }

        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0056b3, #007acc) !important;
        }
        /* Override all text in the sidebar to be white */
        [data-testid="stSidebar"] * {
            color: #ffffff !important;
        }

        /* Button styling */
        .stButton>button {
            background-color: #007acc;
            color: #ffffff;
            border: none;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: 500;
            transition: all 0.3s ease;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .stButton>button:hover {
            background-color: #0056b3;
            transform: translateY(-3px);
        }

        /* Card styling for sections */
        .card {
            background: #f9f9f9;
            border: 1px solid #e0e0e0;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }

        /* DataFrame container styling */
        .css-1r6slb0 {
            background-color: #ffffff !important;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        /* Section headings */
        h3 {
            color: #222222;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        /* Footer styling */
        .footer {
            text-align: center;
            padding: 20px;
            color: #777777;
            font-size: 14px;
            border-top: 1px solid #e0e0e0;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Visualize", "Explore", "Explore Factor", "Implicit Definition"]
)

# Sample Data
df = pd.DataFrame({
    "Variable ID": [151, 153, 155, 159, 58, 187, 42],
    "Variable Name": [
        "Mood And Feelings Questionnaire",
        "Mood and Feelings Questionnaire (Short)",
        "Child Short Version (MFQ)",
        "How did you feel yesterday?",
        "PROMIS Sleep Disturbance",
        "Mini Risk-Resilience Index",
        "CES-D Depression Scale"
    ],
    "Item Text": [
        "I felt miserable or unhappy",
        "I felt miserable or unhappy",
        "I felt miserable or unhappy",
        "I felt depressed/blue",
        "My sleep was restless",
        "I felt down or sad",
        "I was bothered by things that usually don’t bother me"
    ],
    "Emotional Distress Score": [1.41, 1.41, 1.41, 1.40, 1.39, 1.38, 1.37]
})

# Home Page
if page == "Home":
    st.markdown("<p class='title'>Analysis of Latent Indicators to Generate Nomological Structures (ALIGNS)</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Explore the nomological networks of Behavioral Medicine and Information Systems</p>", unsafe_allow_html=True)
    st.markdown("<div class='card'>Welcome to the ALIGNs platform. Navigate through the sections using the sidebar or the buttons below to view interactive visualizations, explore in-depth data, and understand advanced psychometric models.</div>", unsafe_allow_html=True)

    # Set page in session state on button click
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Visualize"):
            st.session_state.page = "Visualize"
    with col2:
        if st.button("Explore"):
            st.session_state.page = "Explore"
    with col3:
        if st.button("Explore Factor"):
            st.session_state.page = "Explore Factor"
    with col4:
        if st.button("Implicit Definition"):
            st.session_state.page = "Implicit Definition"

# Set page in session state if not already set
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Display the selected page content
if st.session_state.page == "Visualize":
    st.markdown("<p class='title'>Data Visualization</p>", unsafe_allow_html=True)
    st.markdown("<div class='card'>Visualize key metrics and trends through interactive charts and tables.</div>", unsafe_allow_html=True)
    st.markdown("<h3>Sample Data Table</h3>", unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)
    st.markdown("<h3>Emotional Distress Score Distribution</h3>", unsafe_allow_html=True)
    st.bar_chart(df.set_index("Variable Name")["Emotional Distress Score"])

elif st.session_state.page == "Explore":
    st.markdown("<p class='title'>Data Exploration</p>", unsafe_allow_html=True)
    st.markdown("<div class='card'>Dive deep into the dataset to uncover trends and correlations among variables.</div>", unsafe_allow_html=True)
    st.markdown("<h3>Filter Data</h3>", unsafe_allow_html=True)
    variable_filter = st.selectbox("Select a variable:", df["Variable Name"])
    filtered_data = df[df["Variable Name"] == variable_filter]
    st.write(filtered_data)

elif st.session_state.page == "Explore Factor":
    st.markdown("<p class='title'>Factor Analysis</p>", unsafe_allow_html=True)
    st.markdown("<div class='card'>Examine psychometric loadings and discover the key contributing factors within the dataset.</div>", unsafe_allow_html=True)
    st.markdown("<h3>Top Contributing Factors</h3>", unsafe_allow_html=True)
    st.bar_chart(df.set_index("Variable Name")["Emotional Distress Score"])

elif st.session_state.page == "Implicit Definition":
    st.markdown("<p class='title'>Implicit Definitions</p>", unsafe_allow_html=True)
    st.markdown("<div class='card'>Explore latent variable definitions and gain insights into modern psychometric constructs.</div>", unsafe_allow_html=True)
    st.markdown("<h3>Psychometric Concepts</h3>", unsafe_allow_html=True)
    st.write("""
    - **Emotional Distress:** Measurement of mood disturbances.
    - **Risk Appraisal:** Assessment of perceived risks in mental health.
    - **Social Influence:** Impact of external factors on behavioral health.
    """)

# Footer
st.markdown("<div class='footer'>© 2025 ALIGNs | Powered by Streamlit</div>", unsafe_allow_html=True)
