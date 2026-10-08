---
name: Artisanal Roast Analytics
colors:
  surface: '#fbf9f5'
  surface-dim: '#dbdad6'
  surface-bright: '#fbf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3ef'
  surface-container: '#efeeea'
  surface-container-high: '#eae8e4'
  surface-container-highest: '#e4e2de'
  on-surface: '#1b1c1a'
  on-surface-variant: '#504440'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f0ed'
  outline: '#827470'
  outline-variant: '#d3c3be'
  surface-tint: '#74584e'
  primary: '#090100'
  on-primary: '#ffffff'
  primary-container: '#2c1810'
  on-primary-container: '#9e7e73'
  inverse-primary: '#e3bfb2'
  secondary: '#865225'
  on-secondary: '#ffffff'
  secondary-container: '#fdb882'
  on-secondary-container: '#78471b'
  tertiary: '#000402'
  on-tertiary: '#ffffff'
  tertiary-container: '#112019'
  on-tertiary-container: '#78897f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbce'
  primary-fixed-dim: '#e3bfb2'
  on-primary-fixed: '#2a170f'
  on-primary-fixed-variant: '#5a4137'
  secondary-fixed: '#ffdcc3'
  secondary-fixed-dim: '#fdb882'
  on-secondary-fixed: '#2f1500'
  on-secondary-fixed-variant: '#6a3b10'
  tertiary-fixed: '#d5e7db'
  tertiary-fixed-dim: '#b9cbbf'
  on-tertiary-fixed: '#0f1f17'
  on-tertiary-fixed-variant: '#3a4a42'
  background: '#fbf9f5'
  on-background: '#1b1c1a'
  surface-variant: '#e4e2de'
typography:
  display-lg:
    fontFamily: Epilogue
    fontSize: 3rem
    fontWeight: '700'
    lineHeight: 3.5rem
    letterSpacing: -0.03em
  headline-xl:
    fontFamily: Epilogue
    fontSize: 2.25rem
    fontWeight: '600'
    lineHeight: 2.75rem
    letterSpacing: -0.02em
  headline-xl-mobile:
    fontFamily: Epilogue
    fontSize: 1.75rem
    fontWeight: '600'
    lineHeight: 2.25rem
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Epilogue
    fontSize: 1.75rem
    fontWeight: '600'
    lineHeight: 2.25rem
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: Epilogue
    fontSize: 1.25rem
    fontWeight: '600'
    lineHeight: 1.75rem
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: 1.75rem
    letterSpacing: 0em
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.9375rem
    fontWeight: '400'
    lineHeight: 1.5rem
    letterSpacing: 0em
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.8125rem
    fontWeight: '400'
    lineHeight: 1.25rem
    letterSpacing: 0.01em
  metric-stat:
    fontFamily: Space Grotesk
    fontSize: 2rem
    fontWeight: '700'
    lineHeight: 2.25rem
    letterSpacing: -0.03em
  label-md:
    fontFamily: Space Grotesk
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: 1rem
    letterSpacing: 0.08em
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 0.6875rem
    fontWeight: '500'
    lineHeight: 0.875rem
    letterSpacing: 0.06em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-sm: 1rem
  gutter-lg: 2rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system expresses the sensory precision and warmth of third-wave specialty roasting married to analytical rigor. Built for independent roasters, specialty café founders, and green coffee buyers, the aesthetic balances high-craft editorial sensibility with dense data visualization.

The stylistic direction blends **Modern Editorial** with **Tactile Warmth**:
- Generous cream-toned negative space that evokes unbleached paper filters, cupping logs, and polished ceramic ware.
- Deliberate micro-textures achieved through soft, tinted borders and warm-cast shadows rather than cold sterile grays.
- Precise data displays where charts, metrics, and roasting telemetry feel integrated into the environment rather than dropped in as generic corporate graphs.

## Colors

The palette derives strictly from the roasting and cupping ritual: deep extraction tones, Maillard browning, steamed oat milk, and botanical accents.

- **Primary (`#2C1810`)**: Deep roast espresso. Used for primary typography, dominant structural controls, primary actions, and key telemetry framing.
- **Secondary (`#C88A58`)**: Warm roasted caramel and amber. Used for active states, highlighted chart series, trends, callout badges, and focus rings. Supported by `#E29578` (terracotta) for warnings or warm secondary metrics.
- **Tertiary (`#76877D`)**: Warm sage. Evokes green coffee bean stock and balance. Used for positive trends, healthy machine telemetry, origin status, and calm informational tags.
- **Neutral Canvas (`#FBF9F5`)**: Creamy oat linen. Serves as the global backdrop.
- **Neutral Elevated (`#F5EFEB`)**: Steamed froth cream. Used for card backgrounds, nested containers, and data table headers.
- **Neutral Surface High (`#EFE8DE`)**: Layered containment tone for hover states and divider strokes.
- **Text & Contrast (`#1A1412`)**: Dark slate umber, providing maximum legibility without the harshness of pure `#000000`.

## Typography

The typographic hierarchy combines editorial weight with data precision:
- **Headlines (Epilogue)**: Imparts a contemporary boutique coffee branding presence with crisp geometric punch.
- **Body & Controls (Plus Jakarta Sans)**: Offers superior legibility for operational telemetry, long-form blend descriptions, and tabular reports.
- **Labels, Codes & Big Metrics (Space Grotesk)**: Provides proportional monospaced clarity for extraction yields, roast profiles, timestamps, and financial summaries.

