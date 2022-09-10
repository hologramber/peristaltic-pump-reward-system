## Peristaltic-Pump-Reward-System

Most commercial water/fluid reward systems used in research settings cost a few hundred dollars (or more) and aren’t easily modified / are difficult to integrate with existing hardware. This is a series of fairly quick hacks, but they do the job well and won’t cost you >$100.. much less if you already have some of the components sitting around. Using a peristaltic pump is preferred, as the motor never actually comes into contact with the fluid itself. There are three different versions here – the one I personally use is built with a Raspberry Pi, the L293D quadruple half-H driver from TI, and a peristaltic pump from Adafruit. The other version uses an Arduino with a SeeedStudio motor shield, but any motor shield made for the Arduino would probably do fine. You could also build an Arduino-based version using an L293D.

![pump_mini](https://user-images.githubusercontent.com/83111496/189475027-5b6132d3-6e77-48fc-98fc-bfedaa1ae14d.jpg)

- Peristaltic Liquid Pump (12VDC / 300mA) with Silicone Tubing
- 12VDC Adapter (leftover wall adapter) to power the motor
- Programmable device to control motor activity:
	- [Option 1] Raspberry Pi Model B
	- [Option 2] Arduino Uno (Or Similar) 
	- [Option 3] Your alternative controller of choice.
- Some way of routing power to/driving the motor:
	- [Option 1] L293D [ http://www.ti.com/lit/ds/symlink/l293d.pdf ]
	- [Option 2: Arduino Only] Seeed Studio Motor Shield (or other shield)
	- [Option 3] Power Transistor
- [Optional] Momentary Push Button/Switch for manual fluid delivery
- [Optional] Something to house the components (I like OpenBeam or MakerSlide)
