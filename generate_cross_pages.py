#!/usr/bin/env python3
"""
Generate 36 city x service cross pages for Meridian Concrete Solutions.
6 cities x 6 services = 36 unique HTML pages.
"""

import os

# Configuration
CITIES = [
    {"name": "Boise", "slug": "boise", "zip_codes": "83702-83716", "landmarks": "North End, the Bench, Foothills, Downtown, Boise State University", "description": "Idaho's capital and largest city, featuring diverse neighborhoods from historic homes in the North End to modern estates in the Foothills."},
    {"name": "Meridian", "slug": "meridian", "zip_codes": "83642, 83646", "landmarks": "Village at Meridian, Cherry Lane, Ten Mile, Eagle Road corridor", "description": "One of the fastest-growing cities in Idaho, known for its family-friendly neighborhoods and excellent schools."},
    {"name": "Eagle", "slug": "eagle", "zip_codes": "83616, 83669", "landmarks": "Eagle Road, the Foothills, Eagle River, downtown Eagle", "description": "An upscale community nestled against the Boise Foothills, known for larger properties and custom homes."},
    {"name": "Star", "slug": "star", "zip_codes": "83669", "landmarks": "Highway 44, Star Road, growing residential communities", "description": "A rapidly expanding city west of Meridian, popular with families seeking newer construction and spacious lots."},
    {"name": "Kuna", "slug": "kuna", "zip_codes": "83634", "landmarks": "Kuna Road, Ten Mile, the Kuna School District", "description": "A growing community south of Meridian with a small-town feel and easy access to the broader Treasure Valley."},
    {"name": "Nampa", "slug": "nampa", "zip_codes": "83651, 83686, 83687", "landmarks": "Downtown Nampa, Lake Lowell, the Idaho Center, Karcher Road", "description": "The largest city in Canyon County, offering a mix of historic charm and modern development."},
]

