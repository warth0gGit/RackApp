---
slug: pams-new-workout
name: Pamela's NEW Workout (ALM017)
maker: ALM Busy Circuits
hp: 8
category: clock
manual_url: https://assets.busycircuits.com/docs/alm017-manual.pdf
product_url: https://busycircuits.com/pages/alm017
read_from: Official ALM017 PDF manual v0.7 (firmware 206) plus the official busycircuits.com product page
---
# Pamela's NEW Workout (ALM017)

## Overview
Pamela's NEW Workout ("Pam's") is a programmable, BPM-based master clock and modulation source. It has eight outputs, and each one runs off the master tempo with its own clock ratio, waveform, timing offsets and rhythm settings. Any output can be a plain clock (gate), a synced LFO (triangle, sine), an envelope, or a random/smooth-random voltage. It is the successor to the original Pamela's Workout, with an OLED display, new hardware and rewritten firmware. ALM has since **discontinued** it in favour of Pamela's PRO Workout (ALM034), but firmware is still available. The product page lists **firmware 207** as current. The manual read here is v0.7, written for firmware 206.

Everything is edited from one push-encoder (the "program knob") and the OLED, plus a Start/Stop button. Settings are saved automatically and come back after a power cycle. Up to 26 banks of 8 output slots hold saved setups.

Optional rear expanders add extra fixed outputs. Only one can be fitted at a time. Pexp-1 adds DIN Sync, MIDI DIN and four fixed gates. Pexp-2/Px2 adds a 3.5 mm MIDI clock out, a x24 clock and a Run out (see the separate `pexp-2` file).

## Panel controls and jacks
- **Program knob (blue encoder with push)** — Turn it to scroll or change values. A short push selects or deselects the highlighted item. A long press (just over 1 s) opens extended menus and sub-menus, and a second long press backs out.
- **Start/Stop button** — Starts the internal clock. Pressing it again stops and resets it. It also works as part of the quick-mute shortcut (long-press the knob, then press Start/Stop; firmware 189+).
- **OLED display** — Shows BPM, per-output screens and parameter lists.
- **Outputs 1–8** — 0 to +5 V, buffered, low impedance, 10-bit, updated at up to 500 Hz. Each has a green LED that shows its level.
- **Clk input** — External clock input. It responds to rising edges of at least 0.7 V and accepts 1–48 PPQN.
- **Run input** — Gate/trigger input, rising edge, 0.7 V minimum. By default it starts and stops the clock, DIN-Sync style. It can be reassigned to Reset, bank-sequencing or rotation actions.
- **CV 1 input** — 0 to +5 V (positive only). It can be assigned to any output parameter.
- **CV 2 input** — −5 to +5 V (bipolar). It can be assigned to any output parameter.
- **Mini USB (side)** — For firmware updates only. Use it with Eurorack power disconnected.
- **5-pin expander header (rear)** — For Pexp-1 or Pexp-2/Px2, using the supplied cable. Line up the "<" and "o" markings.

## Modes, menus and settings
**BPM (home) screen**
- Push, then twist, to set the tempo from 10 to 300 BPM.
- Twisting without pushing steps through the output screens 1–8 and back to BPM.
- A long press on the BPM screen opens the external-clock sub-menu (PPQN, Run? setting, detected BPM, stability warning) and the "All outputs" screens (save, load or reset all 8 outputs to or from a bank).

