import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VEHICLES_PATH = ROOT / "docs/data/vehicles.json"
CHANGELOG_PATH = ROOT / "docs/data/change-log.json"
DATE = "2026-07-24"


def add_source(vehicle, source):
    sources = vehicle.setdefault("sources", [])
    if source not in sources:
        sources.append(source)


def require(by_id, vehicle_id):
    if vehicle_id not in by_id:
        raise KeyError(f"Missing expected vehicle id: {vehicle_id}")
    return by_id[vehicle_id]


with VEHICLES_PATH.open(encoding="utf-8") as f:
    data = json.load(f)

vehicles = data["vehicles"]
by_id = {vehicle["id"]: vehicle for vehicle in vehicles}

data["version"] = 5
data["lastUpdated"] = DATE

# Benchmark only: no candidacy changes.
kia = require(by_id, "kia-ev6-gt")
kia["lastChecked"] = DATE
add_source(kia, "Benchmark-only entry rechecked 2026-07-24; no candidacy research performed.")

# Volvo EX30: current MY27 facts and announced improvements, but recall/control mismatch remains decisive.
ex30 = require(by_id, "volvo-ex30-ultra")
ex30["availabilityUk"] = (
    "On sale in the UK for model year 2027 from £33,060. Volvo lists P8 AWD at up to "
    "279.6 miles WLTP; affected earlier cars still require recall/VIN verification."
)
ex30["facts"]["rangeMiles"] = 279.6
ex30["facts"]["phoneIntegration"] = (
    "Google built-in and wireless Apple CarPlay. Volvo says forthcoming free OTA updates will "
    "introduce a more intuitive UX, but real-world display/software reliability remains a concern."
)
ex30["notes"] = [
    "No status movement. Model-year updates, V2L and promised free UX improvements are positives, but they do not solve the central-screen/minimal-control mismatch.",
    "The battery-recall/VIN check remains mandatory for any earlier-stock vehicle.",
    "Still not worth prioritising for a test drive unless a dealer can demonstrate repaired recall status and current software stability."
]
ex30["lastChecked"] = DATE
add_source(ex30, "Volvo Cars UK EX30 MY27 page and July 2026 product update, checked 2026-07-24.")

# Ford Explorer: exact grant eligibility and retail support now confirmed.
ford = require(by_id, "ford-explorer-ev")
ford["availabilityUk"] = (
    "On sale with strong UK retail and salary-sacrifice support. The £1,500 Electric Car Grant "
    "explicitly covers selected Style/Select Extended Range versions; Ford also advertises a "
    "£1,000 customer saving, 0% APR on eligible versions and Power Promise support to 30 September 2026."
)
ford["scores"]["value"] = 9
ford["flags"]["grantEligibility"] = (
    "Confirmed for 26.75MY Explorer Style RWD Extended Range and Select RWD Extended Range; "
    "Premium/B&O configuration and finance exclusions must be checked against the exact quote."
)
ford["notes"] = [
    "Moves up on value evidence, not formal status. Ford now confirms the grant on selected Extended Range trims and says it is usable through leases/company-car schemes including salary sacrifice.",
    "Current retail promotion also includes a £1,000 customer saving, 0% APR on eligible versions and Ford Power Promise; exact exclusions matter.",
    "Ready for a quote on an Extended Range car with B&O, but performance remains merely adequate rather than exciting."
]
ford["lastChecked"] = DATE
add_source(ford, "Ford UK Explorer page, promotions and EV-grant guidance, checked 2026-07-24.")

# Smart #5: incentives strengthen value; product risks unchanged.
smart = require(by_id, "smart-5-brabus")
smart["availabilityUk"] = (
    "On sale with test-drive visibility. Smart advertises 0% APR across the range and up to "
    "£2,350 in manufacturer offers on #5 model lines through 30 September 2026; confirm the BRABUS-specific amount."
)
smart["scores"]["value"] = 9
smart["flags"]["currentPromotion"] = (
    "0% APR and up to £2,350 manufacturer support on smart #5 model lines; BRABUS-specific support is not stated in the evidence."
)
smart["notes"] = [
    "Remains the strongest overall test-drive candidate. The current 0% APR and #5 manufacturer support improve the value case, subject to BRABUS-specific confirmation.",
    "The £84 annual Premium Connectivity Package remains a concrete subscription red flag.",
    "The test drive must still stress low-speed ride, repeated phone reconnection, common controls, ADAS warnings, insurance and keyless security."
]
smart["lastChecked"] = DATE
add_source(smart, "Smart UK #5 specifications, digital store and summer promotions, checked 2026-07-24.")

