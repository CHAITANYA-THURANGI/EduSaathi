"""
EduSaathi Prerequisite-Aware Recommendation Engine
===================================================
Constructs a Directed Acyclic Graph (DAG) of curriculum dependencies
and sequences prioritized remedial learning paths.
"""

from config import PREREQ_THRESHOLD, MASTERY_THRESHOLD

PREREQUISITE_DAG = {
    "Linear Equations": ["Fractions", "Simple Equations"],
    "Quadratic Equations": ["Linear Equations", "Polynomials"],
    "Mensuration": ["Geometry Basics", "Perimeter & Area"],
    "Percentages": ["Decimals", "Ratio and Proportion"],
    "Ratio and Proportion": ["Fractions"],
    "Chemical Reactions": ["Atoms & Molecules", "Physical & Chemical Changes"],
    "Force & Laws of Motion": ["Force & Pressure"]
}

REMEDIAL_CONTENT_CATALOG = {
    "Linear Equations": {
        "title": "Mastering One-Variable Equations with Step-by-Step Visual Balance",
        "format": "Interactive Step-by-Step Exercise",
        "duration_min": 8,
        "summaries": {
            "en": "Focus on keeping both sides of the equation balanced like a physical scale.",
            "hi": "समीकरण के दोनों पक्षों को तराजू की तरह संतुलित रखने का अभ्यास करें।",
            "te": "సమీకరణం యొక్క రెండు వైపులా త్రాసులా సమానంగా ఉంచడం ప్రాక్టీస్ చేయండి."
        }
    },
    "Fractions": {
        "title": "Visualizing Common Denominators & Fraction Addition",
        "format": "Visual Concept Cards",
        "duration_min": 6,
        "summaries": {
            "en": "Understand fractions as parts of a whole pizza or farm field before adding.",
            "hi": "भिन्नों को जोड़ने से पहले उन्हें एक पूरे हिस्से के रूप में देखें।",
            "te": "భిన్నాలను కలపడానికి ముందు వాటిని సమాన భాగాలుగా అర్థం చేసుకోండి."
        }
    },
    "Percentages": {
        "title": "Converting Fractions & Decimals into Percentages",
        "format": "Bilingual Practice Quiz",
        "duration_min": 7,
        "summaries": {
            "en": "Master calculating discounts, interest, and village market rates.",
            "hi": "छूट, ब्याज और बाज़ार के हिसाब-किताब के माध्यम से प्रतिशत सीखें।",
            "te": "తగ్గింపులు, వడ్డీ మరియు గ్రామ మార్కెట్ లెక్కలతో శాతాలను నేర్చుకోండి."
        }
    },
    "Ratio and Proportion": {
        "title": "Unitary Method & Proportion in Daily Rural Life",
        "format": "Interactive Story Prompts",
        "duration_min": 8,
        "summaries": {
            "en": "Apply proportional thinking to crop yields and recipe mixtures.",
            "hi": "फसल की पैदावार और मिश्रण के व्यावहारिक उदाहरणों से अनुपात समझें।",
            "te": "పంట దిగుబడులు మరియు మిశ్రమాల ఉదాహరణలతో నిష్పత్తులను నేర్చుకోండి."
        }
    },
    "Decimals": {
        "title": "Decimals as Place Value & Real-World Measurements",
        "format": "Interactive Visual Slider",
        "duration_min": 6,
        "summaries": {
            "en": "Master decimal addition, subtraction, and currency calculations.",
            "hi": "दशमलव जोड़, घटाव और मुद्रा गणना में महारत हासिल करें।",
            "te": "దశాంశాల కూడిక, తీసివేత మరియు కరెన్సీ లెక్కలను నేర్చుకోండి."
        }
    },
    "Simple Equations": {
        "title": "Mastering One-Variable Equations with Step-by-Step Balance",
        "format": "Interactive Step-by-Step Exercise",
        "duration_min": 8,
        "summaries": {
            "en": "Focus on keeping both sides of the equation balanced like a physical scale.",
            "hi": "समीकरण के दोनों पक्षों को तराजू की तरह संतुलित रखने का अभ्यास करें।",
            "te": "సమీకరణం యొక్క రెండు వైపులా త్రాసులా సమానంగా ఉంచడం ప్రాక్టీస్ చేయండి."
        }
    },
    "Ratio & Proportion": {
        "title": "Unitary Method & Proportion in Daily Rural Life",
        "format": "Interactive Story Prompts",
        "duration_min": 8,
        "summaries": {
            "en": "Apply proportional thinking to crop yields and recipe mixtures.",
            "hi": "फसल की पैदावार और मिश्रण के व्यावहारिक उदाहरणों से अनुपात समझें।",
            "te": "పంట దిగుబడులు మరియు మిశ్రమాల ఉదాహరణలతో నిష్పత్తులను నేర్చుకోండి."
        }
    }
}

class RecommendationEngine:
    def __init__(self, dag=PREREQUISITE_DAG, catalog=REMEDIAL_CONTENT_CATALOG):
        self.dag = dag
        self.catalog = catalog

    def is_eligible(self, topic: str, mastery_map: dict) -> bool:
        """A topic is eligible only if all its prerequisites have achieved baseline mastery."""
        prereqs = self.dag.get(topic, [])
        return all(mastery_map.get(p, 0.0) >= PREREQ_THRESHOLD for p in prereqs)

    def sequence_path(self, mastery_map: dict) -> list:
        """
        Sequences unmastered topics prioritizing root prerequisites and lowest mastery scores.
        """
        unmastered = [t for t, score in mastery_map.items() if score < MASTERY_THRESHOLD]
        ranked_path = []
        
        # Sort by prerequisite fulfillment then by lowest mastery
        for topic in sorted(unmastered, key=lambda t: (not self.is_eligible(t, mastery_map), mastery_map[t])):
            prereqs = self.dag.get(topic, [])
            resource = self.catalog.get(topic, {
                "title": f"Core Practice & Concepts: {topic}",
                "format": "Targeted Exercise",
                "duration_min": 8,
                "summaries": {
                    "en": f"Focused practice to master {topic}.",
                    "hi": f"{topic} में अपनी समझ को मजबूत करने के लिए विशेष अभ्यास।",
                    "te": f"{topic} లో పట్టు సాధించడానికి ప్రత్యేక అభ్యాసం."
                }
            })
            ranked_path.append({
                "topic": topic,
                "mastery": mastery_map.get(topic, 0.0),
                "is_eligible": self.is_eligible(topic, mastery_map),
                "prerequisites": prereqs,
                "resource": resource,
                "priority": "HIGH" if (not self.is_eligible(topic, mastery_map) or mastery_map.get(topic, 0.0) < 0.40) else "MEDIUM"
            })
            
        return ranked_path
