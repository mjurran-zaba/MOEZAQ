#!/usr/bin/env python3
"""
Landing Page Performance & Health Auditor
Based on Landing Page Guru Skill & Google Android Mobile Web Vitals standards.
"""

import os
import re
import sys

def audit_landing_page(file_path):
    print("==================================================")
    print("  LANDING PAGE AUDIT & PERFORMANCE HEALTH CHECK  ")
    print("==================================================")
    
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return False
        
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
        
    results = {
        "P0_Critical": [],
        "P1_High": [],
        "P2_Optimization": [],
        "Passed": []
    }
    
    # 1. Viewport & Android Safe Area Check
    if 'name="viewport"' in html:
        viewport_match = re.search(r'<meta\s+name=["\']viewport["\']\s+content=["\']([^"\']+)["\']', html)
        if viewport_match:
            vp = viewport_match.group(1)
            if "width=device-width" in vp and "initial-scale=1.0" in vp:
                results["Passed"].append("Viewport: Proper width=device-width & initial-scale=1.0 configured.")
            else:
                results["P1_High"].append("Viewport: Missing standard mobile scaling attributes.")
            if "viewport-fit=cover" in vp:
                results["Passed"].append("Android Edge-to-Edge: viewport-fit=cover active for gesture navigation.")
            else:
                results["P2_Optimization"].append("Android Edge-to-Edge: Consider adding 'viewport-fit=cover' to viewport meta.")
    else:
        results["P0_Critical"].append("Viewport: Missing <meta name='viewport'> tag entirely!")

    # 2. Android Theme Color (Chrome System Bar)
    if 'name="theme-color"' in html:
        results["Passed"].append("Android Theme: <meta name='theme-color'> defined for seamless status bar tinting.")
    else:
        results["P1_High"].append("Android Theme: Missing <meta name='theme-color'> tag (status bar will show default browser white/grey).")

    # 3. SEO & OpenGraph Meta
    if 'name="description"' in html:
        results["Passed"].append("SEO: Meta description is present.")
    else:
        results["P1_High"].append("SEO: Missing <meta name='description'> tag.")

    og_tags = ["og:title", "og:description", "og:image", "og:url", "og:type"]
    missing_og = [tag for tag in og_tags if f'property="{tag}"' not in html and f"property='{tag}'" not in html]
    if not missing_og:
        results["Passed"].append("Social Graph: All essential OpenGraph (og:*) meta tags are present.")
    else:
        results["P2_Optimization"].append(f"Social Graph: Missing OpenGraph tags: {', '.join(missing_og)}")

    # 4. Critical Image Preload & WebP LCP Optimization
    if 'rel="preload"' in html and 'as="image"' in html:
        results["Passed"].append("Performance (LCP): Critical above-the-fold image preloaded via <link rel='preload'>.")
    else:
        results["P2_Optimization"].append("Performance (LCP): Hero background could be preloaded via <link rel='preload'> to eliminate paint delay.")

    # 5. Tap Targets & Accessibility
    aria_matches = len(re.findall(r'aria-label=', html))
    if aria_matches >= 8:
        results["Passed"].append(f"Accessibility (a11y): Rich ARIA labeling present ({aria_matches} elements labeled).")
    else:
        results["P2_Optimization"].append("Accessibility (a11y): Consider adding more aria-labels for screen readers.")

    # 6. Touch Targets Size Check (CSS)
    if 'height: 44px' in html or 'height: 48px' in html:
        results["Passed"].append("Touch Targets: Standard 44dp/48dp mobile touch heights detected on key interactive bars.")
        
    # 7. Print Report
    print(f"\n[+] PASSED CHECKS ({len(results['Passed'])}):")
    for p in results["Passed"]:
        print(f"  ✓ {p}")
        
    if results["P0_Critical"]:
        print(f"\n[!] P0 CRITICAL ISSUES ({len(results['P0_Critical'])}):")
        for c in results["P0_Critical"]:
            print(f"  ✗ {c}")
            
    if results["P1_High"]:
        print(f"\n[-] P1 HIGH IMPACT IMPROVEMENTS ({len(results['P1_High'])}):")
        for h in results["P1_High"]:
            print(f"  ▲ {h}")

    if results["P2_Optimization"]:
        print(f"\n[*] P2 OPTIMIZATION RECOMMENDATIONS ({len(results['P2_Optimization'])}):")
        for o in results["P2_Optimization"]:
            print(f"  • {o}")

    print("\n--------------------------------------------------")
    score = int((len(results["Passed"]) / (len(results["Passed"]) + len(results["P0_Critical"]) + len(results["P1_High"]) + len(results["P2_Optimization"]))) * 100)
    print(f"Health & Compliance Score: {score}/100")
    print("--------------------------------------------------\n")
    return results

if __name__ == "__main__":
    audit_landing_page("/home/user/MOEZAQ/src/pages/index.astro")