SERVICES = [
    {
        "name": "Concrete Driveways",
        "slug": "concrete-driveways",
        "eyebrow": "Concrete Driveway Contractor",
        "hero_desc": "A well-built driveway starts with proper base preparation and ends with a finish that withstands Idaho's freeze-thaw cycles. We've been installing driveways across the Treasure Valley since 2010.",
        "sections": [
            {
                "title": "Why Concrete Driveways Outperform Other Materials in Idaho",
                "content": "The Treasure Valley's climate is tough on outdoor surfaces. Summer temperatures routinely climb above 100°F, while winter brings repeated freeze-thaw cycles that can destroy asphalt and crack paver joints. Concrete handles these conditions better than any alternative.",
                "features": [
                    ("Freeze-Thaw Resistant", "Concrete handles Idaho's repeated freeze-thaw cycles better than any alternative. It doesn't soften in heat and resists salt damage when properly sealed."),
                    ("Long Lifespan", "A well-installed concrete driveway lasts 25 to 30 years with minimal maintenance, compared to asphalt which needs resealing every 2-3 years."),
                    ("Low Maintenance", "Your driveway needs only occasional cleaning and sealing every 5-7 years. For homeowners who want a surface they can park on year-round, concrete is the practical choice."),
                ]
            },
            {
                "title": "Driveway Options We Install",
                "cards": [
                    ("Standard Broom-Finish Concrete", "The most common driveway surface in the Treasure Valley. We use 4,000 PSI concrete with fiber mesh reinforcement, poured 4-5 inches thick over a properly compacted gravel base. The broom finish creates subtle texture that provides excellent traction during icy winters."),
                    ("Stamped Concrete Driveways", "Stamped concrete transforms a functional surface into a design feature. We offer patterns that complement Treasure Valley architecture — ashlar slate, cobblestone, and random flagstone are popular choices. Color options range from warm terracotta to cool slate gray."),
                    ("Exposed Aggregate Driveways", "Exposed aggregate reveals the natural stone within the concrete mix, creating a textured, decorative surface. We use locally sourced Idaho river rock aggregate that blends naturally with the high desert landscape."),
                ]
            },
            {
                "title": "The Installation Process",
                "steps": [
                    ("Site assessment and measurement.", "We visit your property, take measurements, check soil conditions, and discuss your preferences for finish and color."),
                    ("Base preparation.", "We excavate to proper depth, install and compact a 4-6 inch crushed gravel base, and set grading for water runoff — critical where clay soils can cause heaving."),
                    ("Forming and reinforcement.", "Steel rebar or fiber mesh reinforcement, expansion joints every 10-12 feet, and proper edge forms ensure your driveway won't crack prematurely."),
                    ("Pouring and finishing.", "4,000 PSI concrete delivered fresh from local plants. Your chosen finish is applied while the concrete is workable."),
                    ("Curing and sealing.", "We apply a curing compound and return after 28 days to apply a penetrating sealer that protects against Idaho's freeze-thaw cycles."),
                ]
            },
        ],
        "pricing": [
            ("$6-9", "per sq. ft.", "Standard Broom Finish", "Durable, affordable, and provides excellent traction during icy winters."),
            ("$10-15", "per sq. ft.", "Stamped Concrete", "Transforms your driveway into a design feature with patterns that complement your home."),
            ("$8-12", "per sq. ft.", "Exposed Aggregate", "Distinctive natural stone texture with excellent traction."),
        ],
        "faq": [
            ("How much does a concrete driveway cost?", "A standard concrete driveway typically costs between $6 and $15 per square foot installed, depending on thickness, reinforcement, and finish. For an average two-car driveway (approximately 600 square feet), expect to invest between $3,600 and $9,000."),
            ("How long does concrete take to cure?", "Concrete typically reaches initial set within 24-48 hours, allowing light foot traffic. However, full curing takes 28 days. Idaho's variable climate affects curing times."),
            ("Do you offer warranties on driveway work?", "Yes. We stand behind our craftsmanship with comprehensive warranties. Structural concrete work typically carries a multi-year warranty against defects in workmanship."),
            ("Can you repair cracked driveways?", "Absolutely. We specialize in concrete repair services including crack injection, slab jacking, spall repair, and full resurfacing."),
        ]
    },
    {
        "name": "Concrete Patios",
        "slug": "concrete-patios",
        "eyebrow": "Concrete Patio Builder",
        "hero_desc": "Transform your backyard into an outdoor living space with a custom concrete patio. From simple slabs to intricate stamped designs, we build patios that enhance your home and withstand Idaho seasons.",
        "sections": [
            {
                "title": "Why Choose Concrete for Your Patio",
                "content": "Concrete patios offer the perfect balance of durability, versatility, and value. Unlike wood decks that require annual staining or pavers that can shift over time, a properly installed concrete patio provides decades of low-maintenance enjoyment.",
                "features": [
                    ("Weather Resistant", "Concrete withstands Idaho's hot summers and freezing winters without warping, rotting, or shifting. Proper sealing protects against moisture and UV damage."),
                    ("Design Flexibility", "From smooth modern finishes to stamped patterns that mimic natural stone, concrete can be customized to match any architectural style."),
                    ("Cost Effective", "Concrete patios typically cost less per square foot than pavers or natural stone while offering comparable longevity and aesthetics."),
                ]
            },
            {
                "title": "Patio Design Options",
                "cards": [
                    ("Standard Concrete Patios", "Clean, smooth finishes that work well with any home style. We can add control joints in decorative patterns and offer multiple color options through integral coloring."),
                    ("Stamped Concrete Patios", "Create the look of flagstone, slate, brick, or wood at a fraction of the cost. Popular patterns include ashlar slate, cobblestone, and European fan."),
                    ("Covered Patios & Pergolas", "Extend your outdoor living season with a covered patio. We can coordinate with builders to add roof structures over your new concrete slab."),
                ]
            },
            {
                "title": "Our Patio Building Process",
                "steps": [
                    ("Design consultation.", "We discuss your vision, take measurements, and help you choose the best finish and color for your space."),
                    ("Site preparation.", "We excavate, grade for proper drainage, and install a compacted gravel base to prevent settling."),
                    ("Forming and pouring.", "Forms are set to your exact dimensions. We pour 4-inch thick slabs with reinforcement as needed."),
                    ("Finishing touches.", "Your chosen finish is applied, whether smooth, broomed, or stamped. We add control joints to manage cracking."),
                    ("Curing and sealing.", "After proper curing, we apply a sealer that protects your patio and enhances its appearance."),
                ]
            },
        ],
        "pricing": [
            ("$8-12", "per sq. ft.", "Standard Patio", "Simple rectangular or square patios with basic finish."),
            ("$12-18", "per sq. ft.", "Stamped Patio", "Decorative patterns with color and texture options."),
            ("$15-25", "per sq. ft.", "Custom Design", "Complex shapes, multiple levels, or intricate stamp patterns."),
        ],
        "faq": [
            ("How much does a concrete patio cost?", "Standard concrete patios range from $8-12 per square foot. Stamped and decorative options range from $12-25 per square foot depending on complexity."),
            ("How long does patio installation take?", "Most patio projects are completed in 3-5 days, including preparation, pouring, and initial finishing. Full curing takes 28 days."),
            ("Can you match my existing concrete?", "We can often match existing concrete colors and finishes for patio additions. Bring us a photo or sample for the best match."),
            ("Do I need a permit for a patio?", "Most residential patios don't require permits if they're under a certain height and not covered. We'll advise you based on your specific project."),
        ]
    },
    {
        "name": "Stamped Concrete",
        "slug": "stamped-concrete",
        "eyebrow": "Decorative Concrete Specialist",
        "hero_desc": "Get the look of natural stone, brick, or wood with stamped concrete. Our decorative concrete solutions offer beauty and durability at a fraction of the cost of premium materials.",
        "sections": [
            {
                "title": "Why Stamped Concrete is Perfect for Idaho Homes",
                "content": "Stamped concrete gives you the high-end look of natural materials with the practical benefits of concrete. It's ideal for the Treasure Valley climate, resisting freeze-thaw damage while maintaining its beauty for decades.",
                "features": [
                    ("Authentic Appearance", "Modern stamping techniques create incredibly realistic textures that mimic slate, flagstone, brick, wood planks, and more."),
                    ("Durability", "Stamped concrete is still concrete — it offers the same 25-30 year lifespan as standard concrete with proper care."),
                    ("Value", "Get the look of $30-50 per square foot natural stone for $12-20 per square foot with stamped concrete."),
                ]
            },
            {
                "title": "Popular Stamped Concrete Patterns",
                "cards": [
                    ("Ashlar Slate", "A sophisticated pattern of rectangular stones in varying sizes. Perfect for patios, pool decks, and entryways. Works well with both traditional and contemporary homes."),
                    ("Cobblestone", "Classic European-style rounded stones that add old-world charm. Ideal for driveways, walkways, and courtyard areas."),
                    ("Wood Plank", "The warmth of wood without the maintenance. Excellent for pool decks and patios where bare feet are common."),
                ]
            },
            {
                "title": "Color Options for Stamped Concrete",
                "steps": [
                    ("Integral color.", "Color is mixed throughout the concrete before pouring, ensuring consistent color even if the surface chips."),
                    ("Color hardener.", "Applied to the surface before stamping, this creates rich, vibrant colors and adds surface strength."),
                    ("Antiquing release.", "A secondary color applied during stamping that settles into the grooves, creating depth and highlighting the pattern."),
                    ("Sealer with color.", "Tinted sealers can enhance or adjust the final color while providing UV and moisture protection."),
                ]
            },
        ],
        "pricing": [
            ("$12-16", "per sq. ft.", "Basic Pattern", "Single pattern with standard color options."),
            ("$16-20", "per sq. ft.", "Premium Pattern", "Custom patterns with multiple colors and finishes."),
            ("$20-28", "per sq. ft.", "Custom Design", "Intricate borders, medallions, or multi-pattern layouts."),
        ],
        "faq": [
            ("How long does stamped concrete last?", "With proper installation and maintenance, stamped concrete lasts 25+ years. Resealing every 2-3 years keeps it looking fresh."),
            ("Is stamped concrete slippery?", "When properly sealed with a non-slip additive, stamped concrete provides excellent traction even when wet."),
            ("Can stamped concrete be repaired?", "Yes, cracks and chips can be repaired. We can often blend repairs seamlessly with the existing pattern and color."),
            ("What maintenance does stamped concrete require?", "Occasional cleaning and resealing every 2-3 years is all that's needed. Avoid harsh de-icing chemicals in winter."),
        ]
    },
    {
        "name": "Concrete Repair",
        "slug": "concrete-repair",
        "eyebrow": "Concrete Repair Specialist",
        "hero_desc": "Don't replace what can be repaired. We fix cracks, spalls, settling, and cosmetic damage to extend the life of your existing concrete. Save money while restoring appearance and function.",
        "sections": [
            {
                "title": "Common Concrete Problems We Fix",
                "content": "Idaho's climate is hard on concrete. Freeze-thaw cycles cause cracking, heavy loads create settling, and time brings cosmetic wear. Most damaged concrete can be repaired rather than replaced, saving you significant money.",
                "features": [
                    ("Crack Repair", "From hairline cracks to structural fissures, we use epoxy injection, routing and sealing, and other techniques to restore integrity."),
                    ("Slab Jacking", "Sunken or uneven concrete can be lifted back to level using our slab jacking process, avoiding costly replacement."),
                    ("Spall Repair", "Flaking and chipping concrete is repaired with bonding agents and matching patch materials that blend seamlessly."),
                ]
            },
            {
                "title": "Our Concrete Repair Services",
                "cards": [
                    ("Crack Injection", "Epoxy or polyurethane injection fills cracks from the inside out, restoring structural integrity and preventing water intrusion."),
                    ("Concrete Leveling", "Also called slab jacking or mudjacking, this process lifts sunken slabs back to their original position without replacement."),
                    ("Resurfacing", "When surface damage is extensive but the base is sound, we apply a new decorative concrete overlay that looks brand new."),
                ]
            },
            {
                "title": "The Repair Process",
                "steps": [
                    ("Assessment.", "We evaluate the damage, determine the cause, and recommend the most effective repair method."),
                    ("Preparation.", "The area is cleaned, loose material is removed, and the surface is prepared for repair materials."),
                    ("Repair.", "Using professional-grade materials, we execute the repair — whether injection, leveling, or patching."),
                    ("Finishing.", "Repairs are finished to match the surrounding concrete as closely as possible."),
                    ("Protection.", "Sealers and protective coatings are applied to prevent future damage in the repaired area."),
                ]
            },
        ],
        "pricing": [
            ("$250-500", "per project", "Crack Repair", "Epoxy injection or routing and sealing for typical driveway cracks."),
            ("$500-1500", "per slab", "Slab Jacking", "Lifting and leveling sunken concrete sections."),
            ("$5-10", "per sq. ft.", "Resurfacing", "Decorative overlay applied over existing sound concrete."),
        ],
        "faq": [
            ("When should concrete be repaired vs replaced?", "If the base is sound and damage is cosmetic or limited, repair is usually best. Severely compromised slabs may need replacement."),
            ("How long do concrete repairs last?", "Quality repairs can last 10+ years. Proper preparation and materials are key to longevity."),
            ("Will repairs be visible?", "We match color and texture as closely as possible. Some repairs may be slightly visible but blend well with the surrounding concrete."),
            ("Can you repair stamped or decorative concrete?", "Yes, we have techniques to repair decorative concrete while preserving the pattern and color."),
        ]
    },
    {
        "name": "Concrete Sidewalks",
        "slug": "concrete-sidewalks",
        "eyebrow": "Sidewalk Contractor",
        "hero_desc": "Safe, durable sidewalks for homes and businesses. We install new sidewalks, repair damaged sections, and ensure ADA compliance for commercial properties throughout the Treasure Valley.",
        "sections": [
            {
                "title": "Quality Sidewalks Built for Idaho",
                "content": "Sidewalks take constant foot traffic and weather exposure. We build sidewalks that stand up to daily use and Idaho's climate, with proper thickness, reinforcement, and joint placement to minimize cracking.",
                "features": [
                    ("Residential Sidewalks", "From front walkways to backyard paths, we install sidewalks that complement your home's style while providing safe, level surfaces."),
                    ("Commercial Sidewalks", "ADA-compliant sidewalks for businesses, including proper slopes, tactile warnings, and durable surfaces for high-traffic areas."),
                    ("Decorative Options", "Stamped, colored, or exposed aggregate sidewalks that enhance curb appeal while maintaining functionality."),
                ]
            },
            {
                "title": "Sidewalk Services We Offer",
                "cards": [
                    ("New Sidewalk Installation", "Complete sidewalk installation from planning to completion. We handle permits, excavation, forming, pouring, and finishing."),
                    ("Sidewalk Repair", "Trip hazards, cracks, and sunken sections are repaired or replaced. We match existing sidewalks for seamless results."),
                    ("ADA Upgrades", "We upgrade existing sidewalks to meet current ADA requirements, including ramp installation and surface corrections."),
                ]
            },
            {
                "title": "Our Sidewalk Installation Process",
                "steps": [
                    ("Planning and permits.", "We determine the best route, obtain necessary permits, and mark utilities before any digging."),
                    ("Excavation and base.", "We excavate to proper depth and install a compacted gravel base for stability."),
                    ("Forming and reinforcement.", "Forms define the sidewalk shape. Wire mesh or rebar is added for strength in high-traffic areas."),
                    ("Pouring and finishing.", "Concrete is poured, screeded, and finished with your chosen texture — typically broom finish for slip resistance."),
                    ("Curing and cleanup.", "The sidewalk cures properly, forms are removed, and the area is cleaned and restored."),
                ]
            },
        ],
        "pricing": [
            ("$8-12", "per sq. ft.", "Standard Sidewalk", "4-inch thick residential sidewalk with broom finish."),
            ("$12-18", "per sq. ft.", "Decorative Sidewalk", "Stamped or colored sidewalks with enhanced aesthetics."),
            ("$150-300", "per section", "Sidewalk Repair", "Repair or replace damaged sidewalk sections."),
        ],
        "faq": [
            ("How wide should a sidewalk be?", "Residential sidewalks are typically 4 feet wide. Commercial and ADA-compliant sidewalks require minimum 5 feet width."),
            ("How long does sidewalk installation take?", "Most residential sidewalk projects are completed in 1-2 days. Commercial projects vary based on size."),
            ("Do I need a permit for a new sidewalk?", "Most cities require permits for new sidewalk installation. We handle the permit process for you."),
            ("Can you match my existing sidewalk?", "We can match existing concrete color and finish for sidewalk additions and repairs."),
        ]
    },
    {
        "name": "Foundations & Slabs",
        "slug": "foundations-slabs",
        "eyebrow": "Foundation & Slab Contractor",
        "hero_desc": "Strong foundations and slabs for new construction, additions, garages, and outbuildings. We pour foundations that meet code and stand the test of time in Idaho soil conditions.",
        "sections": [
            {
                "title": "Expert Foundation Work for Idaho Homes",
                "content": "Your foundation is the most critical part of your structure. We pour foundations and slabs engineered for Idaho's soil conditions, with proper reinforcement, vapor barriers, and drainage considerations.",
                "features": [
                    ("New Construction Foundations", "Full foundation systems for new homes, including footings, stem walls, and basement walls where applicable."),
                    ("Garage & Shop Slabs", "Thick, reinforced slabs designed for vehicle loads, with proper vapor barriers and control joints."),
                    ("Addition Foundations", "Seamless foundation work for home additions, matched to your existing structure's specifications."),
                ]
            },
            {
                "title": "Foundation & Slab Services",
                "cards": [
                    ("Residential Foundations", "Complete foundation systems for new homes, built to local code with proper engineering and inspection coordination."),
                    ("Garage Slabs", "5-6 inch thick reinforced slabs with vapor barriers, designed for vehicle loads and Idaho climate."),
                    ("Commercial Slabs", "Industrial-grade slabs for warehouses, retail, and office buildings with specialized finishes as needed."),
                ]
            },
            {
                "title": "Our Foundation Process",
                "steps": [
                    ("Site evaluation.", "We assess soil conditions, review plans, and coordinate with engineers and inspectors."),
                    ("Excavation and footings.", "Footings are dug to proper depth below frost line and poured with precise dimensions."),
                    ("Forming and reinforcement.", "Foundation forms are set, and extensive rebar grids are installed for structural strength."),
                    ("Pouring and curing.", "High-strength concrete is poured in continuous operations. Proper curing is critical for foundation integrity."),
                    ("Waterproofing and backfill.", "Foundations are waterproofed, drainage is installed, and careful backfilling prevents damage."),
                ]
            },
        ],
        "pricing": [
            ("$8-15", "per sq. ft.", "Slab Foundation", "Standard residential slab with reinforcement and vapor barrier."),
            ("$20-35", "per sq. ft.", "Full Foundation", "Complete foundation system with footings and stem walls."),
            ("$10-18", "per sq. ft.", "Garage Slab", "Thick reinforced slab designed for vehicle loads."),
        ],
        "faq": [
            ("How deep do footings need to be?", "In the Treasure Valley, footings typically need to extend 12-18 inches below grade to be below the frost line."),
            ("How long before I can build on a new foundation?", "Foundations should cure for at least 7 days before framing begins. Full strength is reached at 28 days."),
            ("Do you coordinate with inspectors?", "Yes, we schedule and coordinate all required inspections for foundation work."),
            ("Can you pour slabs in winter?", "Yes, with proper precautions including heated enclosures and cold-weather concrete mixes."),
        ]
    },
]

