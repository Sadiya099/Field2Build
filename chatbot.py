# chatbot.py
"""
Pure logic backend — Universal Project Idea Generator.
"""

import random

# ============================================================
# SHORT-FORM ALIASES
# ============================================================
DOMAIN_ALIASES = {
    "ai": "artificial intelligence",
    "ml": "machine learning",
    "dl": "deep learning",
    "ds": "data science",
    "da": "data analytics",
    "bd": "big data",
    "cc": "cloud computing",
    "ec": "edge computing",
    "qc": "quantum computing",
    "iot": "internet of things",
    "cv": "computer vision",
    "nlp": "natural language processing",
    "web": "web development",
    "app": "mobile development",
    "game": "game development",
    "se": "software engineering",
    "it": "information technology",
    "db": "database management",
    "dbms": "database management",
    "net": "networking",
    "os": "operating systems",
    "cs": "computer science",
    "ece": "electronics",
    "eee": "electrical engineering",
    "mech": "mechanical engineering",
    "civil": "civil engineering",
    "chem": "chemical engineering",
    "aero": "aerospace engineering",
    "vlsi": "vlsi design",
    "sp": "signal processing",
    "comm": "communication engineering",
    "ar": "augmented reality",
    "vr": "virtual reality",
    "ux": "ui ux design",
    "ui": "ui ux design",
    "dm": "digital marketing",
    "eh": "ethical hacking",
    "pentest": "penetration testing",
    "df": "digital forensics",
    "sec": "cyber security",
    "cyber": "cyber security",
    "csec": "cyber security",
    "infosec": "cyber security",
    "fin": "finance",
    "acct": "accounting",
    "bank": "banking",
    "ins": "insurance",
    "inv": "investment",
    "stock": "stock market",
    "crypto": "cryptocurrency",
    "ecom": "e-commerce",
    "mkt": "marketing",
    "hr": "human resources",
    "scm": "supply chain",
    "logi": "logistics",
    "ba": "business analytics",
    "pm": "project management",
    "med": "healthcare",
    "bio": "biotechnology",
    "agri": "agriculture",
    "agti": "agritech",
    "agtech": "agritech",
    "ag": "agriculture",
    "food": "food technology",
    "env": "environmental science",
    "re": "renewable energy",
    "solar": "solar energy",
    "wind": "wind energy",
    "sust": "sustainability",
    "phy": "physics",
    "math": "mathematics",
    "stats": "statistics",
    "geo": "geology",
    "edu": "education",
    "elearn": "e-learning",
    "psy": "psychology",
    "soc": "sociology",
    "journ": "journalism",
    "tour": "tourism",
    "hosp": "hospitality",
    "sports": "sports technology",
}

# ============================================================
# VOCABULARY POOLS
# ============================================================
PREFIXES = [
    "AI-Powered", "Autonomous", "Scalable", "Distributed", "Intelligent",
    "Real-Time", "Predictive", "Adaptive", "Cloud-Native", "Edge-Optimized",
    "Self-Healing", "Blockchain-Enabled", "Quantum-Resistant", "Low-Latency",
    "Federated", "Explainable", "Generative", "Zero-Trust", "Event-Driven",
    "Microservice-Based", "Serverless", "Hyper-Automated", "Cognitive",
    "Context-Aware", "Multi-Modal", "Hybrid", "Reinforcement-Learned"
]

CORE_CONCEPTS = [
    "Analytics Engine", "Detection Framework", "Optimization Platform",
    "Decision Support System", "Monitoring Suite", "Threat Intelligence Hub",
    "Forecasting Pipeline", "Recommendation Engine", "Classification System",
    "Segmentation Framework", "Risk Assessment Model", "Automation Workflow",
    "Data Fusion Platform", "Anomaly Detection System", "Knowledge Graph",
    "Simulation Environment", "Control Plane", "Orchestration Layer",
    "Insight Dashboard", "Prediction Service", "Diagnostic Tool",
    "Compliance Auditor", "Resource Allocator", "Pattern Recognition Module"
]

DOMAIN_SUFFIXES = [
    "for Smart Cities", "for Healthcare", "for Financial Services",
    "for Supply Chain", "for Cybersecurity", "for Agriculture",
    "for Education", "for E-Commerce", "for Manufacturing",
    "for Energy Grids", "for Transportation", "for Telecommunications",
    "for Retail Intelligence", "for Environmental Monitoring",
    "for Aerospace Systems", "for Legal Tech", "for Insurance",
    "for Real Estate", "for Media and Entertainment", "for Logistics"
]

