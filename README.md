# Nenuco-hAPPy-school

Nenuco hAPPy school toy protocol implementation

About Nenuco hAPPy school
=========================

Nenuco Happy School is a toy sold by Famosa at least in the Spanish market ( http://www.nenucofamosa.es/juguetes/nenuco-happy-school ).

The toy uses a ultrasound-based protocol for the communication between the device and the corresponding iOS and Andoid app. In effect there's no need for any other hardware than an speaker and a microphone to communicate with Nenuco.

This project is an educational attempt to analyze and re-create the audio protocol in order to communicate with the Nenuco without the need of using the provided app in any computer. Once the protocol is understood and implemented the possibilities are endless for Nenuco! ;):

   - Nenuco raises his hand every time a new e-mail arrives
   - Nenuco greets you when you get home with a "Hello, teacher!"


Careful attention at making this implementation script-able has been taken,

This project includes a:

 1. Description of the protocol as it is currently understood so far
 2. An incomplete description of the different commands identified so far
 3. A Python implementation of the protocol


Audio protocol
==============

Nenuco hAPPy school protocol uses ultrasound frequencies to encode special commands that go back and forth between the Nenuco and the corresponding provided mobile app.

Nenuco communication uses 17 kHz as the central fequency where bursts of pulses in different frequencies separated by a 50 ms gap are sent.

Each command consists of a package that contains 5 pulses in frequencies separated 200 Hz between each other and 200 ms duration. As a result, efective transmission speed for Nenuco is an astonishing 5 baud. However this transmission speed is affected by the waiting period in Nenuco which doesn't listen for commands while executing the previous command.

The list of identified commands and their pulse frequencies is the following  ( check nenuco.py for a full list in "command" dictonary  )



Tools
=====

The main entry point is the "nenuco.py" Python script.  It uses already available APIs in Python and PyAudio as dependency ( pip install pyaudio ).

This script receives as parameter an string that represents the command that is to be sent to Nenuco.

You can call this script using the following syntax:

      python nenuco.py sync

Should you want to start communication with Nenuco, there's an initial synchronization process that is triggered with the "sync" command. Nenuco responds with an acknowledgement in the form of a packet sent back in the same central frequency but with 17000 Hz tones interleaved, raising his hand and blinking twice. Syncronization finishes when the blinking blue led in her chest is steady.

Once the sync command has been received and acknowledged by Nenuco, any number of commands can be sent afterwards and will be executed by the Nenuco.


Disclaimer
==========

### This information is provided for personal educational purposes only
### The author does not guarantee the accuracy of this information
### By using the provided information, libraries or software, you solely take the risks of damaging your hardware or your ears.

See License for more information



### TO-DO

- [ ] Reverse engineer packet structure
- [ ] Stream wave directly without the need of temporal WAV file
- [ ] Listener and packet decoder for Nenuco's responses