# Base HTML template components
def get_header():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{meta_title}}</title>
    <meta name="description" content="{{meta_description}}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://craigclaw.github.io/meridianidconcrete/{{filename}}">

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{{og_title}}">
    <meta property="og:description" content="{{meta_description}}">
    <meta property="og:image" content="https://craigclaw.github.io/meridianidconcrete/images/{{service.slug}}.jpg">
    <meta property="og:url" content="https://craigclaw.github.io/meridianidconcrete/{{filename}}">
    <meta property="og:site_name" content="Meridian Concrete Solutions">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{{og_title}}">
    <meta name="twitter:description" content="{{meta_description}}">

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">

    <!-- Stylesheet -->
    <link rel="stylesheet" href="css/style.css">

    <!-- Schema Markup -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "Meridian Concrete Solutions",
        "image": "https://craigclaw.github.io/meridianidconcrete/images/logo.jpg",
        "telephone": "(208) 555-0147",
        "email": "info@meridianidconcrete.com",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "123 E Fairview Ave",
            "addressLocality": "Meridian",
            "addressRegion": "ID",
            "postalCode": "83642",
            "addressCountry": "US"
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": "{{city_lat}}",
            "longitude": "{{city_lng}}"
        },
        "url": "https://craigclaw.github.io/meridianidconcrete/{{filename}}",
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "07:00",
            "closes": "18:00"
        },
        "priceRange": "$$",
        "areaServed": [
            {"@type": "City", "name": "Meridian"},
            {"@type": "City", "name": "Boise"},
            {"@type": "City", "name": "Eagle"},
            {"@type": "City", "name": "Kuna"},
            {"@type": "City", "name": "Nampa"},
            {"@type": "City", "name": "Star"}
        ]
    }
    </script>

    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "{{service.name}} in {{city.name}}, ID",
        "provider": {
            "@type": "LocalBusiness",
            "name": "Meridian Concrete Solutions",
            "telephone": "+1-208-555-0147",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "123 E Fairview Ave",
                "addressLocality": "Meridian",
                "addressRegion": "ID",
                "postalCode": "83642"
            }
        },
        "areaServed": {
            "@type": "City",
            "name": "{{city.name}}"
        },
        "description": "Professional {{service.name}} serving {{city.name}} and the Treasure Valley."
    }
    </script>

    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
{{faq_schema}}
        ]
    }
    </script>

    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://craigclaw.github.io/meridianidconcrete/"},
            {"@type": "ListItem", "position": 2, "name": "{{service.name}}", "item": "https://craigclaw.github.io/meridianidconcrete/{{service.slug}}.html"},
            {"@type": "ListItem", "position": 3, "name": "{{city.name}}, ID"}
        ]
    }
    </script>
