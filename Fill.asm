// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Variable for maximum write to SCREEN
@24575
D = A
@m
M = D
@KBD
D = M
@t
M = D

(INPUTCHECK)
@KBD
D = M
@t
D = M - D // When Key is pressed: input - state before /= 0

// When State is unchanged: input = state before
@INPUTCHECK
D; JEQ

// When Key is newly pressed: input > state before
// But another Key can be presssed, so first check for input == 0
@KBD
D = M
@DELETE
D; JEQ  // GoTo Delete
// Else Fill screen
@FILL
D; JMP  // GoTo Fill

// Fill screen to black
(FILL)
// Write new state before
@KBD
D = M
@t
M = D
// Declare var s -> adress of bits-to–draw-to
@SCREEN
D = A
@s
M = D
@c
M = -1
(FILLLOOP)
// Read color to D
@c
D = M
// Save screen pointer to A
@s
A = M
// Write color to screen (s value)
M = D
@s // increment screen counter
M = M + 1
@m
D = M
@s
A = M
D = D-A
D = D + 1
@FILLLOOP
D; JGT
@INPUTCHECK
D; JEQ


@INPUTCHECK
0; JMP

// Fill screen to white
(DELETE)
// Write new state before
@KBD
D = M
@t
M = D
// Declare var s -> adress of bits-to–draw-to
@SCREEN
D = A
@s
M = D
@c
M = 0

(DELETELOOP)
// Read color to D
@c
D = M
// Save screen pointer to A
@s
A = M
// Write color to screen (s value)
M = D
@s // increment screen counter
M = M + 1
@m
D = M
@s
A = M
D = D-A
D = D+1
@DELETELOOP
D; JNE
@INPUTCHECK
D; JEQ

@INPUTCHECK
0; JMP
