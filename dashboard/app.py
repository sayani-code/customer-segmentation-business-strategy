import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE CONFI

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# DAT

DATA_PATH = "data/processed/customer_segmentation_final.csv"

rfm = pd.read_csv(DATA_PATH)

# CUSTOM CS

st.markdown(
    """
    <style>

    /* ======================================================
       GLOBAL
       ====================================================== */

    .stApp {
        background: #F5F2EA;
        color: #17233C;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Hide Streamlit menu/footer */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }


    /* ======================================================
       TYPOGRAPHY
       ====================================================== */

    h1 {
        color: #17233C !important;
        font-size: 2.45rem !important;
        font-weight: 750 !important;
        letter-spacing: -0.8px;
        margin-bottom: 0.15rem !important;
    }

    h2 {
        color: #17233C !important;
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        margin-top: 1.4rem !important;
        margin-bottom: 0.8rem !important;
    }

    h3 {
        color: #17233C !important;
        font-weight: 700 !important;
    }

    .subtitle {
        color: #647089;
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
    }


    /* ======================================================
       GENERAL CARD
       ====================================================== */

    .dashboard-card {
        background: #FFFDFC;
        border: 1px solid #E7E3DA;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 5px 18px rgba(39, 48, 64, 0.06);
    }


    /* ======================================================
       KPI CARDS
       ====================================================== */

    .kpi-card {
        background: #FFFDFC;
        border: 1px solid #E6E2D9;
        border-radius: 16px;
        padding: 16px 18px;
        min-height: 105px;
        box-shadow: 0 5px 18px rgba(39, 48, 64, 0.055);

        display: flex;
        align-items: center;
        gap: 15px;
    }

    .kpi-icon {
        width: 52px;
        height: 52px;
        min-width: 52px;
        border-radius: 50%;

        display: flex;
        align-items: center;
        justify-content: center;

        font-size: 1.45rem;
    }

    .icon-blue {
        background: #E7F0FF;
        color: #1769C2;
    }

    .icon-green {
        background: #E4F5EA;
        color: #198754;
    }

    .icon-yellow {
        background: #FFF1D7;
        color: #C98700;
    }

    .icon-purple {
        background: #EEE6FF;
        color: #6841C6;
    }

    .icon-pink {
        background: #FBE5EF;
        color: #C13E76;
    }

    .icon-cyan {
        background: #E1F5F7;
        color: #158A99;
    }

    .icon-red {
        background: #FBE6E6;
        color: #C23B3B;
    }

    .kpi-content {
        display: flex;
        flex-direction: column;
    }

    .kpi-label {
        color: #69748A;
        font-size: 0.78rem;
        font-weight: 500;
        margin-bottom: 3px;
    }

    .kpi-value {
        color: #17233C;
        font-size: 1.55rem;
        font-weight: 750;
        line-height: 1.15;
    }


    /* ======================================================
       CHART CONTAINER
       ====================================================== */

    .chart-wrapper {
        background: #FFFDFC;
        border: 1px solid #E7E3DA;
        border-radius: 16px;
        padding: 10px 12px 5px 12px;
        box-shadow: 0 5px 18px rgba(39, 48, 64, 0.055);
    }


    /* ======================================================
       SELECTBOX
       ====================================================== */

    div[data-baseweb="select"] > div {
        background: #FFFDFC !important;
        border: 1px solid #DCD8CF !important;
        border-radius: 10px !important;
        color: #17233C !important;
    }


    /* ======================================================
       STRATEGY CARDS
       ====================================================== */

    .strategy-container {
       ....
    }

    .strategy-column {
        ....
    }

    .strategy-column:not(:last-child) {
       ....
    }

    .strategy-icon {
        ....
    }

    .strategy-label {
       ....
    }

    .strategy-text {
       ....
    }


    /* ======================================================
       DOWNLOAD BUTTON
       ====================================================== */

    .stDownloadButton button {
        background: #176B48 !important;
        color: white !important;
        border: none !important;
        border-radius: 9px !important;
        padding: 0.55rem 1.1rem !important;
        font-weight: 650 !important;
    }

    .stDownloadButton button:hover {
        background: #12583B !important;
    }


    /* ======================================================
       INFO NOTE
       ====================================================== */

    .info-note {
        background: #E8F1FC;
        border: 1px solid #D5E5F7;
        border-radius: 12px;
        padding: 14px 18px;
        color: #53667E;
        font-size: 0.82rem;
        line-height: 1.5;
    }

    .info-icon {
        font-size: 1.1rem;
        margin-right: 7px;
    }


    /* ======================================================
       DIVIDER
       ====================================================== */

    hr {
        border: none;
        border-top: 1px solid #DDD8CF;
        margin: 2rem 0 1.2rem 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# HEADE

st.markdown(
    """
    <h1>Customer Segmentation Dashboard</h1>

    <div class="subtitle">
        Customer behavior, value concentration, and segment-level business strategy
    </div>
    """,
    unsafe_allow_html=True
)

# EXECUTIVE KPI DAT

total_customers = rfm["CustomerID"].nunique()
total_segments = rfm["Segment"].nunique()
total_revenue = rfm["Total_Revenue"].sum()
avg_revenue = rfm["Total_Revenue"].mean()

# DATASET OVERVIE

st.subheader("Dataset Overview")

kpi_cols = st.columns(4)


# KPI 1
with kpi_cols[0]:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon icon-blue">👥</div>
            <div class="kpi-content">
                <div class="kpi-label">Customers</div>
                <div class="kpi-value">{total_customers:,}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# KPI 2
with kpi_cols[1]:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon icon-green">▥</div>
            <div class="kpi-content">
                <div class="kpi-label">Segments</div>
                <div class="kpi-value">{total_segments}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# KPI 3
with kpi_cols[2]:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon icon-yellow">🪙</div>
            <div class="kpi-content">
                <div class="kpi-label">Total Revenue</div>
                <div class="kpi-value">£{total_revenue:,.0f}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# KPI 4
with kpi_cols[3]:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon icon-purple">▥</div>
            <div class="kpi-content">
                <div class="kpi-label">Avg Revenue / Customer</div>
                <div class="kpi-value">£{avg_revenue:,.2f}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# CUSTOMER DISTRIBUTIO

st.subheader("Customer Distribution by Segment")

segment_counts = (
    rfm["Segment"]
    .value_counts()
    .rename_axis("Segment")
    .reset_index(name="Customers")
)

fig_customers = px.bar(
    segment_counts,
    x="Segment",
    y="Customers",
    text="Customers"
)

fig_customers.update_traces(
    marker_color="#77B5F5",
    textposition="outside",
    textfont=dict(
        color="#40516B",
        size=12
    )
)

fig_customers.update_layout(
    plot_bgcolor="#FFFDFC",
    paper_bgcolor="#FFFDFC",
    font=dict(
        family="Arial",
        color="#17233C"
    ),
    xaxis=dict(
        title="",
        tickangle=0,
        showgrid=False,
        zeroline=False
    ),
    yaxis=dict(
        title="Customers",
        gridcolor="#E3E6EA",
        zeroline=False
    ),
    margin=dict(
        l=20,
        r=20,
        t=25,
        b=25
    ),
    height=390
)

st.markdown('<div class="chart-wrapper">', unsafe_allow_html=True)

st.plotly_chart(
    fig_customers,
    use_container_width=True,
    config={
        "displayModeBar": False
    }
)

st.markdown('</div>', unsafe_allow_html=True)

# REVENUE CONTRIBUTIO

st.subheader("Revenue Contribution by Segment")

revenue_share = (
    rfm
    .groupby("Segment")["Total_Revenue"]
    .sum()
    .reset_index()
)

revenue_share["Revenue_Share"] = (
    revenue_share["Total_Revenue"]
    / revenue_share["Total_Revenue"].sum()
    * 100
)

revenue_share = revenue_share.sort_values(
    "Revenue_Share",
    ascending=False
)

fig_revenue = px.bar(
    revenue_share,
    x="Segment",
    y="Revenue_Share",
    text=revenue_share["Revenue_Share"].round(1).astype(str) + "%"
)

fig_revenue.update_traces(
    marker_color="#70C6A0",
    textposition="outside",
    textfont=dict(
        color="#40516B",
        size=12
    )
)

fig_revenue.update_layout(
    plot_bgcolor="#FFFDFC",
    paper_bgcolor="#FFFDFC",
    font=dict(
        family="Arial",
        color="#17233C"
    ),
    xaxis=dict(
        title="",
        tickangle=0,
        showgrid=False,
        zeroline=False
    ),
    yaxis=dict(
        title="Revenue Share (%)",
        range=[0, 100],
        gridcolor="#E3E6EA",
        zeroline=False
    ),
    margin=dict(
        l=20,
        r=20,
        t=25,
        b=25
    ),
    height=390
)

st.markdown('<div class="chart-wrapper">', unsafe_allow_html=True)

st.plotly_chart(
    fig_revenue,
    use_container_width=True,
    config={
        "displayModeBar": False
    }
)

st.markdown('</div>', unsafe_allow_html=True)

# SEGMENT EXPLORE

st.subheader("Segment Explorer")

st.caption("Select a customer segment")

selected_segment = st.selectbox(
    "Select a customer segment",
    sorted(rfm["Segment"].unique()),
    label_visibility="collapsed"
)

selected_data = rfm[
    rfm["Segment"] == selected_segment
]

# SELECTED SEGMENT KPI

segment_kpi_cols = st.columns(4)


with segment_kpi_cols[0]:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon icon-blue">👥</div>
            <div class="kpi-content">
                <div class="kpi-label">Customers</div>
                <div class="kpi-value">
                    {selected_data['CustomerID'].nunique():,}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with segment_kpi_cols[1]:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon icon-green">◉</div>
            <div class="kpi-content">
                <div class="kpi-label">Avg Revenue</div>
                <div class="kpi-value">
                    £{selected_data['Total_Revenue'].mean():,.2f}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with segment_kpi_cols[2]:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon icon-yellow">🛒</div>
            <div class="kpi-content">
                <div class="kpi-label">Avg Orders</div>
                <div class="kpi-value">
                    {selected_data['Total_Orders'].mean():.2f}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with segment_kpi_cols[3]:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon icon-purple">◷</div>
            <div class="kpi-content">
                <div class="kpi-label">Avg Recency</div>
                <div class="kpi-value">
                    {selected_data['Recency'].mean():.1f} days
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# SECONDARY SEGMENT KPI

secondary_cols = st.columns(2)

with secondary_cols[0]:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon icon-pink">◇</div>
            <div class="kpi-content">
                <div class="kpi-label">Avg Product Diversity</div>
                <div class="kpi-value">
                    {selected_data['Unique_Products'].mean():.1f}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with secondary_cols[1]:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon icon-cyan">▣</div>
            <div class="kpi-content">
                <div class="kpi-label">Avg Active Days</div>
                <div class="kpi-value">
                    {selected_data['Active_Days'].mean():.1f}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# STRATEG

strategy_map = {

    "High-Value Loyal": {
        "Objective": "Protect customer value",
        "Action": "Retention-focused communication and relevant cross-sell",
        "KPI": "Customer retention rate"
    },

    "Regular / Mid-Value": {
        "Objective": "Increase customer value",
        "Action": "Encourage repeat purchases and product expansion",
        "KPI": "Orders per customer"
    },

    "One-Time": {
        "Objective": "Create repeat behavior",
        "Action": "Post-purchase re-engagement",
        "KPI": "Second-purchase rate"
    },

    "Inactive / At-Risk": {
        "Objective": "Test reactivation",
        "Action": "Targeted re-engagement",
        "KPI": "Reactivation rate"
    }
}
# RECOMMENDED BUSINESS FOCU

st.subheader("Recommended Business Focus")

strategy = strategy_map[selected_segment]

with st.container(border=True):

    strategy_cols = st.columns(3)

    with strategy_cols[0]:
        st.markdown("🎯")
        st.caption("OBJECTIVE")
        st.markdown(f"**{strategy['Objective']}**")

    with strategy_cols[1]:
        st.markdown("⚙️")
        st.caption("RECOMMENDED ACTION")
        st.markdown(f"**{strategy['Action']}**")

    with strategy_cols[2]:
        st.markdown("📊")
        st.caption("PRIMARY KPI")
        st.markdown(f"**{strategy['KPI']}**")

# DOWNLOA

st.subheader("Selected Segment Data")

file_name = (
    selected_segment.lower()
    .replace(" ", "_")
    .replace("/", "_")
    + "_customers.csv"
)

st.download_button(
    label="⬇  Download Segment Data",
    data=selected_data.to_csv(index=False),
    file_name=file_name,
    mime="text/csv"
)

# FOOTER NOT

st.divider()

st.markdown(
    """
    <div class="info-note">
        <span class="info-icon">ⓘ</span>
        <strong>Note:</strong>
        Segments are based on historical transaction behavior.
        They are descriptive and do not represent confirmed churn probabilities
        or guaranteed future customer behavior.
    </div>
    """,
    unsafe_allow_html=True
)