</head>
<body>
    <!-- Header -->
    <header class="site-header">
        <div class="header-inner">
            <a href="index.html" class="logo" aria-label="Meridian Concrete Solutions Home">
                <svg class="logo-icon" viewBox="0 0 42 42" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                    <rect width="42" height="42" rx="8" fill="#b15335"/>
                    <path d="M10 30L18 18L26 26L34 12" stroke="#f4f3ee" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
                    <circle cx="34" cy="12" r="3.5" fill="#f4f3ee"/>
                </svg>
                <span class="logo-text">
                    Meridian Concrete
                    <span>Solutions</span>
                </span>
            </a>
            <a href="tel:2085550147" class="header-phone" style="font-size: 1.5rem; font-weight: 700;">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                </svg>
                (208) 555-0147
            </a>
        </div>
    </header>

    <!-- Navigation -->
    <nav class="main-nav-container" aria-label="Main navigation">
        <div class="nav-inner">
            <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="3" y1="6" x2="21" y2="6"></line>
                    <line x1="3" y1="12" x2="21" y2="12"></line>
                    <line x1="3" y1="18" x2="21" y2="18"></line>
                </svg>
            </button>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="concrete-driveways.html">Driveways</a></li>
                <li><a href="concrete-patios.html">Patios</a></li>
                <li><a href="stamped-concrete.html">Stamped Concrete</a></li>
                <li><a href="concrete-repair.html">Repair</a></li>
                <li><a href="concrete-sidewalks.html">Sidewalks</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="contact.html" class="nav-cta">Get Quote</a></li>
            </ul>
        </div>
    </nav>
