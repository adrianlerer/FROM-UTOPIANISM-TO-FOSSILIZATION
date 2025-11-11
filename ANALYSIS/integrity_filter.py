#!/usr/bin/env python3
"""
INTEGRITY FILTER - Operational Risk Assessment for AI-Assisted Research
Based on Miyai et al. (2025) Jr. AI Scientist Risk Framework

This filter runs DURING analysis to prevent common AI-research pitfalls:
1. Ideas working by chance (no theoretical justification)
2. Citation fabrication or irrelevance
3. Experiments claimed but not performed
4. Metric hacking (optimizing for appearance vs substance)
5. Overconfidence in projections/estimates

Usage:
    from integrity_filter import IntegrityFilter
    
    filter = IntegrityFilter()
    
    # Before running analysis
    filter.validate_hypothesis("Colombia succeeded due to adequate support")
    
    # Before claiming results
    filter.validate_claim(
        claim="Chile CF = 0.004",
        evidence_type="calculated",
        source="chile_h2_analysis.py line 142",
        verification_level="estimation"
    )
    
    # Generate compliance report
    filter.generate_report()

Author: Ignacio Adrián Lerer
Date: November 2025
Reference: Miyai et al. (2025) "Jr. AI Scientist and Its Risk Report"
"""

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Literal
from dataclasses import dataclass, asdict
import hashlib

# ============================================================================
# CONFIGURATION
# ============================================================================

VERIFICATION_LEVELS = {
    "verified": {
        "weight": 1.0,
        "description": "Official data, published sources, direct measurement",
        "examples": ["SERVEL election results", "World Bank statistics", "CSJN fallos"]
    },
    "calculated": {
        "weight": 0.85,
        "description": "Derived from verified inputs with explicit formula",
        "examples": ["CF = [PE × (1-Gap) × (1-CD) × SP] / CLI", "FSI = (1-Gap) × 100%"]
    },
    "estimated": {
        "weight": 0.65,
        "description": "Proxy measures, interpolation, expert judgment",
        "examples": ["Elite support from polling aggregates", "Pre-1990 Argentina CLI"]
    },
    "inferred": {
        "weight": 0.45,
        "description": "Logical derivation with stated assumptions",
        "examples": ["Cultural distance from survey responses", "Institutional fit scoring"]
    },
    "projected": {
        "weight": 0.25,
        "description": "Counterfactual scenarios, forecasts, simulations",
        "examples": ["Chile 'if passed' scenario", "Argentina 2030 CLI projection"]
    }
}

RISK_THRESHOLDS = {
    "critical": 0.30,  # <30% verified = CRITICAL RISK
    "high": 0.50,      # 30-50% verified = HIGH RISK
    "moderate": 0.70,  # 50-70% verified = MODERATE RISK
    "low": 0.85        # >85% verified = LOW RISK
}

# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class Claim:
    """Individual research claim with provenance tracking"""
    claim_id: str
    claim_text: str
    evidence_type: Literal["verified", "calculated", "estimated", "inferred", "projected"]
    source: str
    timestamp: str
    verification_score: float
    theoretical_justification: Optional[str] = None
    external_validation: Optional[str] = None
    limitations: List[str] = None
    
    def __post_init__(self):
        if self.limitations is None:
            self.limitations = []
        # Generate hash ID if not provided
        if not self.claim_id:
            claim_hash = hashlib.md5(self.claim_text.encode()).hexdigest()[:8]
            self.claim_id = f"claim_{claim_hash}"
        # Set verification score based on evidence type
        self.verification_score = VERIFICATION_LEVELS[self.evidence_type]["weight"]

@dataclass
class Hypothesis:
    """Research hypothesis with risk assessment"""
    hypothesis_id: str
    hypothesis_text: str
    baseline_source: str
    theoretical_basis: str
    testable: bool
    timestamp: str
    risk_flags: List[str] = None
    
    def __post_init__(self):
        if self.risk_flags is None:
            self.risk_flags = []

# ============================================================================
# INTEGRITY FILTER CLASS
# ============================================================================

