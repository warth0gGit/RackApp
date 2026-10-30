---
slug: beads
name: Beads
maker: Mutable Instruments
hp: 14
category: effect
manual_url: https://pichenettes.github.io/mutable-instruments-documentation/modules/beads/manual/
product_url: https://pichenettes.github.io/mutable-instruments-documentation/modules/beads/
read_from: Official Mutable Instruments online manual (archived docs site by Émilie Gillet); panel width from Mutable's published spec (14HP), not stated in the manual text
---
# Beads

## Overview
Beads is Mutable Instruments' granular texture synthesizer, the successor to Clouds. Incoming mono or stereo audio is recorded continuously into a buffer. **Grains** — short snippets with an envelope — are played back from that buffer. Each grain's position, length, pitch and envelope come from four main controls (TIME, SIZE, PITCH, SHAPE), each with its own **attenurandomizer**.

Grains can be generated in three ways:
- **Latched**: free-running at a rate set by DENSITY.
- **Clocked**: from a clock at SEED, with DENSITY as divider or probability.
- **Gated/triggered**: on SEED button or gate.

Beads also has:
- A **delay/beat-slicer mode** (SIZE fully clockwise).
- A built-in **feedback** path, a **reverb**, and a **dry/wet** control.
- **Auto-gain** on the input.
- Four recording **quality** settings with different sonic character.
- A **wavetable synth mode** that starts automatically when nothing is patched to the inputs.

## Panel controls and jacks
**Buttons**
- **[A] Quality button** — cycles the four recording-quality settings. Long press (1 s) restarts auto-gain. Hold it while turning FEEDBACK [J] to set the input gain manually.
- **[B] FREEZE** (latching, illuminated) — stops recording into the buffer, so grains keep playing from the frozen contents. Holding it for more than 10 s saves the buffer, which is restored at the next power-on.
- **[C] SEED** — short press: switch to gated/triggered mode (and play grains while held). Hold for 4 s, or press FREEZE while holding SEED: back to latched mode (the default at power-on).
- **[M] CV assign button** — chooses which of FEEDBACK, DRY/WET or REVERB the assignable CV input controls. Hold M and turn J/K/L to set the CV amount for each. Hold M + press SEED to toggle the R output carrying a grain trigger.

