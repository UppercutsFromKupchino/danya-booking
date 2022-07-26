import mouse
import time
from ahk import AHK
from ahk.window import Window
import win32api
from win32con import *
from random import randint
import requests
import keyboard
import asyncio

global starter
starter = 0


async def main():
	while True:
		print('Waiting for start\n')
		await asyncio.sleep(5)
		if starter == 1:
			await starter1()
			

def starter2():
	global starter
	starter = 1
	print('Starting...\n')

def stopper():
	global starter
	starter = 0
	print('Stopping...\n')

async def starter1():
	await asyncio.sleep(2)
	mouse.move(1453, 647)
	win32api.mouse_event(MOUSEEVENTF_WHEEL, 1450, 410, 10000, 0)
	global finder
	global stopper

	ahk = AHK()
	while True:
		while True:
			mouse.move(1453, 647)
			smooth = randint(10, 20)
			win32api.mouse_event(MOUSEEVENTF_WHEEL, 1450, 410, -smooth, 0)
			color = ahk.pixel_get_color(1453, 647)
			if color == '0x0071C2': #0x00487A
				print('Blue was found')
				await asyncio.sleep(1)
				mouse.click()
				break
			elif color == '0x00224F':
				print('The page ended!')
			if starter == 0:
				break

		if starter == 0:
			break

		while True:
			await asyncio.sleep(1)
			colorsite = ahk.pixel_get_color(620, 310)
			if colorsite == '0xFEBB01' or colorsite == '0xFEBB02':
				await asyncio.sleep(0.5)
				break

		if starter == 0:
			break
				

		mouse.move(1040, 500)
		await asyncio.sleep(0.5)
		mouse.click()

		randomx = randint(140, 200)
		randomy = randint(250, 300)
		mouse.move(randomx, randomy)
		await asyncio.sleep(5)
		mouse.click()

		mouse.move(1567, 530)

		photo = randint(6, 10)
		for i in range(photo+1):
			await asyncio.sleep(0.5)
			await asyncio.sleep(randint(2, 5))
			mouse.click()

		if starter == 0:
			break

		mouse.move(1820, 120)
		await asyncio.sleep(1.5)
		mouse.click()

		while True:
			smooth = randint(10, 20)
			win32api.mouse_event(MOUSEEVENTF_WHEEL, 1450, 410, -smooth, 0)
			color = ahk.pixel_get_color(1453, 647)
			if color == '0x0071C2': #0x00487A #00224f
				print('Blue was found')
				await asyncio.sleep(1)
				mouse.click()
				break
		await asyncio.sleep(randint(12, 15))

		mouse.move(949, 17)
		await asyncio.sleep(0.5)
		mouse.click()
		await asyncio.sleep(0.2)
		win32api.mouse_event(MOUSEEVENTF_WHEEL, 1450, 410, -120, 0)

keyboard.add_hotkey("E", lambda: starter2())
keyboard.add_hotkey("R", lambda: stopper())

if __name__ == '__main__':
	try:
		asyncio.run(main())
	except Exception as error:
		print(error)

input('Press any key to exit')