# ============================================================
# DOMAIN TAXONOMY
# ============================================================
DOMAIN_TAXONOMY = {
    "electronics": {
        "concepts": [
            "Circuit Design Suite", "Embedded Controller Platform",
            "PCB Layout Engine", "VLSI Optimization Tool",
            "IoT Sensor Framework", "Microcontroller Debugger",
            "Analog Signal Analyzer", "Power Management System",
            "FPGA Synthesis Pipeline", "Signal Conditioning Module",
            "Digital Logic Verifier", "Semiconductor Test Bench",
            "RISC-V Emulator", "FPGA Bitstream Optimizer",
            "Real-Time Oscilloscope Dashboard"
        ],
        "suffix": "for Electronics Engineering"
    },
    "electrical engineering": {
        "concepts": [
            "Power Distribution Analyzer", "Smart Grid Controller",
            "Motor Drive Optimizer", "Transformer Monitoring Suite",
            "Load Forecasting Engine", "Renewable Integration Platform",
            "Protection Relay Simulator", "Energy Metering Dashboard"
        ],
        "suffix": "for Electrical Engineering"
    },
    "communication engineering": {
        "concepts": [
            "Antenna Design Suite", "Digital Modulation Analyzer",
            "MIMO Channel Simulator", "Wireless Protocol Stack",
            "Optical Fiber Link Budget Tool", "RF Circuit Optimizer",
            "Software-Defined Radio Platform", "Satellite Link Planner",
            "5G NR Simulation Framework", "Spectrum Analyzer Dashboard",
            "Cellular Network Optimizer", "Beamforming Controller"
        ],
        "suffix": "for Communication Engineering"
    },
    "wireless communication": {
        "concepts": [
            "Bluetooth Mesh Network Manager", "Wi-Fi Performance Analyzer",
            "LoRa Gateway Orchestrator", "Cognitive Radio Engine",
            "Interference Mitigation Suite", "mmWave Channel Modeler"
        ],
        "suffix": "for Wireless Systems"
    },
    "mechanical engineering": {
        "concepts": [
            "CAD Automation Toolkit", "Thermal Analysis Suite",
            "Vibration Monitor", "Finite Element Solver",
            "CFD Simulation Platform", "Robotics Kinematics Designer"
        ],
        "suffix": "for Mechanical Engineering"
    },
    "civil engineering": {
        "concepts": [
            "Structural Health Monitor", "BIM Integration Platform",
            "Traffic Flow Simulator", "Construction Project Tracker",
            "Geotechnical Analyzer", "Smart City Infrastructure Planner"
        ],
        "suffix": "for Civil Engineering"
    },
    "chemical engineering": {
        "concepts": [
            "Process Simulation Engine", "Reactor Optimization Suite",
            "Safety Compliance Tracker", "Material Property Database",
            "Distillation Column Designer", "Heat Exchanger Modeler"
        ],
        "suffix": "for Chemical Engineering"
    },
    "aerospace engineering": {
        "concepts": [
            "Flight Dynamics Simulator", "Satellite Orbit Planner",
            "Rocket Propulsion Analyzer", "UAV Autopilot Stack",
            "Aerodynamic CFD Suite", "Space Mission Planner"
        ],
        "suffix": "for Aerospace"
    },
    "mechatronics": {
        "concepts": [
            "Motion Control Framework", "Sensor Fusion Platform",
            "Actuator Optimization Suite", "HIL Test Bench",
            "Industrial Robot Controller"
        ],
        "suffix": "for Mechatronics"
    },
    "control systems": {
        "concepts": [
            "PID Autotuner", "State-Space Controller Designer",
            "Model Predictive Control Engine", "Robust Control Framework",
            "Adaptive Controller Suite", "Nonlinear System Simulator"
        ],
        "suffix": "for Control Systems"
    },
    "instrumentation": {
        "concepts": [
            "Sensor Calibration Suite", "Industrial Measurement Platform",
            "Data Acquisition Framework", "Process Control Instrumentation",
            "Smart Meter Analytics"
        ],
        "suffix": "for Instrumentation"
    },
    "vlsi design": {
        "concepts": [
            "RTL Synthesis Optimizer", "Timing Analysis Suite",
            "Place-and-Route Engine", "Verification Testbench Generator",
            "Low-Power Design Toolkit"
        ],
        "suffix": "for VLSI Design"
    },
    "signal processing": {
        "concepts": [
            "DSP Filter Designer", "Audio Enhancement Engine",
            "Radar Signal Analyzer", "Image Compression Toolkit",
            "Speech Enhancement Framework"
        ],
        "suffix": "for Signal Processing"
    },
    "telecommunications": {
        "concepts": [
            "5G Network Slicer", "Spectrum Allocation Engine",
            "VoIP Quality Monitor", "Fiber Optic Diagnostic Suite",
            "Network Capacity Planner"
        ],
        "suffix": "for Telecommunications"
    },
    "embedded systems": {
        "concepts": [
            "RTOS Scheduler Toolkit", "Firmware Update Framework",
            "Low-Power Optimization Suite", "Hardware-in-Loop Simulator",
            "Bare-Metal Driver Generator"
        ],
        "suffix": "for Embedded Systems"
    },
    "artificial intelligence": {
        "concepts": [
            "Neural Network Trainer", "LLM Fine-Tuning Platform",
            "Computer Vision Pipeline", "Reinforcement Learning Sandbox",
            "Generative Model Studio", "AI Ethics Auditor",
            "Knowledge Graph Reasoner", "Multi-Agent Simulator",
            "Explainable AI Dashboard", "AutoML Orchestrator",
            "Prompt Engineering Studio", "Retrieval-Augmented Generator"
        ],
        "suffix": "for Enterprise AI"
    },
    "machine learning": {
        "concepts": [
            "Model Training Pipeline", "Feature Store Platform",
            "Hyperparameter Optimizer", "MLOps Deployment Suite",
            "Drift Detection Engine", "AutoML Benchmark Framework",
            "Ensemble Model Orchestrator", "Model Explainability Suite",
            "Active Learning Loop"
        ],
        "suffix": "for Production ML"
    },
    "deep learning": {
        "concepts": [
            "CNN Architecture Lab", "Transformer Trainer",
            "GAN Synthesis Studio", "Transfer Learning Toolkit",
            "Neural Architecture Search Engine"
        ],
        "suffix": "for Deep Learning"
    },
    "cyber security": {
        "concepts": [
            "Intrusion Detection System", "Threat Intelligence Hub",
            "Zero-Trust Access Gateway", "Vulnerability Scanner",
            "SIEM Correlation Engine", "Malware Analysis Sandbox",
            "Phishing Detection Framework", "Endpoint Protection Platform",
            "Security Posture Dashboard", "Incident Response Orchestrator",
            "Honeypot Network Manager", "Red Team Simulation Suite"
        ],
        "suffix": "for Enterprise Security"
    },
    "cybersecurity": {
        "concepts": [
            "Threat Hunting Platform", "Attack Surface Mapper",
            "SOC Automation Engine", "Ransomware Defense Suite",
            "Cloud Security Posture Manager"
        ],
        "suffix": "for Cybersecurity"
    },
    "data science": {
        "concepts": [
            "Exploratory Analytics Engine", "Statistical Modeling Suite",
            "Data Wrangling Pipeline", "Visualization Studio",
            "Predictive Modeling Platform", "Time-Series Forecaster",
            "Causal Inference Toolkit"
        ],
        "suffix": "for Data-Driven Decisions"
    },
    "data analytics": {
        "concepts": [
            "Business Intelligence Dashboard", "KPI Tracking Engine",
            "Real-Time Analytics Pipeline", "Customer Segmentation Studio"
        ],
        "suffix": "for Analytics"
    },
    "big data": {
        "concepts": [
            "Distributed Query Engine", "Stream Processing Framework",
            "Data Lake Manager", "Columnar Storage Optimizer"
        ],
        "suffix": "for Big Data"
    },
    "web development": {
        "concepts": [
            "Progressive Web App Platform", "Headless CMS Framework",
            "Realtime Collaboration Suite", "API Gateway",
            "Static Site Generator", "Web Performance Monitor",
            "Design System Library"
        ],
        "suffix": "for Modern Web"
    },
    "mobile development": {
        "concepts": [
            "Cross-Platform App Framework", "Offline-First Sync Engine",
            "Push Notification Orchestrator", "Mobile Analytics SDK",
            "In-App Purchase Platform"
        ],
        "suffix": "for Mobile Apps"
    },
    "game development": {
        "concepts": [
            "Physics Engine", "Procedural World Generator",
            "Multiplayer Netcode Framework", "Game AI Behavior Tree",
            "Asset Pipeline Toolkit"
        ],
        "suffix": "for Game Studios"
    },
    "software engineering": {
        "concepts": [
            "Code Review Automation", "Static Analysis Toolkit",
            "Dependency Vulnerability Scanner", "Refactoring Assistant",
            "Architecture Diagram Generator"
        ],
        "suffix": "for Software Teams"
    },
    "information technology": {
        "concepts": [
            "IT Service Management Suite", "Network Operations Center",
            "Help Desk Automation Engine", "Asset Management Platform",
            "Access Control Framework"
        ],
        "suffix": "for IT Operations"
    },
    "operating systems": {
        "concepts": [
            "Kernel Scheduler Simulator", "Memory Management Visualizer",
            "File System Analyzer", "Process Tracing Toolkit",
            "Hypervisor Benchmark Suite"
        ],
        "suffix": "for Operating Systems"
    },
    "database management": {
        "concepts": [
            "Query Optimizer Toolkit", "Index Recommendation Engine",
            "Distributed Transaction Manager", "Backup and Restore Orchestrator",
            "Schema Migration Framework"
        ],
        "suffix": "for Database Systems"
    },
    "computer science": {
        "concepts": [
            "Algorithm Visualizer", "Compiler Design Toolkit",
            "Distributed Systems Simulator", "Concurrency Debugger",
            "Data Structure Benchmark Suite"
        ],
        "suffix": "for Computer Science"
    },
    "networking": {
        "concepts": [
            "SDN Controller", "Network Traffic Analyzer",
            "Load Balancer Framework", "DNS Management Platform",
            "VPN Orchestrator", "Bandwidth Optimizer"
        ],
        "suffix": "for Network Operations"
    },
    "cloud computing": {
        "concepts": [
            "Multi-Cloud Orchestrator", "Serverless Framework",
            "Container Autoscaler", "Cost Optimization Engine",
            "Cloud Migration Planner", "Observability Platform",
            "Service Mesh Controller"
        ],
        "suffix": "for Cloud Infrastructure"
    },
    "edge computing": {
        "concepts": [
            "Edge Inference Runtime", "Federated Learning Orchestrator",
            "Edge Cache Manager", "Low-Latency Stream Processor"
        ],
        "suffix": "for Edge Computing"
    },
    "quantum computing": {
        "concepts": [
            "Quantum Circuit Simulator", "Qubit Error Corrector",
            "Quantum Algorithm Library", "Hybrid Classical-Quantum Solver",
            "Quantum Cryptography Suite"
        ],
        "suffix": "for Quantum Systems"
    },
    "computer vision": {
        "concepts": [
            "Object Detection Pipeline", "Facial Recognition Suite",
            "OCR Platform", "Pose Estimation Engine",
            "Video Analytics Dashboard", "Image Segmentation Framework",
            "3D Reconstruction Engine"
        ],
        "suffix": "for Visual Intelligence"
    },
    "natural language processing": {
        "concepts": [
            "Sentiment Analysis Engine", "Named Entity Recognizer",
            "Chatbot Framework", "Text Summarization Platform",
            "Machine Translation Suite", "Intent Classification Engine",
            "Question Answering System"
        ],
        "suffix": "for Language AI"
    },
    "devops": {
        "concepts": [
            "CI CD Pipeline Orchestrator", "Infrastructure-as-Code Engine",
            "Container Registry Platform", "Deployment Automation Suite",
            "Release Management Dashboard", "Chaos Engineering Toolkit"
        ],
        "suffix": "for DevOps"
    },
    "blockchain": {
        "concepts": [
            "Smart Contract Auditor", "DeFi Protocol Engine",
            "NFT Marketplace Platform", "Consensus Mechanism Simulator",
            "Wallet Security Suite", "Cross-Chain Bridge",
            "Zero-Knowledge Proof Toolkit"
        ],
        "suffix": "for Blockchain"
    },
    "internet of things": {
        "concepts": [
            "Device Management Platform", "Edge Analytics Engine",
            "Sensor Fusion Hub", "MQTT Broker Framework",
            "Predictive Maintenance System", "Smart Home Controller",
            "Industrial IoT Gateway"
        ],
        "suffix": "for IoT Systems"
    },
    "robotics": {
        "concepts": [
            "Autonomous Navigation Stack", "Robot Arm Controller",
            "SLAM Framework", "Swarm Coordination Engine",
            "Vision-Based Grasping System", "Path Planning Optimizer",
            "Human-Robot Interaction Suite"
        ],
        "suffix": "for Robotics"
    },
    "automation": {
        "concepts": [
            "Workflow Orchestration Engine", "RPA Bot Framework",
            "Process Mining Toolkit", "Task Scheduler Platform"
        ],
        "suffix": "for Automation"
    },
    "augmented reality": {
        "concepts": [
            "AR Navigation Framework", "Marker Tracking Engine",
            "AR Content Studio", "Spatial Mapping Toolkit"
        ],
        "suffix": "for AR Experiences"
    },
    "virtual reality": {
        "concepts": [
            "VR Training Simulator", "Immersive Meeting Platform",
            "Haptic Feedback Engine", "VR Content Pipeline"
        ],
        "suffix": "for VR"
    },
    "finance": {
        "concepts": [
            "Algorithmic Trading Engine", "Fraud Detection System",
            "Credit Risk Analyzer", "Portfolio Optimization Platform",
            "Real-Time Market Analytics", "Regulatory Compliance Tracker",
            "Loan Underwriting Engine", "Robo-Advisor Platform",
            "High-Frequency Trading Simulator"
        ],
        "suffix": "for Financial Services"
    },
    "fintech": {
        "concepts": [
            "Digital Payments Platform", "Open Banking Gateway",
            "KYC Automation Engine", "Lending Marketplace",
            "Wealth Management Advisor"
        ],
        "suffix": "for Fintech"
    },
    "e-commerce": {
        "concepts": [
            "Personalization Engine", "Inventory Optimization Platform",
            "Recommendation System", "Checkout Optimization Suite",
            "Customer Churn Predictor", "Dynamic Pricing Engine"
        ],
        "suffix": "for E-Commerce"
    },
    "marketing": {
        "concepts": [
            "Campaign Attribution Engine", "Customer Journey Mapper",
            "Content Recommendation Platform", "A B Testing Framework"
        ],
        "suffix": "for Marketing"
    },
    "human resources": {
        "concepts": [
            "Resume Ranking Engine", "Employee Attrition Predictor",
            "Onboarding Automation Platform", "Skills Taxonomy Mapper"
        ],
        "suffix": "for HR"
    },
    "supply chain": {
        "concepts": [
            "Demand Forecasting Engine", "Route Optimization Platform",
            "Warehouse Management System", "Supplier Risk Analyzer",
            "Shipment Tracking Dashboard"
        ],
        "suffix": "for Supply Chain"
    },
    "logistics": {
        "concepts": [
            "Fleet Management Platform", "Last-Mile Delivery Optimizer",
            "Real-Time Tracking System", "Route Planning Engine",
            "Warehouse Robotics Controller"
        ],
        "suffix": "for Logistics"
    },
    "healthcare": {
        "concepts": [
            "Patient Monitoring Platform", "Medical Imaging Analyzer",
            "Clinical Decision Support System", "Telemedicine Framework",
            "Drug Interaction Checker", "EHR Analytics Dashboard",
            "Diagnostic AI Assistant", "Remote Vital Tracking System",
            "Hospital Resource Optimizer"
        ],
        "suffix": "for Healthcare"
    },
    "medical imaging": {
        "concepts": [
            "MRI Segmentation Engine", "CT Scan Analyzer",
            "Radiology AI Assistant", "Pathology Image Classifier"
        ],
        "suffix": "for Medical Imaging"
    },
    "agriculture": {
        "concepts": [
            "Crop Yield Predictor", "Soil Health Monitor",
            "Precision Irrigation System", "Pest Detection Platform",
            "Farm Drone Analytics", "Weather Advisory Engine",
            "Smart Greenhouse Controller", "Livestock Tracker"
        ],
        "suffix": "for Smart Agriculture"
    },
    "agritech": {
        "concepts": [
            "Precision Farming Platform", "Crop Disease Detector",
            "IoT Soil Sensor Network", "Farm Management Dashboard",
            "Drone-Based Crop Analytics", "Vertical Farm Controller"
        ],
        "suffix": "for Agritech Innovation"
    },
    "renewable energy": {
        "concepts": [
            "Solar Output Forecaster", "Wind Turbine Monitor",
            "Grid Balancing Engine", "Battery Storage Optimizer",
            "Energy Trading Platform"
        ],
        "suffix": "for Clean Energy"
    },
    "solar energy": {
        "concepts": [
            "PV Performance Analyzer", "Solar Farm Monitor",
            "Inverter Optimization Suite", "Irradiance Forecasting Engine"
        ],
        "suffix": "for Solar Energy"
    },
    "sustainability": {
        "concepts": [
            "Carbon Footprint Tracker", "ESG Reporting Platform",
            "Circular Economy Optimizer", "Waste Reduction Engine"
        ],
        "suffix": "for Sustainability"
    },
    "environmental science": {
        "concepts": [
            "Air Quality Monitor", "Water Quality Analyzer",
            "Climate Data Explorer", "Biodiversity Tracker"
        ],
        "suffix": "for Environmental Science"
    },
    "biotechnology": {
        "concepts": [
            "Gene Sequence Analyzer", "Protein Folding Predictor",
            "Lab Automation Suite", "CRISPR Design Toolkit"
        ],
        "suffix": "for Biotechnology"
    },
    "bioinformatics": {
        "concepts": [
            "Genomic Variant Caller", "Phylogenetic Tree Builder",
            "Transcriptomics Pipeline", "Protein Interaction Mapper"
        ],
        "suffix": "for Bioinformatics"
    },
    "physics": {
        "concepts": [
            "Particle Simulation Engine", "Quantum Mechanics Visualizer",
            "Thermodynamics Modeler", "Optics Ray Tracer"
        ],
        "suffix": "for Physics Research"
    },
    "chemistry": {
        "concepts": [
            "Molecular Structure Visualizer", "Reaction Pathway Simulator",
            "Spectroscopy Analyzer", "Periodic Table Explorer"
        ],
        "suffix": "for Chemistry"
    },
    "biology": {
        "concepts": [
            "Cell Simulation Engine", "Ecosystem Modeler",
            "Genetic Sequence Analyzer", "Microscopy Image Classifier"
        ],
        "suffix": "for Biology"
    },
    "mathematics": {
        "concepts": [
            "Symbolic Solver Engine", "Theorem Prover Framework",
            "Graph Theory Visualizer", "Numerical Methods Toolkit"
        ],
        "suffix": "for Mathematics"
    },
    "statistics": {
        "concepts": [
            "Hypothesis Testing Suite", "Bayesian Inference Engine",
            "Monte Carlo Simulator", "Regression Analysis Toolkit"
        ],
        "suffix": "for Statistics"
    },
    "education": {
        "concepts": [
            "Adaptive Learning Platform", "Student Analytics Dashboard",
            "Virtual Classroom Suite", "Assessment Automation Engine",
            "Curriculum Recommendation System", "Plagiarism Detection Engine"
        ],
        "suffix": "for Education"
    },
    "edtech": {
        "concepts": [
            "Personalized Tutor Bot", "Gamified Learning Engine",
            "Skill Gap Analyzer", "Interactive Course Builder"
        ],
        "suffix": "for EdTech"
    },
    "psychology": {
        "concepts": [
            "Behavioral Pattern Analyzer", "Cognitive Assessment Suite",
            "Sentiment Tracker", "Therapy Session Assistant"
        ],
        "suffix": "for Psychology"
    },
    "law": {
        "concepts": [
            "Contract Analysis Engine", "Case Law Research Assistant",
            "Legal Document Summarizer", "Compliance Checker"
        ],
        "suffix": "for Legal Practice"
    },
    "legal tech": {
        "concepts": [
            "eDiscovery Platform", "IP Portfolio Manager",
            "Litigation Analytics Suite", "Regulatory Change Tracker"
        ],
        "suffix": "for Legal Tech"
    },
    "journalism": {
        "concepts": [
            "Fact-Check Automation", "News Aggregation Platform",
            "Source Verification Engine", "Investigative Data Toolkit"
        ],
        "suffix": "for Journalism"
    },
    "tourism": {
        "concepts": [
            "Itinerary Recommendation Engine", "Travel Demand Forecaster",
            "Destination Analytics Platform", "Virtual Tour Builder"
        ],
        "suffix": "for Tourism"
    },
    "hospitality": {
        "concepts": [
            "Guest Experience Platform", "Dynamic Room Pricing Engine",
            "Hotel Operations Dashboard", "Review Sentiment Analyzer"
        ],
        "suffix": "for Hospitality"
    },
    "sports technology": {
        "concepts": [
            "Athlete Performance Tracker", "Game Strategy Analyzer",
            "Injury Risk Predictor", "Fan Engagement Platform"
        ],
        "suffix": "for Sports Tech"
    },
}

