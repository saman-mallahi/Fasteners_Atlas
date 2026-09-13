import json, zipfile, os, textwrap
p='/mnt/data/atlas_work/data/database.json'
with open(p,encoding='utf-8') as f: D=json.load(f)

# Fix corrupted thread designations found in the prior package.
fix = {'Tr12×/tmp/fa/Fastener_Engineering_Atlas_V2/data/database.json':'Tr12×3','Tr16×/tmp/fa/Fastener_Engineering_Atlas_V2/data/database.json':'Tr16×4','Tr20×/tmp/fa/Fastener_Engineering_Atlas_V2/data/database.json':'Tr20×4','Tr24×/tmp/fa/Fastener_Engineering_Atlas_V2/data/database.json':'Tr24×5','Tr30×/tmp/fa/Fastener_Engineering_Atlas_V2/data/database.json':'Tr30×6','Tr40×/tmp/fa/Fastener_Engineering_Atlas_V2/data/database.json':'Tr40×7'}
for x in D['threads']:
    if x.get('designation') in fix: x['designation']=fix[x['designation']]

coating_details = {
'Electroplated zinc': {
 'procedure':'Typical sequence: alkaline cleaning/degreasing → rinsing → acid activation/pickling as appropriate → zinc electrodeposition → rinsing → conversion treatment/sealant/topcoat when specified → controlled drying → dimensional, appearance, adhesion and corrosion/process verification. For susceptible high-strength steel, hydrogen-embrittlement controls must be part of the qualified process; post-plating baking is not a universal substitute for process control.',
 'engineering':'Common for general corrosion protection. Coating thickness, supplementary treatment and lubricant affect corrosion life, thread fit and torque–tension behavior. For high-strength fasteners, specify the complete coating system and hydrogen-control requirements rather than simply “zinc plated.”',
 'references':[('ISO 4042:2022 — Electroplated coating systems','https://www.iso.org/standard/77913.html'),('ASTM F1940 — Hydrogen embrittlement process control','https://store.astm.org/standards/f1940')]
},
'Hot-dip galvanizing': {
 'procedure':'Typical fastener sequence: surface preparation/cleaning → fluxing or equivalent pretreatment → immersion in molten zinc → withdrawal/drainage → controlled cooling/quenching where specified → inspection of coating, thread fit and appearance. Fastener geometry and thread allowance are designed around the coating system; nuts and bolts should be specified as a matched galvanized system.',
 'engineering':'Produces a relatively thick zinc coating with sacrificial/cathodic protection and is widely used outdoors and in structural applications. Thread dimensional changes and friction scatter are important for assembly preload. Current ISO 10684:2004 remains published while a replacement edition is under development.',
 'references':[('ISO 10684:2004 — Hot dip galvanized coatings','https://www.iso.org/standard/36897.html'),('ISO/CD 10684 — replacement under development','https://www.iso.org/standard/88237.html')]
},
'Zinc flake': {
 'procedure':'Typical sequence: clean/degrease → controlled surface preparation → apply zinc-flake base coat by dip-spin, spray or approved process → cure/bake according to the qualified coating system → apply optional topcoat/lubricant → cure → verify thickness, appearance, adhesion and friction where required. The process is non-electrolytic, so the hydrogen-introduction mechanism differs from conventional electroplating.',
 'engineering':'Especially useful for high-strength fasteners where corrosion performance and low risk of process-induced internal hydrogen embrittlement are important. Friction is a property of the complete coating/topcoat/lubricant system, not the zinc-flake name alone.',
 'references':[('ISO 10683:2018 — Zinc flake coating systems','https://www.iso.org/standard/70609.html'),('ASTM F1940 — Process control for IHE','https://store.astm.org/standards/f1940')]
},
'Phosphate': {
 'procedure':'Typical sequence: clean/degrease → rinse → activate/pickle when required → phosphate conversion treatment → rinse or post-treatment → dry → apply oil, wax, sealant or paint when specified. Manganese phosphate is commonly selected where wear-in and lubricity are important; zinc phosphate is frequently used as a paint/lubricant base.',
 'engineering':'Phosphate is a conversion coating rather than a thick metallic barrier coating. Its corrosion and friction performance depends strongly on the phosphate type, crystal structure, oil/sealant and assembly lubricant. Specify the complete treatment and post-treatment.',
 'references':[('ISO metallic-coatings catalogue','https://www.iso.org/ics/25.220.40/x/')]
},
'Black oxide': {
 'procedure':'Typical sequence: clean/degrease → alkaline black-oxide treatment appropriate to the substrate → rinse → post-treatment/seal or oil → dry. Black oxide is intentionally thin, so dimensional change is small compared with galvanizing. The oil/sealant is normally a major part of the corrosion-performance system.',
 'engineering':'Useful where appearance, low dimensional build and mild corrosion protection are required. Bare black oxide should not be treated as a heavy-duty corrosion barrier; specify the post-treatment and service environment.',
 'references':[('ISO metallic-coatings catalogue','https://www.iso.org/ics/25.220.40/x/')]
},
'PTFE / fluoropolymer': {
 'procedure':'Typical sequence: degrease/clean → substrate preparation or blast/chemical preparation as required → apply primer where the qualified system requires it → apply fluoropolymer layer(s) by spray, dip or other approved method → flash/dry → bake/cure → inspect coating thickness, continuity and friction. The exact cure window is manufacturer/system specific.',
 'engineering':'Selected for low friction, chemical resistance and controlled torque. Because friction can be much lower than for uncoated steel, the same tightening torque can generate substantially higher preload. Use coating-specific torque–tension data.',
 'references':[('ISO 4042:2022 — coating systems and lubricants','https://www.iso.org/standard/77913.html')]
},
'Stainless passivation': {
 'procedure':'Typical sequence: remove oil and fabrication contamination → mechanically or chemically descale/pickle when necessary → rinse thoroughly → apply qualified nitric, citric or electrochemical passivation treatment → rinse/neutralize as required → dry without recontamination → verify cleanliness/passivation by the specified acceptance test. Passivation is not a substitute for removing heavy oxide scale or weld heat tint when those remain.',
 'engineering':'Passivation restores a clean stainless surface and supports formation of the passive chromium-rich oxide film. It does not add a plated corrosion barrier and does not change the base alloy into a higher corrosion-resistance grade.',
 'references':[('ASTM A967/A967M — Chemical passivation treatments','https://store.astm.org/a0967_a0967m-25.html'),('ASTM A380/A380M — Cleaning, descaling and passivation','https://store.astm.org/a0380_a0380m-17.html')]
},
'Zinc-flake coating': {
 'procedure':'Same basic process family as zinc flake: controlled cleaning → substrate preparation → non-electrolytic zinc-flake base application → cure → optional topcoat/lubricant → final cure and inspection. Process parameters must be qualified for the specific coating chemistry, fastener geometry and required friction class.',
 'engineering':'Use when corrosion resistance, dimensional control and reduced hydrogen risk for high-strength steel are priorities. The topcoat/lubricant can materially change friction and chemical resistance.',
 'references':[('ISO 10683:2018','https://www.iso.org/standard/70609.html')]
},
'Hot-dip galvanized zinc': {
 'procedure':'Prepare the steel surface, apply flux/pretreatment, immerse in molten zinc, withdraw and drain, cool/finish and inspect. For threaded fasteners, coating build and thread allowance must be compatible with the mating nut and the specified assembly method.',
 'engineering':'A heavy sacrificial zinc coating suited to atmospheric exposure. Coating thickness and roughness influence thread fit and torque–tension scatter, so galvanized fasteners should be specified and assembled as a controlled system.',
 'references':[('ISO 10684:2004','https://www.iso.org/standard/36897.html'),('ISO/CD 10684 — replacement under development','https://www.iso.org/standard/88237.html')]
},
'Geomet / zinc-flake system': {
 'procedure':'Treat this as a proprietary zinc-flake coating system: clean and prepare the substrate → apply qualified basecoat → cure → apply system-specific topcoat/lubricant → cure → verify coating thickness, appearance, adhesion, corrosion performance and friction. Do not infer process temperatures or friction values from the trade name alone.',
 'engineering':'Useful for high-performance corrosion protection and controlled assembly friction. Procurement documents should identify the exact product/system, coating class and friction requirements rather than only the trade family.',
 'references':[('ISO 10683:2018 — zinc-flake system framework','https://www.iso.org/standard/70609.html')]
},
'PTFE topcoat': {
 'procedure':'Typical sequence: clean/prepare substrate → apply primer where required → spray/dip PTFE-containing topcoat → flash/dry → controlled thermal cure → inspect thickness and continuity → determine torque–tension/friction for the finished fastener system. Cure temperature must be compatible with both coating and fastener metallurgy.',
 'engineering':'Low friction is the key engineering variable. Torque-based tightening can over-preload a PTFE-coated fastener if uncoated torque values are reused. Use measured or qualified torque–tension data and specify the friction range.',
 'references':[('ISO 16047 — Torque/clamp force testing','https://www.iso.org/standard/29384.html'),('ISO 4042:2022','https://www.iso.org/standard/77913.html')]
},
'Xylan-type fluoropolymer coating': {
 'procedure':'Typical proprietary-system process: degrease/clean → blast or otherwise prepare the substrate → primer application when specified → fluoropolymer topcoat application → flash/dry → controlled bake/cure → inspect thickness, adhesion, continuity and friction. The exact chemistry and cure schedule must come from the coating supplier specification.',
 'engineering':'Can combine corrosion resistance with low and relatively controlled friction. Coating thickness, temperature capability and friction must be treated as controlled design inputs, particularly for pressure-boundary and high-preload joints.',
 'references':[('ISO 16047 — Torque/clamp force testing','https://www.iso.org/standard/29384.html')]
},
'Phosphate coating': {
 'procedure':'Typical process: alkaline cleaning → rinse → activation/pickling as needed → phosphate conversion → rinse/post-treatment → dry → oil, sealant or paint. The post-treatment is normally essential when corrosion protection is required.',
 'engineering':'Phosphate improves surface characteristics and can provide useful lubricity, but it is not normally a stand-alone heavy corrosion barrier. Friction is strongly affected by oil and assembly lubricant.',
 'references':[('ISO metallic-coatings catalogue','https://www.iso.org/ics/25.220.40/x/')]
},
'Cadmium coating': {
 'procedure':'Typical controlled electroplating sequence: clean/degrease → activate/pickle → cadmium electrodeposition → rinse → conversion treatment/seal where specified → controlled drying and inspection. For high-strength steels, hydrogen-control and post-plating treatment requirements must be explicitly qualified. Cadmium processing requires strict environmental and occupational controls.',
 'engineering':'Historically important in aerospace because of corrosion protection, lubricity and compatibility characteristics. Modern environmental restrictions mean cadmium should only be selected where the governing specification and regulatory controls explicitly permit it.',
 'references':[('ISO 2082 — cadmium electroplated coatings','https://www.iso.org/standard/63968.html'),('ISO 4042:2022 — electroplated fastener systems','https://www.iso.org/standard/77913.html')]
},
'Silver plating': {
 'procedure':'Typical sequence: clean/activate substrate → apply appropriate underplate when required → electrodeposit silver to the specified thickness → rinse → optional anti-tarnish/post-treatment → inspect thickness, adhesion and surface condition. Aerospace or electrical applications normally require a qualified supplier process specification.',
 'engineering':'Silver can provide low friction and anti-galling behavior in selected applications and retains useful properties at elevated temperature. Compatibility, tarnishing, galvanic effects and friction should be evaluated for the actual mating materials.',
 'references':[('ISO metallic-coatings catalogue','https://www.iso.org/ics/25.220.40/x/')]
},
'Nickel plating': {
 'procedure':'Typical sequence: clean/degrease → activate substrate → optional strike/underplate → nickel electrodeposition → rinse → post-treatment if specified → inspect thickness, adhesion and hardness. Electroless nickel uses a different deposition chemistry and should not be assumed equivalent to electrolytic nickel.',
 'engineering':'Provides a hard, dimensionally controllable corrosion-resistant surface. For high-strength steel fasteners, hydrogen uptake, coating adhesion, internal stress and friction need process-specific verification.',
 'references':[('ISO metallic-coatings catalogue','https://www.iso.org/ics/25.220.40/x/')]
}

}

for x in D['coatings']:
    key=x['name']
    info=coating_details.get(key)
    if info:
        x.update(info)

D['meta']['version']='1.0.0'
D['meta']['release']='v1.0'
D['meta']['updated']='2026-09-12'
D['meta']['description']='Expanded engineering reference database with detailed standards, materials, fasteners, threads, coating procedures, compatibility records and engineering warnings.'
with open(p,'w',encoding='utf-8') as f: json.dump(D,f,ensure_ascii=False,indent=2)
