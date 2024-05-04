from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Emin Aghamirzayev "
PAGE_ICON = ":wave:"
NAME = "Emin Aghamirzayev"
DESCRIPTION = """
Head of Analytics division, assisting enterprises by supporting data-driven, visualition and decision-making.
"""
EMAIL = "eminagamirzeyev@yahoo.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/emin-aghamirzayev-95ab765a/",
    "GitHub": "https://github.com/enagamirzayev",
    "HugginFace": "https://huggingface.co/Enagamirzayev",
    "Kaggle": "https://www.kaggle.com/",
}
PROJECTS = {
    "🏆 Sales KPI Dashboards for branches in web - Comparing sales across period of times": "https://resume-enagamirzayev.onrender.com/",#"https://youtu.be/Sb0A9i6d320",
    "🏆 Loan and Card Tracker and etc Portfolio Dahbaords - Web app with plSQL database": "https://resume-enagamirzayev.onrender.com/",
    "🏆 Service Time KPI Application and Dashboard - converter with product mangement time": "https://resume-enagamirzayev.onrender.com/",
    "🏆 Chatbot in mobile - Related to database report and daily updated": "https://resume-enagamirzayev.onrender.com/",
    "🏆 Chatbot in mobile - Related to database report and daily updated": "https://resume-enagamirzayev.onrender.com/",
}


CERTIFICATES = {
    "🏅 IBM. Applied Data Science Capstone": "https://www.coursera.org/account/accomplishments/verify/LJUBC8ENF96B?utm_source%3Dandroid%26utm_medium%3Dcertificate%26utm_content%3Dcert_image%26utm_campaign%3Dsharing_cta%26utm_product%3Dcourse",#"https://youtu.be/Sb0A9i6d320",
    "🏅 Univercity of Michigan. Applied Machine Learning in Python": "https://www.coursera.org/account/accomplishments/verify/QZTBEPAZK8CF",
    "🏅 IBM. Data Analysis with Python": "https://www.coursera.org/account/accomplishments/verify/SARYBYABMPZR?utm_source%3Dandroid%26utm_medium%3Dcertificate%26utm_content%3Dcert_image%26utm_campaign%3Dsharing_cta%26utm_product%3Dcourse",
    "🏅 IBM. Python for Data Science, AI & Development": "https://www.coursera.org/account/accomplishments/verify/HELB9T23UPLM?utm_source%3Dandroid%26utm_medium%3Dcertificate%26utm_content%3Dcert_image%26utm_campaign%3Dsharing_cta%26utm_product%3Dcourse",
    "🏅 Data SoCool. Oracle Database SQL": "https://data.edu.az/az/verified/2022984/",
    "🏅 IBM. Data Science Methodology": "https://www.coursera.org/account/accomplishments/verify/HFYC3BJ563C2?utm_source%3Dandroid%26utm_medium%3Dcertificate%26utm_content%3Dcert_image%26utm_campaign%3Dsharing_cta%26utm_product%3Dcourse",

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# # Define column width
# num_cols = len(SOCIAL_MEDIA)
# col_width = 12 // num_cols

# # Create columns with specified background color
# cols = st.columns(num_cols)
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     with cols[index]:
#         st.markdown(
#             f"<a href='{link}' style='color: #FFFFFF; text-decoration: none; background-color: #1DA1F2; padding: 8px 12px; border-radius: 5px;'>{platform}</a>",
#             unsafe_allow_html=True
#         )

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 7 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, TensorFlow, Pytourch), SQL, VBA, NLP, Django, Streamlit, Flask
- 📊 Data Visulization: PowerBi, MS Excel, Plotly, Dash
- 📚 Modeling: Logistic regression, linear regression, SVM, SVR, decition trees, Ridg and LASSO regression, Huggingface transformer
- 🗄️ Databases: Postgres, MongoDB, MySQL, PL OracleSQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Head of Analytics devision | ABB**")
st.write("10/2016 - Present")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost sales.
- ► Led a team of 4 analysts to brainstorm potential KPI and sales improvements, and implemented client service times.
- ► Redesigned data model through iterations that improved predictions.
- ► Providing reports on various promotion dashboards that have the role of influencing increased sales for affiliates on the WEB platform.
- ► At the same time, the reports are integrated into the chat bot according to the latest technologies.

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Senior loan expert | Bank of Baku**")
st.write("01/2011 - 09/2016")
st.write(
    """
- ► Analysis, payment calculation and sale of consumer loans.
- ► Follow-up of clients' follow-up payments and taking actions related to portfolio maintenance.
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Consultant | Ministry of Economic of the Republic of Azerbaijan**")
st.write("04/2010 - 11/2010")
st.write(
    """
- ► Conduct research on interstate measures.
- ► Conduct preliminary analysis of events. 
- ► Constantly preparing offers. Conduct research on the development of relations, etc.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")




# --- Certificates & Accomplishments ---
st.write('\n')
st.subheader("Certificates")
st.write("---")
for i, link in CERTIFICATES.items():
    st.write(f"[{i}]({link})")