'''

def get_hero(service, city):
    return f'''
    <!-- Hero Section -->
    <section class="hero" aria-labelledby="hero-heading">
        <div class="hero-inner">
            <div class="hero-content">
                <p class="hero-eyebrow">{service["eyebrow"]}</p>
                <h1 id="hero-heading">{service["name"]} in {city["name"]}, ID</h1>
                <p class="lead">{service["hero_desc"]} Serving {city["name"]} homeowners and businesses with quality concrete work since 2010.</p>
                <div class="hero-ctas">
                    <a href="tel:2085550147" class="btn btn-primary btn-lg">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                        </svg>
                        Call (208) 555-0147
                    </a>
                    <a href="contact.html" class="btn btn-secondary btn-lg">Request Online Quote</a>
                </div>
                <div class="trust-badges">
                    <span class="trust-badge trust-star">
                        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                        4.9 Google Rating (62 reviews)
                    </span>
                    <span class="trust-badge trust-shield">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                        Licensed &amp; Insured
                    </span>
                    <span class="trust-badge">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                        Fast Quotes Available
                    </span>
                    <span class="trust-badge">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                        Local &amp; Trusted Since 2010
                    </span>
                </div>
            </div>
            <div class="hero-image">
                <picture>
                    <source srcset="images/{service["slug"]}.webp" type="image/webp">
                    <img src="images/{service["slug"]}.jpg" alt="{service["name"]} in {city["name"]}, Idaho" width="600" height="450" loading="eager">
                </picture>
                <div class="hero-badge">
                    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                    Licensed &amp; Insured
                </div>
            </div>
        </div>
    </section>
