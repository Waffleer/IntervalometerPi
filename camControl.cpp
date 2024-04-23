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

        int shutter = 24;
        int focus = 23;
        gpioSetMode(shutter, PI_OUTPUT);
        gpioSetMode(focus, PI_OUTPUT);
        cout << "Started" << "\n";

        int pLen;
        int interval;
        int count;
	int report;
	//int bulb;

        pLen = strtol(argv[1], NULL, 10); //Will take in variables as args
        interval = strtol(argv[2], NULL, 10);
        count = strtol(argv[3], NULL, 10);
        report = strtol(argv[4], NULL, 10);
        //bulb = strtol(argv[4], NULL, 10);

	//cin >> pLen >> interval >> count >> bulb;

        cout << "pLen: " << pLen << " interval: " << interval << " count: " << count << " reporting " << report << "\n";//  bulb:  " << bulb << "\n";

        //IDK why this is needed but it tells the camera to pay attention to this port i think, the first picture might not go off without it
        // Might be a Nikon D90 problem idk

        //You need to focus the camera to actually take a picture, you can just leave the shutter on
	gpioWrite(focus, PI_ON);
	std::this_thread::sleep_for(std::chrono::milliseconds(100));
	int parser = 2;
	if(count > 20){ parser = 4; }
	if(count > 50){ parser = 5; }
        for(int x = 1; x<=count; ++x){
                gpioWrite(shutter, PI_ON);
                std::this_thread::sleep_for(std::chrono::milliseconds(10));
                gpioWrite(shutter, PI_OFF);
			if(x%parser == 0 && report == 1)
		{
			thread* teller = new thread(thread_tell, x);
                       	teller->detach();
		}
		std::this_thread::sleep_for(std::chrono::milliseconds(pLen-1));
                std::this_thread::sleep_for(std::chrono::milliseconds(interval));
        }
	gpioWrite(focus,PI_OFF);
	if(report == 1){
		thread* teller = new thread(thread_tell, count);
        	teller->detach();
	}
        gpioTerminate();
        return 0;
}