# Audi: offers are real but too small to change candidacy.
audi = require(by_id, "audi-a6-etron-sportback")
audi["availabilityUk"] = (
    "On sale from £63,365. Current retail support offers either a complimentary Ohme charger "
    "or £500 off; this does not materially resolve the budget problem."
)
audi["notes"] = [
    "No status movement. The product fit remains strong, but current retail support is too small to overcome the purchase-price ceiling.",
    "Only an unusually favourable salary-sacrifice quote can move it back to the shortlist.",
    "Any dealer enquiry should specify B&O, conventional mirrors and a comfort-oriented wheel/suspension configuration."
]
audi["lastChecked"] = DATE
add_source(audi, "Audi UK A6 Sportback e-tron finance and offers page, checked 2026-07-24.")

# ES90: finance/lease availability is now concrete, but an observed monthly example reinforces poor value.
es90 = require(by_id, "volvo-es90")
es90["availabilityUk"] = (
    "UK-configurable with official Personal/Business Contract Hire and finance options. Volvo advertises "
    "3.9% APR plus £1,500 contribution, or 0% Volvo Loan with 50% deposit, and a complimentary Ohme charger. "
    "A current stock Ultra Twin Motor example was listed at about £987/month PCP."
)
es90["evidenceConfidence"] = "high"
es90["flags"]["leaseVisibility"] = (
    "Official PCH/BCH availability is now confirmed, but observed Ultra Twin Motor pricing remains far outside the target value envelope."
)
es90["notes"] = [
    "Lease availability is no longer an evidence gap, but the available evidence makes the affordability problem clearer rather than better.",
    "The 25-speaker Bowers & Wilkins system, quiet cabin and charging remain highly attractive; price and missing Euro NCAP confirmation still block progression.",
    "Do not prioritise a test drive unless a salary-sacrifice quote is unexpectedly close to the Smart/Cupra alternatives."
]
es90["lastChecked"] = DATE
add_source(es90, "Volvo UK ES90 model, offers and live stock pages, checked 2026-07-24.")

# Tavascan: V2 provides the previously missing audio-within-budget alternative.
tavascan = require(by_id, "cupra-tavascan")
tavascan["availabilityUk"] = (
    "On sale with strong dealer and finance visibility. V2 is £44,495 and includes the 12-speaker "
    "Sennheiser system; VZ1 remains £54,930 and VZ2 £59,830."
)
tavascan["flags"]["alternativeTrim"] = (
    "V2 at £44,495 includes Sennheiser and is the value/audio alternative; it gives up the VZ dual-motor performance and must be compared directly."
)
tavascan["flags"]["currentPromotion"] = (
    "0% APR or £7,750 finance-deposit contribution on current official Tavascan offers, ordered by 2 August 2026."
)
tavascan["notes"] = [
    "Moves up in practical consideration because V2 resolves the previous audio-versus-budget conflict: £44,495 with Sennheiser.",
    "The trade-off is performance. Test V2 and VZ back-to-back rather than assuming the faster VZ is automatically the better fit.",
    "Current 0% APR / deposit-contribution support strengthens the dealer-enquiry case, but salary-sacrifice pricing remains the relevant comparison."
]
tavascan["lastChecked"] = DATE
add_source(tavascan, "Cupra UK Tavascan range and PCP offers, checked 2026-07-24.")

# Born: official 2026 VZ data materially improves the case and justifies promotion.
born = require(by_id, "cupra-born-77kwh")
born["model"] = "Born VZ 79kWh (2026)"
born["status"] = "shortlist"
born["availabilityUk"] = (
    "New 2026 Born VZ is on sale from £45,995 with established dealer, test-drive and salary-sacrifice visibility."
)
born["facts"].update({
    "priceGbp": 45995,
    "rangeMiles": 388,
    "charge10To80Min": 26,
    "maxDcKw": 183,
    "audio": "Sennheiser AMBEO immersive sound system is standard on VZ.",
    "dashboard": "10.25-inch driver display, 12.9-inch Android-based infotainment and mechanical steering-wheel controls; materially better aligned with the control preference.",
    "phoneIntegration": "Google/Apple Maps can be shown in the driver display; My Cupra app and phone integration are offered, but reconnect reliability still needs testing."
})
born["scores"].update({
    "sound": 8,
    "dashboard_controls": 8,
    "phone_integration": 7,
    "value": 9,
    "range_charging": 8
})
born["flags"]["featureSubscription"] = "Verify My Cupra/Cupra Connect renewal terms; no hardware comfort-feature subscription found."
born["flags"]["newModelSoftware"] = "New Android-based infotainment needs real-world reliability validation."
born["notes"] = [
    "Promoted to shortlist. The 2026 VZ now combines £45,995 pricing, standard Sennheiser audio, 326 PS, 5.6-second acceleration, up to 388 miles and improved mechanical steering-wheel controls.",
    "It is less dramatic than the Smart #5 Brabus but currently looks like the strongest balanced/value alternative.",
    "Book a test drive focused on ride comfort, Sennheiser quality, Android infotainment stability, phone reconnection, keyless security and road-bike practicality."
]
born["evidenceConfidence"] = "high"
born["lastChecked"] = DATE
add_source(born, "Cupra UK New Born 2026 model page and current offers, checked 2026-07-24.")

