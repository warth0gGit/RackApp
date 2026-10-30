---
slug: maths
name: Maths
maker: Make Noise
hp: 20
category: modulation
manual_url: https://www.makenoise-manuals.com/maths/maths-manual.pdf
product_url: https://www.makenoisemusic.com/modules/maths/
read_from: Official Make Noise MATHS PDF manual (current edition, linked from makenoisemusic.com; covers the 2013 revision) plus the official product page specs
---
# Maths

## Overview
Make Noise call MATHS "an analog computer designed for musical purposes". It has four channels:

- **Channels 1 and 4** are full **function generators**. Each one makes a rise-then-fall voltage when triggered, slews (lags) any voltage patched into it, or loops itself to become an LFO or oscillator. Their range runs from about **25 minutes per cycle** up to about **1 kHz**. Rise time, fall time and curve shape (Vari-Response) can all be set, and rise and fall can be voltage controlled.
- **Channels 2 and 3** are **attenuverters**. When nothing is patched, they output a DC offset: channel 2 is normalled to +10 V (±10 V offset) and channel 3 to +5 V (±5 V, finer control).
- **The SUM / INV / OR bus** combines all four channels. It gives a weighted sum, an inverted sum, and an analog OR (the highest positive voltage).

With these, MATHS can be an AD or ASR envelope, an ADSR (using two channels), an LFO, portamento, an envelope follower, a clock divider or delay, a comparator, a rectifier, a mixer, an offset generator and more. The current manual describes the 2013 revision. Today's MATHS is that design, so the "classic" MATHS is the older, different panel.

## Panel controls and jacks
**Channels 1 and 4 (function generators)**
- **Signal In** — DC-coupled, ±10 V. The voltage is slewed by the Rise and Fall settings, which gives lag or portamento. Send a gate here to get an ASR envelope that follows the gate's level. Anything patched here also reaches the bus.
- **Trigger In** — Starts a full 0→10 V rise-then-fall function, whatever the length of the incoming gate. It retriggers during the **fall** but not during the **rise**.
- **Rise knob** — Sets the rise time. Turning clockwise makes it longer.
- **Rise CV In** — Linear CV over the rise time, ±8 V. Positive CV lengthens it, negative shortens it.
- **Fall knob** — Sets the fall time. Turning clockwise makes it longer.
- **Fall CV In** — Linear CV over the fall time, ±8 V. Positive CV lengthens it, negative shortens it.
- **Both CV In** — Exponential CV over the whole cycle time, ±8 V. **Positive CV makes it shorter (faster)** and negative makes it longer. This is the input to use for "V/oct-ish" or FM control of a cycling channel.
- **Vari-Response knob** — Sets the curve. It goes from logarithmic through linear (the tick at the centre) to exponential and hyper-exponential. Changing the curve also changes the effective rise and fall times.
- **Cycle button + LED** — Latches the channel into self-oscillation (looping).
- **Cycle In** — A gate turns cycling on: high (at least +2.5 V) cycles, low stops. The button overrides it.
- **Unity Out + LED** — The channel's function at full level, ignoring the attenuverter. It is **not** sent to the bus. When cycling it runs 0 to about 8–10 V; otherwise it follows the input. The LED is green for positive and red for negative.
- **Attenuverter** — Scales or inverts the channel's signal before it goes to the Variable Out and the bus.
- **Variable Out** — The attenuverted signal, ±10 V. It is normalled into SUM/INV/OR. **Patching this jack removes the channel from the bus.**
- **EOR (channel 1 only) + LED** — End of Rise. It goes high (10 V) at the top of the rise and stays high through the fall. At rest it is 0 V.
- **EOC (channel 4 only) + LED** — End of Cycle. It goes high (10 V) at the end of the fall and stays high while the channel is idle. It is low while the channel rises and falls, and it is buffered.

**Channels 2 and 3 (attenuverters / offsets)**
- **Signal In** — DC-coupled, ±10 V. Channel 2 is normalled to +10 V and channel 3 to +5 V.
- **Attenuverter** — Scales, attenuates, amplifies or inverts the input. With nothing patched, it sets the offset: ±10 V on channel 2, ±5 V on channel 3.
- **Variable Out** — ±10 V, normalled to the bus. Patching it removes the channel from the bus.

**Bus section**
- **SUM Out** — The sum of the variable signals from all four channels, ±10 V. A green/red LED shows its polarity.
- **INV Out** — SUM inverted, ±10 V.
- **OR Out** — An analog maximum of the channels' positive voltages, 0 to 10 V. It ignores negative voltages.

## Modes, menus and settings
MATHS has no menus. Its "modes" depend on what you patch and which buttons are on:
- **One-shot function (AD)** — Trigger into Trigger In.
- **Slew, lag or portamento** — Voltage into Signal In.
- **ASR envelope** — Gate into Signal In.
- **LFO or oscillator** — Press Cycle or send a high gate to Cycle In. Rise and Fall set the rate and shape (for example, a short rise and a long fall give a saw).
- **Curve** — Vari-Response: log, linear or exponential.
- **Bus use** — Patched Variable Outs drop out of the bus. Unpatched ones (including the ch2/ch3 offsets) are always being summed.
- **Retrigger rule** — A trigger is ignored during the rise and accepted during the fall. This is what makes clock division possible.

