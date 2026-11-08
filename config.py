"""
EduSaathi Global Configuration
==============================
Central constants, curriculum taxonomies, theme tokens, and metadata.
No personal identifiable information (PII) - strictly institutional.
"""

APP_NAME = "EduSaathi"
APP_TAGLINE = "AI-Powered Personalized Learning Companion for Rural Students"
APP_SUBTITLE = "Bridging the Rural-Urban Educational Divide via Offline-First Adaptive Edge AI"
APP_VERSION = "2.5.0 Enterprise"

# Institutional & Program Metadata (Strictly Institutional / No Personal Identifiers)
INITIATIVE = "National Rural EdTech AI Initiative"
AFFILIATION = "Center for Educational Artificial Intelligence & Assistive Technologies"
INSTITUTION = "Department of Artificial Intelligence & Data Science"
PROGRAM_NAME = "National Rural Education Enablement Initiative"
PARTNERSHIP = "AICTE Approved | In Collaboration with IBM SkillsBuild & BharatCares"
ACADEMIC_FRAMEWORK = "National Education Policy (NEP 2020) & UN SDG 4 Aligned"
COUNCIL = "Academic Oversight & AI Curriculum Advisory Directorate"

# Supported Vernacular Languages
LANGUAGES = {
    "en": "English",
    "te": "తెలుగు (Telugu)",
    "hi": "हिन्दी (Hindi)"
}
DEFAULT_LANGUAGE = "en"

# Pedagogical Thresholds
MASTERY_THRESHOLD = 0.85
PREREQ_THRESHOLD = 0.60
DIAGNOSTIC_QUESTIONS_PER_TOPIC = 1

# BKT Baseline Constants (Corbett & Anderson standard parameters)
BKT_DEFAULT_PARAMS = {
    "p_init": 0.30,   # Prior probability of mastery
    "p_transit": 0.15, # Transition probability per opportunity
    "p_slip": 0.10,   # Probability of making an error despite knowing concept
    "p_guess": 0.25   # Probability of lucky guess without knowing concept
}

# Modern GovTech/EdTech Palette (High-contrast, accessible WCAG 2.1 AAA compliant)
THEME = {
    "primary": "#0F2942",       # Deep Oceanic Navy
    "secondary": "#0D9488",     # Vibrant Modern Emerald / Teal
    "accent": "#F59E0B",        # Amber Gold
    "surface": "#FFFFFF",
    "background": "#F8FAFC",   # Clean Slate
    "text": "#0F172A",
    "muted": "#64748B",
    "border": "#E2E8F0",
    "card_bg": "#FFFFFF",
    "success": "#10B981",
    "danger": "#EF4444",
    "warning": "#F59E0B"
}
