import wave, struct, math, sys
import pyaudio

commands = {
	'sync':[17200.0,17400.0,17800.0,17600.0,17800.0],
	'hello_teacher':[17200.0,17400.0,18200.0,17400.0,18200.0],
	'i_knew_it':[17200.0,17800.0,18000.0,18200.0,18000.0],
	'i_know_this':[17200.0,17800.0,18200.0,17800.0,18200.0],
	'get_the_class_started':[17200.0,17400.0,17600.0,17800.0,17600.0]
}

wavef = wave.open('temp.wav','w')

sampleRate = 44100.0 # hertz
pulse_duration = 0.200
silence_period = 0.050

def generate_silence(duration):
	for i in range(int(duration * sampleRate)):
		data = struct.pack('<h',0)
		wavef.writeframesraw(data)

def generate_tone(frequency):
	generate_silence(silence_period)
	print "generating tone " + str(frequency) + " Hz"
	for i in range(int(pulse_duration * sampleRate)):
    		value = int(1024.0*math.sin(frequency*2*math.pi*float(i)/float(sampleRate)))
    		data = struct.pack('<h', value)
    		wavef.writeframesraw( data )

def send_command(command):
	print "synthezising command: " + command
	for tone in commands[command]:
		generate_tone(tone)

def play_command():
	chunk = 1024
	p = pyaudio.PyAudio()
	stream = p.open(format=p.get_format_from_width(2),channels=1,rate=44100,output=True)
	f = wave.open(r"temp.wav","rb")
	data = f.readframes(chunk)
	while data:
		stream.write(data)
		data = f.readframes(chunk)
	stream.stop_stream()
	stream.close()
	p.terminate()
	f.close()

if __name__ == '__main__':
	if len(sys.argv) > 1:
		command = sys.argv[1]
		if command != None and command != '':
			if command in commands.keys():
				wavef.setnchannels(1) # mono
				wavef.setsampwidth(2) 
				wavef.setframerate(sampleRate)
				send_command(command)
				wavef.writeframes('')
				wavef.close()
				play_command()
			else:
				print "ERROR: Command [" + command + "] is not supported."
		else:
			print "ERROR: Command [" + command + "] is invalid."
	else:
		print "Error: Please provide a valid command as parameter"


