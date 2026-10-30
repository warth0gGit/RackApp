---
slug: dixie-ii-plus
name: Dixie II+
maker: Intellijel
hp: 8
category: oscillator
manual_url: https://intellijel.com/downloads/manuals/dixie-2-plus_manual_2021.08.01.pdf
product_url: https://intellijel.com/shop/eurorack/dixie-2-plus/
read_from: Official PDF manual (revision 2021.08.01) plus the official Intellijel product page
---
# Dixie II+

## Overview
Dixie II+ (written Dixie²+ by Intellijel) is an 8HP, fully analog **triangle-core VCO** that doubles as an **LFO**. It is the larger, more featured version of the 4HP Dixie II. It keeps the same core and adds:
- an 8-position octave switch
- a pulse-width knob with PWM input and attenuator
- an exponential/linear switch on FM1
- an improved FLIP sync circuit

It has six simultaneous outputs: sine, triangle, zig-zag, saw, pulse and a sub-octave square. A triangle core means it starts from a triangle wave and shapes the other waveforms from it. It tracks well, and the core lends itself to through-zero-style "flip" sync, which reverses direction rather than resetting.

In VCO mode it runs from about 20 Hz to almost 60 kHz. In LFO mode it runs from cycles several minutes long up to around 1 kHz. The module has no firmware; everything is analog.

## Panel controls and jacks
**Controls**
- **OCTAVE switch (8 positions)** — coarse tuning, one octave per click.
- **FINE knob** — about ±6 semitones in VCO mode. In LFO mode it becomes a wide-range rate control, about ±7 octaves. With FINE turned up and OCTAVE high, LFO mode can hit its upper limit.
- **VCO/LFO switch** — VCO: about 20 Hz to almost 60 kHz. LFO: several minutes per cycle up to about 1 kHz.
- **EXP/LIN switch** — sets FM1's response to exponential (musical, pitch-like) or linear (classic FM timbres, stays more in tune at depth).
- **FM1 attenuator** — sets the depth of the FM 1 input.
- **PWM attenuator** — sets the depth of the PWM input.
- **PULSE WIDTH knob** — manual pulse width: fully CCW ≈ 10% duty, noon = square (50%), fully CW ≈ 90%. Summed with the PWM CV.

**Inputs**
- **1V/OCT** — main pitch input (or LFO rate).
- **FM 1** — FM input, exponential or linear per the switch, through the FM1 attenuator.
- **FM 2** — exponential FM input. No attenuator, so it is full depth.
- **PWM** — pulse-width CV, ±5V range, through the PWM attenuator and summed with the PULSE WIDTH knob. Width can reach 0% or 100%, where the pulse disappears (no output).
- **SYNC** — hard sync: when the incoming waveform crosses zero, the core is reset to zero.
- **FLIP** — "flip" (reversing) sync: at each zero crossing of the incoming signal, the core reverses direction instead of resetting. This is a softer, often more musical sync.

**Outputs**
- **SINE** — sine shaped from the triangle core.
- **TRIANGLE** — the raw core waveform.
- **ZIG-ZAG** — a distinctive extra waveform derived from the core. The manual lists it without describing its shape, so listen or scope it (DATA) to see it.
- **SAW** — sawtooth.
- **PULSE** — pulse with width from PULSE WIDTH + PWM.
- **SUB** — 50% square one octave below the main oscillator.

## Modes, menus and settings
There are no menus. The modes are set with switches:
- **VCO/LFO** — range switch.
- **EXP/LIN** — FM1 response.
- **OCTAVE** — coarse range in both modes.

Sync behaviour depends on which jack you use (SYNC = reset, FLIP = reverse). Both can be patched at once for complex results.

## How to (common procedures)
**Tune as a VCO**
1. Set VCO/LFO to VCO.
2. Patch your pitch CV (from a sequencer or keyboard) into 1V/OCT and send its "C" (for example 0V).
3. Pick the octave with OCTAVE, then trim with FINE against a tuner.
4. Check an octave higher to confirm tracking.

**Use as an LFO**
1. Set VCO/LFO to LFO.
2. Use OCTAVE for the general range and FINE for rate (FINE is now ±7 octaves).
3. Take sine or triangle for smooth modulation, saw for ramps, pulse for square LFO with variable duty, sub for half-rate square.
4. CV the rate via 1V/OCT or FM.

**Hard sync sweep**
1. Patch a master oscillator (a second VCO) into SYNC.
2. Tune Dixie higher than the master.
3. Modulate Dixie's pitch (FM 2 or FM 1 + EXP) with an envelope for the classic tearing sync sweep. Use FLIP instead of SYNC for a smoother, less harsh variant.

**Linear FM timbres**
1. Set EXP/LIN to LIN.
2. Patch an audio-rate modulator into FM 1 and raise the FM1 attenuator.
3. Linear FM keeps the perceived pitch more stable as depth changes, compared with exponential FM.

**PWM**
1. Set PULSE WIDTH near noon.
2. Patch an LFO (any LFO) into PWM and raise the PWM attenuator.
3. Keep the depth below the point where the width hits 0% or 100%, where the pulse drops out.

## Specifications
- Width: 8HP
- Depth: 40 mm maximum (the product page lists 38 mm)
- Current: 60 mA on +12V, 70 mA on −12V (from the manual; the product page lists the rails the other way round). No +5V.
- VCO range about 20 Hz to almost 60 kHz; LFO range several minutes per cycle to about 1 kHz
- FINE ±6 semitones (VCO), ±7 octaves (LFO)
- Pulse width 10–90% manual; PWM CV ±5V
- Outputs: sine, triangle, zig-zag, saw, pulse, sub (−1 oct square)
- No firmware; fully analog

## Tips and gotchas
- **Pulse vanishes?** The PULSE WIDTH knob plus PWM CV has pushed the width to 0% or 100%. Reduce the PWM attenuator or recentre the knob.
- **FM 2 has no attenuator** — attenuate the source first (Veils, Maths, a mixer) or use FM 1.
- **EXP vs LIN on FM 1:** EXP is for vibrato and pitch modulation; LIN is for clangy, harmonic FM. With LIN, small depths still sound musical.
- **FLIP vs SYNC:** FLIP keeps the slope continuous (reversal), so it sounds smoother and less buzzy than hard reset. Both need an audio-rate or clock-like source with zero crossings.
- **LFO range limit:** in LFO mode, high OCTAVE + high FINE can max out the LFO. Lower one of them.
- The manual doesn't publish output levels or a calibration procedure. Treat outputs as roughly standard Eurorack audio levels (about 10 Vpp) and check with a scope (DATA) if exact levels matter.
- Being analog, give it a few minutes to warm up before fine tuning.