# ============================================================
# KNOWN DOMAINS
# ============================================================
KNOWN_DOMAINS = [
    "artificial intelligence", "machine learning", "deep learning",
    "cyber security", "cybersecurity", "data science", "data analytics",
    "big data", "cloud computing", "edge computing", "quantum computing",
    "blockchain", "internet of things", "robotics", "automation",
    "computer vision", "natural language processing", "devops",
    "web development", "mobile development", "game development",
    "software engineering", "information technology",
    "database management", "networking", "embedded systems",
    "operating systems", "computer science",
    "augmented reality", "virtual reality", "mixed reality",
    "digital marketing", "ui ux design", "graphic design",
    "animation", "ethical hacking", "penetration testing",
    "digital forensics", "cloud security", "network security",
    "electronics", "electrical engineering", "communication engineering",
    "wireless communication", "mechanical engineering",
    "civil engineering", "chemical engineering", "aerospace engineering",
    "mechatronics", "vlsi design", "signal processing",
    "control systems", "instrumentation", "telecommunications",
    "finance", "fintech", "accounting", "banking", "insurance",
    "investment", "stock market", "cryptocurrency", "e-commerce",
    "marketing", "human resources", "supply chain", "logistics",
    "business analytics", "project management", "entrepreneurship",
    "healthcare", "medical imaging", "bioinformatics",
    "biotechnology", "genomics", "pharmacy", "nursing",
    "agriculture", "agritech", "food technology",
    "environmental science", "climate change", "renewable energy",
    "solar energy", "wind energy", "sustainability",
    "physics", "chemistry", "biology", "mathematics",
    "statistics", "geology", "oceanography",
    "education", "edtech", "e-learning", "psychology",
    "sociology", "law", "legal tech", "journalism",
    "media studies", "tourism", "hospitality", "sports technology"
]

