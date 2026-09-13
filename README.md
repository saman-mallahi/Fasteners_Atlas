# Fastener Engineering Atlas

Fastener Engineering Atlas is an AI-assisted engineering reference and preliminary screening tool for mechanical fasteners and threaded joints. It brings fastener families, materials and grades, thread systems, standards, coatings, compatibility information, engineering warnings and basic calculations into one searchable interface.

## What it covers

- **Engineering Selector** — preliminary screening of material/grade candidates by service environment, strength, temperature range, material group and specific grade.
- **Standards Library** — structured references to DIN, ISO, ASTM, ASME, SAE, API, NACE/ISO 15156, EN, JIS and GB/T documents.
- **Fastener Database** — bolts, screws, studs, nuts, washers, anchors, structural and specialized fastener families.
- **Materials & Grades** — engineering-oriented records for carbon/alloy steels, stainless steels, duplex/super-duplex, nickel alloys, titanium and other fastener materials.
- **Thread Database** — metric, Unified, pipe, trapezoidal and ACME thread references, including pitch/TPI, diameters, tap-drill and clearance references.
- **Coatings & Finishes** — coating systems, typical processes, engineering uses and risks such as hydrogen embrittlement and friction changes.
- **Compatibility Matrix** — preliminary material and fastener pairing guidance.
- **Engineering Warnings** — common issues including galling, fatigue, corrosion, hydrogen effects, temperature and preload concerns.
- **Calculators** — preliminary torque/preload, thread stress-area and thermal-expansion helpers.

## Database

The engineering data is separated from the application in `data/database.json`. The current baseline contains approximately **94 standards, 46 material/grade records, 32 fastener families, 239 thread records, 16 coating records, 27 compatibility entries, 20 warnings and 15 industry/application records**.

## Engineering philosophy

The Atlas is designed for **reference, education and preliminary screening**, not final design approval. Values may depend on diameter, product form, heat treatment, temperature, coating, manufacturing condition and the exact standard edition. Thread dimensions may be reference/basic values rather than manufacturing tolerance limits.

Always verify critical information against the current governing standard, manufacturer documentation, MTCs, project specifications and applicable design code before design, procurement, fabrication or safety-critical use.

> **AI-MADE ENGINEERING TOOL — USE WITH DISCRETION**
>
> This project was created with AI assistance. AI-generated engineering information can contain omissions or errors. The Atlas is not a substitute for applicable standards, design codes, manufacturer data, certified material documentation or qualified engineering review.

## Project structure

```text
Fastener_Engineering_Atlas/
├── index.html
├── manifest.json
├── sw.js
├── README.md
├── assets/
│   └── logo.svg
├── css/
│   └── style.css
├── js/
│   └── app.js
└── data/
    └── database.json
```

The application is intentionally modular so that additional standards, materials, thread series, coating systems and engineering calculations can be added without redesigning the core interface.
