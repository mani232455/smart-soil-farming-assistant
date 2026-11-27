# Smart Soil & Farming Assistant (Prototype)

An early-stage educational prototype for exploring how soil measurements and local weather context could support farm planning.

## What it does
- Accepts soil pH and N-P-K values entered by the user.
- Accepts a crop name and basic weather notes.
- Displays simple, rule-based observations and questions to discuss with a local agriculture expert.
- Includes a clear warning that the output is **not** a fertilizer prescription or a substitute for a laboratory soil test.

## Current project status
This is a starter prototype, not a validated agricultural product. It has no real users, downloads, field trials, or verified impact yet. Do not claim otherwise in applications or project descriptions.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

## Inputs
The app uses manually entered values only. It does not currently connect to soil sensors, weather APIs, satellite data, or a laboratory.

## Roadmap
- Add locally validated soil-test interpretation for a selected region.
- Add a verified weather-data source.
- Consult agricultural scientists / extension officers before offering crop or nutrient recommendations.
- Test usability with farmers only after expert review and informed consent.
- Add multilingual support.

## Safety and limitations
Soil nutrient interpretation depends on units, extraction method, soil type, crop, region, season, and local recommendations. This prototype intentionally avoids prescribing fertilizer quantities or pesticides. Confirm all decisions with a qualified local agriculture expert or government agriculture extension service.

## License
MIT. See [LICENSE](LICENSE).