class IntegrityFilter:
    """
    Operational filter for AI-assisted research integrity.
    Runs during analysis to prevent Jr. AI Scientist risks.
    """
    
    def __init__(self, project_name: str = "analysis", output_dir: str = "../OUTPUTS"):
        self.project_name = project_name
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Storage
        self.hypotheses: List[Hypothesis] = []
        self.claims: List[Claim] = []
        self.risk_log: List[Dict] = []
        
        # Tracking
        self.start_time = datetime.now()
        
        print(f"🛡️  Integrity Filter initialized for project: {project_name}")
        print(f"📊 Verification thresholds: {RISK_THRESHOLDS}")
    
    # ========================================================================
    # HYPOTHESIS VALIDATION (Pre-Analysis)
    # ========================================================================
    
    def validate_hypothesis(
        self,
        hypothesis_text: str,
        baseline_source: str,
        theoretical_basis: str,
        testable: bool = True
    ) -> Dict:
        """
        Validate hypothesis BEFORE running analysis.
        Prevents "ideas working by chance" risk.
        
        Args:
            hypothesis_text: Clear statement of hypothesis
            baseline_source: Citation to baseline paper/theory
            theoretical_basis: Why this hypothesis is justified
            testable: Whether hypothesis is empirically testable
        
        Returns:
            Dict with validation result and risk flags
        """
        hypothesis_id = f"H{len(self.hypotheses) + 1}"
        risk_flags = []
        
        # Risk Check 1: Theoretical justification present?
        if not theoretical_basis or len(theoretical_basis) < 20:
            risk_flags.append("WEAK_THEORY: Insufficient theoretical justification")
        
        # Risk Check 2: Baseline source cited?
        if not baseline_source or not self._is_valid_citation(baseline_source):
            risk_flags.append("NO_BASELINE: Missing or invalid baseline citation")
        
        # Risk Check 3: Testable claim?
        if not testable:
            risk_flags.append("NOT_TESTABLE: Hypothesis cannot be empirically tested")
        
        # Risk Check 4: Circular reasoning?
        if self._contains_circular_reasoning(hypothesis_text, theoretical_basis):
            risk_flags.append("CIRCULAR: Hypothesis assumes its own conclusion")
        
        # Store hypothesis
        hypothesis = Hypothesis(
            hypothesis_id=hypothesis_id,
            hypothesis_text=hypothesis_text,
            baseline_source=baseline_source,
            theoretical_basis=theoretical_basis,
            testable=testable,
            timestamp=datetime.now().isoformat(),
            risk_flags=risk_flags
        )
        self.hypotheses.append(hypothesis)
        
        # Log result
        if risk_flags:
            self._log_risk(f"Hypothesis {hypothesis_id} validation", "WARNING", risk_flags)
            print(f"⚠️  Hypothesis {hypothesis_id}: {len(risk_flags)} risk flag(s)")
            for flag in risk_flags:
                print(f"    - {flag}")
        else:
            print(f"✅ Hypothesis {hypothesis_id} validated (no risks)")
        
        return {
            "hypothesis_id": hypothesis_id,
            "valid": len(risk_flags) == 0,
            "risk_flags": risk_flags,
            "recommendation": "PROCEED" if len(risk_flags) == 0 else "REVISE_THEORY"
        }
    
    # ========================================================================
    # CLAIM VALIDATION (During/Post-Analysis)
    # ========================================================================
    
    def validate_claim(
        self,
        claim: str,
        evidence_type: Literal["verified", "calculated", "estimated", "inferred", "projected"],
        source: str,
        theoretical_justification: Optional[str] = None,
        external_validation: Optional[str] = None,
        limitations: Optional[List[str]] = None
    ) -> Dict:
        """
        Validate research claim with provenance tracking.
        Prevents "experiments not performed" and "citation fabrication" risks.
        
        Args:
            claim: Specific claim being made (e.g., "Chile CF = 0.004")
            evidence_type: Level of verification (verified/calculated/estimated/inferred/projected)
            source: Where evidence comes from (file, line, citation)
            theoretical_justification: Why this result makes theoretical sense
            external_validation: Independent validation if available
            limitations: Known limitations of this claim
        
        Returns:
            Dict with validation result, score, and warnings
        """
        claim_obj = Claim(
            claim_id="",  # Auto-generated in __post_init__
            claim_text=claim,
            evidence_type=evidence_type,
            source=source,
            timestamp=datetime.now().isoformat(),
            verification_score=0.0,  # Set in __post_init__
            theoretical_justification=theoretical_justification,
            external_validation=external_validation,
            limitations=limitations or []
        )
        
        warnings = []
        
        # Warning 1: Low verification level for strong claim
        if evidence_type in ["projected", "inferred"] and self._is_strong_claim(claim):
            warnings.append("WEAK_EVIDENCE: Strong claim based on weak evidence")
        
        # Warning 2: No source provided
        if not source or source == "":
            warnings.append("NO_SOURCE: Missing data source or code reference")
        
        # Warning 3: Projection without limitations
        if evidence_type == "projected" and not limitations:
            warnings.append("NO_LIMITS: Projection lacks stated limitations")
        
        # Warning 4: Calculated without formula
        if evidence_type == "calculated" and not self._contains_formula(source):
            warnings.append("NO_FORMULA: Calculated claim without explicit formula")
        
        # Store claim
        self.claims.append(claim_obj)
        
        # Log warnings
        if warnings:
            self._log_risk(f"Claim validation: {claim[:50]}...", "WARNING", warnings)
            print(f"⚠️  Claim [{evidence_type}]: {len(warnings)} warning(s)")
            for warning in warnings:
                print(f"    - {warning}")
        else:
            print(f"✅ Claim [{evidence_type}] validated: {claim[:60]}...")
        
        return {
            "claim_id": claim_obj.claim_id,
            "verification_score": claim_obj.verification_score,
            "warnings": warnings,
            "recommendation": "USE_WITH_CAUTION" if warnings else "APPROVED"
        }
    
    # ========================================================================
    # METRIC HACKING DETECTION
    # ========================================================================
    
    def check_metric_optimization(
        self,
        metric_name: str,
        metric_values: Dict[str, float],
        expected_pattern: Optional[str] = None
    ) -> Dict:
        """
        Detect if metric appears to be "hacked" or optimized artificially.
        Prevents "optimizing for appearance vs substance" risk.
        
        Args:
            metric_name: Name of metric (e.g., "CF", "FSI", "CLI")
            metric_values: Dict mapping cases to metric values
            expected_pattern: Optional description of theoretically expected pattern
        
        Returns:
            Dict with suspicion flags
        """
        flags = []
        
        # Flag 1: All values conveniently support narrative
        values = list(metric_values.values())
        if len(values) >= 3:
            # Check if variance is suspiciously low (all similar)
            variance = sum((x - sum(values)/len(values))**2 for x in values) / len(values)
            if variance < 0.01:
                flags.append("LOW_VARIANCE: Suspiciously uniform metric values")
        
        # Flag 2: Perfect separation (all "good" cases high, all "bad" cases low)
        if self._perfect_separation(metric_values):
            flags.append("PERFECT_SEP: Metric perfectly separates cases (too good?)")
        
        # Flag 3: Round numbers (suggests fabrication)
        if self._too_many_round_numbers(values):
            flags.append("ROUND_NUMBERS: Suspiciously many round metric values")
        
        # Log result
        if flags:
            self._log_risk(f"Metric optimization check: {metric_name}", "CAUTION", flags)
            print(f"🔍 Metric '{metric_name}': {len(flags)} suspicion flag(s)")
            for flag in flags:
                print(f"    - {flag}")
        else:
            print(f"✅ Metric '{metric_name}' appears natural")
        
        return {
            "metric_name": metric_name,
            "suspicious": len(flags) > 0,
            "flags": flags,
            "recommendation": "REVIEW_CAREFULLY" if flags else "APPROVED"
        }
    
    # ========================================================================
    # AGGREGATED RISK ASSESSMENT
    # ========================================================================
    
    def calculate_project_risk(self) -> Dict:
        """
        Calculate overall project integrity risk score.
        
        Returns:
            Dict with risk level, score breakdown, and recommendations
        """
        if not self.claims:
            return {
                "risk_level": "UNKNOWN",
                "message": "No claims validated yet"
            }
        
        # Calculate weighted verification score
        total_weight = sum(c.verification_score for c in self.claims)
        avg_verification = total_weight / len(self.claims)
        
        # Count by evidence type
        evidence_breakdown = {
            "verified": sum(1 for c in self.claims if c.evidence_type == "verified"),
            "calculated": sum(1 for c in self.claims if c.evidence_type == "calculated"),
            "estimated": sum(1 for c in self.claims if c.evidence_type == "estimated"),
            "inferred": sum(1 for c in self.claims if c.evidence_type == "inferred"),
            "projected": sum(1 for c in self.claims if c.evidence_type == "projected")
        }
        
        # Determine risk level
        if avg_verification >= RISK_THRESHOLDS["low"]:
            risk_level = "LOW"
            color = "🟢"
        elif avg_verification >= RISK_THRESHOLDS["moderate"]:
            risk_level = "MODERATE"
            color = "🟡"
        elif avg_verification >= RISK_THRESHOLDS["high"]:
            risk_level = "HIGH"
            color = "🟠"
        else:
            risk_level = "CRITICAL"
            color = "🔴"
        
        # Count total risk flags
        hypothesis_flags = sum(len(h.risk_flags) for h in self.hypotheses)
        risk_log_entries = len(self.risk_log)
        
        print(f"\n{'='*70}")
        print(f"INTEGRITY RISK ASSESSMENT - {self.project_name.upper()}")
        print(f"{'='*70}")
        print(f"{color} Risk Level: {risk_level}")
        print(f"📊 Average Verification Score: {avg_verification:.2%}")
        print(f"📝 Total Claims: {len(self.claims)}")
        print(f"   - Verified: {evidence_breakdown['verified']}")
        print(f"   - Calculated: {evidence_breakdown['calculated']}")
        print(f"   - Estimated: {evidence_breakdown['estimated']}")
        print(f"   - Inferred: {evidence_breakdown['inferred']}")
        print(f"   - Projected: {evidence_breakdown['projected']}")
        print(f"⚠️  Risk Flags: {hypothesis_flags + risk_log_entries}")
        print(f"{'='*70}\n")
        
        return {
            "risk_level": risk_level,
            "verification_score": avg_verification,
            "total_claims": len(self.claims),
            "evidence_breakdown": evidence_breakdown,
            "risk_flags_count": hypothesis_flags + risk_log_entries,
            "recommendation": self._get_recommendation(risk_level, avg_verification)
        }
    
    # ========================================================================
    # REPORT GENERATION
    # ========================================================================
    
    def generate_report(self, output_file: Optional[str] = None) -> str:
        """
        Generate comprehensive integrity report.
        
        Args:
            output_file: Optional filename (default: integrity_report_TIMESTAMP.json)
        
        Returns:
            Path to generated report
        """
        if not output_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"integrity_report_{timestamp}.json"
        
        output_path = self.output_dir / output_file
        
        report = {
            "metadata": {
                "project_name": self.project_name,
                "generated_at": datetime.now().isoformat(),
                "duration": str(datetime.now() - self.start_time),
                "framework": "Miyai et al. (2025) Jr. AI Scientist Risk Assessment"
            },
            "risk_assessment": self.calculate_project_risk(),
            "hypotheses": [asdict(h) for h in self.hypotheses],
            "claims": [asdict(c) for c in self.claims],
            "risk_log": self.risk_log,
            "recommendations": self._generate_recommendations()
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"📄 Integrity report saved: {output_path}")
        
        # Also generate human-readable markdown
        md_path = output_path.with_suffix('.md')
        self._generate_markdown_report(report, md_path)
        print(f"📄 Markdown report saved: {md_path}")
        
        return str(output_path)
    
    # ========================================================================
    # HELPER METHODS
    # ========================================================================
    
    def _is_valid_citation(self, citation: str) -> bool:
        """Check if citation looks valid (author + year pattern)"""
        # Simple heuristic: contains year (19xx or 20xx) and text
        return bool(re.search(r'(19|20)\d{2}', citation)) and len(citation) > 10
    
    def _contains_circular_reasoning(self, hypothesis: str, justification: str) -> bool:
        """Detect if hypothesis assumes its conclusion"""
        # Extract key terms from hypothesis
        hypothesis_terms = set(re.findall(r'\b\w{5,}\b', hypothesis.lower()))
        justification_terms = set(re.findall(r'\b\w{5,}\b', justification.lower()))
        
        # If >80% overlap, likely circular
        if hypothesis_terms and justification_terms:
            overlap = len(hypothesis_terms & justification_terms) / len(hypothesis_terms)
            return overlap > 0.8
        return False
    
    def _is_strong_claim(self, claim: str) -> bool:
        """Check if claim uses strong language (definitive, certain, proves, etc.)"""
        strong_words = [
            'proves', 'demonstrates', 'confirms', 'definitively',
            'certainly', 'undoubtedly', 'clearly shows', 'establishes'
        ]
        return any(word in claim.lower() for word in strong_words)
    
    def _contains_formula(self, source: str) -> bool:
        """Check if source reference mentions formula or calculation"""
        formula_indicators = ['=', 'calculate', 'formula', 'equation', 'def ', 'return']
        return any(indicator in source.lower() for indicator in formula_indicators)
    
    def _perfect_separation(self, metric_values: Dict) -> bool:
        """Check if metric perfectly separates cases (suspiciously convenient)"""
        # TODO: Implement based on case labels (success/failure)
        # For now, just check if std dev is very high relative to mean
        values = list(metric_values.values())
        if len(values) < 3:
            return False
        mean = sum(values) / len(values)
        std = (sum((x - mean)**2 for x in values) / len(values)) ** 0.5
        return std / (mean + 0.01) > 2.0  # Coefficient of variation > 2
    
    def _too_many_round_numbers(self, values: List[float]) -> bool:
        """Check if suspiciously many values are round numbers"""
        round_count = sum(1 for v in values if v == round(v, 1))
        return round_count > len(values) * 0.7  # >70% round
    
    def _log_risk(self, context: str, level: str, messages: List[str]):
        """Log risk event"""
        self.risk_log.append({
            "timestamp": datetime.now().isoformat(),
            "context": context,
            "level": level,
            "messages": messages
        })
    
    def _get_recommendation(self, risk_level: str, verification_score: float) -> str:
        """Get recommendation based on risk assessment"""
        if risk_level == "LOW":
            return "APPROVED for publication. High integrity standards met."
        elif risk_level == "MODERATE":
            return "REVISION SUGGESTED. Add more verified data sources or acknowledge limitations."
        elif risk_level == "HIGH":
            return "MAJOR REVISION REQUIRED. Strengthen empirical foundation before publication."
        else:
            return "NOT READY. Critical integrity issues must be resolved."
    
    def _generate_recommendations(self) -> List[str]:
        """Generate specific recommendations based on analysis"""
        recommendations = []
        
        # Check verification score breakdown
        verified_pct = sum(1 for c in self.claims if c.evidence_type == "verified") / max(len(self.claims), 1)
        projected_pct = sum(1 for c in self.claims if c.evidence_type == "projected") / max(len(self.claims), 1)
        
        if verified_pct < 0.30:
            recommendations.append("Increase proportion of verified claims (currently <30%)")
        
        if projected_pct > 0.20:
            recommendations.append("Reduce reliance on projections/counterfactuals (currently >20%)")
        
        # Check for missing external validation
        no_validation = [c for c in self.claims if not c.external_validation and c.evidence_type != "verified"]
        if len(no_validation) > len(self.claims) * 0.5:
            recommendations.append("Add external validation for key claims (>50% lack validation)")
        
        # Check hypothesis quality
        weak_hypotheses = [h for h in self.hypotheses if len(h.risk_flags) > 0]
        if weak_hypotheses:
            recommendations.append(f"Strengthen theoretical justification for {len(weak_hypotheses)} hypothesis/es")
        
        if not recommendations:
            recommendations.append("No major improvements needed. Maintain current standards.")
        
        return recommendations
    
    def _generate_markdown_report(self, report: Dict, output_path: Path):
        """Generate human-readable markdown report"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"# Integrity Assessment Report\n\n")
            f.write(f"**Project**: {report['metadata']['project_name']}\n")
            f.write(f"**Generated**: {report['metadata']['generated_at']}\n")
            f.write(f"**Framework**: {report['metadata']['framework']}\n\n")
            
            # Risk assessment
            risk = report['risk_assessment']
            f.write(f"## 🎯 Risk Level: {risk['risk_level']}\n\n")
            f.write(f"- **Verification Score**: {risk['verification_score']:.1%}\n")
            f.write(f"- **Total Claims**: {risk['total_claims']}\n")
            f.write(f"- **Risk Flags**: {risk['risk_flags_count']}\n\n")
            
            # Evidence breakdown
            f.write(f"### Evidence Breakdown\n\n")
            for evidence_type, count in risk['evidence_breakdown'].items():
                pct = count / risk['total_claims'] * 100 if risk['total_claims'] > 0 else 0
                f.write(f"- **{evidence_type.capitalize()}**: {count} ({pct:.1f}%)\n")
            
            # Recommendations
            f.write(f"\n## 📋 Recommendations\n\n")
            for rec in report['recommendations']:
                f.write(f"- {rec}\n")
            
            # Hypotheses
            if report['hypotheses']:
                f.write(f"\n## 🔬 Hypotheses ({len(report['hypotheses'])})\n\n")
                for h in report['hypotheses']:
                    f.write(f"### {h['hypothesis_id']}: {h['hypothesis_text'][:100]}...\n\n")
                    f.write(f"- **Baseline**: {h['baseline_source']}\n")
                    f.write(f"- **Theoretical Basis**: {h['theoretical_basis'][:200]}...\n")
                    if h['risk_flags']:
                        f.write(f"- **⚠️ Risk Flags**: {', '.join(h['risk_flags'])}\n")
                    f.write(f"\n")
            
            # Claims summary (top 10)
            if report['claims']:
                f.write(f"\n## 📊 Sample Claims (showing {min(10, len(report['claims']))}/{len(report['claims'])})\n\n")
                for c in report['claims'][:10]:
                    f.write(f"**[{c['evidence_type'].upper()}]** {c['claim_text'][:80]}...\n")
                    f.write(f"- Score: {c['verification_score']:.2f}\n")
                    f.write(f"- Source: {c['source'][:100]}\n\n")

# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

def quick_check(claims_data: List[Dict]) -> Dict:
    """
    Quick integrity check for ad-hoc analysis.
    
    Args:
        claims_data: List of dicts with keys: claim, evidence_type, source
    
    Returns:
        Risk assessment dict
    """
    filter = IntegrityFilter(project_name="quick_check")
    
    for claim_dict in claims_data:
        filter.validate_claim(
            claim=claim_dict['claim'],
            evidence_type=claim_dict['evidence_type'],
            source=claim_dict.get('source', 'Not specified')
        )
    
    return filter.calculate_project_risk()

# ============================================================================
# MAIN (for testing)
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("INTEGRITY FILTER - Test Suite")
    print("="*70 + "\n")
    
    # Initialize filter
    filter = IntegrityFilter(project_name="dixon_landau_ept_test")
    
    # Test hypothesis validation
    print("\n### TEST 1: Hypothesis Validation ###\n")
    filter.validate_hypothesis(
        hypothesis_text="Colombia 1991 succeeded due to adequate popular support and institutional pathways",
        baseline_source="Dixon & Landau (2025) 'Utopian Constitutionalism'",
        theoretical_basis="Dixon & Landau framework predicts transformative success when both support and pathways are adequate. Colombia had 70% popular support (above threshold) and CLI = 0.135 (open pathways).",
        testable=True
    )
    
    # Test claim validation - verified
    print("\n### TEST 2: Claim Validation (Verified) ###\n")
    filter.validate_claim(
        claim="Chile 2022 plebiscite resulted in 62% rejection (38.14% approval)",
        evidence_type="verified",
        source="SERVEL official election results, September 4, 2022",
        external_validation="Multiple news sources, international observers"
    )
    
    # Test claim validation - calculated
    print("\n### TEST 3: Claim Validation (Calculated) ###\n")
    filter.validate_claim(
        claim="Chile Constitutional Fitness CF = 0.0037",
        evidence_type="calculated",
        source="chile_h2_analysis.py line 142: CF = [PE × (1-Gap) × (1-CD) × SP] / (CLI + ε)",
        theoretical_justification="Low CF expected given high CLI (0.81), high Gap (0.77), and low SP (0.304)"
    )
    
    # Test claim validation - projected (with warning)
    print("\n### TEST 4: Claim Validation (Projected - should warn) ###\n")
    filter.validate_claim(
        claim="If Chile constitution had passed, implementation rate would be ~12%",
        evidence_type="projected",
        source="Counterfactual projection based on fiscal gap analysis",
        limitations=["Assumes no budget increases", "Does not account for political shifts", "Based on 2022 fiscal capacity"]
    )
    
    # Test metric optimization check
    print("\n### TEST 5: Metric Hacking Detection ###\n")
    filter.check_metric_optimization(
        metric_name="Constitutional_Fitness",
        metric_values={
            "Colombia": 0.913,
            "Chile": 0.004,
            "Argentina": 0.011
        }
    )
    
    # Generate final report
    print("\n### TEST 6: Generate Report ###\n")
    risk_assessment = filter.calculate_project_risk()
    report_path = filter.generate_report()
    
    print(f"\n✅ Test suite complete. Report saved to: {report_path}")
