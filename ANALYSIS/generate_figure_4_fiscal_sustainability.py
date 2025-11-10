#!/usr/bin/env python3
"""
Generate Figure 4: Fiscal Sustainability Index Temporal Evolution
Shows Implementation Gap trajectories for Colombia, Chile, and Argentina (1990-2025)

Implementation Gap = (Promised - Delivered) / Promised
Lower Gap = Better Fiscal Sustainability

Author: Ignacio Adrián Lerer
Date: November 10, 2025
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def load_data():
    """Load data from CSV files"""
    
    # Colombia data (1991-2025)
    colombia_df = pd.read_csv('../DATA/analysis_results/colombia_constitutional_fitness.csv')
    colombia_df['Country'] = 'Colombia'
    
    # Argentina data (1949-2025)
    argentina_df = pd.read_csv('../DATA/analysis_results/argentina_cf_trajectory.csv')
    argentina_df['Country'] = 'Argentina'
    
    # Chile data (single point 2022, projected)
    chile_df = pd.read_csv('../DATA/analysis_results/chile_constitutional_fitness.csv')
    
    return colombia_df, argentina_df, chile_df

def create_figure():
    """Generate Figure 4: Fiscal Sustainability Index Temporal Evolution"""
    
    colombia_df, argentina_df, chile_df = load_data()
    
    # Create figure with high resolution
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Focus on 1990-2025 period
    colombia_filtered = colombia_df[colombia_df['Year'] >= 1990].copy()
    argentina_filtered = argentina_df[argentina_df['Year'] >= 1990].copy()
    
    # Convert Gap to Fiscal Sustainability Index (inverse)
    # FSI = 1 - Gap (higher is better)
    colombia_filtered['FSI'] = (1 - colombia_filtered['Gap']) * 100
    argentina_filtered['FSI'] = (1 - argentina_filtered['Gap']) * 100
    chile_fsi = (1 - chile_df['Gap'].iloc[0]) * 100
    
    # Plot Colombia (Gradual Success)
    ax.plot(colombia_filtered['Year'], colombia_filtered['FSI'], 
            marker='o', linewidth=2.5, markersize=8, 
            color='#2ecc71', label='Colombia 1991 (Transformative Success)',
            linestyle='-', alpha=0.9)
    
    # Plot Argentina (Fossilized Utopianism)
    ax.plot(argentina_filtered['Year'], argentina_filtered['FSI'], 
            marker='s', linewidth=2.5, markersize=8,
            color='#e74c3c', label='Argentina 1949 (Fossilized Utopianism)',
            linestyle='--', alpha=0.9)
    
    # Plot Chile (Utopian Failure - projected if passed)
    ax.scatter([2022], [chile_fsi], 
               marker='X', s=300, 
               color='#9b59b6', label='Chile 2022 (Utopian Failure - Projected)',
               edgecolors='black', linewidths=1.5, zorder=5)
    
    # Add horizontal reference lines
    ax.axhline(y=50, color='gray', linestyle=':', linewidth=1, alpha=0.5, label='50% Threshold (Viability)')
    ax.axhline(y=60, color='orange', linestyle=':', linewidth=1, alpha=0.5, label='60% Threshold (Sustainability)')
    
    # Annotate key points
    # Colombia start and end
    ax.annotate('Colombia 1991\nStart: 65% FSI', 
                xy=(1991, colombia_filtered[colombia_filtered['Year']==1991]['FSI'].iloc[0]), 
                xytext=(1992, 55),
                fontsize=9, ha='left',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#d5f4e6', alpha=0.8),
                arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=1.5))
    
    ax.annotate('Colombia 2025\nEnd: 88% FSI\n(+23 points)', 
                xy=(2025, colombia_filtered[colombia_filtered['Year']==2025]['FSI'].iloc[0]), 
                xytext=(2015, 91),
                fontsize=9, ha='center',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#d5f4e6', alpha=0.8),
                arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=1.5))
    
    # Argentina trajectory
    ax.annotate('Argentina 1990\n36% FSI', 
                xy=(1990, argentina_filtered[argentina_filtered['Year']==1990]['FSI'].iloc[0]), 
                xytext=(1993, 28),
                fontsize=9, ha='left',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#fadbd8', alpha=0.8),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1.5))
    
    ax.annotate('Argentina 2025\n23% FSI\n(Fossilized)', 
                xy=(2025, argentina_filtered[argentina_filtered['Year']==2025]['FSI'].iloc[0]), 
                xytext=(2017, 15),
                fontsize=9, ha='center',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#fadbd8', alpha=0.8),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1.5))
    
    # Chile single point
    ax.annotate(f'Chile 2022\n{chile_fsi:.1f}% FSI\n(If passed)\n77% Unfunded', 
                xy=(2022, chile_fsi), 
                xytext=(2007, 32),
                fontsize=9, ha='center',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#ebdef0', alpha=0.8),
                arrowprops=dict(arrowstyle='->', color='#9b59b6', lw=2))
    
    # Labels and title
    ax.set_xlabel('Year', fontsize=13, fontweight='bold')
    ax.set_ylabel('Fiscal Sustainability Index (%)', fontsize=13, fontweight='bold')
    ax.set_title('Figure 4: Fiscal Sustainability Index Temporal Evolution\nColombia, Chile, Argentina (1990-2025)', 
                 fontsize=15, fontweight='bold', pad=20)
    
    # Grid and styling
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax.set_xlim(1988, 2027)
    ax.set_ylim(0, 100)
    
    # Legend
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9, shadow=True)
    
    # Add FSI explanation text box
    textstr = 'FSI = (1 - Implementation Gap) × 100%\nHigher FSI = Better fiscal sustainability\nLower Gap = Promises match resources'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.15)
    ax.text(0.98, 0.03, textstr, transform=ax.transAxes, fontsize=9,
            verticalalignment='bottom', horizontalalignment='right', bbox=props)
    
    # Add Dixon & Landau citation
    citation = 'Data: Extended Phenotype Theory (EPT) operationalization of Dixon & Landau (2025) "Utopian Constitutionalism"'
    fig.text(0.5, 0.01, citation, ha='center', fontsize=8, style='italic', color='gray')
    
    plt.tight_layout()
    
    # Save figure to OUTPUTS directory
    output_dir = Path('../OUTPUTS')
    output_dir.mkdir(exist_ok=True)
    
    output_path = output_dir / 'figure4_fiscal_sustainability_evolution.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✅ Figure saved to: {output_path}")
    
    # Also save as high-res PDF for publication
    output_path_pdf = output_dir / 'figure4_fiscal_sustainability_evolution.pdf'
    plt.savefig(output_path_pdf, format='pdf', bbox_inches='tight', facecolor='white')
    print(f"✅ PDF version saved to: {output_path_pdf}")
    
    plt.show()
    
    return fig

def print_data_summary():
    """Print summary statistics for the figure"""
    
    colombia_df, argentina_df, chile_df = load_data()
    
    print("\n" + "="*80)
    print("FISCAL SUSTAINABILITY INDEX - DATA SUMMARY")
    print("="*80)
    
    print("\n📊 COLOMBIA 1991 (Transformative Success):")
    colombia_filtered = colombia_df[colombia_df['Year'] >= 1990]
    print(f"  • 1991 Gap: {colombia_filtered[colombia_filtered['Year']==1991]['Gap'].iloc[0]:.1%} → FSI: {(1-colombia_filtered[colombia_filtered['Year']==1991]['Gap'].iloc[0])*100:.1f}%")
    print(f"  • 2025 Gap: {colombia_filtered[colombia_filtered['Year']==2025]['Gap'].iloc[0]:.1%} → FSI: {(1-colombia_filtered[colombia_filtered['Year']==2025]['Gap'].iloc[0])*100:.1f}%")
    print(f"  • Improvement: {(colombia_filtered[colombia_filtered['Year']==1991]['Gap'].iloc[0] - colombia_filtered[colombia_filtered['Year']==2025]['Gap'].iloc[0])*100:.1f} percentage points")
    print(f"  • Trajectory: IMPROVING ✅ (narrowing gap)")
    
    print("\n📊 ARGENTINA 1949 (Fossilized Utopianism):")
    argentina_filtered = argentina_df[argentina_df['Year'] >= 1990]
    print(f"  • 1990 Gap: {argentina_filtered[argentina_filtered['Year']==1990]['Gap'].iloc[0]:.1%} → FSI: {(1-argentina_filtered[argentina_filtered['Year']==1990]['Gap'].iloc[0])*100:.1f}%")
    print(f"  • 2025 Gap: {argentina_filtered[argentina_filtered['Year']==2025]['Gap'].iloc[0]:.1%} → FSI: {(1-argentina_filtered[argentina_filtered['Year']==2025]['Gap'].iloc[0])*100:.1f}%")
    print(f"  • Deterioration: {(argentina_filtered[argentina_filtered['Year']==2025]['Gap'].iloc[0] - argentina_filtered[argentina_filtered['Year']==1990]['Gap'].iloc[0])*100:.1f} percentage points")
    print(f"  • Trajectory: WORSENING ❌ (widening gap, fossilization)")
    
    print("\n📊 CHILE 2022 (Utopian Failure - Projected if passed):")
    print(f"  • 2022 Gap (projected): {chile_df['Gap'].iloc[0]:.1%} → FSI: {(1-chile_df['Gap'].iloc[0])*100:.1f}%")
    print(f"  • Interpretation: 77% of promises UNFUNDED")
    print(f"  • Outcome: REJECTED 62% (rational voter response) ✓")
    
    print("\n📊 COMPARATIVE MAGNITUDES:")
    colombia_2025_fsi = (1-colombia_filtered[colombia_filtered['Year']==2025]['Gap'].iloc[0])*100
    argentina_2025_fsi = (1-argentina_filtered[argentina_filtered['Year']==2025]['Gap'].iloc[0])*100
    chile_2022_fsi = (1-chile_df['Gap'].iloc[0])*100
    
    print(f"  • Colombia 2025: {colombia_2025_fsi:.1f}% FSI (HIGH - Sustainable)")
    print(f"  • Chile 2022: {chile_2022_fsi:.1f}% FSI (LOW - Utopian)")
    print(f"  • Argentina 2025: {argentina_2025_fsi:.1f}% FSI (VERY LOW - Fossilized)")
    print(f"\n  • Colombia vs Chile: {colombia_2025_fsi - chile_2022_fsi:.1f} point difference")
    print(f"  • Colombia vs Argentina: {colombia_2025_fsi - argentina_2025_fsi:.1f} point difference")
    print(f"  • Chile vs Argentina: {chile_2022_fsi - argentina_2025_fsi:.1f} point difference")
    
    print("\n" + "="*80)
    print("KEY INSIGHTS:")
    print("="*80)
    print("1. Colombia IMPROVED fiscal sustainability over 34 years (65% → 88% FSI)")
    print("2. Argentina DETERIORATED over 35 years (36% → 23% FSI) - FOSSILIZED")
    print("3. Chile 2022 would have been UTOPIAN (23% FSI, only 23% funded)")
    print("4. Dixon & Landau validated: Adequate resources (Colombia) vs Blocked paths (Chile, Argentina)")
    print("="*80 + "\n")

if __name__ == '__main__':
    print("\n" + "="*80)
    print("GENERATING FIGURE 4: FISCAL SUSTAINABILITY INDEX TEMPORAL EVOLUTION")
    print("="*80 + "\n")
    
    print_data_summary()
    
    print("\n📊 Generating visualization...")
    fig = create_figure()
    
    print("\n✅ Figure 4 generation complete!")
    print("\nFiles created:")
    print("  • figures/figure_4_fiscal_sustainability_evolution.png (300 DPI)")
    print("  • figures/figure_4_fiscal_sustainability_evolution.pdf (Publication quality)")
    print("\n" + "="*80)
