#!/usr/bin/python2.7
from __future__ import print_function
import wiringpi2 as wiringpi
import pygame, sys, os
from pygame.locals import *
from time import sleep

class motor_handler():
    def __init__(self):
        wiringpi.wiringPiSetupGpio()				# initialise wiringpi GPIO
        wiringpi.pinMode(18,2)                      
        wiringpi.pinMode(17,1)                     
        wiringpi.digitalWrite(17,0)               
        wiringpi.pwmWrite(18,0)                  
    def motor_loop(self, stepSize,motorHold):
		wiringpi.pwmWrite(18,stepSize)   			# pwmWrite(pinNum,StepSize)    	 
		sleep(motorHold)
		wiringpi.pwmWrite(18,0)
    def reset_motor(self):
        wiringpi.pwmWrite(18,0)                 
        wiringpi.digitalWrite(18, 0)            	# ports 17 & 18 off
        wiringpi.digitalWrite(17, 0)
        wiringpi.pinMode(17,0)                  	# set ports back to input mode
        wiringpi.pinMode(18,0)

# Displays pump # every time the pump is run.
class info_text_handler():
    def __init__(self):
        self.trialNumber = 0
        self.fontObj = pygame.font.Font(None,24)
    def trial_increment(self):
        self.trialNumber += 1
    def render_text(self, colorName, winSurface):
        msg = 'Trial ' + str(self.trialNumber)
        msgSurface = self.fontObj.render(msg, False, colorName)
        msgRect = msgSurface.get_rect()
        msgRect.bottomright = (200,100)
        winSurface.blit(msgSurface, msgRect)
    def trial_reset(self):
        self.trialNumber = 0

def main():
    pygame.init()
    pygame.mouse.set_visible(0)

    fpsClock = pygame.time.Clock()
    winSurface = pygame.display.set_mode((400,200))
    pygame.display.set_caption('Gertboard Pump')

    red = pygame.Color(255,0,0)
    black = pygame.Color(0,0,0)
    winSurface.fill(black)

    infotext = info_text_handler()
    motor = motor_handler()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                motor.reset_motor()
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_w:										# press "w" to run the pump
					winSurface.fill(black)
					infotext.trial_increment()								# increment the trial number	
					infotext.render_text(red, winSurface)
					pygame.display.update()
					motor.motor_loop(1000,1)									# motor.motor_loop(size of the step, seconds to run the motor)
                if event.key == K_ESCAPE or event.key == K_q:				# ESC to quit program
                    motor.reset_motor()
                    pygame.event.post(pygame.event.Event(QUIT))
             
        pygame.display.update()
        msSince = fpsClock.tick(30)

# calls the 'main' function when this script is executed
if __name__ == '__main__': main()