# ============================================================
# TOKEN SETS
# ============================================================
AFFIRMATIVE = {"yes", "yeah", "yup", "s", "yea", "y", "yep", "sure",
               "ok", "okay", "correct", "right"}
NEGATIVE    = {"no", "nope", "nah", "n", "nay", "negative", "wrong", "incorrect"}
GREETINGS   = {"hi", "hello"}


# ============================================================
# LEVENSHTEIN CORE
# ============================================================
def levenshtein_distance(s1: str, s2: str) -> int:
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions    = previous_row[j + 1] + 1
            deletions     = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


def _proportional_threshold(s: str) -> int:
    n = len(s)
    if n <= 4:  return 1
    if n <= 7:  return 2
    if n <= 12: return 3
    return 4


def _best_match(user_input: str, candidates: list):
    cleaned = user_input.strip().lower()
    if not cleaned:
        return None, None
    best_match, best_distance = None, float("inf")
    for cand in candidates:
        d = levenshtein_distance(cleaned, cand)
        if d < best_distance:
            best_distance, best_match = d, cand
    return best_match, best_distance


def _word_matches_domain(user_words, domain_words):
    domain_words = list(domain_words)
    used = [False] * len(domain_words)
    for uw in user_words:
        best_idx, best_dist = -1, 99
        for i, dw in enumerate(domain_words):
            if used[i]:
                continue
            if len(uw) >= 3 and dw.startswith(uw):
                best_dist, best_idx = 0, i
                break
            d = levenshtein_distance(uw, dw)
            if d < best_dist:
                best_dist, best_idx = d, i
        if best_idx == -1 or best_dist > 2:
            return False
        used[best_idx] = True
    return True