**Output screens (1–8)**
- **Modifier (ratio)** — Push to highlight it, twist to change it, push again to leave. Choose a multiplier (x) or divider (/) from /512 to x48, including non-integer triplet and dotted values. There are also utility types with no extended parameters: constant on, constant off, a single pulse at start, and a single pulse at stop.
- Long-press (about 1 s) on an output to open its **extended parameters**:
  1. **Wave** — Gate, Triangle, Sine, Envelope, Random, Smooth Random.
  2. **Level** — 0–100% of 5 V.
  3. **Offset** — 0–100% of 5 V, added to the wave and clipped at 5 V (firmware 189+).
  4. **Width** — What it does depends on the wave:
     - Gate: duty cycle.
     - Triangle and sine: skew (50% gives a true triangle, 100% a saw).
     - Envelope: release time as a percentage of the step.
     - Random: no effect.
     - Smooth random: peak shape (0% sharp, 100% rounded).
  5. **Phase** — Where in the waveform the output starts (for example 25% or 50%). Use it to offset LFOs against each other.
  6. **Delay** — Delays the waveform start by 0–100% of a step. It only acts on the steps chosen by Dly/.
  7. **Dly /** — Which steps get delayed. 1 = every step, 2 = every other step (classic swing), 3 = every third, and so on.
  8. **Slop** — 0–100% chance of small timing errors, to humanise.
  9. **EStep** — Euclidean pattern length in steps.
  10. **ETrig** — Euclidean hits. Must be lower than EStep.
  11. **ERot** — Rotates the Euclidean pattern by a number of steps.
  12. **RSkip** — 0–100% chance that a step is skipped.
  13. **Loop** — Number of beats (not steps) before the output resets. It loops the random wave, RSkip and Euclidean timing so "random" becomes repeatable. Setting it to 0 re-seeds the randomness, and the seed is saved.
  14. **Quant** — Quantises output levels to 1 V/oct scales over 5 octaves (firmware 204+). Options: NO, MA (major), mi (minor), Hm (harmonic minor), PM (pentatonic major), Pm (pentatonic minor), Ly (Lydian), Ph (Phrygian), Jp (Japanese), P5 (root + fifth), C1 (I chord), C4 (IV chord), C5 (chord), Ch (chromatic). While quantised, empty steps hold the last value instead of dropping to 0 V.
  15. **Logic** — Combines this output with another channel (firmware 205+). Options: NO, & (AND), + (OR), ^ (XOR), followed by the other channel's number.
  16. **Mute** — Mutes the output. You can still edit it while muted.
  17. **Save / Load / Reset** — Per-output bank operations.

**CV assignment**
- Most parameters, including the modifier, list CV1 and CV2 as options in their value list.
- With CV1 or CV2 highlighted, push and hold to open the CV edit page. It has attenuation (negative values invert), offset, and a live monitor of the incoming CV.
- One CV input can drive several parameters at once. Out-of-range values are clamped safely.

**Run input options** (set in the external-clock sub-menu)
- **Default** — External start/stop.
- **RS** — Reset all outputs.
- **LD** — Load the next or previous sequenced bank. CV1 below about 2 V steps forward (a→b), above about 2 V steps back.
- **RA / RR** — Rotate the output settings. RA rotates all 8 outputs, RR the top row only. CV1 low rotates anticlockwise, high rotates clockwise.
- **LC** — Load the bank chosen by the CV1 voltage. Limited to the first 16 slots (banks A and B).
- When Run is set to anything other than start/stop, Pam's works out run state from whether a clock is arriving on Clk.

**External clock sub-menu**
- **PPQN** — 1 to 48. Can also be set to "CV", where CV1 sets the tempo.
- **Run?** — Y = the Run input starts and stops the clock. Otherwise the clock starts automatically when pulses are detected.
- **Readout** — Shows the detected external BPM and warns when the incoming clock is unstable.

## How to (common procedures)
1. **Set the tempo:** On the BPM screen, push the knob, twist to the BPM you want, then push again.
2. **Make an output a clock divider:** Twist to the output's screen, push to highlight the ratio, twist to (for example) /4, then push to confirm.
3. **Turn an output into a synced LFO:** On that output, long-press to open the extended list. Select Wave and pick Triangle or Sine. Use Width for skew and Phase for offset. Set the ratio to something slow, such as /16. Long-press to exit.
4. **Make a Euclidean rhythm:** On a gate output, open the extended list. Set EStep (for example 8), ETrig (for example 3) and ERot to rotate it.
5. **Make repeating random melodies:** Set Wave to Random, set Quant to a scale, and set Loop to a number of beats (for example 8). Change Loop to 0 and back to re-seed.
6. **Add swing:** Set Delay (for example 10–20%) and set Dly/ to 2.
7. **Assign CV:** Open the parameter, scroll its value to CV1 or CV2, push and hold, then set attenuation and offset while watching the monitor.
8. **Save an output:** In the extended list, go to Save, push, scroll to a bank and slot, then push to confirm (or pick NO to abort). Load works the same way. Reset returns the output to defaults.
9. **Save or load all 8 outputs:** Long-press on the BPM screen, open the All outputs screens, and choose save, load or reset for a bank.
10. **Slave to an external clock:** Patch the clock into Clk and the run gate into Run. Set PPQN to match the source (24 is ideal). Check the detected BPM readout.
11. **Quick mute:** Long-press the knob on an output, then press Start/Stop.
12. **Service mode and calibration:** Hold the knob while powering on. From there you can calibrate the internal clock (default 50; lower runs faster, higher runs slower), clear saved outputs, test the OLED, or check the firmware version. Press Start to exit. Hardware rev 063 and later has no clock calibration (it is fixed at 0). The revision number is printed on the rear PCB.
13. **Firmware update:**
    1. Take the module out of the case and disconnect Eurorack power.
    2. Connect only mini USB to the computer.
    3. Install dfu-util (Homebrew or the GUI installer on macOS, your package manager on Linux, dfu-util 0.8 plus the Zadig WinUSB driver on Windows).
    4. Run `dfu-util -a 0 -d 0x0483:0xdf11 --dfuse-address 0x08000000 -D <firmware.bin>`. The screen stays blank during the update, which takes a few seconds.
    5. Disconnect USB and refit the module.
    Updating probably wipes saved outputs. Use only official firmware from assets.busycircuits.com/firmware/alm017/ that matches your hardware revision.

## Specifications
- **Width** — 8 HP.
- **Depth** — The manual says 22 mm including the power header. The product page says 32 mm.
- **Power** — +12 V 50 mA max. −12 V draw is about 0.5 mA in the manual and 5 mA on the product page. Expanders add more: Pexp-1 +25 mA, Px2 15 mA.
- **Tempo** — 10–300 BPM.
- **Ratios** — /512 to x48, including non-integer values.
- **Outputs** — 8 × 0–5 V, 10-bit, 500 Hz maximum update rate.
- **CV inputs** — CV1 0 to +5 V, CV2 ±5 V.
- **Clk and Run inputs** — Rising edge, 0.7 V minimum. External sync accepts 1–48 PPQN.
- **Storage** — 26 banks (a–z) × 8 slots. The product page describes this as "200 banks"/configs.
- **Other** — Reverse-power protected, skiff friendly, made in England.

## Tips and gotchas
- Outputs only reach 5 V. Modules that expect 8–10 V envelopes or LFOs need the signal boosted, for example with Veils (exponential response) or Maths channel 2/3.
- Pam's is very stable, so make it the master clock where you can. It cannot clean up a sloppy external clock.
- When slaving, use the highest PPQN the source offers (24 is recommended) and use the Run input for start/stop. If the BPM reads 10 while slaved, the PPQN setting is probably too high.
- Avoid syncing to USB MIDI clock from a computer, because it is often jittery. Make Pam's the master and send MIDI clock to the DAW via a Pexp-2/Px2.
- Saving or loading while the clock runs can cause timing glitches.
- For DIN Sync, use an adapter cable (ALM-UT001) or the ALM D.S.G. As a DIN Sync master, set one output to x24 (the clock) and another to constant-on (the start/stop line). The Pexp-1 has a direct DIN Sync socket.
- Logic example from the manual: set Out 1 to x4, Out 2 to /3, and Out 1's Logic to &2. Out 1 then passes its fast clock only while Out 2 is high, which gives bursts.
- Only one expander can be fitted at a time. Expanders for this module do not work with Pam's PRO, and the reverse is also true.
