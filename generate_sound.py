import numpy as np
from scipy.io.wavfile import write

def generate_505(sample_rate, sound):
    # Storing all middle note frequency values in Hz 
    A_freq = 440
    B_freq = 493.88
    C_freq = 261.63
    D_freq = 293.66
    E_freq = 329.63
    F_freq = 349.23
    G_freq = 392

    # Durations and time array for the chord progression
    duration_chord = 4 
    t_chord = np.linspace(0, duration_chord, int(sample_rate * duration_chord))
    # Create 505 chord progression: Dm Em Dm Em
    D_minor = np.vstack([sound(t_chord, D_freq, 0.1), sound(t_chord, F_freq, 0.1), sound(t_chord, A_freq, 0.1)]).T
    E_minor = np.vstack([sound(t_chord, E_freq, 0.1), sound(t_chord, G_freq, 0.1), sound(t_chord, B_freq, 0.1)]).T
    chord_progression = np.vstack((D_minor, E_minor, D_minor, E_minor, D_minor, E_minor, D_minor, E_minor))
    
    # # Create melody notes (C, E, G) each lasting for one second
    # melody_E = sound(np.linspace(0, 1, int(sample_rate * 1)), E_freq, 0.5)
    # melody_D = sound(np.linspace(0, 1, int(sample_rate * 1)), D_freq, 0.5)
    # melody_B = sound(np.linspace(0, 1, int(sample_rate * 1)), B_freq, 0.5)
    
    # # Stack the melody notes horizontally and then vertically with the chord progression
    # generate_505 = np.vstack([np.hstack([melody_E, melody_D, melody_B]), D_minor]).T
    # For rhythm:
    generate_505 = chord_progression
    
    # Write down to file
    write('505.wav', sample_rate, generate_505.astype(np.float32))

if __name__ == '__main__':
    sample_rate = 8000
    sound = lambda time, freq, amp=1: amp * np.sin(2 * np.pi * freq * time)
    generate_505(sample_rate, sound)
