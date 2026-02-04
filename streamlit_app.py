import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# -----------------------------
# Character Lock
# -----------------------------

CHARACTER_BLOCK = """
Anastasia Ingram is a compact, athletic gymnast in her mid-to-late 20s,
4'7", dirty blonde hair, blue-gray eyes, strong gymnast build.
She is a quiet force who enjoys being observed.
Movement style is fluid, precise, realistic, more gymnast than superhero.
Signature move: Spiral Step.
Emotional system:
- Baseline: composed
- Smirk: brief mischievous one-sided smirk
- Smile: rare, only on true breakthrough success
She wears a small hollow ribbon sphere pendant with visible negative space,
matte finish, seasonally muted palette.
Location anchor: Portland, Oregon.
"""

SEASONS = {
    "Spring": "Light layers, soft muted tones, curious playful energy.",
    "Summer": "Minimal athletic wear, warm tones, magnetic mischievous tone.",
    "Fall": "Layered, grounded, moss and slate palette, refined control.",
    "Winter": "Architectural layers, cooler tones, composed minimalism."
}

CAMERA_PHASES = {
    "Phase 1": "Observational, mostly static, full-body framing.",
    "Phase 2": "Responsive tracking, subtle push-ins.",
    "Phase 3": "Symbiotic movement, smooth orbit during Spiral Step."
}

LOCATIONS = [
    "Waterfront plaza",
    "Rooftop deck",
    "Pedestrian bridge",
    "Concrete urban courtyard"
]

SUCCESS_LEVELS = [
    "Normal clean execution",
    "Strong refinement improvement",
    "Breakthrough success (rare full smile)"
]

# -----------------------------
# UI
# -----------------------------

st.title("Anastasia Ingram – AI Video Prompt Generator")

season = st.selectbox("Season", list(SEASONS.keys()))
location = st.selectbox("Location", LOCATIONS)
camera_phase = st.selectbox("Camera Phase", list(CAMERA_PHASES.keys()))
intensity = st.slider("Movement Intensity", 1, 10, 6)
mistake = st.checkbox("Include Minor Mistake Reset?")
success = st.selectbox("Success Level", SUCCESS_LEVELS)

generate = st.button("Generate Video Prompt")

# -----------------------------
# Prompt Builder
# -----------------------------

if generate:

    user_directive = f"""
Create a cinematic AI video prompt using the structured framework.

Season: {season}
Location: {location}, Portland Oregon
Camera Style: {CAMERA_PHASES[camera_phase]}
Movement Intensity: {intensity}/10
Mistake Included: {"Yes, minor balance correction with calm reset." if mistake else "No mistake."}
Success Level: {success}

Follow this output format:

Subject
Action
Movement Quality
Emotional Tone
Cinematography
Lighting
Symbol Integration
Ending Beat
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini"
,
        messages=[
            {"role": "system", "content": "You are a professional cinematographer and movement director."},
            {"role": "system", "content": CHARACTER_BLOCK},
            {"role": "user", "content": user_directive}
        ],
        temperature=0.8
    )

    st.subheader("Generated Prompt")
    st.write(response.choices[0].message.content)

