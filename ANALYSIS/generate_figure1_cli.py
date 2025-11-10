#!/usr/bin/env python3
"""
Figure 1: Constitutional Lock-in Index (CLI) Comparison
Compares CLI values across Colombia (1991), Chile (2022), and Argentina (2025)

Author: Ignacio Adrián Lerer
Date: November 2025
License: CC-BY 4.0
"""

import matplotlib.pyplot as plt
import numpy as np

def generate_cli_comparison():
    """
    Generate bar chart comparing CLI values across three cases.
    
    Data Sources:
    - Colombia: Comparative Constitutions Project + author calculations [Verificado]
    - Chile: Inherited from 1980 constitution, author analysis [Estimación]
    - Argentina: Author calculations based on CSJN precedent [Estimación]
    """
    
    # CLI values [Verificado/Estimación per source documentation]
    countries = ['Colombia\n1991', 'Chile\n2022', 'Argentina\n2025']
    cli_values = [0.135, 0.810, 0.870]
    colors = ['#2ecc71', '#e74c3c', '#95a5a6']  # Green, Red, Gray
    
    # Threshold lines
    cli_open_threshold = 0.50  # Below this = open pathways
    cli_blocked_threshold = 0.65  # Above this = blocked pathways
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Bar chart
    bars = ax.bar(countries, cli_values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    # Threshold lines
    ax.axhline(y=cli_open_threshold, color='green', linestyle='--', linewidth=2, 
               label='Open Pathways Threshold (< 0.50)', alpha=0.7)
    ax.axhline(y=cli_blocked_threshold, color='red', linestyle='--', linewidth=2, 
               label='Blocked Pathways Threshold (> 0.65)', alpha=0.7)
    
    # Value labels on bars
    for bar, value in zip(bars, cli_values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                f'{value:.3f}',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    # Outcome labels
    outcomes = ['✓ Transformative', '✗ Utopian Failure', '🪦 Fossilized']
    for bar, outcome in zip(bars, outcomes):
        ax.text(bar.get_x() + bar.get_width()/2., 0.05,
                outcome,
                ha='center', va='bottom', fontsize=10, style='italic')
    
    # Formatting
    ax.set_ylabel('Constitutional Lock-in Index (CLI)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Case Study', fontsize=12, fontweight='bold')
    ax.set_title('Figure 1: Constitutional Lock-in Index Comparison\n' + 
                 'Colombia (Transformative) vs Chile (Utopian) vs Argentina (Fossilized)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_ylim(0, 1.0)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(axis='y', alpha=0.3, linestyle=':')
    
    # Add interpretation box
    textstr = 'Interpretation:\n' \
              '• CLI < 0.50: Pathways open for transformation\n' \
              '• CLI > 0.65: Pathways blocked (structural utopianism)\n' \
              '• Colombia: Low CLI enabled successful transformation\n' \
              '• Chile: High CLI blocked implementation (inherited 1980)\n' \
              '• Argentina: Highest CLI, fossilized utopianism (76 years)'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.3)
    ax.text(0.98, 0.97, textstr, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', horizontalalignment='right', bbox=props)
    
    plt.tight_layout()
    
    # Save figure
    output_path = '../OUTPUTS/figure1_cli_comparison.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Figure 1 saved to: {output_path}")
    print(f"   CLI values: Colombia={cli_values[0]:.3f}, Chile={cli_values[1]:.3f}, Argentina={cli_values[2]:.3f}")
    
    # Also save as PDF for publication
    pdf_path = '../OUTPUTS/figure1_cli_comparison.pdf'
    plt.savefig(pdf_path, format='pdf', bbox_inches='tight')
    print(f"✅ PDF version saved to: {pdf_path}")
    
    plt.close()

if __name__ == "__main__":
    print("Generating Figure 1: CLI Comparison...")
    generate_cli_comparison()
    print("Done!")