'''

def get_features_section(section, city):
    features_html = ""
    for i, (title, desc) in enumerate(section.get("features", []), 1):
        stagger = f" stagger-{i}" if i > 1 else ""
        features_html += f'''
                            <div class="feature-item reveal{stagger}">
                                <svg class="feature-icon" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                                    <path d="M24 4L4 14v20l20 10 20-10V14L24 4z"/>
                                    <path d="M24 24v20M4 14l20 10 20-10"/>
                                </svg>
                                <h3>{title}</h3>
                                <p>{desc}</p>
                            </div>
'''
    return f'''
    <!-- Why Choose Section -->
    <section class="section" aria-labelledby="why-heading" style="padding-top: 0;">
        <div class="container" style="padding-left: 0; padding-right: 0;">
            <p class="eyebrow reveal">Why Choose Concrete</p>
            <h2 id="why-heading" class="text-center reveal">{section["title"]}</h2>
            <p class="lead text-center reveal" style="max-width: 65ch; margin: 0.5rem auto 2.5rem;">{section["content"]} Our {city["name"]} customers trust us for quality work that lasts.</p>

            <div class="features-grid">
{features_html}
            </div>
        </div>
    </section>
'''

def get_cards_section(section):
    cards_html = ""
    for i, (title, desc) in enumerate(section.get("cards", []), 1):
        stagger = f" stagger-{i}" if i > 1 else ""
        cards_html += f'''
                            <article class="card card-surface reveal{stagger}">
                                <svg class="card-icon" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                                    <rect x="8" y="8" width="32" height="32" rx="4"/>
                                    <path d="M16 24h16M24 16v16"/>
                                </svg>
                                <h3>{title}</h3>
                                <p>{desc}</p>
                            </article>
'''
    return f'''
    <!-- Options Section -->
    <section class="section section-alt" aria-labelledby="options-heading">
        <div class="container" style="padding-left: 0; padding-right: 0;">
            <p class="eyebrow reveal">Options Available</p>
            <h2 id="options-heading" class="text-center reveal">{section["title"]}</h2>

            <div class="services-grid">
{cards_html}
            </div>
        </div>
    </section>
'''

def get_process_section(section):
    steps_html = ""
    for i, (title, desc) in enumerate(section.get("steps", []), 1):
        stagger = f" stagger-{i}" if i > 1 else ""
        num = f"{i:02d}"
        steps_html += f'''
                                <li class="reveal{stagger}">
                                    <span class="process-number">{num}</span>
                                    <div>
                                        <strong>{title}</strong> {desc}
                                    </div>
                                </li>
'''
    return f'''
    <!-- Process Section -->
    <section class="section" aria-labelledby="process-heading">
        <div class="container content-width" style="padding-left: 0; padding-right: 0;">
            <p class="eyebrow reveal">How We Work</p>
            <h2 id="process-heading" class="text-center reveal">{section["title"]}</h2>
            <p class="lead text-center reveal" style="max-width: 65ch; margin: 0.5rem auto 2.5rem;">Every project we complete in the Treasure Valley follows our proven process for quality results.</p>

            <div class="prose">
                <ol class="process-list">
{steps_html}
                </ol>
            </div>
        </div>
    </section>