## How to (common procedures)
1. **AD envelope:** Patch a gate or trigger into ch1 or ch4 Trigger In. Set the attack with Rise, the decay with Fall and the curve with Vari-Response. Take the output from Unity Out or Variable Out.
2. **ASR envelope:** Patch the gate into ch1 or ch4 Signal In. The output rises at the Rise rate, holds at the gate level while the gate is high, then falls at the Fall rate.
3. **Portamento:** Patch the pitch CV (for example from a keyboard) into ch1 Signal In and take the output from Unity Out. Turn Rise and Fall up a little. Log curves give the "East Coast" glide feel.
4. **LFO:** Press Cycle on ch1 or ch4. Rise and Fall at noon with a linear curve gives a triangle. Rise fully anticlockwise gives a saw/ramp. Send a gate to Cycle In for remote run/stop.
5. **Voltage-controlled LFO rate:** Set the cycling channel. Patch SUM (with ch2 as an offset) or an external CV into Both CV In. Positive voltage speeds it up.
6. **Clock divider:** Patch a clock into ch1 or ch4 Trigger In. Rise sets the division (a longer rise ignores more clocks). Fall sets the pulse width. Take the output from EOR (ch1) or EOC (ch4).
7. **Pulse delay:** Patch a trigger into ch1 Trigger In. Rise sets the delay time and Fall sets the width. Take the output from EOR.
8. **ADSR from two channels:**
   1. Patch the gate into ch1 Signal In and set ch1's attenuverter below full (this sets the sustain level).
   2. Patch ch1 EOR into ch4 Trigger In and set ch4's attenuverter fully clockwise.
   3. Take the output from OR, with ch2 and ch3 at noon.
   4. Rise on ch1 and ch4 sets the attack. ch4 Fall sets the decay. ch1 Fall sets the release.
9. **Envelope follower:** Patch audio into ch1 or ch4 Signal In. Set Rise around noon and adjust Fall. Take a positive-only output from OR.
10. **Offsets and mixing:** Leave ch2 or ch3 empty and use them as ±10 V or ±5 V offsets. Patch signals into ch1–ch4 Signal Ins and take the mix from SUM (or INV for the mirrored version).
11. **Voltage mirror (invert around a point):** Patch the CV into ch2 with its attenuverter fully anticlockwise. Leave ch3 empty with its attenuverter fully clockwise. Take the output from SUM.
12. **Rectifier:**
    - Half-wave: patch a bipolar signal into any channel and take OR.
    - Full-wave: mult the signal into ch2 and ch3, set ch2 fully clockwise and ch3 fully anticlockwise, and take OR.
13. **Comparator / gate extractor:**
    1. Patch the signal into ch2 and set ch3 negative (this is the threshold).
    2. Patch SUM into ch1 Signal In, with ch1 Rise and Fall at minimum.
    3. Take the gate from EOR. Turn ch3 to move the threshold.
14. **281-style quadrature LFOs:** Cycle both channels. Patch ch1 EOR into ch4 Trigger and ch4 EOC into ch1 Trigger. Take the two LFOs from Unity Outs 1 and 4.
15. **Bouncing ball:**
    1. Set ch1 Rise fully anticlockwise and Fall to 3:00, linear. Set ch4 Rise fully anticlockwise and Fall to 11:00, linear.
    2. Patch ch1 EOR into ch4 Cycle In, and ch1 Variable Out into ch4 Fall CV.
    3. Patch ch4's output into a VCA or LPG.
    4. Fire it with a gate into ch1 Trigger.
16. **Flip-flop / logic NOT:**
    - Flip-flop: set into ch1 Trigger, reset into ch1 Both. Set ch1 Rise to minimum and Fall to maximum. Take Q from EOC (it holds for about 3 minutes).
    - NOT: patch a logic gate into ch4 Signal In and take the inverted gate from EOC.

## Specifications
- **Width** — 20 HP.
- **Depth** — 32 mm maximum, including the power cable (product page).
- **Power** — 60 mA at +12 V, 50 mA at −12 V.
- **Time range** — About 25 minutes per cycle (slowest, with CV) up to about 1 kHz.
- **Signal inputs** — ±10 V.
- **CV inputs** — ±8 V.
- **Outputs** — Variable Outs and SUM/INV ±10 V. OR 0–10 V. EOR/EOC 0/10 V. Unity outs up to about 8–10 V.
- **Offsets** — ch2 ±10 V, ch3 ±5 V.
- **Ribbon cable** — Red stripe to −12 V. Reverse-power protected (2013 revision).

## Tips and gotchas
- **Park unused ch2 and ch3 at noon.** Their unpatched offsets are always fed into SUM and OR, so if they are off-centre, every bus output gets a DC shift. A dummy cable in their input also removes them.
- **Patching a Variable Out removes that channel from SUM/INV/OR.** To use the bus and still have an individual output, use the Unity Outs on ch1 and ch4.
- **Both CV is reversed compared with Rise and Fall CV.** Positive CV makes Both faster, but makes Rise and Fall slower.
- **The rise ignores retriggers**, which is what lets MATHS divide clocks. To get a fully retriggerable envelope, keep Rise short.
- **Vari-Response changes timing as well as shape.** Re-check Rise and Fall after moving it.
- **OR ignores negative voltages.** Use SUM or INV for bipolar results.
- **Boost small signals.** To boost Pam's 0–5 V shapes, patch them into ch2 or ch3 and turn the attenuverter up past halfway. Channel 2 amplifies, and an offset can be added from the other channel.
- **Self-running clock.** Cycle ch4 and take EOC to a sequencer clock input.
- **Pluck-style envelopes.** Feeding ch1 into the 2LPG with a short rise, a medium fall and an exponential curve gives a classic pluck.
- **Self-patching.** Patching EOR/EOC into the other channel's Trigger, Signal or Cycle input, or feeding a Variable Out back into the channel's own Rise/Fall CV, gives complex, evolving contours.
