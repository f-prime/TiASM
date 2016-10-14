; Moves the letter A accross the screen
mov r1 i0 ; Puts the integer value 0 into r1. We will use this value as a memory address later 
mov r2 i-1 ; This saves the previous location so that it can be overwritten
add r1 r1 i1 ; Increment the letter memory address location
add r2 r2 i1 ; increment the trailing character location
mov pr1 i65 ; Moves the letter to the memory address located in r1
mov pr2 i64 ; Move a space into the previous locatio that the A was in
cmp r1 i512 ; Check if we've run out of video memory (otherwise we start to overflow into 'RAM'!)
jmpne i2    ; Loop until r1 equal 512
jmp i0 ; while True