'''

def get_pricing_section(service, city):
    pricing_html = ""
    for i, (price, unit, title, desc) in enumerate(service.get("pricing", []), 1):
        stagger = f" stagger-{i}" if i > 1 else ""
        pricing_html += f'''
                            <div class="card card-surface reveal{stagger}" style="text-align: center;">
                                <div style="font-family: var(--font-display); font-size: 2.5rem; color: var(--accent); font-weight: 700;">{price}</div>
                                <p style="color: var(--text-muted); margin-top: 0.25rem;">{unit}</p>
                                <h3 style="margin-top: 0.75rem;">{title}</h3>
                                <p>{desc}</p>
                            </div>
'''
    return f'''
    <!-- Pricing Section -->
    <section class="section section-alt" aria-labelledby="cost-heading">
        <div class="container" style="padding-left: 0; padding-right: 0;">
            <p class="eyebrow reveal">Pricing</p>
            <h2 id="cost-heading" class="text-center reveal">{city["name"]} {service["name"]} Cost</h2>
            <p class="lead text-center reveal" style="max-width: 65ch; margin: 0.5rem auto 2.5rem;">Transparent pricing with no hidden fees — every estimate we provide is itemized and detailed.</p>

            <div class="info-grid" style="grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));">
{pricing_html}
            </div>

            <p class="reveal" style="text-align: center; margin-top: 2rem; color: var(--text-secondary);">We offer free on-site estimates throughout the Treasure Valley. Whether you're in {city["name"]} or nearby communities, we'll assess the site and provide a written quote within 48 hours.</p>
        </div>
    </section>
'''

def get_faq_section(service):
    faq_html = ""
    for i, (question, answer) in enumerate(service.get("faq", []), 1):
        expanded = "true" if i == 1 else "false"
        faq_html += f'''
                            <div class="faq-item reveal">
                                <button class="faq-question" aria-expanded="{expanded}">
                                    {question}
                                    <span class="faq-icon" aria-hidden="true">
                                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                                    </span>
                                </button>
                                <div class="faq-answer">
                                    <div class="faq-answer-inner">
                                        <p>{answer}</p>
                                    </div>
                                </div>
                            </div>
'''
    return f'''
    <!-- FAQ Section -->
    <section class="section section-alt" aria-labelledby="faq-heading">
        <div class="container" style="padding-left: 0; padding-right: 0;">
            <p class="eyebrow reveal">Common Questions</p>
            <h2 id="faq-heading" class="text-center reveal">Frequently Asked Questions</h2>

            <div class="faq-list">
{faq_html}
            </div>
        </div>
    </section>
'''

def get_service_area_section(city, all_cities):
    city_links = ""
    for i, c in enumerate(all_cities, 1):
        if c["name"] != city["name"]:
            stagger = f" stagger-{i}" if i > 1 else ""
            city_links += f'''
                            <a href="{c["slug"]}-id.html" class="location-card reveal{stagger}">
                                <h3>{c["name"]}</h3>
                                <p>Quality concrete services for {c["name"]} residents and businesses.</p>
                                <span class="arrow">Learn more <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:14px;height:14px"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span>
                            </a>
'''
    return f'''
    <!-- Service Area Section -->
    <section class="section" aria-labelledby="area-heading">
        <div class="container" style="padding-left: 0; padding-right: 0;">
            <p class="eyebrow reveal">Service Area</p>
            <h2 id="area-heading" class="text-center reveal">Serving {city["name"]} and the Treasure Valley</h2>
            <p class="lead text-center reveal" style="max-width: 65ch; margin: 0.5rem auto 2.5rem;">While we specialize in {city["name"]} concrete services, our team serves the entire Treasure Valley region with the same quality and attention to detail.</p>

            <div class="info-grid">
{city_links}
            </div>
        </div>
    </section>
'''

def get_cta_banner():
    return '''
    <!-- CTA Banner -->
    <section class="cta-banner" aria-labelledby="cta-heading">
        <div class="container">
            <h2 id="cta-heading">Ready to Start Your Concrete Project?</h2>
            <p>Free estimates, transparent pricing, and concrete work built for Idaho weather.</p>
            <div class="hero-ctas" style="justify-content: center;">
                <a href="tel:2085550147" class="btn btn-inverse btn-lg">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                    </svg>
                    (208) 555-0147
                </a>
                <a href="contact.html" class="btn btn-ghost btn-lg">Request Quote Online</a>
            </div>
        </div>
    </section>