**Main knobs**
- **[D] DENSITY** — latched: rate of grains (12 o'clock = none; CW = increasingly random timing; CCW = increasingly regular timing). Clocked: CW = probability 0–100%, CCW = clock divider 1/16 to 1. Delay mode: delay time or subdivision.
- **[E] TIME** — where in the buffer grains start: CCW = most recent audio, CW = oldest.
- **[F] PITCH** — −24 to +24 semitones, with virtual notches at semitones.
- **[G] SIZE** — grain length. About 30 ms near 11 o'clock. Clockwise grows up to 4 s forward; counter-clockwise from there gives reversed grains up to 4 s. Fully CW (∞) = delay / slicing mode.
- **[H] SHAPE** — grain envelope: CCW = rectangular and clicky; CW = slow attack. Independent of direction.

**Attenurandomizers [I]** (one each for TIME, SIZE, SHAPE, PITCH)
- With CV patched into that parameter's CV input: clockwise = CV amount; counter-clockwise = CV controls the amount of randomization.
- With nothing patched: sets the amount of internal randomness, moving from a "peaky" to a uniform distribution as you turn.

**Secondary knobs**
- **[J] FEEDBACK** — feeds output back to the input. The limiter behaviour depends on the quality mode.
- **[K] DRY/WET** — balance of input against grains.
- **[L] REVERB** — amount of built-in reverb.

**Jacks**
- **IN L / IN R** — audio inputs. Patch one for mono, both for stereo. Auto-gain adds +0 to +32 dB.
- **Input level LED** — blinks while auto-gain is measuring.
- **FREEZE gate input** — recording stops while the gate is high.
- **SEED input** — trigger, gate or clock. Fires grains, sets tempo in delay mode, or acts as a clock.
- **DENSITY CV input** — modulates grain rate; at audio rate it is 1V/oct exponential FM of the grain clock.
- **TIME / SIZE / SHAPE / PITCH CV inputs** — each works through its attenurandomizer. PITCH is 1V/oct (always so in wavetable mode).
- **Assignable CV input** — goes to FEEDBACK, DRY/WET or REVERB, as chosen with [M]. LEDs under those knobs show the target.
- **OUT L / OUT R** — stereo output. If R is unpatched, L carries a mono sum. R can be reassigned to a grain-trigger output (M + SEED).

## Modes, menus and settings

### Recording quality ([A])
Four settings from clean to characterful. The named ones are:
- **Cold digital** — closest to the sonic character of the late Clouds.
- **Sunny tape** — the dry signal runs at a bright, clean 48 kHz.
- **Scorched cassette** — adds wow and flutter.
The fourth setting, and each mode's exact sample rate, bit depth and buffer length, are given in a table image on the manual page that could not be read here. Check the manual's quality table for buffer lengths. Quality also changes how the feedback is limited.

### Grain generation modes
| Mode | How to enter | DENSITY does |
|---|---|---|
| Latched (default) | Hold SEED 4 s, or FREEZE while holding SEED | Grain rate: noon = none, CW = random timing, CCW = regular |
| Clocked | Patch a clock into SEED | CW = probability, CCW = divider |
| Gated/triggered | Short press SEED | Grains play while SEED or the gate is high; at noon, exactly one grain per trigger |

Grain parameters are sampled when each grain starts, so knob moves affect only new grains. Randomized grains also get random stereo pan.

### Delay / slicing mode (SIZE fully CW, ∞)
- **Base time**: set by DENSITY (noon = the full buffer length) or by tapping or clocking SEED. CCW gives only binary subdivisions; CW gives more ratios.
- **FREEZE off**: a delay. TIME picks a multiple of the base time.
- **FREEZE on**: loops a slice of the buffer (a beat-repeat or slicer). TIME picks which slice.
- **SHAPE**: a tempo-synced envelope on the repeats (fully CCW = normal).
- **PITCH**: a rotary-tape-head pitch shifter (noon = none).

### Wavetable synth mode
- Starts when both inputs have been unpatched for 10 s.
- FEEDBACK [J] selects one of 8 wavetable banks derived from Plaits.
- DRY/WET [K] balances the raw oscillator against the granulated signal.
- FREEZE halts the grain envelopes and new grains.
- Quality [A] sets the output resolution.
- PITCH CV is 1V/oct; the PITCH attenurandomizer sets the pitch randomization.

## How to (common procedures)
**Set input gain manually (stop the hiss)**
1. Hold [A].
2. Turn FEEDBACK [J] to set the gain.
3. Release. The gain is remembered until you long-press [A] (1 s) to go back to auto-gain.

**Re-run auto-gain** after changing sources: long-press [A] for 1 s, then play a representative signal for about 5 s.

**Clocked grains**
1. Patch a clock into SEED.
2. DENSITY CCW of noon divides the clock (1/16 to 1); CW of noon sets grain probability.

**One grain per hit (percussive granular)**
1. Short-press SEED (gated mode).
2. Set DENSITY to noon.
3. Send triggers to SEED.

**Tempo-synced delay or slicer**
1. Turn SIZE fully CW.
2. Tap SEED, or clock it, to set the base time.
3. Use TIME to choose the multiple; engage FREEZE to slice and loop.

**Save a buffer across power cycles**: hold FREEZE for more than 10 s.

**Hear feedback clearly** (test settings from the manual)
1. DRY/WET fully CW, SIZE noon, DENSITY 9 o'clock, SHAPE 2 o'clock, TIME fully CCW, PITCH 11 or 1 o'clock, attenurandomizers at noon.
2. Then raise FEEDBACK. It's even more obvious in delay mode (SIZE fully CW).

**Firmware update**
1. Unplug all CV. Patch the computer's audio output to IN L. Set TIME to its midpoint.
2. Power on while holding FREEZE.
3. Mute other computer sounds and turn monitors down — the update audio is harsh.
4. LED [A] acts as a level meter (yellow = good); use TIME to adjust gain.
5. Play the update file. Red blinking = bad level: press B and retry with more gain.
6. Don't update to "fix" odd behaviour — check the patch first.

## Specifications
- Width: 14HP (from Mutable's spec)
- Power: +12V 100 mA, −12V 10 mA
- Stereo in and out; inputs auto-gain +0 to +32 dB, with a limiter
- Grain size about 30 ms to 4 s, forward or reversed; pitch ±24 semitones
- Internal audio at up to 48 kHz (Sunny tape dry path)
- 10-pin ribbon, red stripe = −12V; match the "Red stripe" marking on the PCB

## Tips and gotchas
- **Background hiss** usually means auto-gain is boosting silence (an input patched to nothing, or a quiet source). Set gain manually.
- **Pops or clicks on one channel** when changing DENSITY or SEED: check whether R OUT has been set to output grain triggers (M + SEED). Note that the trigger only appears on R when a cable is plugged into R, so L is unaffected.
- **"Feedback does nothing"**: TIME is far back in the buffer, TIME is randomized, grains are sparse, the output is quiet, or the attenurandomizers are at extremes. Use the test settings above.
- **Synth mode surprise**: unplug the inputs for 10 s and Beads becomes a wavetable drone. Patch any input to leave that mode.
- **SIZE below about 11 o'clock plays backwards** — easy to do by accident.
- DENSITY at exactly noon = silence in latched mode.
- Randomization also scatters grains across the stereo field, so attenurandomizers widen the image.
