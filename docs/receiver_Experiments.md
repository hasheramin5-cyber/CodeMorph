# Audio Receiver Experiment Log

## Purpose

The purpose of this experiment was to observe the microphone input levels under different real-world conditions before selecting an appropriate threshold for Morse audio detection.

The values below represent the maximum recorded audio amplitude obtained using:

```python
sound_level = np.max(np.abs(my_recording))
```

---

## Test Results

| Test | Condition                |                                                         Maximum Amplitude |
| ---- | ------------------------ | ------------------------------------------------------------------------: |
| 1    | Microphone OFF           |                                                           `3.0517578e-05` |
| 2    | Microphone ON (Silence)  |                                                           `6.1035156e-05` |
| 3    | Slow Voice               | `0.038330078`, `0.06454468`, `0.030761719`, `0.009979248`, `0.0039978027` |
| 4    | Normal Voice             |                    `0.10971069`, `0.06655884`, `0.09362793`, `0.10153198` |
| 5    | Loud Voice               |                                   `0.17944336`, `0.5284424`, `0.09454346` |
| 6    | Speaking from a Distance |                                            `0.0138549805`, `0.0013122559` |
| 7    | Hand Clap                |                          `0.00018310547`, `0.00021362305`, `0.0002746582` |
| 8    | Table Knock              |          `9.1552734e-05`, `0.00015258789`, `0.002960205`, `6.1035156e-05` |

---

## Initial Observations

* Background noise remains extremely low when the microphone is muted or the environment is silent.
* Human speech produces significantly higher amplitudes than background noise.
* Loud speech generates the highest values observed during the experiment.
* Distant speech still remains detectable above the background noise level.
* Clap and table knock results varied depending on timing and recording conditions, indicating that transient sounds may require additional testing.

---

## Conclusion

These experiments provide a baseline understanding of the microphone's input characteristics. The collected data will be used to determine a reliable sound threshold before implementing real-time Morse code detection.

**Note:** Final threshold selection will be based on dedicated Morse beep experiments rather than human voice, since the receiver is designed to detect Morse audio signals instead of speech.