All labels (`label-md`, `label-sm`) default to uppercase transformations to anchor analytical context across complex dashboards.

## Layout & Spacing

The dashboard relies on an adaptable 12-column layout grid:
- **Desktop (≥ 1280px)**: 12 columns, 2rem margins, 1.5rem gutters. KPI metrics occupy 3-column slots (4 across); chart cards occupy 6, 8, or 12 columns.
- **Tablet (768px - 1279px)**: 8 columns, 1.5rem margins, 1rem gutters. KPI cards collapse to 2 columns (2x2 grid); master-detail views stack vertically.
- **Mobile (< 768px)**: 4 columns, 1rem margins, 1rem gutters. Metric groups scroll horizontally or stack into 1-column cards.

Spacing maintains strict vertical rhythm in multiples of 4px and 8px, prioritizing clear analytical separation between chart controls, summary filters, and data canvases.

## Elevation & Depth

To avoid sterile tech shadows, this design system uses low-contrast physical outlines and espresso-tinted ambient glows:

- **Flat Canvas Tier**: The global background (`#FBF9F5`) sets the base.
- **Surface Elevation Tier 1 (Cards, metric tiles)**: Layered with `#F5EFEB`, bounded by a hairline border: `1px solid rgba(44, 24, 16, 0.08)`. Subtle grounding shadow: `0 2px 8px -2px rgba(44, 24, 16, 0.04), 0 1px 3px rgba(44, 24, 16, 0.02)`.
- **Surface Elevation Tier 2 (Hover cards, active drawer panels, dropdowns)**: Card background `#FFFFFF`, bordered by `1px solid rgba(44, 24, 16, 0.12)`. Warm ambient drop: `0 12px 24px -6px rgba(44, 24, 16, 0.08), 0 4px 8px -2px rgba(44, 24, 16, 0.04)`.
- **Surface Elevation Tier 3 (Modals, cupping scorecards)**: Pure `#FFFFFF`, floating over a tinted scrim `rgba(26, 20, 18, 0.4)` with backdrop-filter blur `4px`, backed by `0 24px 48px -12px rgba(44, 24, 16, 0.16)`.

## Shapes

The design system incorporates intentional, gentle curves inspired by handcrafted ceramic mugs and pour-over carafes. 

- Base UI components (buttons, text inputs, segment pickers) feature `0.5rem` (8px) corner rounding.
- Dashboard cards and analytics visualization panels use `rounded-lg` (`1rem` / 16px).
- Modals, large summary containers, and sliding telemetry trays use `rounded-xl` (`1.5rem` / 24px).
- Status pills, tag badges, and live indicator dots use continuous organic radii (full pill).

## Components

### Buttons
- **Primary**: Solid rich espresso `#2C1810` background, `#FBF9F5` typography, height 40px, padding `0 18px`, `rounded-md` (8px). Hover transitions to `#43261A` with a micro translateY(-1px).
- **Secondary**: Soft oat background `#F5EFEB`, border `1px solid rgba(44, 24, 16, 0.15)`, text `#2C1810`. Hover switches background to `#EFE8DE`.
- **Accent / Special Action**: Warm caramel `#C88A58` background with `#FFFFFF` text. Used for primary telemetry actions (e.g., "Start Roast Log", "Export Batch").

### Metric & KPI Cards
- Base surface `#F5EFEB` with `1px solid rgba(44, 24, 16, 0.08)` border and `16px` rounding.
- Category label in `label-md` (`Space Grotesk`, uppercase, color: `rgba(26, 20, 18, 0.6)`).
- Metric figure displayed in `metric-stat`.
- Trend delta badge: Sage green background `rgba(118, 135, 125, 0.16)` with `#4E5C54` text for positive/yield improvement; Terracotta `rgba(226, 149, 120, 0.18)` with `#A6563B` text for negative/loss.

### Filter Chips & Segment Controls
- Segment bar styled as an inset pill track with `#EFE8DE` fill and 4px internal padding.
- Active segment is a white pill (`#FFFFFF`) featuring `0 1px 3px rgba(44, 24, 16, 0.08)` elevation and espresso text.
- Origin filter chips: Border `1px solid rgba(44, 24, 16, 0.12)`, `Space Grotesk` uppercase text, transitioning to solid caramel `#C88A58` when selected.

### Input Fields & Selectors
- Background: `#FFFFFF` inside an oat field container, height 40px, padding horizontal 12px.
- Inactive border: `1px solid rgba(44, 24, 16, 0.14)`.
- Focus border: `1.5px solid #C88A58` paired with an ambient ring: `0 0 0 3px rgba(200, 138, 88, 0.18)`.

### Roasting Profile & Time-Series Visualizers
- Chart backgrounds inherit transparent or `#F5EFEB` fills.
- Grid lines utilize hairline strokes: `rgba(44, 24, 16, 0.05)`.
- Roaster telemetry lines: Bean Temp (Caramel `#C88A58`, 2.5px stroke width), Environment Temp (Espresso `#2C1810`, 1.5px dashed), Rate of Rise (Terracotta `#E29578`, area gradient fade to transparent).