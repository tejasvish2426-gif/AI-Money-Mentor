import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
MY_API_KEY = "AIzaSyCXdEQd86Dd-qMYdLdqRAPCZNFXtZEVQlo"

genai.configure(api_key="AIzaSyCXdEQd86Dd-qMYdLdqRAPCZNFXtZEVQlo")
model = genai.GenerativeModel('gemini-pro')

# --- UI SETUP ---
st.set_page_config(page_title="AI Money Mentor", layout="wide")
st.title("💰 AI Money Mentor")
st.markdown("### From Confused Savers to Confident Investors")

# --- SIDEBAR: USER INPUTS ---
with st.sidebar:
    st.header("1. Your Financial Snapshot")
    income = st.number_input("Monthly Income (₹)", min_value=0, value=50000)
    expenses = st.number_input("Monthly Expenses (₹)", min_value=0, value=30000)
    savings = income - expenses
    
    st.subheader("Current Security")
    has_insurance = st.selectbox("Term Insurance?", ["No", "Yes"])
    emergency_fund = st.number_input("Emergency Fund Balance (₹)", min_value=0, value=10000)

# --- MAIN DASHBOARD ---
tab1, tab2, tab3 = st.tabs(["Money Health Score", "Tax Wizard", "FIRE Roadmap"])

with tab1:
    st.header("Financial Wellness Diagnostic")
    if st.button("Calculate My Health Score"):
        with st.spinner("Analyzing your finances..."):
            prompt = (f"Analyze these Indian personal finances: Income ₹{income}, Expenses ₹{expenses}, "
                      f"Emergency Fund ₹{emergency_fund}, Insurance: {has_insurance}. "
                      f"Provide a Health Score out of 100 and 3 critical improvements.")
            response = model.generate_content(prompt)
            st.success("Analysis Complete!")
            st.write(response.text)

with tab2:
    st.header("Tax Regime Optimizer")
    st.info("Paste your Form 16 components or salary breakdown below.")
    tax_data = st.text_area("Example: Basic 40k, HRA 20k, Special Allowance 10k...")
    
    if st.button("Compare Regimes"):
        with st.spinner("Modeling tax savings..."):
            prompt = (f"Based on this salary structure: {tax_data}, compare the Old vs New Indian Tax Regimes. "
                      f"Highlight which saves more money and suggest 2 tax-saving investments.")
            response = model.generate_content(prompt)
            st.write(response.text)

with tab3:
    st.header("FIRE Path Planner")
    target_age = st.slider("Target Retirement Age", 40, 70, 55)
    if st.button("Generate FIRE Roadmap"):
        prompt = (f"User is saving ₹{savings} per month and wants to retire at {target_age}. "
                  f"Calculate a rough month-by-month SIP goal and asset allocation (Equity/Debt) for an Indian investor.")
        st.write(model.generate_content(prompt).text)