def _word_level_score(user_words, domain_words):
    domain_words = list(domain_words)
    used = [False] * len(domain_words)
    total = 0
    for uw in user_words:
        best_idx, best_dist = -1, 99
        for i, dw in enumerate(domain_words):
            if used[i]:
                continue
            if len(uw) >= 3 and dw.startswith(uw):
                best_dist, best_idx = 0, i
                break
            d = levenshtein_distance(uw, dw)
            if d < best_dist:
                best_dist, best_idx = d, i
        if best_idx != -1:
            used[best_idx] = True
            total += best_dist
    return total


def find_closest_domain(user_input: str):
    cleaned = user_input.strip().lower()
    if not cleaned:
        return None, None

    if cleaned in DOMAIN_ALIASES:
        return DOMAIN_ALIASES[cleaned], 0

    m, d = _best_match(cleaned, list(DOMAIN_ALIASES.keys()))
    if m is not None and 0 < d <= 2:
        return DOMAIN_ALIASES[m], d

    words = cleaned.split()

    if len(words) == 1:
        first_word_map = {}
        for domain in KNOWN_DOMAINS:
            fw = domain.split()[0]
            if fw not in first_word_map or len(domain) > len(first_word_map[fw]):
                first_word_map[fw] = domain
        m, d = _best_match(cleaned, list(first_word_map.keys()))
        if m is not None and 0 < d <= _proportional_threshold(cleaned):
            return first_word_map[m], d
        m, d = _best_match(cleaned, KNOWN_DOMAINS)
        if m is not None and 0 < d <= _proportional_threshold(cleaned):
            return m, d
        return None, None

    candidates = []
    for domain in KNOWN_DOMAINS:
        if _word_matches_domain(words, domain.split()):
            score = _word_level_score(words, domain.split())
            candidates.append((score, domain))
    if candidates:
        candidates.sort(key=lambda x: x[0])
        score, domain = candidates[0]
        if score > 0:
            return domain, score

    m, d = _best_match(cleaned, KNOWN_DOMAINS)
    if m is not None:
        threshold = max(_proportional_threshold(cleaned), 3)
        if 0 < d <= threshold:
            return m, d
    return None, None


def is_exact_known_domain(user_input: str) -> bool:
    return user_input.strip().lower() in KNOWN_DOMAINS


def is_exact_alias(user_input: str):
    return DOMAIN_ALIASES.get(user_input.strip().lower())


def is_greeting(text: str) -> bool:
    return text.strip().lower() in GREETINGS


def is_affirmative(text: str) -> bool:
    return text.strip().lower() in AFFIRMATIVE


def is_negative(text: str) -> bool:
    return text.strip().lower() in NEGATIVE


def is_shuffle_command(text: str) -> bool:
    return text.strip().lower() in {"new", "different", "more"}


def pretty_domain(domain: str) -> str:
    return " ".join(w.capitalize() for w in domain.strip().split())


def _lookup_taxonomy(domain: str):
    d = domain.strip().lower()
    if d in DOMAIN_TAXONOMY:
        return DOMAIN_TAXONOMY[d]
    for key, val in DOMAIN_TAXONOMY.items():
        if key in d or d in key:
            return val
    d_words = set(d.split())
    best, best_overlap = None, 0
    for key, val in DOMAIN_TAXONOMY.items():
        overlap = len(d_words & set(key.split()))
        if overlap > best_overlap:
            best_overlap, best = overlap, val
    if best is not None and best_overlap > 0:
        return best
    return {"concepts": CORE_CONCEPTS, "suffix": f"for {domain}"}