'''

def get_footer():
    return '''
    <footer class="site-footer">
        <div class="footer-grid">
            <div class="footer-brand">
                <a href="index.html" class="logo" style="margin-bottom: 1.25rem;">
                    <svg class="logo-icon" viewBox="0 0 42 42" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <rect width="42" height="42" rx="8" fill="#b15335"/>
                        <path d="M10 30L18 18L26 26L34 12" stroke="#f4f3ee" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
                        <circle cx="34" cy="12" r="3.5" fill="#f4f3ee"/>
                    </svg>
                    <span class="logo-text" style="color: #f4f3ee;">Meridian Concrete <span style="color: rgba(244, 243, 238, 0.65);">Solutions</span></span>
                </a>
                <p>Your trusted concrete contractor serving Meridian and the Treasure Valley since 2010.</p>
                <div class="footer-contact-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                        <circle cx="12" cy="10" r="3"/>
                    </svg>
                    <span>123 E Fairview Ave<br>Meridian, ID 83642</span>
                </div>
                <div class="footer-contact-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                    </svg>
                    <a href="tel:2085550147">(208) 555-0147</a>
                </div>
            </div>
            <div class="footer-col">
                <h4>Services</h4>
                <ul>
                    <li><a href="concrete-driveways.html">Concrete Driveways</a></li>
                    <li><a href="concrete-patios.html">Concrete Patios</a></li>
                    <li><a href="stamped-concrete.html">Stamped Concrete</a></li>
                    <li><a href="concrete-repair.html">Concrete Repair</a></li>
                    <li><a href="concrete-sidewalks.html">Sidewalks &amp; Walkways</a></li>
                    <li><a href="foundations-slabs.html">Foundations &amp; Slabs</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Service Areas</h4>
                <ul>
                    <li><a href="meridian-id.html">Meridian</a></li>
                    <li><a href="boise-id.html">Boise</a></li>
                    <li><a href="eagle-id.html">Eagle</a></li>
                    <li><a href="kuna-id.html">Kuna</a></li>
                    <li><a href="nampa-id.html">Nampa</a></li>
                    <li><a href="star-id.html">Star</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Contact</h4>
                <div class="footer-contact-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                        <polyline points="22,6 12,13 2,6"/>
                    </svg>
                    <a href="mailto:info@meridianidconcrete.com">info@meridianidconcrete.com</a>
                </div>
                <div class="footer-contact-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"/>
                        <polyline points="12 6 12 12 16 14"/>
                    </svg>
                    <span>Mon-Sat: 7:00 AM - 6:00 PM</span>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Meridian Concrete Solutions. All rights reserved.</p>
            <p><a href="privacy.html">Privacy Policy</a><span>|</span><a href="terms.html">Terms of Service</a></p>
        </div>
    </footer>
    <div class="mobile-cta-bar" aria-label="Mobile contact">
        <div class="mobile-cta-bar-inner">
            <a href="tel:2085550147" class="mobile-cta-bar-phone">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                </svg>
                (208) 555-0147
            </a>
            <a href="contact.html" class="btn btn-primary btn-sm">Get Quote</a>
        </div>
    </div>

    <script src="js/main.js"></script>
</body>
</html>
'''

def generate_faq_schema(service):
    faq_items = []
    for question, answer in service.get("faq", []):
        faq_items.append(f'''            {{
                "@type": "Question",
                "name": "{question}",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "{answer}"
                }}
            }}''')
    return ",\n".join(faq_items)

def generate_page(service, city, all_cities):
    """Generate a complete HTML page for a city x service combination."""
    filename = f"{service['slug']}-{city['slug']}.html"

    # City coordinates (approximate)
    city_coords = {
        "boise": ("43.6150", "-116.2023"),
        "meridian": ("43.6121", "-116.3915"),
        "eagle": ("43.6954", "-116.3540"),
        "star": ("43.6921", "-116.4932"),
        "kuna": ("43.4921", "-116.4210"),
        "nampa": ("43.5826", "-116.5635"),
    }
    city_lat, city_lng = city_coords.get(city["slug"], ("43.6121", "-116.3915"))

    # Generate meta tags
    meta_title = f"{service['name']} in {city['name']}, ID | Free Estimates"
    meta_description = f"Professional {service['name'].lower()} in {city['name']}, ID. Licensed, insured, and trusted by {city['name']} homeowners since 2010. Free estimates. Call (208) 555-0147."
    og_title = f"{service['name']} in {city['name']}, ID | Meridian Concrete Solutions"

    # Build the HTML
    html = get_header()
    html = html.replace("{{meta_title}}", meta_title)
    html = html.replace("{{meta_description}}", meta_description)
    html = html.replace("{{og_title}}", og_title)
    html = html.replace("{{filename}}", filename)
    html = html.replace("{{service.slug}}", service["slug"])
    html = html.replace("{{service.name}}", service["name"])
    html = html.replace("{{city.name}}", city["name"])
    html = html.replace("{{city_lat}}", city_lat)
    html = html.replace("{{city_lng}}", city_lng)
    html = html.replace("{{faq_schema}}", generate_faq_schema(service))

    html += get_hero(service, city)
    html += '''    <main>
'''

    # Add content sections
    for section in service.get("sections", []):
        if "features" in section:
            html += get_features_section(section, city)
        elif "cards" in section:
            html += get_cards_section(section)
        elif "steps" in section:
            html += get_process_section(section)

    html += get_pricing_section(service, city)
    html += get_faq_section(service)
    html += get_service_area_section(city, all_cities)
    html += get_cta_banner()
    html += get_footer()

    return html

def main():
    """Generate all 36 city x service cross pages."""
    output_dir = "/Users/craigassistant/Projects/meridianidconcrete"

    pages_generated = 0

    for service in SERVICES:
        for city in CITIES:
            html_content = generate_page(service, city, CITIES)
            filename = f"{service['slug']}-{city['slug']}.html"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)

            pages_generated += 1
            print(f"Generated: {filename}")

    print(f"\n{'='*50}")
    print(f"Successfully generated {pages_generated} cross pages!")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
