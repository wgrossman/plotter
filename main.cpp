#include "mbed.h"
 
Serial pc(USBTX, USBRX); // tx, rx
AnalogIn pot1(p19);
DigitalOut myled(LED1);

int baud_rate = 119200;
int bits = 8;
int stop_bits = 1;
 
int main()
{
    pc.baud(baud_rate);
    
    while(1) {
        pc.printf("%.2f\n", pot1.read());
        wait(0.1);
        myled = !myled;
    }
}
