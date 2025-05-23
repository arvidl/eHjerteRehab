#!/usr/bin/env python3
"""
Direkte analyse av Ola Nordmanns pasientprofil for eHjerteRehab
Unngår CrewAI-rekursjonsproblemer ved å gi direkte svar
"""

def analyser_ola_nordmann_profil():
    """
    Analyserer Ola Nordmanns profil og identifiserer nøkkelinnsikter
    for persontilpasset eHjerteRehab-program
    """
    
    print("=== PASIENTPROFIL ANALYSE: OLA NORDMANN (67 ÅR) ===\n")
    
    pasient_profil = {
        "medisinsk": "PCI for 3 uker siden, hypertensjon, diabetes type 2, lett overvektig",
        "livsstil": "Nylig pensjonert, stillesittende tidligere, bor alene, liker naturen",
        "psykososialt": "Bekymret for fremtiden, litt isolert, moderat motivasjon",
        "teknologi": "Bruker smarttelefon/nettbrett til enkle ting",
        "mål": "Komme i bedre form, føle seg tryggere, ha noe meningsfylt å gjøre"
    }
    
    print("PASIENTOPPLYSNINGER:")
    for kategori, info in pasient_profil.items():
        print(f"• {kategori.upper()}: {info}")
    
    print("\n" + "="*60)
    print("NØKKELINNSIKTER FOR PERSONTILPASSET eHJERTEREHAB-PROGRAM")
    print("="*60)
    
    innsikter = [
        {
            "nummer": 1,
            "tema": "KOMORBIDITET-MANAGEMENT",
            "innsikt": "Hans diabetes type 2 og hypertensjon krever kontinuerlig monitorering under fysisk aktivitet. Rehabiliteringsprogrammet må inkludere blodsukkerkontroll før/etter trening og blodtrykksmåling.",
            "implikasjon": "Teknologisk støtte for logging av verdier, påminnelser om medisiner, og varsling ved avvikende verdier."
        },
        {
            "nummer": 2,
            "tema": "MOTIVASJON GJENNOM NATURINTERESSE",
            "innsikt": "Hans preferanse for naturen og 'pusling med ting' kan utnyttes som motivasjonsdrivere. Utendørsaktiviteter som hagearbeid, korte skogsturer og naturbaserte øvelser vil appellere til ham.",
            "implikasjon": "Integrer værbaserte aktivitetsforslag og sesongmessige utendørsøvelser i den digitale plattformen."
        },
        {
            "nummer": 3,
            "tema": "SOSIAL ISOLASJON ETTER PENSJONERING",
            "innsikt": "Overgangen til pensjonisttilværelse har skapt isolasjon som kan påvirke mental helse negativt. Rehabiliteringen bør inkludere sosiale elementer for å skape tilhørighet og støtte.",
            "implikasjon": "Digitale felleskap, mentorordninger med andre hjerterehabilitering-pasienter, eller lokale gruppetilbud."
        },
        {
            "nummer": 4,
            "tema": "TEKNOLOGISK TILGJENGELIGHET",
            "innsikt": "Begrenset teknologisk kompetanse krever en svært brukervennlig og forenklet digital løsning. Komplekse funksjoner vil skape barrierer for deltakelse.",
            "implikasjon": "Stort skrift, enkle navigasjonsmenyer, talebaserte instruksjoner, og mulighet for telefonbasert støtte."
        },
        {
            "nummer": 5,
            "tema": "ANGST OG TRYGGHETSBEHOV",
            "innsikt": "Frykten for nytt hjerteinfarkt skaper betydelig angst som kan hemme deltakelse i fysisk aktivitet. Han trenger kontinuerlig trygghet og forsikring om at aktivitetene er sikre.",
            "implikasjon": "Gradvis progresjon, tydelige sikkerhetsguidelines, direkte kontakt med helsepersonell ved bekymringer, og hjerterate-monitorering under aktivitet."
        }
    ]
    
    for innsikt in innsikter:
        print(f"\n{innsikt['nummer']}. {innsikt['tema']}")
        print(f"   Innsikt: {innsikt['innsikt']}")
        print(f"   Implikasjon: {innsikt['implikasjon']}")
    
    print("\n" + "="*60)
    print("SAMMENDRAG - PERSONTILPASSINGSSTRATEGI")
    print("="*60)
    
    strategi = [
        "• Fokus på sikkerhet og gradvis progresjon for å redusere angst",
        "• Utnytt naturinteresse gjennom utendørsaktiviteter og hagearbeid", 
        "• Inkluder sosiale elementer for å motvirke isolasjon",
        "• Holdt teknologien enkel og tilgjengelig",
        "• Kontinuerlig monitorering av komorbiditeter (diabetes/hypertensjon)",
        "• Koble rehabiliteringen til hans uttrykte mål om trygghet og mening"
    ]
    
    for punkt in strategi:
        print(punkt)
    
    print(f"\nDenne analysen følger retningslinjene i eHjerteRehab WP1.3 for komorbiditetshåndtering")
    print("og WP2.2 for helsekompetansetilpassede intervensjoner.\n")

if __name__ == "__main__":
    analyser_ola_nordmann_profil() 