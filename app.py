import streamlit as st
import tempfile
import os

from resume_matcher import (
    read_resume,
    parse_job_description,
    parse_resume,
    final_score
)


st.set_page_config(
    page_title="Resume Match Analyzer",
    page_icon="🎯",
    layout="wide"
)


st.title("🎯 Resume Match Analyzer")

st.write(
    "Assess candidate fit against your hiring requirements."
)


resume_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "💼 Job Description",
    placeholder="Paste the job description here...",
    height=300
)



if st.button("🚀 Analyze Resume", type="primary"):

    # Validate resume
    if resume_file is None:
        st.warning("Please upload a resume.")

    # Validate JD
    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:

        try:

            with st.spinner("Reading resume..."):

                suffix = os.path.splitext(
                    resume_file.name
                )[1]

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=suffix
                ) as temp_file:

                    temp_file.write(
                        resume_file.getbuffer()
                    )

                    temp_file_path = temp_file.name


                resume_text = read_resume(
                    temp_file_path
                )


                parsed_resume = parse_resume(
                    resume_text
                )

            with st.spinner(
                "Analyzing job description..."
            ):

                job = parse_job_description(
                    job_description
                )



            with st.spinner(
                "Evaluating candidate fit..."
            ):

                result = final_score(
                    job,
                    parsed_resume
                )


            st.divider()

            st.subheader("🎯 Candidate Assessment")

            # Candidate name
            st.write(
                f"**Candidate:** {parsed_resume.name or 'Not available'}"
            )

            score = result.score

            if score >= 85:
                status = "🔥 Strong Match"

            elif score >= 70:
                status = "👍 Good Match"

            elif score >= 55:
                status = "⚠️ Moderate Match"

            else:
                status = "❌ Weak Match"


            col1, col2, col3= st.columns(3)

            with col1:

                st.metric(
                    "Overall Match",
                    f"{score:.0f}%"
                )

            with col2:

                st.metric(
                    "Assessment",
                    status
                )

            with col3:

                st.metric(
                    "🏆 Recommendation",
                    result.verdict
                )  

            st.progress(score / 100)      


            st.divider()

            st.subheader("✅ Strong Areas")

            if result.strengths:

                strengths_html = ""

                for strength in result.strengths:
                    strengths_html += f'<span class="strength-chip">{strength}</span>'

                st.markdown(
                    f"""
                    <style>
                    .strength-container{{
                         display:flex;
                         flex-wrap:wrap;
                         gap:8px;
                         margin-top:8px;
                    }}
                    
                    .strength-chip{{
                        display: inline-block;
                        padding: 6px 12px;
                        border-radius: 16px;
                        
                        background: #17251d;
                        border: 1px solid #285c3a;
                        color: #8ee6ad;

                        font-size: 14px;
                        font-weight: 500;
                        white-space: nowrap;
                    }}
                    </style>

                    <div class="strength-container">
                            {strengths_html}
                    </div>

                    """ ,
                     unsafe_allow_html=True
                )    
                    

            else:
             st.write("No major strengths identified.")


            # Required Skill Gaps
           

            st.subheader("⚠️ Missing Required Skills")

            if result.missing_required_skills:

                skills = ""

                for skill in result.missing_required_skills:
                    skills += f'<span class="skill-chip">{skill}</span>'

                st.markdown(
                    f"""
                    <style>
                    .skill-container {{
                        display: flex;
                        flex-wrap: wrap;
                        gap: 8px;
                        margin-top: 8px;
                    }}

                    .skill-chip {{
                        display: inline-block;
                        padding: 6px 12px;
                                    border-radius: 16px;
                        background: #2a1d1d;
                        border: 1px solid #6b3a3a;
                        font-size: 14px;
                        font-weight: 500;
                        white-space: nowrap;
                    }}
                    </style>

                    <div class="skill-container">
                        {skills}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.success("✅ No major required skill gaps found.")


            # Preferred Skill Gaps
          

            st.subheader(
                "ℹ️ Missing Preferred Skills"
            )

            if result.missing_preferred_skills:

                preferred_skills = ""

                for skill in result.missing_preferred_skills:
                   preferred_skills += f'<span class="preferred-chip">{skill}</span>'

                st.markdown(
                    f"""
                    <style>
                    .preferred-container {{
                     display: flex;
                     flex-wrap: wrap;
                     gap: 8px;
                     margin-top: 8px;
                    }}

                    .preferred-chip {{
                     display: inline-block;
                     padding: 6px 12px;
                     border-radius: 16px;
                     background: #2a271d;
                     border: 1px solid #6b5930;
                     color: #e6d58a
                     font-size: 14px;
                     font-weight: 500;
                     white-space: nowrap;
                     }}
                    </style>
                    
                    <div class="preferred-container">
                        {preferred_skills}
                    </div>
                    """,
                    unsafe_allow_html=True

                )   

            else:

                st.write(
                    "No major preferred skill gaps found."
                )


      
            # Experience
            st.subheader("💼 Experience Fit")

            if result.meets_experience_requirement:

                st.success(
                    f"✅ Meets requirement — {result.experience_summary}"
                )

            else:

                st.error(
                    f"❌ Does not meet requirement — {result.experience_summary}"
                )    

            # Concerns
       
            st.subheader("⚠️ Key Concerns")

            if result.concerns:
                with st.expander("View concerns"):
                    for concern in result.concerns:
                       st.write(f"• {concern}")

            else:

                st.success(
                    "No major concerns identified."
                )


            # Final Recommendation
     
            st.divider()

            st.subheader(
                "🏆 Final Recommendation"
            )

            verdict = result.verdict.upper()

            if verdict == "SHORTLIST":

                st.success(
                    "✅ SHORTLIST"
                )
                st.write("Strong alignment with the role.")

            elif verdict == "CONSIDER":

                st.warning(
                    "⚠️ CONSIDER"
                )
                st.write("Relevant profile with some skill gaps.")

            else:

                st.error(
                    "❌ LOW FIT"
                )
                st.write("Core requirements are not sufficiently met.")


        except Exception as e:

            st.error(
                f"Something went wrong: {e}"
            )


        finally:

            # Remove temporary file
            if "temp_file_path" in locals():
                if os.path.exists(temp_file_path):
                    os.remove(temp_file_path)