def generate_unique_title(domain: str, registry: set) -> str:
    tax = _lookup_taxonomy(domain)
    suffix = tax["suffix"]
    concepts = tax["concepts"]
    for _ in range(500):
        title = f"{random.choice(PREFIXES)} {random.choice(concepts)} {suffix}"
        if title not in registry:
            return title
    return (
        f"{random.choice(PREFIXES)} {random.choice(concepts)} "
        f"{suffix} #{random.randint(1000, 9999)}"
    )


def generate_batch(domain: str, registry: set):
    difficulties = ["Beginner"] * 3 + ["Intermediate"] * 3 + ["Advanced"] * 3
    projects = []
    for diff in difficulties:
        title = generate_unique_title(domain, registry)
        registry.add(title)
        projects.append({"title": title, "difficulty": diff, "domain": domain})
    return projects


# ============================================================
# BUILD GUIDE — DOMAIN STACK MAPPING
# ============================================================
DOMAIN_STACK = {
    "electronics":               ("Arduino / STM32", "C / Embedded C", "KiCad, LTspice, Logic Analyzer"),
    "electrical engineering":    ("PLCs / SCADA",    "Ladder Logic / Python", "MATLAB/Simulink, ETAP"),
    "communication engineering": ("SDR / GNU Radio", "Python / C++", "MATLAB, Wireshark, VNA"),
    "wireless communication":    ("SDR / OpenAirInterface", "C / Python", "MATLAB, Wireshark, USRP"),
    "mechanical engineering":    ("CAD / FEA",       "Python / MATLAB", "SolidWorks, ANSYS, Fusion 360"),
    "civil engineering":         ("BIM / GIS",       "Python / C#", "Revit, AutoCAD, QGIS"),
    "chemical engineering":      ("Aspen HYSYS",     "Python / VBA", "Aspen Plus, MATLAB"),
    "aerospace engineering":     ("MATLAB / X-Plane","Python / C++", "ANSYS Fluent, OpenVSP"),
    "mechatronics":              ("ROS 2 / Arduino", "C++ / Python", "Gazebo, SolidWorks"),
    "control systems":           ("MATLAB / Simulink","Python / C",  "LabVIEW, PLCs"),
    "instrumentation":           ("LabVIEW / Arduino","Python / C",  "MATLAB, Oscilloscope"),
    "vlsi design":               ("Cadence / Verilog","Verilog / VHDL","Synopsys, ModelSim"),
    "signal processing":         ("MATLAB / SciPy",  "Python / C++", "GNU Radio, Audacity"),
    "telecommunications":        ("SDR / ns-3",      "Python / C++", "Wireshark, MATLAB"),
    "embedded systems":          ("STM32 / ESP32",   "C / Embedded C","PlatformIO, FreeRTOS"),
    "artificial intelligence":   ("PyTorch / HuggingFace", "Python", "Jupyter, Weights & Biases, Docker"),
    "machine learning":          ("scikit-learn / XGBoost", "Python", "MLflow, DVC, FastAPI"),
    "deep learning":             ("PyTorch / TensorFlow", "Python", "CUDA, Weights & Biases, ONNX"),
    "data science":              ("pandas / NumPy",  "Python / SQL", "Jupyter, Plotly, DuckDB"),
    "data analytics":            ("dbt / DuckDB",    "SQL / Python", "Metabase, Plotly, Airflow"),
    "big data":                  ("Spark / Kafka",   "Scala / Python","Hadoop, Airflow"),
    "cyber security":            ("Wireshark / Nmap","Python / Bash", "Kali Linux, ELK, Suricata"),
    "cybersecurity":             ("Burp / Metasploit","Python / Bash","Splunk, Zeek, Wazuh"),
    "cloud computing":           ("AWS / GCP",       "Python / Terraform", "Docker, K8s, Grafana"),
    "edge computing":            ("Edge TPU / Jetson","Python / C++", "TensorFlow Lite, ONNX"),
    "quantum computing":         ("Qiskit / Cirq",   "Python",       "IBM Quantum, PennyLane"),
    "computer vision":           ("OpenCV / YOLO",   "Python",       "PyTorch, LabelImg, ONNX"),
    "natural language processing": ("Hugging Face / spaCy", "Python", "Transformers, LangChain"),
    "web development":           ("React / Next.js", "TypeScript",   "Node.js, Vite, Vercel"),
    "mobile development":        ("Flutter / RN",    "Dart / TS",    "Firebase, Expo"),
    "game development":          ("Unity / Godot",   "C# / GDScript", "Blender, FMOD"),
    "software engineering":      ("Node / Python",   "TypeScript / Python", "GitHub Actions, Docker"),
    "information technology":    ("Linux / Ansible", "Bash / Python", "Zabbix, Grafana"),
    "operating systems":         ("Linux / QEMU",    "C / Assembly", "GDB, perf"),
    "database management":       ("PostgreSQL / Redis","SQL / Python", "pgAdmin, DBeaver"),
    "computer science":          ("C++ / Python",    "C++ / Python", "Git, GDB, Valgrind"),
    "networking":                ("Cisco / FRR",     "Python / C",   "Wireshark, GNS3"),
    "devops":                    ("Docker / K8s",    "Bash / YAML",  "Terraform, GitHub Actions"),
    "blockchain":                ("Solidity / Hardhat","JavaScript / TS","Ganache, Ethers.js, IPFS"),
    "internet of things":        ("ESP32 / MQTT",    "C / Python",   "Node-RED, InfluxDB, Grafana"),
    "robotics":                  ("ROS 2 / Gazebo",  "C++ / Python", "RViz, OpenCV, MoveIt"),
    "automation":                ("Ansible / n8n",   "Python / YAML","Selenium, Playwright"),
    "augmented reality":         ("Unity AR / ARKit","C# / Swift",   "Blender, ARCore"),
    "virtual reality":           ("Unity XR / Unreal","C# / C++",    "Blender, OpenXR"),
    "finance":                   ("pandas / QuantLib","Python / R",  "Bloomberg API, SQL"),
    "fintech":                   ("Node.js / Plaid", "TypeScript",   "Stripe, PostgreSQL, Redis"),
    "e-commerce":                ("Next.js + Stripe","TypeScript",   "Postgres, Redis, Algolia"),
    "marketing":                 ("n8n / HubSpot",   "Python / JS",  "GA4, Mixpanel"),
    "human resources":           ("Python / Airtable","Python",      "Power BI, Streamlit"),
    "supply chain":              ("ERP / Kafka",     "Python / SQL", "Neo4j, Mapbox, Redis"),
    "logistics":                 ("Routing engine",  "Python / Go",  "OSRM, PostGIS, Redis"),
    "healthcare":                ("FHIR / HL7",      "Python / Java","TensorFlow Med, DICOM"),
    "medical imaging":           ("MONAI / ITK",     "Python",       "PyTorch, 3D Slicer"),
    "agriculture":               ("IoT sensors / Drone", "Python",   "Soil APIs, Sentinel-2"),
    "agritech":                  ("IoT + ML",        "Python",       "Edge TPU, TensorFlow Lite"),
    "renewable energy":          ("SCADA / IoT",     "Python",       "PVLib, NREL APIs"),
    "solar energy":              ("PVLib / IoT",     "Python",       "NREL, MATLAB"),
    "sustainability":            ("ESG / GIS",       "Python",       "QGIS, Tableau"),
    "environmental science":     ("QGIS / R",        "Python / R",   "Remote sensing, InVEST"),
    "biotechnology":             ("Biopython / BLAST","Python / R",  "Galaxy, SnapGene"),
    "bioinformatics":            ("Biopython / Scanpy","Python / R", "Jupyter, Galaxy"),
    "physics":                   ("NumPy / SciPy",   "Python / C++", "Matplotlib, PyVista"),
    "chemistry":                 ("RDKit / PySCF",   "Python",       "Jupyter, Matplotlib"),
    "biology":                   ("Biopython / Scanpy","Python / R", "Jupyter, Galaxy"),
    "mathematics":               ("SymPy / SageMath","Python / Julia","Jupyter, Manim"),
    "statistics":                ("statsmodels / R", "Python / R",   "Jupyter, Stan"),
    "education":                 ("React / LMS",     "TypeScript",   "Firebase, OpenAI API"),
    "edtech":                    ("Next.js / OpenAI","TypeScript",   "Supabase, Stripe"),
    "psychology":                ("R / SPSS",        "R / Python",   "Qualtrics, R Shiny"),
    "law":                       ("LLM + RAG",       "Python",       "OpenAI, Pinecone"),
    "legal tech":                ("LLM + RAG",       "Python",       "LangChain, Weaviate"),
    "journalism":                ("NLP + scrapers",  "Python",       "spaCy, Newspaper3k"),
    "tourism":                   ("Maps + API",      "Python / JS",  "Google Maps, Amadeus"),
    "hospitality":               ("PMS + ML",        "Python",       "RevPAR models, Power BI"),
    "sports technology":         ("CV + wearables",  "Python",       "OpenCV, TensorFlow"),
}