# MG IM5: official UK site confirms connectivity/audio; reliability/security remain blockers.
im5 = require(by_id, "mg-im5")
im5["availabilityUk"] = "On sale through the dedicated UK MG IM site with configurator and test-drive booking."
im5["facts"]["audio"] = "Official UK site confirms a 20-speaker system, double-layer glass and road-noise cancelling technology."
im5["facts"]["phoneIntegration"] = (
    "Official UK site confirms wireless Apple CarPlay and Android Auto across the 26.3-inch display; reconnect/app reliability remains unproven."
)
im5["flags"]["officialConnectivityConfirmed"] = "Wireless CarPlay/Android Auto confirmed; reliability is still an evidence gap."
im5["notes"] = [
    "Moves up only in evidence quality: official UK material now confirms the 20-speaker system, wireless CarPlay/Android Auto, configurator and test-drive availability.",
    "It remains research-only because screen dependence, intrusive ADAS reports, UK software maturity, insurance and theft resistance are not proven strongly enough.",
    "Suitable for a research-oriented demonstration, not for ordering."
]
im5["evidenceConfidence"] = "medium"
im5["lastChecked"] = DATE
add_source(im5, "Official MG IM5 UK model, configurator and test-drive pages, checked 2026-07-24.")
add_source(im5, "Euro NCAP IM5 2025 assessment rechecked 2026-07-24.")

# MG IM6: official UK page now confirms core UK specification and connectivity.
im6 = require(by_id, "mg-im6")
im6["availabilityUk"] = "On sale through the dedicated UK MG IM site with configurator and test-drive booking."
im6["facts"]["rangeMiles"] = 388
im6["facts"]["zeroTo62Sec"] = 3.5
im6["facts"]["audio"] = "20-speaker system is presented as part of the UK IM experience; exact trim inclusion still needs confirmation."
im6["facts"]["phoneIntegration"] = (
    "Official UK site confirms wireless Apple CarPlay and Android Auto; reconnect/app reliability remains unproven."
)
im6["flags"]["officialConnectivityConfirmed"] = "Wireless CarPlay/Android Auto confirmed; reliability is still an evidence gap."
im6["notes"] = [
    "Moves up only in evidence quality: the UK site confirms 751 hp, 3.5-second acceleration, up to 388 miles, wireless CarPlay/Android Auto and active test-drive availability.",
    "Air suspension/four-wheel steering and cabin quietness make a dealer demonstration worthwhile, but screen dependence, security, insurance and long-term software support still block promotion.",
    "Research-oriented demonstration only; do not order without strong UK owner and insurer evidence."
]
im6["evidenceConfidence"] = "medium"
im6["lastChecked"] = DATE
add_source(im6, "Official MG IM6 UK model, configurator and test-drive pages, checked 2026-07-24.")
add_source(im6, "Euro NCAP IM6 2025 assessment rechecked 2026-07-24.")

# Every entry was reviewed on this run.
for vehicle in vehicles:
    vehicle["lastChecked"] = DATE

with VEHICLES_PATH.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    f.write("\n")

with CHANGELOG_PATH.open(encoding="utf-8") as f:
    changelog = json.load(f)

entry = {
    "date": DATE,
    "type": "research",
    "summary": "Current UK-market refresh: Born VZ promoted; Ford, Smart and Cupra offers clarified.",
    "details": [
        "Promoted the 2026 Cupra Born VZ to shortlist after official confirmation of £45,995 pricing, standard Sennheiser audio, improved mechanical controls, 388-mile maximum range and 26-minute charging.",
        "Strengthened the Ford Explorer value case: selected Extended Range trims explicitly qualify for the £1,500 grant, which Ford says also applies through lease/company-car and salary-sacrifice schemes; current retail support is substantial.",
        "Strengthened Smart #5 value evidence with 0% APR and up to £2,350 support on #5 model lines, while retaining subscription, software, phone and security red flags.",
        "Identified Tavascan V2 at £44,495 with Sennheiser as the audio-within-budget alternative to the faster, more expensive VZ trims.",
        "Confirmed ES90 Personal/Business Contract Hire availability, but current stock pricing reinforces rather than resolves the affordability problem.",
        "Confirmed official UK IM5/IM6 wireless CarPlay/Android Auto, configurator and test-drive availability; both remain research-only because reliability, security, insurance and control ergonomics are still insufficiently proven."
    ]
}

if not changelog.get("entries") or changelog["entries"][0].get("date") != DATE:
    changelog.setdefault("entries", []).insert(0, entry)

with CHANGELOG_PATH.open("w", encoding="utf-8") as f:
    json.dump(changelog, f, ensure_ascii=False, indent=2)
    f.write("\n")
