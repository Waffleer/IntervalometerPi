
#include <iostream>
#include <pigpio.h>
#include <chrono>
#include <thread>
#include <stdlib.h>

using namespace std;


/*

REQUIRES

pigpio.h //https://abyz.me.uk/rpi/pigpio/

TO BUILD

g++ camControl.cpp -lpigpio -lrt -lpthread

TO RUN
// 1000=pLen, 100=interval, 10=count, 0=bulb(T/F)
sudo ./a.out 1000 100 10 0
*/


int main(int argc, char *argv[])
{
        gpioInitialise();

        int shutter = 23;
        int focus = 24;
        gpioSetMode(shutter, PI_OUTPUT);
        gpioSetMode(focus, PI_OUTPUT);
        cout << "Started" << "\n";

        int pLen;
        int interval;
        int count;
        int bulb;

        pLen = strtol(argv[1], NULL, 10); //Will take in variables as args
        interval = strtol(argv[2], NULL, 10);
        count = strtol(argv[3], NULL, 10);
        bulb = strtol(argv[4], NULL, 10);
        //cin >> pLen >> interval >> count >> bulb;

        cout << "pLen: " << pLen << " interval: " << interval << " count: " << count << " bulb:  " << bulb << "\n";

        //IDK why this is needed but it tells the camera to pay attention to this port i think, the first picture might not go off without it
        // Might be a Nikon D90 problem idk
        gpioWrite(shutter, PI_ON); //You need to focus the camera to actually take a picture
        std::this_thread::sleep_for(std::chrono::milliseconds(40));
        gpioWrite(shutter, PI_OFF);
        //Idk why



        if(bulb == 0)
        {
                for(int x = 0; x<count; ++x){
                        gpioWrite(focus, PI_ON);
                        std::this_thread::sleep_for(std::chrono::milliseconds(40));
                        gpioWrite(shutter, PI_ON);
                        std::this_thread::sleep_for(std::chrono::milliseconds(10));
                        gpioWrite(focus, PI_OFF);
                        std::this_thread::sleep_for(std::chrono::milliseconds(10));
                        gpioWrite(shutter, PI_OFF);
                        std::this_thread::sleep_for(std::chrono::milliseconds(pLen));
                        if(x != count-1)
                        {
                                std::this_thread::sleep_for(std::chrono::milliseconds(interval));
                        }
                }
        }
        gpioTerminate();
        return 0;
}



