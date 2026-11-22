# Landing Page Management & Performance Skill (Android & Web Vitals)

An AI Agent Skill for managing, auditing, and optimizing the MOEZAQ landing page, specifically tailored for mobile Android viewports, high-conversion UX, and Google Core Web Vitals.

## Core Directives & Guardrails
1. **Preserve UI Art Direction (P0)**:
   - Do NOT alter or regress the existing Smoked Obsidian Glassmorphism visual theme, typography, layout cards, or bespoke animations unless explicitly requested by the user.
2. **Mobile-First Android Baseline (P0)**:
   - Standard minimum width: **360px** (no horizontal overflow, zero layout shift).
   - Above-the-fold zone: Primary message and CTA must fit cleanly within the top **550px** without requiring scrolling.
   - Touch targets: Minimum **48x48dp** or 44dp with 8dp spacing for touch interactions.
   - Android system bar: Must define `<meta name="theme-color" content="#05070a">` matching the dark background.
   - Edge-to-edge: Must support `viewport-fit=cover` and `env(safe-area-inset-bottom)`.
3. **Core Web Vitals Thresholds (P1)**:
   - **LCP (Largest Contentful Paint)**: < 2.5s (achieved via WebP format + high-priority image preloading).
   - **CLS (Cumulative Layout Shift)**: < 0.1 (achieved by explicit card height constraints and zero layout reflows).
   - **INP (Interaction to Next Paint)**: < 200ms (achieved by 0ms pointerdown listeners and GPU hardware-accelerated transforms).

## Automated Audit Tool
Run the built-in auditor anytime to inspect page health:
```bash
python3 scripts/audit_landing_page.py
```