DEFAULT_STACK = ("Python", "Python", "Jupyter, Git, Docker")


def _infer_project_type(title: str) -> str:
    t = title.lower()
    if "detection" in t or "monitoring" in t: return "detection"
    if "predict" in t or "forecast" in t:     return "prediction"
    if "recommend" in t:                      return "recommendation"
    if "classif" in t:                        return "classification"
    if "dashboard" in t or "insight" in t or "analytics" in t: return "dashboard"
    if "optimiz" in t:                        return "optimization"
    if "simulat" in t:                        return "simulation"
    if "assistant" in t or "chatbot" in t:    return "assistant"
    if "platform" in t or "framework" in t or "suite" in t: return "platform"
    if "engine" in t or "pipeline" in t:      return "pipeline"
    if "tracker" in t or "monitor" in t:      return "tracking"
    if "generator" in t or "studio" in t:     return "generator"
    return "pipeline"


def build_blueprint(project: dict) -> str:
    """Return a concrete, step-by-step build guide for the project."""
    title  = project["title"]
    diff   = project["difficulty"]
    domain = project["domain"]
    key    = domain.strip().lower()

    stack = DOMAIN_STACK.get(key, DEFAULT_STACK)
    tool, lang, env = stack
    kind = _infer_project_type(title)

    # ---------- Phase 1 — Setup & Data ----------
    phase1 = [
        ("Set up the workspace.",
         f"Install **{lang}**, **{tool}**, and these tools: **{env}**. "
         f"Create a Git repo `{domain.lower().replace(' ', '-')}-{kind}` "
         f"with folders `data/`, `src/`, `notebooks/`, `tests/`."),
        ("Collect the dataset.",
         f"Gather {domain} data relevant to *{title}*. "
         f"Aim for 500+ records (or 30 min of signal). Save raw copies untouched in `data/raw/`."),
        ("Clean the data.",
         f"Handle missing values, duplicates, and outliers. "
         f"Normalize units / encodings. Write the cleaning script to `src/clean.py`."),
        ("Explore the data.",
         f"Open a Jupyter notebook. Plot distributions, correlations, and any time patterns. "
         f"Write down 3 insights — this becomes the 'Motivation' slide of your portfolio."),
        ("Split into train / validation / test.",
         f"80 / 10 / 10 for most cases; time-based split if the data is sequential. "
         f"Freeze the test set — never touch it until the very end."),
    ]

    # ---------- Phase 2 — varies by kind ----------
    if kind == "detection":
        phase2 = [
            ("Build a baseline detector.",
             "Start with the simplest thing that works — a threshold, a regex, or Logistic Regression. Log its precision and recall."),
            ("Train the primary model.",
             f"Move to a stronger model (Random Forest, CNN, or XGBoost) using **{tool}**. Tune hyperparameters on the validation set."),
            ("Add a false-positive filter.",
             "Suppression windows, allowlists, and cooldown timers. Aim for precision ≥ 0.85 in production."),
            ("Add explainability.",
             "For each alert, log which feature / region triggered it. Use SHAP or LIME for tabular data, Grad-CAM for images."),
            ("Evaluate on the test set.",
             "Report precision, recall, F1, and ROC-AUC. Compare against the baseline."),
        ]
    elif kind == "prediction":
        phase2 = [
            ("Fit a naive baseline.",
             "Predict the mean, or the last observed value. Record its RMSE — this is your bar to beat."),
            ("Engineer features.",
             "Rolling averages, lags, calendar features, external signals. Save as `features.parquet`."),
            ("Train the primary model.",
             f"Linear / ARIMA first, then XGBoost or LSTM via **{tool}**. Use time-series cross-validation with rolling origin."),
            ("Report metrics.",
             "RMSE, MAE, and MAPE on the validation set. Plot predictions vs actuals."),
            ("Save the model artifact.",
             "Pickle or ONNX with a version tag. Write a `load_model()` helper."),
        ]
    elif kind == "recommendation":
        phase2 = [
            ("Build a popularity baseline.",
             "Recommend the top-N items to everyone. Record recall@10 — this is your bar."),
            ("Train a collaborative filter.",
             f"Implicit ALS or matrix factorization in **{tool}**."),
            ("Add content-based signals.",
             "Item descriptions, tags, or embeddings — blend into a hybrid."),
            ("Re-rank with business rules.",
             "Filter out-of-stock, boost fresh content, deduplicate."),
            ("Offline evaluation.",
             "Recall@K, NDCG@K, coverage, and diversity. Compare to baseline."),
        ]
    elif kind == "classification":
        phase2 = [
            ("Fit the baseline.",
             "Logistic Regression or Naive Bayes. Record accuracy and per-class F1."),
            ("Handle imbalance.",
             "Class weights, SMOTE, or focal loss — whichever fits."),
            ("Train the primary classifier.",
             f"Tree ensemble or fine-tuned transformer via **{tool}**."),
            ("Evaluate.",
             "Confusion matrix, per-class precision/recall, AUC. Report the worst-performing class."),
            ("Calibrate probabilities.",
             "Platt scaling or isotonic regression if the score is used as a probability."),
        ]
    elif kind == "dashboard":
        phase2 = [
            ("Define KPIs.",
             "Pick 5–8 metrics that matter. Write them in a `metrics.md`."),
            ("Build the aggregation layer.",
             "Pre-compute rollups so the dashboard doesn't query raw data on every load."),
            ("Wire the data connectors.",
             "Pull from the source DB / API / CSV. Schedule a refresh (cron or Airflow)."),
            ("Build the KPI tiles.",
             "One card per KPI with a sparkline. Click → detail view."),
            ("Add drill-downs and filters.",
             "Date range, segment, region. Save user's last selection."),
        ]
    elif kind == "optimization":
        phase2 = [
            ("Write the objective function.",
             "Encode cost / profit / risk precisely. This is the heart of the project."),
            ("Encode constraints.",
             "Budget, capacity, regulatory, physical limits."),
            ("Pick a solver.",
             f"Linear / MILP / genetic — via **{tool}**."),
            ("Run sensitivity analysis.",
             "Vary constraints ±20% and observe how the optimum moves."),
            ("Benchmark against the current process.",
             "Report % improvement — this number goes on your resume."),
        ]
    elif kind == "simulation":
        phase2 = [
            ("Define the entities and states.",
             "What exists in the system, what states can each be in?"),
            ("Model the transitions.",
             "Event-driven or fixed-tick. Write the state machine."),
            ("Seed the RNG.",
             "Reproducibility matters — set a global seed."),
            ("Instrument the sim.",
             "Snapshot state every N ticks to disk (parquet or CSV)."),
            ("Validate against reality.",
             "Compare to known real-world outcomes. Report % error."),
        ]
    elif kind == "assistant":
        phase2 = [
            ("Chunk the corpus.",
             "300–500 token chunks with 50-token overlap. Store in JSONL."),
            ("Embed and index.",
             "Use a sentence-transformer or OpenAI embeddings. Store in a vector DB."),
            ("Build the retriever.",
             "Top-k (k=5) retrieval + optional BM25 hybrid."),
            ("Wire the LLM.",
             "System prompt + retrieved context + user question. Response must cite sources."),
            ("Evaluate.",
             "Curate 30–50 Q/A pairs. Score faithfulness and relevance (LLM-as-judge works)."),
        ]
    elif kind == "platform":
        phase2 = [
            ("Split into 3–5 services.",
             "Keep cohesion high, coupling low. Draw the architecture diagram."),
            ("Define the API contract.",
             "OpenAPI or GraphQL schema first, implementation second."),
            ("Pick the data store.",
             "Primary DB + cache + blob. Justify each choice."),
            ("Build background jobs.",
             "Celery / RQ / SQS workers for slow tasks."),
            ("Write tests per service.",
             "Unit + integration. Aim for 70%+ coverage on critical paths."),
        ]
    elif kind == "tracking":
        phase2 = [
            ("Model the state machine.",
             "Each tracked entity has a lifecycle. Enumerate the states."),
            ("Write the update logic.",
             "Merge incoming events with current state — be idempotent."),
            ("Add alerts.",
             "Trigger on state change, geofence breach, or timeout."),
            ("Store history.",
             "Append-only log so past states are queryable."),
            ("Scale.",
             "Partition by entity ID for horizontal scaling."),
        ]
    elif kind == "generator":
        phase2 = [
            ("Write the template / prompt.",
             "3–5 starter patterns. Iterate fast."),
            ("Add sampling controls.",
             "Temperature, top-k, top-p for variety vs safety."),
            ("Filter output.",
             "Regex or classifier to reject malformed generations."),
            ("Cache frequent inputs.",
             "In-memory or Redis. Cuts cost 10x."),
            ("Collect feedback.",
             "Thumbs up/down per generation. Store for future fine-tuning."),
        ]
    else:  # pipeline
        phase2 = [
            ("Choose the orchestrator.",
             "Airflow, Prefect, or cron — whichever fits your scale."),
            ("Build the transform stages.",
             "Extract → enrich → aggregate. One function per stage."),
            ("Make it idempotent.",
             "Hash-based deduplication before writes."),
            ("Route failures.",
             "Dead-letter queue + replay script."),
            ("Add stage metrics.",
             "Rows in/out, latency, error rate per stage."),
        ]

    # ---------- Phase 3 ----------
    phase3 = [
        ("Build the UI.",
         "Streamlit for speed; React if you need polish. One screen: input on top, results below."),
        ("Add visualizations.",
         "Plotly or Chart.js. At minimum: one time-series, one distribution, one alert feed."),
        ("Wire notifications.",
         "Email / Slack / webhook on threshold breach. One channel is enough for a portfolio."),
        ("Add structured logging.",
         "JSON logs with request IDs. Ship to ELK or Grafana Loki."),
        ("Add monitoring.",
         "Uptime, latency, error rate on a public status page (UptimeRobot is free)."),
        ("Add auth.",
         "Role-based: admin / analyst / viewer. Even a simple session cookie works."),
        ("Add export.",
         "CSV and PDF downloads — stakeholders love this."),
        ("Containerize and deploy.",
         "Dockerfile + `docker-compose.yml`. Deploy to Render / Railway / AWS EC2."),
        ("Write the README.",
         "Setup steps, architecture diagram, screenshots, live URL. This is your portfolio entry."),
    ]

    def fmt(steps, phase_no):
        out = []
        for i, (title_s, detail) in enumerate(steps, start=1):
            out.append(f"**Step {phase_no}.{i} — {title_s}**\n\n{detail}\n")
        return "\n".join(out)

    return f"""
## 🧭 Build Guide — {title}
**Difficulty:** `{diff}` · **Domain:** `{domain}` · **Type:** `{kind}`

**Stack you'll use** — `{tool}` · `{lang}` · `{env}`

Follow the steps in order. Each step ends with something you can show.

---

### 🔹 Phase 1 — Setup & Data Preparation

{fmt(phase1, 1)}
---

### 🔹 Phase 2 — Core Engine

{fmt(phase2, 2)}
---

### 🔹 Phase 3 — Interface, Deployment & Portfolio

{fmt(phase3, 3)}
---

*Done with this blueprint? Choose **Continue** to explore other projects, or **Shift** to try a new domain.*
"""