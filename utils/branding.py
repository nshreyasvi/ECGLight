# ==============================================================================
# ECGLight: Compute-Light Framework for Paper ECG Digitization & Classification
# 
# Author: Shreyasvi Natraj (ETH Zürich / SCAI Lab)
# Contact: snatraj@ethz.ch
# Licensed under the Non-Commercial Academic and Research License Agreement.
# ==============================================================================
"""
Logo and branding helpers for the ECGLight Dashboard.
Renders the custom ECGLight vector graphics, SCAI Lab branding, author card, and institutional footer.
All logo file reads are cached for maximum performance.
"""

import os
import base64
import streamlit as st

_ASSET_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")


@st.cache_data(show_spinner=False)
def _load_logo_b64(filename: str) -> str | None:
    """Load a logo file as base64 string. Cached per filename."""
    filepath = os.path.join(_ASSET_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None


def render_sidebar_logo():
    """Render the ECGLight vector graphics icon and SCAI Lab badge in the sidebar."""
    icon_b64 = _load_logo_b64("ecglight_icon.svg")
    scai_b64 = _load_logo_b64("scai_lab_logo.svg")

    if icon_b64:
        st.sidebar.markdown(
            f'<div style="text-align: center; padding: 10px 0 2px 0;">'
            f'<img src="data:image/svg+xml;base64,{icon_b64}" alt="ECGLight Icon" '
            f'style="height: 85px; filter: drop-shadow(0 4px 12px rgba(230, 57, 70, 0.25));" />'
            f'</div>',
            unsafe_allow_html=True
        )
    elif scai_b64:
        st.sidebar.markdown(
            f'<div style="text-align: center; padding: 8px 0 4px 0;">'
            f'<img src="data:image/svg+xml;base64,{scai_b64}" alt="SCAI Lab" '
            f'style="height: 65px;" />'
            f'</div>',
            unsafe_allow_html=True
        )


def render_sidebar_author_card():
    """Render a sleek author attribution card in the sidebar."""
    st.sidebar.markdown(
        """
        <div style="background: linear-gradient(135deg, #FFF1F2 0%, #F8FAFC 100%); 
                    border: 1px solid #FECDD3; border-radius: 10px; padding: 12px; margin-top: 10px; margin-bottom: 5px;">
            <div style="font-size: 0.75rem; font-weight: 700; color: #E63946; text-transform: uppercase; letter-spacing: 0.8px;">
                ⚡ Author
            </div>
            <div style="font-size: 0.95rem; font-weight: 700; color: #1E293B; margin-top: 2px;">
                Shreyasvi Natraj
            </div>
            <div style="font-size: 0.75rem; color: #64748B; margin-top: 1px;">
                ETH Zürich • SCAI Lab
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_logo_footer():
    """
    Render institutional logos as a footer bar at the bottom of each page,
    along with author attribution for Shreyasvi Natraj.
    Order: ETH Zürich → EOC → USI → Vanvitelli.
    """
    logos = [
        ("ETH_Zürich_Logo_black.svg.png", "ETH Zürich", "30px"),
        ("eoc_logo.png", "Istituto Cardiocentro Ticino (EOC)", "36px"),
        ("usi_logo.png", "USI", "36px"),
        ("Logo_Vanvitelli_university.svg.png", "Università della Campania Luigi Vanvitelli", "36px"),
    ]

    logo_html_items = []
    for filename, alt, height in logos:
        b64 = _load_logo_b64(filename)
        if b64:
            logo_html_items.append(
                f'<img src="data:image/png;base64,{b64}" alt="{alt}" '
                f'style="height: {height}; opacity: 0.75; transition: opacity 0.2s ease;" '
                f'onmouseover="this.style.opacity=1" onmouseout="this.style.opacity=0.75" />'
            )

    st.markdown("---")

    if logo_html_items:
        logos_row = "".join(logo_html_items)
        st.markdown(
            f'<div style="display: flex; align-items: center; justify-content: center; '
            f'gap: 36px; padding: 8px 0 10px 0; flex-wrap: wrap;">'
            f'{logos_row}</div>',
            unsafe_allow_html=True
        )

    # Author statement
    st.markdown(
        """
        <div style="text-align: center; color: #94A3B8; font-size: 0.78rem; padding: 4px 0 16px 0; line-height: 1.4;">
            <strong>ECGLight</strong> &bull; Author: <strong>Shreyasvi Natraj</strong> (ETH Zürich / SCAI Lab)<br/>
            <span>Released under the Non-Commercial Academic and Research License Agreement.</span>
        </div>
        """,
        unsafe_allow_html=True
    )


