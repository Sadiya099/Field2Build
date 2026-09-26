# app.py
"""
Field2Build — Deep Forest UI with clickable blueprint cards.
Choose a Domain. Discover What to Build.
"""

import streamlit as st
import chatbot as cb

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Field2Build",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# GLOBAL STYLING
# ============================================================
st.markdown("""
<style>
    :root {
        --paper:      #F7F4EC;
        --paper-2:    #EFEBDF;
        --paper-3:    #E5DFCC;
        --line:       #D5CFBD;
        --line-soft:  #E2DCCB;

        --ink:        #14211A;
        --ink-2:      #2F3D34;
        --ink-3:      #5F6D62;
        --ink-4:      #97A399;

        --forest:     #1F3D2B;
        --forest-2:   #2A5340;
        --forest-3:   #3A6B52;
        --moss:       #6B8E5A;

        --gold:       #C28A2C;
        --gold-2:     #A87620;
        --gold-bg:    #FAF0DA;

        --success:    #4D7C4B;
        --warning:    #B8791F;

        --serif: 'Fraunces', 'Playfair Display', 'Georgia', serif;
        --sans:  'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        --mono:  'JetBrains Mono', 'SF Mono', 'Menlo', 'Consolas', monospace;
    }

    html, body, [data-testid="stAppViewContainer"] {
        background: var(--paper);
        color: var(--ink);
    }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stSidebar"] {
        background: var(--paper-2);
        border-right: 1px solid var(--line);
    }
    [data-testid="stSidebar"] * { color: var(--ink-2); }
    [data-testid="stSidebar"] h2 {
        color: var(--forest);
        font-family: var(--mono);
        font-size: 11px;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        font-weight: 700;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 8rem;
        max-width: 1160px;
    }
    html, body, [class*="css"] { font-family: var(--sans); }
    h1, h2, h3 { color: var(--ink); letter-spacing: -0.02em; }

    /* ---------- Masthead ---------- */
    .masthead {
        display: flex;
        align-items: center;
        padding: 4px 0 18px 0;
        border-bottom: 2px solid var(--forest);
        margin-bottom: 32px;
    }
    .masthead .badge {
        width: 30px; height: 30px;
        background: var(--forest);
        color: var(--paper);
        display: grid;
        place-items: center;
        font-family: var(--serif);
        font-weight: 700;
        font-size: 18px;
        border-radius: 2px;
        margin-right: 14px;
    }
    .masthead .name {
        font-family: var(--serif);
        font-weight: 700;
        font-size: 24px;
        letter-spacing: -0.02em;
        color: var(--forest);
    }

    /* ---------- Hero ---------- */
    .hero {
        display: grid;
        grid-template-columns: 1.5fr 1fr;
        gap: 44px;
        align-items: start;
        padding: 12px 0 40px 0;
        border-bottom: 1px solid var(--line);
        margin-bottom: 26px;
    }
    .hero .kicker {
        font-family: var(--mono);
        font-size: 11px;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        color: var(--gold);
        font-weight: 700;
        margin-bottom: 18px;
        display: inline-flex;
        align-items: center;
        gap: 10px;
    }
    .hero .kicker::before {
        content: "";
        width: 26px; height: 2px;
        background: var(--gold);
        display: inline-block;
    }
    .hero h1 {
        font-family: var(--serif);
        font-size: 48px;
        line-height: 1.05;
        letter-spacing: -0.03em;
        font-weight: 700;
        color: var(--forest);
        margin: 0 0 20px 0;
    }
    .hero h1 em {
        font-style: italic;
        font-weight: 400;
        color: var(--gold);
    }
    .hero p.lede {
        font-family: var(--serif);
        font-size: 17.5px;
        line-height: 1.6;
        color: var(--ink-2);
        max-width: 560px;
        margin: 0 0 26px 0;
    }
    .hero .specs {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 4px;
    }
    .hero .spec {
        font-family: var(--mono);
        font-size: 10.5px;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--forest);
        background: var(--paper-2);
        border: 1px solid var(--line);
        padding: 6px 12px;
        border-radius: 2px;
        font-weight: 600;
    }
    .hero .spec::before {
        content: "●";
        color: var(--gold);
        font-size: 7px;
        margin-right: 8px;
        vertical-align: 1px;
    }

    .hero .aside {
        background: var(--forest);
        color: var(--paper);
        padding: 26px 26px 24px 26px;
        border-radius: 3px;
        position: relative;
        overflow: hidden;
    }
    .hero .aside::before {
        content: "";
        position: absolute;
        top: 0; right: 0;
        width: 60px; height: 60px;
        background: var(--gold);
        opacity: 0.12;
        clip-path: polygon(100% 0, 0 0, 100% 100%);
    }
    .hero .aside .label {
        font-family: var(--mono);
        font-size: 10.5px;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--gold);
        font-weight: 700;
        margin-bottom: 12px;
    }
    .hero .aside .defn {
        font-family: var(--serif);
        font-size: 15px;
        line-height: 1.55;
        color: #E8E5DA;
        font-style: italic;
        margin-bottom: 22px;
        padding-bottom: 22px;
        border-bottom: 1px solid rgba(255,255,255,0.12);
    }
    .hero .aside .stat {
        display: flex;
        justify-content: space-between;
        padding: 9px 0;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        font-family: var(--mono);
        font-size: 11.5px;
        color: #D5D0BE;
    }
    .hero .aside .stat:last-child { border-bottom: none; }
    .hero .aside .stat b {
        color: var(--gold);
        font-weight: 700;
        font-family: var(--sans);
        font-size: 13px;
    }

    /* ---------- Status strip ---------- */
    .statusline {
        display: flex;
        align-items: center;
        gap: 14px;
        font-family: var(--mono);
        font-size: 11.5px;
        color: var(--ink-2);
        background: var(--paper-2);
        border: 1px solid var(--line);
        border-left: 3px solid var(--gold);
        padding: 11px 18px;
        border-radius: 2px;
        margin-bottom: 30px;
        letter-spacing: 0.04em;
    }
    .statusline .dot {
        width: 8px; height: 8px;
        border-radius: 50%;
        background: var(--ink-4);
        display: inline-block;
        margin-right: 4px;
    }
    .statusline .dot.live  { background: var(--success); }
    .statusline .dot.await { background: var(--warning); }
    .statusline .tag {
        text-transform: uppercase;
        letter-spacing: 0.16em;
        color: var(--gold);
        font-weight: 700;
    }

    /* ---------- Section head ---------- */
    .section-head {
        display: flex;
        align-items: baseline;
        gap: 16px;
        margin: 40px 0 22px 0;
        padding-bottom: 14px;
        border-bottom: 2px solid var(--forest);
    }
    .section-head .title {
        font-family: var(--serif);
        font-size: 26px;
        font-weight: 700;
        color: var(--forest);
        letter-spacing: -0.02em;
    }
    .section-head .sub {
        margin-left: auto;
        font-family: var(--mono);
        font-size: 11px;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--ink-3);
    }

    /* ---------- Tier heading ---------- */
    .tierh {
        display: flex;
        align-items: center;
        gap: 14px;
        margin: 32px 0 14px 0;
        padding-bottom: 10px;
        border-bottom: 1px dashed var(--line);
    }
    .tierh .mark {
        width: 30px; height: 30px;
        border-radius: 50%;
        background: var(--forest);
        color: var(--paper);
        display: grid;
        place-items: center;
        font-family: var(--serif);
        font-weight: 700;
        font-size: 14px;
    }
    .tierh .nm {
        font-family: var(--mono);
        font-size: 12px;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--forest);
        font-weight: 700;
    }
    .tierh .ct {
        margin-left: auto;
        font-family: var(--mono);
        font-size: 11px;
        letter-spacing: 0.14em;
        color: var(--ink-3);
    }

    /* ---------- Clickable project card ---------- */
    div[data-testid="stButton"] > button.card-button {
        width: 100%;
        background: transparent;
        border: none;
        border-bottom: 1px solid var(--line-soft);
        border-radius: 0;
        padding: 18px 4px;
        text-align: left;
        color: var(--ink);
        font-family: var(--sans);
        font-weight: 500;
        font-size: 17px;
        letter-spacing: -0.005em;
        display: block;
        line-height: 1.45;
        transition: all 0.18s ease;
        white-space: normal;
        height: auto;
    }
    div[data-testid="stButton"] > button.card-button:hover {
        background: rgba(194,138,44,0.06);
        border-bottom-color: var(--gold);
        color: var(--forest);
        padding-left: 16px;
    }
    div[data-testid="stButton"] > button.card-button:focus {
        outline: none;
        box-shadow: none;
        color: var(--forest);
    }
    div[data-testid="stButton"] > button.card-button p {
        font-family: var(--sans);
        font-size: 17px;
        font-weight: 500;
        line-height: 1.45;
        margin: 0;
        text-align: left;
        color: inherit;
        white-space: normal;
    }

    /* ---------- Hint block ---------- */
    .hintblock {
        margin-top: 30px;
        padding: 18px 22px;
        background: var(--gold-bg);
        border-left: 3px solid var(--gold);
        border-radius: 2px;
        font-family: var(--serif);
        font-size: 15px;
        line-height: 1.6;
        color: var(--ink-2);
        font-style: italic;
    }
    .hintblock b {
        color: var(--forest);
        font-style: normal;
        font-weight: 700;
    }
    .hintblock .mono {
        font-family: var(--mono);
        font-style: normal;
        font-size: 12.5px;
        background: rgba(194,138,44,0.14);
        color: var(--gold-2);
        padding: 2px 7px;
        border-radius: 2px;
        font-weight: 600;
    }

    /* ---------- Action buttons (Continue / Shift) ---------- */
    div[data-testid="stButton"] > button.action-btn {
        background: var(--forest);
        border: 1px solid var(--forest);
        border-radius: 2px;
        color: var(--paper);
        font-family: var(--sans);
        font-weight: 500;
        font-size: 13.5px;
        letter-spacing: 0.02em;
        padding: 13px 18px;
        transition: all 0.18s ease;
        width: 100%;
    }
    div[data-testid="stButton"] > button.action-btn:hover {
        background: var(--gold);
        border-color: var(--gold);
        color: var(--ink);
    }
    div[data-testid="stButton"] > button[kind="primary"] {
        background: var(--gold);
        border-color: var(--gold);
        color: var(--ink);
        font-weight: 600;
    }
    div[data-testid="stButton"] > button[kind="primary"]:hover {
        background: var(--gold-2);
        border-color: var(--gold-2);
        color: var(--paper);
    }

    /* ---------- Chat bubbles ---------- */
    [data-testid="stChatMessage"] {
        background: #FBF9F3;
        border: 1px solid var(--line);
        border-radius: 3px;
        padding: 18px 22px;
        margin-bottom: 10px;
    }
    [data-testid="stChatMessage"] p,
    [data-testid="stChatMessage"] li,
    [data-testid="stChatMessage"] span { color: var(--ink); }
    [data-testid="stChatMessage"] code {
        background: var(--gold-bg);
        color: var(--gold-2);
        padding: 2px 7px;
        border-radius: 2px;
        font-family: var(--mono);
        font-size: 12.5px;
        font-weight: 600;
    }
    [data-testid="stChatMessage"] h3 {
        font-family: var(--serif);
        font-size: 22px;
        font-weight: 700;
        color: var(--forest);
        letter-spacing: -0.02em;
    }
    [data-testid="stChatMessage"] h2 {
        font-family: var(--serif);
        font-weight: 700;
        color: var(--forest);
        border-bottom: 1px solid var(--line);
        padding-bottom: 8px;
    }
    [data-testid="stChatMessage"] strong {
        color: var(--gold-2);
        font-weight: 700;
    }

    /* ---------- Chat input ---------- */
    [data-testid="stChatInput"] { border-radius: 2px; }
    [data-testid="stChatInput"] > div {
        background: #FBF9F3;
        border: 1px solid var(--forest);
        border-radius: 3px;
        transition: all 0.18s ease;
    }
    [data-testid="stChatInput"] > div:focus-within {
        border-color: var(--gold);
        box-shadow: 0 0 0 3px rgba(194,138,44,0.18);
    }
    [data-testid="stChatInput"] textarea {
        background: transparent !important;
        color: var(--ink) !important;
        caret-color: var(--gold) !important;
        font-family: var(--sans);
        font-size: 14px;
    }
    [data-testid="stChatInput"] textarea::placeholder {
        color: var(--ink-3) !important;
        font-family: var(--serif);
        font-style: italic;
        font-size: 14px;
    }
    [data-testid="stChatInput"] button {
        background: var(--forest);
        color: var(--paper);
        border-radius: 2px;
        border: none;
    }
    [data-testid="stChatInput"] button:hover { background: var(--gold); }
    [data-testid="stChatInput"] svg { color: var(--paper); fill: var(--paper); }

    /* ---------- Alerts ---------- */
    [data-testid="stAlert"] {
        background: #FDF3E0;
        border: 1px solid #E8CE94;
        border-left: 3px solid var(--warning);
        color: #5C400F;
        border-radius: 2px;
        font-family: var(--serif);
        font-size: 14.5px;
        font-style: italic;
    }
    [data-testid="stAlert"] p { color: #5C400F; }

    ::-webkit-scrollbar { width: 10px; height: 10px; }
    ::-webkit-scrollbar-track { background: var(--paper-2); }
    ::-webkit-scrollbar-thumb { background: var(--line); border-radius: 0; }
    ::-webkit-scrollbar-thumb:hover { background: var(--gold); }

    hr { border: none; border-top: 1px solid var(--line); margin: 24px 0; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# SESSION STATE
# ============================================================
def init_state():
    defaults = {
        "stage": "greeting",
        "unlocked": False,
        "domain": None,
        "pending_correction": None,
        "projects": [],
        "title_registry": set(),
        "active_index": None,
        "messages": [],
        "warning": None,
        "show_list": False,
        "await_buttons": False,
        "shuffle_count": 0,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


init_state()


# ============================================================
# HELPERS
# ============================================================
def push_message(role: str, content: str):
    st.session_state.messages.append({"role": role, "content": content})


def render_chat():
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


def show_blueprint(idx: int):
    """Common transition: display blueprint #idx and pause for buttons."""
    project = st.session_state.projects[idx - 1]
    st.session_state.active_index = idx
    st.session_state.show_list = False
    st.session_state.await_buttons = True
    st.session_state.stage = "await_buttons"
    push_message(
        "assistant",
        f"**Blueprint {idx}** — *{project['title']}* ({project['difficulty']})"
    )
    push_message("assistant", cb.build_blueprint(project))
    push_message("assistant", "Choose your next step from the buttons below.")


def render_projects():
    """Render clickable cards for each project, grouped by tier."""
    if not st.session_state.show_list or not st.session_state.projects:
        return

    st.markdown(
        """
        <div class="section-head">
            <div class="title">The Blueprint Set</div>
            <div class="sub">Click any card to open its build guide</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    tiers = {"Beginner": [], "Intermediate": [], "Advanced": []}
    for i, p in enumerate(st.session_state.projects, start=1):
        tiers[p["difficulty"]].append((i, p))

    tier_meta = [
        ("Beginner",     "Ⅰ", "Easy · 01–03"),
        ("Intermediate", "Ⅱ", "Medium · 04–06"),
        ("Advanced",     "Ⅲ", "Hard · 07–09"),
    ]

    for tier_key, numeral, sub in tier_meta:
        st.markdown(
            f"""
            <div class="tierh">
                <div class="mark">{numeral}</div>
                <div class="nm">{tier_key} Level</div>
                <div class="ct">{sub}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        for idx, proj in tiers[tier_key]:
            label = f"{idx:02d}   ·   {proj['title']}"
            if st.button(label, key=f"card_{idx}", use_container_width=True):
                show_blueprint(idx)
                st.rerun()

    st.markdown(
        """
        <div class="hintblock">
            <b>How to use</b> — Click any blueprint above to reveal its full
            step-by-step build guide. Type
            <span class="mono">new</span>,
            <span class="mono">different</span>, or
            <span class="mono">more</span>
            in the chat to shuffle the batch.
        </div>
        """,
        unsafe_allow_html=True
    )


def render_status_bar():
    if not st.session_state.unlocked:
        dot, tag, text = "", "LOCKED", "type hi or hello to begin"
    elif st.session_state.stage == "confirm_typo":
        dot, tag, text = "await", "AWAIT", "confirm correction — yes / no"
    elif st.session_state.stage == "await_buttons":
        dot, tag, text = "await", "AWAIT", "choose an option below"
    elif st.session_state.stage == "domain_input":
        dot, tag, text = "live", "READY", "enter a domain or field"
    elif st.session_state.stage == "project_list":
        dot, tag, text = "live", "ACTIVE", f"{st.session_state.domain} — click any blueprint below"
    else:
        dot, tag, text = "live", "ACTIVE", "—"

    st.markdown(
        f"""
        <div class="statusline">
            <span><span class="dot {dot}"></span></span>
            <span class="tag">{tag}</span>
            <span>—</span>
            <span>{text}</span>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# MASTHEAD
# ============================================================
st.markdown(
    """
    <div class="masthead">
        <span class="badge">F</span>
        <span class="name">Field2Build</span>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HERO
# ============================================================
st.markdown(
    """
    <div class="hero">
        <div class="main">
            <div class="kicker">Project Discovery Engine</div>
            <h1>Choose a domain.<br>
                Discover <em>what to build.</em></h1>
            <p class="lede">
                Nine resume-grade blueprints per domain — beginner, intermediate,
                and advanced — each paired with a step-by-step three-phase
                build guide.
            </p>
            <div class="specs">
                <span class="spec">Resume / CV-Ready</span>
                <span class="spec">Step-by-Step Guides</span>
                <span class="spec">Typo-Aware</span>
                <span class="spec">Non-Repeating</span>
            </div>
        </div>
        <div class="aside">
            <div class="label">Definition</div>
            <div class="defn">
                A blueprint is a structural plan — phase by phase, step by step —
                for building a real, portfolio-worthy technical project.
            </div>
            <div class="label">Session</div>
            <div class="stat"><span>Domain</span><span><b>{domain}</b></span></div>
            <div class="stat"><span>Blueprints</span><span><b>{bp_count}</b> / 9</span></div>
            <div class="stat"><span>Shuffles</span><span><b>{shuffles}</b></span></div>
        </div>
    </div>
    """.format(
        domain=st.session_state.domain or "—",
        bp_count=len(st.session_state.projects),
        shuffles=st.session_state.shuffle_count
    ),
    unsafe_allow_html=True
)

render_status_bar()


# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("## Session")
    st.markdown(f"**Domain** — {st.session_state.domain or 'not set'}")
    st.markdown(f"**Stage** — `{st.session_state.stage}`")
    st.markdown(f"**Blueprints** — {len(st.session_state.title_registry)}")
    st.markdown(f"**Shuffles** — {st.session_state.shuffle_count}")

    st.markdown("---")
    st.markdown("## How it works")
    st.markdown(
        "1. Type `hi` or `hello` to unlock\n"
        "2. Enter any domain — typos are auto-corrected\n"
        "3. **Click any blueprint card** to open its build guide\n"
        "4. Continue in this domain, or Shift to a new one\n"
        "5. Type `new` anytime to shuffle all 9"
    )

    st.markdown("---")
    if st.button("↻ Reset session", use_container_width=True):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()


# ============================================================
# CHAT TRANSCRIPT
# ============================================================
if not st.session_state.messages and not st.session_state.unlocked:
    push_message(
        "assistant",
        "### Welcome to Field2Build\n"
        "*Choose a domain. Discover what to build.*\n\n"
        "To start, type `hi` or `hello` below."
    )

render_chat()


# ============================================================
# WARNING
# ============================================================
if st.session_state.warning:
    st.warning(st.session_state.warning)
    st.session_state.warning = None


# ============================================================
# PROJECT LIST (clickable cards)
# ============================================================
render_projects()


# ============================================================
# TWO-BUTTON PANEL (Continue / Shift)
# ============================================================
if st.session_state.await_buttons:
    st.markdown(
        """
        <div class="section-head">
            <div class="title">Next Action</div>
            <div class="sub">Chat paused</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Continue in this domain", key="btn_continue",
                     use_container_width=True, type="primary"):
            st.session_state.await_buttons = False
            st.session_state.show_list = True
            st.session_state.active_index = None
            st.session_state.stage = "project_list"
            push_message(
                "assistant",
                f"Continuing in **{st.session_state.domain}**. "
                "Click any blueprint card below, or type `new` to shuffle."
            )
            st.rerun()

    with col2:
        if st.button("Shift to another domain", key="btn_shift",
                     use_container_width=True):
            st.session_state.await_buttons = False
            st.session_state.show_list = False
            st.session_state.active_index = None
            st.session_state.projects = []
            st.session_state.pending_correction = None
            st.session_state.stage = "domain_input"
            push_message("assistant", "Shift mode — enter a **new domain / field**.")
            st.rerun()


# ============================================================
# BOTTOM INPUT
# ============================================================
user_input = st.chat_input(
    "Type a message… (hi / domain / yes / no / new)",
    disabled=st.session_state.await_buttons
)


# ============================================================
# STATE MACHINE
# ============================================================
if user_input:
    raw = user_input.strip()
    if not raw:
        st.session_state.warning = "Please enter a valid message."
        st.rerun()

    # ---------- STAGE 1: GREETING LOCK ----------
    if not st.session_state.unlocked:
        push_message("user", raw)
        if cb.is_greeting(raw):
            st.session_state.unlocked = True
            st.session_state.stage = "domain_input"
            push_message(
                "assistant",
                "**Unlocked.** Enter the **domain / field** you want blueprints for.\n\n"
                "*Examples: Artificial Intelligence, Cyber Security, Electronics, Finance.*"
            )
        else:
            st.session_state.warning = "Type `hi` or `hello` to unlock the workflow."
        st.rerun()

    # ---------- STAGE 2: DOMAIN INPUT ----------
    if st.session_state.stage == "domain_input":
        push_message("user", raw)

        if cb.is_exact_known_domain(raw):
            st.session_state.domain = cb.pretty_domain(raw)
            st.session_state.projects = cb.generate_batch(
                st.session_state.domain, st.session_state.title_registry
            )
            st.session_state.active_index = None
            st.session_state.show_list = True
            st.session_state.stage = "project_list"
            push_message(
                "assistant",
                f"**Domain confirmed:** {st.session_state.domain}\n\n"
                "Click any blueprint card below to open its build guide."
            )
            st.rerun()

        alias_target = cb.is_exact_alias(raw)
        if alias_target:
            st.session_state.pending_correction = alias_target
            st.session_state.stage = "confirm_typo"
            push_message(
                "assistant",
                f"Sorry, did you mean **'{cb.pretty_domain(alias_target)}'**?\n\n"
                "Reply `yes` to proceed, or `no` to rewrite."
            )
            st.rerun()

        corrected, _ = cb.find_closest_domain(raw)
        if corrected:
            st.session_state.pending_correction = corrected
            st.session_state.stage = "confirm_typo"
            push_message(
                "assistant",
                f"Sorry, did you mean **'{cb.pretty_domain(corrected)}'**?\n\n"
                "Reply `yes` to proceed, or `no` to rewrite."
            )
            st.rerun()

        st.session_state.domain = cb.pretty_domain(raw)
        st.session_state.projects = cb.generate_batch(
            st.session_state.domain, st.session_state.title_registry
        )
        st.session_state.active_index = None
        st.session_state.show_list = True
        st.session_state.stage = "project_list"
        push_message(
            "assistant",
            f"**Domain accepted:** {st.session_state.domain}\n\n"
            "Click any blueprint card below to open its build guide."
        )
        st.rerun()

    # ---------- STAGE 3: TYPO CONFIRMATION ----------
    if st.session_state.stage == "confirm_typo":
        push_message("user", raw)

        if cb.is_affirmative(raw):
            st.session_state.domain = cb.pretty_domain(st.session_state.pending_correction)
            st.session_state.pending_correction = None
            st.session_state.projects = cb.generate_batch(
                st.session_state.domain, st.session_state.title_registry
            )
            st.session_state.active_index = None
            st.session_state.show_list = True
            st.session_state.stage = "project_list"
            push_message(
                "assistant",
                f"**Domain set:** {st.session_state.domain}\n\n"
                "Click any blueprint card below to open its build guide."
            )
            st.rerun()

        elif cb.is_negative(raw):
            st.session_state.pending_correction = None
            st.session_state.stage = "domain_input"
            push_message("assistant", "Enter a **different domain / field**.")
            st.rerun()

        else:
            st.session_state.warning = "Reply `yes` to proceed, or `no` to rewrite."
            st.rerun()

    # ---------- STAGE 4: PROJECT LIST ----------
    if st.session_state.stage == "project_list":
        push_message("user", raw)

        if cb.is_shuffle_command(raw):
            st.session_state.active_index = None
            st.session_state.projects = cb.generate_batch(
                st.session_state.domain, st.session_state.title_registry
            )
            st.session_state.shuffle_count += 1
            st.session_state.show_list = True
            push_message("assistant", "Fresh batch — nine new blueprints.")
            st.rerun()

        if raw.isdigit() and 1 <= int(raw) <= 9:
            show_blueprint(int(raw))
            st.rerun()

        st.session_state.warning = "Type `new` to shuffle the batch, or click a blueprint card above."
        st.rerun()