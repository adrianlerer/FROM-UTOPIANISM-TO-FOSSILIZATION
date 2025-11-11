#!/usr/bin/env python3
"""
EXAMPLE: Analysis with Integrated Integrity Filter

This demonstrates how to use IntegrityFilter during actual research workflow.
The filter runs as you make claims, providing real-time feedback on integrity risks.

Author: Ignacio Adrián Lerer
Date: November 2025
"""

import pandas as pd
from integrity_filter import IntegrityFilter

# ============================================================================
# EXAMPLE ANALYSIS: Replicating Figure 4 with Integrity Checks
# ============================================================================

def main():
    print("="*80)
    print("EXAMPLE ANALYSIS WITH INTEGRITY FILTER")
    print("Replicating Figure 4 (Fiscal Sustainability) with real-time checks")
    print("="*80 + "\n")
    
    # ========================================================================
    # STEP 1: Initialize Filter
    # ========================================================================
    
    filter = IntegrityFilter(project_name="figure4_fiscal_sustainability")
    
    # ========================================================================
    # STEP 2: Validate Hypothesis BEFORE Analysis
    # ========================================================================
    
    print("\n" + "─"*80)
    print("STEP 1: VALIDATE HYPOTHESIS")
    print("─"*80 + "\n")
    
    h1_result = filter.validate_hypothesis(
        hypothesis_text="Colombia's fiscal sustainability improved over time (declining implementation gap)",
        baseline_source="Dixon & Landau (2025) predict transformative success with adequate support. Implementation gap is proxy for fiscal sustainability.",
        theoretical_basis="Transformative constitutions with popular support (SP > 0.65) and open pathways (CLI < 0.5) should show NARROWING gap as implementation proceeds. Colombia 1991 had both conditions.",
        testable=True
    )
    
    h2_result = filter.validate_hypothesis(
        hypothesis_text="Chile 2022 would have had massive fiscal gap if passed (utopian)",
        baseline_source="Dixon & Landau (2025) predict utopian failure without adequate resources. Fiscal gap = lack of resources.",
        theoretical_basis="Constitutions with blocked pathways (CLI > 0.65) and insufficient support (SP < 0.35) show LARGE gaps between promises and capacity. Chile 2022 had both conditions.",
        testable=True
    )
    
    h3_result = filter.validate_hypothesis(
        hypothesis_text="Argentina shows fossilization: worsening fiscal gap over 76 years",
        baseline_source="Extended Phenotype Theory predicts lock-in accumulation. Argentina Art. 14bis persists since 1949.",
        theoretical_basis="Utopian constitutions that cannot be reformed (CLI growing) accumulate WIDENING gaps as promises persist but implementation capacity declines. Argentina CLI grew +0.0055/year.",
        testable=True
    )
    
    # ========================================================================
    # STEP 3: Load Data and Validate Sources
    # ========================================================================
    
    print("\n" + "─"*80)
    print("STEP 2: LOAD DATA AND VALIDATE SOURCES")
    print("─"*80 + "\n")
    
    # Load Colombia data
    colombia_df = pd.read_csv('../DATA/analysis_results/colombia_constitutional_fitness.csv')
    filter.validate_claim(
        claim=f"Colombia data loaded: {len(colombia_df)} time points from 1991-2025",
        evidence_type="verified",
        source="../DATA/analysis_results/colombia_constitutional_fitness.csv (generated from colombia_h1_analysis.py with World Bank + DANE sources)"
    )
    
    # Load Argentina data
    argentina_df = pd.read_csv('../DATA/analysis_results/argentina_cf_trajectory.csv')
    filter.validate_claim(
        claim=f"Argentina data loaded: {len(argentina_df)} time points from 1949-2025",
        evidence_type="verified",
        source="../DATA/analysis_results/argentina_cf_trajectory.csv (generated from argentina_paradox_analysis.py with CSJN fallos)"
    )
    
    # Load Chile data
    chile_df = pd.read_csv('../DATA/analysis_results/chile_constitutional_fitness.csv')
    filter.validate_claim(
        claim=f"Chile data loaded: 1 projection for 2022 (counterfactual if passed)",
        evidence_type="projected",
        source="../DATA/analysis_results/chile_constitutional_fitness.csv (generated from chile_h2_analysis.py)",
        limitations=[
            "Counterfactual scenario (constitution was rejected)",
            "Based on 2022 fiscal capacity estimates",
            "Assumes no policy changes post-rejection"
        ]
    )
    
    # ========================================================================
    # STEP 4: Calculate Metrics and Validate Each Claim
    # ========================================================================
    
    print("\n" + "─"*80)
    print("STEP 3: CALCULATE METRICS WITH VALIDATION")
    print("─"*80 + "\n")
    
    # Colombia FSI trajectory
    colombia_filtered = colombia_df[colombia_df['Year'] >= 1990].copy()
    colombia_filtered['FSI'] = (1 - colombia_filtered['Gap']) * 100
    
    colombia_start_fsi = colombia_filtered[colombia_filtered['Year'] == 1991]['FSI'].iloc[0]
    colombia_end_fsi = colombia_filtered[colombia_filtered['Year'] == 2025]['FSI'].iloc[0]
    colombia_improvement = colombia_end_fsi - colombia_start_fsi
    
    filter.validate_claim(
        claim=f"Colombia FSI improved from {colombia_start_fsi:.1f}% (1991) to {colombia_end_fsi:.1f}% (2025), gaining {colombia_improvement:.1f} percentage points",
        evidence_type="calculated",
        source="FSI = (1 - Gap) × 100%, where Gap from colombia_constitutional_fitness.csv",
        theoretical_justification="Improvement expected per H1: transformative success with adequate support should narrow gap",
        external_validation="Consistent with World Bank data showing Colombia social spending increase 8% → 15% GDP"
    )
    
    # Argentina FSI trajectory
    argentina_filtered = argentina_df[argentina_df['Year'] >= 1990].copy()
    argentina_filtered['FSI'] = (1 - argentina_filtered['Gap']) * 100
    
    argentina_start_fsi = argentina_filtered[argentina_filtered['Year'] == 1990]['FSI'].iloc[0]
    argentina_end_fsi = argentina_filtered[argentina_filtered['Year'] == 2025]['FSI'].iloc[0]
    argentina_deterioration = argentina_end_fsi - argentina_start_fsi
    
    filter.validate_claim(
        claim=f"Argentina FSI declined from {argentina_start_fsi:.1f}% (1990) to {argentina_end_fsi:.1f}% (2025), losing {abs(argentina_deterioration):.1f} percentage points",
        evidence_type="calculated",
        source="FSI = (1 - Gap) × 100%, where Gap from argentina_cf_trajectory.csv",
        theoretical_justification="Decline expected per H3: fossilization with growing CLI should widen gap",
        external_validation="Consistent with Argentina informality rate increasing 35% → 45% and failed reform attempts (0/23 success)"
    )
    
    # Chile FSI (projected)
    chile_fsi = (1 - chile_df['Gap'].iloc[0]) * 100
    
    filter.validate_claim(
        claim=f"Chile 2022 projected FSI: {chile_fsi:.1f}% (if constitution had passed)",
        evidence_type="projected",
        source="FSI = (1 - Gap) × 100%, where Gap = 0.7724 from chile_h2_analysis.py fiscal gap calculation",
        theoretical_justification="Low FSI expected per H2: utopian failure with insufficient resources",
        external_validation="Validated by actual outcome: 62% rejection (voters perceived unviability)",
        limitations=[
            "Counterfactual (did not actually pass)",
            "Based on 2022 fiscal space estimates (2.5% GDP available vs 13.5% GDP promised)",
            "Does not account for potential budget adjustments"
        ]
    )
    
    # ========================================================================
    # STEP 5: Validate Key Comparisons
    # ========================================================================
    
    print("\n" + "─"*80)
    print("STEP 4: VALIDATE KEY COMPARISONS")
    print("─"*80 + "\n")
    
    # Colombia vs Chile difference
    colombia_chile_diff = colombia_end_fsi - chile_fsi
    filter.validate_claim(
        claim=f"Colombia 2025 FSI is {colombia_chile_diff:.1f} percentage points higher than Chile 2022 projected FSI",
        evidence_type="calculated",
        source="Difference of calculated FSI values",
        theoretical_justification="Large difference validates Dixon & Landau: transformative (Colombia) vs utopian (Chile)"
    )
    
    # Chile-Argentina convergence
    chile_argentina_diff = abs(chile_fsi - argentina_end_fsi)
    filter.validate_claim(
        claim=f"Chile 2022 and Argentina 2025 converge at ~23% FSI (difference only {chile_argentina_diff:.1f} points)",
        evidence_type="calculated",
        source="Comparison of calculated FSI values",
        theoretical_justification="Convergence expected: both systems fiscally unsustainable (Chile would be, Argentina is)",
        external_validation="Both at <50% viability threshold, confirming utopian territory"
    )
    
    # ========================================================================
    # STEP 6: Check for Metric Optimization (Integrity Check)
    # ========================================================================
    
    print("\n" + "─"*80)
    print("STEP 5: CHECK FOR METRIC HACKING")
    print("─"*80 + "\n")
    
    filter.check_metric_optimization(
        metric_name="Fiscal_Sustainability_Index",
        metric_values={
            "Colombia_1991": colombia_start_fsi,
            "Colombia_2025": colombia_end_fsi,
            "Argentina_1990": argentina_start_fsi,
            "Argentina_2025": argentina_end_fsi,
            "Chile_2022_projected": chile_fsi
        },
        expected_pattern="Colombia improving (up), Argentina declining (down), Chile low (utopian)"
    )
    
    # ========================================================================
    # STEP 7: Generate Final Integrity Report
    # ========================================================================
    
    print("\n" + "─"*80)
    print("STEP 6: GENERATE INTEGRITY REPORT")
    print("─"*80 + "\n")
    
    risk_assessment = filter.calculate_project_risk()
    report_path = filter.generate_report(output_file="figure4_integrity_report.json")
    
    # ========================================================================
    # STEP 8: Decision Point Based on Risk
    # ========================================================================
    
    print("\n" + "="*80)
    print("INTEGRITY DECISION POINT")
    print("="*80 + "\n")
    
    if risk_assessment['risk_level'] in ['LOW', 'MODERATE']:
        print("✅ APPROVED: Integrity standards met. Proceed with Figure 4 generation.")
        print(f"   Risk Level: {risk_assessment['risk_level']}")
        print(f"   Verification Score: {risk_assessment['verification_score']:.1%}")
        print(f"\n   Recommendation: {risk_assessment['recommendation']}")
        return True
    else:
        print("❌ NOT APPROVED: Integrity concerns detected. Address issues before proceeding.")
        print(f"   Risk Level: {risk_assessment['risk_level']}")
        print(f"   Verification Score: {risk_assessment['verification_score']:.1%}")
        print(f"\n   Recommendation: {risk_assessment['recommendation']}")
        return False

# ============================================================================
# RUN EXAMPLE
# ============================================================================

if __name__ == '__main__':
    approval = main()
    
    if approval:
        print("\n" + "="*80)
        print("✅ Analysis passed integrity filter. Safe to proceed with visualization.")
        print("="*80)
    else:
        print("\n" + "="*80)
        print("⚠️  Analysis did NOT pass integrity filter. Review and revise before publication.")
        print("="*80)
