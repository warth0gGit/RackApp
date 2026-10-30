---
slug: ripples
name: Ripples (2020 edition)
maker: Mutable Instruments
hp: 8
category: filter
manual_url: https://pichenette.readthedocs.io/en/latest/modules/ripples_2020/manual/
product_url: https://pichenettes.github.io/mutable-instruments-documentation/modules/ripples/manual/
read_from: Official Mutable Instruments Ripples 2020 manual (pichenettes documentation, readthedocs mirror; the github.io page failed to load). Also read the original 2016 Ripples manual for comparison.
---
# Ripples (2020 edition)

## Overview
Ripples is an analog **voltage-controlled multimode filter with a built-in VCA**. The 2020 edition is a revised design of the original 2016 Ripples:
- **HP, BP and LP outputs**. The **BP and LP slope is switchable between 2-pole (12 dB/oct) and 4-pole (24 dB/oct)**.
- The filtering is done by a **quad VCA**. An **OTA in the resonance feedback path** puts resonance under voltage control and acts as a soft limiter, so self-oscillation stays clean.
- A **VCA on the LP output**, controlled by the LEVEL input, makes Ripples a complete back end for a subtractive voice (filter + amp).
- Two audio inputs: **IN 1 with a level control and soft clipping (drive)**, and **IN 2, clean**, voiced like the original Ripples. They are mixed together.
- The character is inspired by 1980s Japanese polysynths (the SH/Juno/Jupiter family): "liquid" resonance that does not thin out the bass.

## Panel controls and jacks
Letters and numbers follow the manual.
- **A. Frequency (cutoff)** — 20 Hz to 20 kHz.
- **B. Slope switch** — down = 2-pole (12 dB/oct), up = 4-pole (24 dB/oct). It affects the **BP and LP** outputs only.
- **C. Resonance** — self-oscillation starts at about **75%** of travel.
- **D. Input 1 level** — gain from 0 to ×5. At high gain, modular-level signals are soft-clipped for overdrive.
- **E. FM attenuverter** — amount and polarity of the FM CV input.
- **1. Audio inputs:**
  - **IN 1** — goes through the level control and soft clipper.
  - **IN 2** — always clean, at fixed gain, with the mkI character.
  - Both are mixed into the filter.
- **2. CV inputs:**
  - **FM** — cutoff modulation through the attenuverter.
  - **RES** — resonance CV, added to the knob.
  - **V/OCT** — cutoff with 1 V/oct tracking.
- **3. LEVEL (LP VCA input)** — 0 V = silent, +5 V = unity gain. Above +5 V the gain is progressively compressed. **Unpatched, it is normalled to +7 V**, so the LP output is fully open.
- **4. Outputs:**
  - **HP** — its slope varies with the resonance setting.
  - **BP** — slope set by switch B.
  - **LP** — slope set by switch B, and passes through the VCA (LEVEL).

## Modes, menus and settings
No menus. The only "mode" is the **2-pole/4-pole switch**:
- **2-pole (12 dB/oct)** — brighter and more open. The 2-pole BP is wider.
- **4-pole (24 dB/oct)** — classic, steeper low-pass. Clean sine when self-oscillating.

Self-oscillation: with Resonance above about 75% and no input, Ripples outputs a sine at the cutoff frequency. It tracks V/OCT over about 4 octaves once calibrated.

**Differences from the original (2016) Ripples**, from the old manual:
- The original had BP2, LP2, LP4 and LP4>VCA outputs, a single DC-coupled input, a GAIN CV input for the VCA, and self-oscillation at about 80% resonance.
- The 2020 version replaces these with HP/BP/LP outputs plus the slope switch, adds the IN 1 drive control and a second clean input, and normals LEVEL to +7 V.

## How to (common procedures)
1. **Classic subtractive voice (filter + VCA in one)**
   1. Oscillator (for example Dixie II+) → IN 2 for clean, or IN 1 for drive.
   2. Set switch B to 4-pole and take the LP output.
   3. Envelope → FM with the attenuverter clockwise, for filter sweeps.
   4. The same or a second envelope → **LEVEL**. The LP output is now enveloped, with no extra VCA needed.
2. **Drive / overdrive** — use IN 1 and turn up the Input 1 level until it soft-clips. Mix in a clean signal on IN 2 if wanted.
3. **Sine oscillator / filter ping**
   1. Remove the audio inputs and turn Resonance to maximum.
   2. Patch pitch CV into V/OCT and listen at LP (4-pole for the cleanest sine).
   3. For a "ping", keep Resonance just below self-oscillation and send short triggers into IN.
4. **Resonance as a modulation target** — patch an envelope or LFO into RES. Around +4 V (from the knob at zero) pushes it toward self-oscillation, and higher voltages are compressed.
5. **Calibrate V/OCT tracking**
   1. Set Frequency to about 10 o'clock and Resonance to maximum.
   2. Disconnect the audio and FM inputs.
   3. Feed V/OCT from a well-calibrated keyboard or MIDI-to-CV.
   4. Listen at LP and adjust the trimmer on the side of the board until intervals are correct. An octave must sound like an octave. Absolute pitch doesn't matter.

## Specifications
- Width: 8 HP
- Power: ±12 V via 2×5 header, about 35 mA on each rail (the red stripe goes to −12 V, matching the "Red stripe" mark)
- Cutoff range: 20 Hz–20 kHz
- Slopes: HP (varies with resonance); BP and LP switchable 2-pole/4-pole
- Self-oscillation: from about 75% resonance; tracks V/OCT over about 4 octaves
- IN 1 gain: 0 to ×5 with soft clipping; IN 2: clean, fixed gain
- VCA (LEVEL): 0 V = off, 5 V = unity, normalled to 7 V
- Not temperature-compensated

## Tips and gotchas
- **LEVEL only affects the LP output.** HP and BP are never enveloped by the VCA.
- **With nothing in LEVEL, the LP output is fully open** (normalled to 7 V, slightly above unity). Once you patch an envelope, silence between notes is expected.
- **Resonance doesn't thin the bass** as much as many 4-pole ladders, so the low end stays full.
- **Tracking drifts with temperature.** Recheck it in a warm case before relying on it as an oscillator.
- **The HP slope changes with resonance.** Expect a different sound than you would get from a fixed 12 or 24 dB/oct HP.
