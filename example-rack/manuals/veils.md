---
slug: veils
name: Veils (2020)
maker: Mutable Instruments
hp: 10
category: vca
manual_url: https://pichenettes.github.io/mutable-instruments-documentation/modules/veils_2020/manual/
product_url: https://pichenettes.github.io/mutable-instruments-documentation/modules/veils_2020/
read_from: Official Mutable Instruments Veils 2020 manual and index page (readthedocs mirror of the pichenettes.github.io docs), official quickstart PDF, plus designer (pichenettes) answers on the official MI forum
---
# Veils (2020)

## Overview
Veils is a **quad VCA**: four identical voltage-controlled amplifiers. This file covers the 2020 redesign, which was made from October 2020 to December 2022. Compared with the original, it is a narrower 10 HP, it uses **sliders** for the main CV-amount/gain control, it adds a gain-indicator LED, and it adds a **positive offset** knob (0 to +8 V) on each channel.

Each channel has three controls:
- A **response** knob, which morphs from exponential to linear.
- An **offset** knob.
- A **CV-amount slider**.

All signal inputs are DC-coupled. They pass audio or CV, so a Veils channel can shape an envelope's amplitude, scale modulation depth, set FM depth, or mix oscillators.

The outputs **daisy-chain**: an unpatched output sums into the next channel. That makes Veils a 2-, 3- or 4-channel mixer as well.

The gain law is: **output = input × (CV × slider amount + offset)**. Here +5 V of effective control gives unity gain (0 dB) in both linear and exponential response. In exponential response, gain can go well above unity: more than +20 dB per the product page, up to about +30 dB per the quickstart, and over 100× with a large offset. That is enough to boost line-level signals, or to clip deliberately.

## Panel controls and jacks
Per channel (×4):
- **A. Response knob** — Continuously variable from exponential (one end) to linear (the other). Exponential gives snappier envelopes and much more maximum gain. Linear is more even.
- **B. Offset knob** — Adds 0 to +8 V to the **gain CV**, not to the audio. It raises the "resting" gain, so a bipolar LFO in the CV input produces tremolo around a level instead of silence on its negative half.
- **C. Gain CV amount slider** — Sets how much the CV input moves the gain. With no cable in the CV input, the slider is a manual gain/level control, because the input is normalled to +8 V.
- **1. Gain LED** — Brightness follows the VCA's gain on a dB scale. Off means muted.
- **2. Gain CV input** — The CV that controls the gain, normalled to a constant **+8 V**. At full slider, +5 V gives unity, and more than +5 V at full slider can distort.
- **3. Signal input** — DC-coupled audio or CV, 100 kΩ impedance.
- **4. Output LED** — Brightness shows the output level and colour shows the polarity (green = positive).
- **5. Signal output** — The VCA output. **If unpatched, its signal is added into the next channel's output.**

## Modes, menus and settings
There are no menus or digital settings. Behaviour depends only on the knobs, sliders and patching:
- **Response** — Exponential, linear, or anywhere in between, per channel.
- **Manual gain mode** — No cable in the CV input. The slider sets the gain against the +8 V normal: about 1.6× (8/5) at full slider, and roughly unity a little past the halfway point. The response knob still shapes the slider's taper.
- **CV mode** — A cable in the CV input. The slider attenuates the CV and the offset adds a fixed gain.
- **Mixing (daisy chain)**:
  - With outputs 1–3 unpatched, output 4 carries the sum of channels 1–4.
  - Patching an output ends the chain at that channel, so you can split the four channels into groups, for example 1+2 out of jack 2 and 3+4 out of jack 4.

## How to (common procedures)
1. **Shape a voice with an envelope:** Patch the oscillator or filter into Signal In and the envelope into CV In. Set the slider to full and the offset to zero. Use the response knob to choose a snappy (exponential) or smooth (linear) feel. Take the output from the channel's output.
2. **Use it as a manual mixer:** Patch up to four sources into the four Signal Ins, with no CV cables. Leave outputs 1–3 empty and take the mix from output 4. Set each level with its slider.
3. **Tremolo:** Patch audio into Signal In and an LFO into CV In. Raise the offset so the gain never drops to zero, and use the slider for depth.
4. **Scale modulation depth:** Patch a modulation source (for example a random CV or an LFO) into Signal In, and a second CV or the slider alone into CV. The output is the modulation at the chosen depth. Feed it to filter cutoff, FM amount and so on.
5. **Boost small CVs such as Pam's 0–5 V shapes:** Patch the signal into Signal In and turn the response knob towards exponential. Raise the offset and/or patch a CV so the gain goes above unity. Watch for clipping.
6. **Turn a bipolar LFO into unipolar modulation (designer's workaround):**
   1. Patch a constant voltage (for example +5 V from a 3xMIA offset or Maths ch3) into **Signal In**.
   2. Patch the ±5 V LFO into **CV In**.
   3. Use the slider for depth, the offset for base level, and the response knob to reshape the curve.
   The output is effectively half-wave rectified: the negative half of the LFO clamps at the offset level.
7. **Envelope-controlled FM depth:** Patch the modulator oscillator into Signal In and the envelope into CV. Patch the output into the carrier's linear FM input.

## Specifications
- **Width** — 10 HP.
- **Depth** — 25 mm.
- **Power** — About 50 mA at +12 V and 50 mA at −12 V, typical. Up to about 70 mA per rail depending on LED brightness and colour. 2×5-pin connector, red stripe to −12 V.
- **Inputs** — DC-coupled, 100 kΩ, audio-rate capable.
- **Gain** — +5 V CV at full slider gives unity (0 dB) in both linear and exponential response. Exponential reaches more than +20 dB (the quickstart says up to +30 dB).
- **Offset** — 0 to +8 V added to the gain CV.
- **CV normal** — +8 V.
- **Production** — October 2020 to December 2022.

## Tips and gotchas
- **The offset shifts the gain, not the signal.** Turning it up makes the output louder, not DC-shifted. To DC-shift a signal, use a mixer or offset module such as the 3xMIA or Maths ch2/ch3 instead.
- **Daisy-chain surprise.** If you hear a channel you didn't expect, check that the previous channel's output jack is empty. An empty output feeds the next channel. Patch a dummy cable to stop it.
- **The exponential setting plus offset can give huge gains** and clip hard. That's great for distortion, but bad if you want a clean signal path. Back off the response or offset if the output LED is saturated.
- **With nothing in CV, full slider is 1.6× gain**, not unity. For clean unity on manual use, set the slider a bit past halfway.
- **Very small CVs at full slider may never open the VCA fully.** Use the exponential response, or add offset, to get more range.
- **The Gain LED is a quick way to see envelope activity** without a scope.
- **Typical uses:**
  - The final amplitude stage for an oscillator voice.
  - Making small 0–5 V modulation shapes bigger.
  - Scaling modulation.
  - Audio-rate CV for AM.
  - A 4-into-1 mixer.
