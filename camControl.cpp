#include <iostream>
#include <pigpio.h>
#include <chrono>
#include <thread>
#include <stdlib.h>
#include <string.h>

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


void thread_tell(int x){
	//cout << "Thread Talking : " << x << endl;
	string command = "python3 /home/waffleer/IntervalometerPi/intervalometerPi/manage.py updateRun " + to_string(x);
	system(command.c_str());
	cout << "Finished : " << x << endl;
}



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


	int parser = 3;
	if(count > 20){ parser = 4; }
	if(count > 50){ parser = 5; }
        if(bulb == 0)
        {
                for(int x = 1; x<=count; ++x){
                        gpioWrite(focus, PI_ON);
                        std::this_thread::sleep_for(std::chrono::milliseconds(40));
                        gpioWrite(shutter, PI_ON);
                        std::this_thread::sleep_for(std::chrono::milliseconds(10));
                        gpioWrite(focus, PI_OFF);
                        std::this_thread::sleep_for(std::chrono::milliseconds(10));
                        gpioWrite(shutter, PI_OFF);
			if(x%parser == 0)
			{
				thread* teller = new thread(thread_tell, x);
                        	teller->detach();
			}
			std::this_thread::sleep_for(std::chrono::milliseconds(pLen));
                        std::this_thread::sleep_for(std::chrono::milliseconds(interval));
                }
        }
	thread* teller = new thread(thread_tell, count);
        teller->detach();
        gpioTerminate();
        return 0;
}
