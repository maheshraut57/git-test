import io

import pandas as pd
import plotly.express as px
import streamlit as st


def get_demo_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            "Region": ["North", "South", "West", "East", "North", "South"],
            "Revenue": [12000, 15500, 13200, 17800, 19000, 21000],
            "Orders": [220, 260, 240, 300, 320, 340],
        }
    )


st.set_page_config(page_title="Tables", page_icon="📊", layout="wide")
st.title("📊 Tables")
st.caption("Upload an Excel file and generate instant business visualizations.")

with st.sidebar:
    st.header("Quick actions")
    use_demo_data = st.toggle("Use demo data", value=True)

uploaded_file = st.file_uploader("Upload your Excel file (.xlsx or .xls)", type=["xlsx", "xls"])

if use_demo_data and uploaded_file is None:
    dataframe = get_demo_dataframe()
    sheet_name = "demo_sheet"
    st.success("Showing demo data. Upload your Excel anytime to replace this preview.")
else:
    if uploaded_file is None:
        st.info("Upload an Excel file, or enable 'Use demo data' from the sidebar.")
        st.stop()

    try:
        bytes_data = uploaded_file.read()
        workbook = pd.ExcelFile(io.BytesIO(bytes_data))
    except Exception as error:
        st.error(f"Unable to read this file as Excel: {error}")
        st.stop()

    sheet_name = st.selectbox("Choose a sheet", workbook.sheet_names)

    try:
        dataframe = workbook.parse(sheet_name=sheet_name)
    except Exception as error:
        st.error(f"Unable to parse sheet '{sheet_name}': {error}")
        st.stop()

if dataframe.empty:
    st.warning("This sheet has no rows.")
    st.stop()

st.subheader("Preview")
st.dataframe(dataframe.head(100), use_container_width=True)

numeric_columns = dataframe.select_dtypes(include=["number"]).columns.tolist()
all_columns = dataframe.columns.tolist()

if not numeric_columns:
    st.warning("No numeric columns found for charting. Try another sheet.")
    st.stop()

st.subheader("Visualization Builder")
col1, col2, col3 = st.columns(3)

with col1:
    chart_type = st.selectbox("Chart type", ["Bar", "Line", "Scatter", "Histogram"])

with col2:
    x_axis = st.selectbox("X-axis", all_columns)

with col3:
    y_axis = st.selectbox("Y-axis", numeric_columns)

plot_data = dataframe.dropna(subset=[x_axis, y_axis])

if plot_data.empty:
    st.warning("No valid rows left after removing missing values for selected columns.")
    st.stop()

if chart_type == "Bar":
    fig = px.bar(plot_data, x=x_axis, y=y_axis)
elif chart_type == "Line":
    fig = px.line(plot_data, x=x_axis, y=y_axis)
elif chart_type == "Scatter":
    fig = px.scatter(plot_data, x=x_axis, y=y_axis)
else:
    fig = px.histogram(plot_data, x=x_axis, y=y_axis)

fig.update_layout(margin=dict(l=10, r=10, t=40, b=10))
st.plotly_chart(fig, use_container_width=True)

st.download_button(
    label="Download cleaned CSV",
    data=plot_data.to_csv(index=False).encode("utf-8"),
    file_name=f"{sheet_name}_cleaned.csv",
    mime="text/csv",
)
