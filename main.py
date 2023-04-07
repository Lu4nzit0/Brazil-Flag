import pyautogui as actionMouse
import pyautogui as timeWait

timeWait.sleep(2)

actionMouse.moveTo(x=22, y=1050)
actionMouse.click()

actionMouse.typewrite('Paint')
timeWait.sleep(2)
actionMouse.moveTo(x=189, y=568)
actionMouse.click()

timeWait.sleep(2)
actionMouse.moveTo(x=506, y=68)
actionMouse.click()

timeWait.sleep(2)
actionMouse.moveTo(x=270, y=239)
actionMouse.mouseDown(x=270, y=239)
# timeWait.sleep(4)
actionMouse.mouseUp(x=1066, y=712)

timeWait.sleep(2)
actionMouse.moveTo(x=464, y=82)
actionMouse.click()

timeWait.sleep(2)
actionMouse.moveTo(x=280, y=290)
actionMouse.mouseDown(x=280, y=290)
actionMouse.mouseUp(x=1046, y=655)


timeWait.sleep(1)
actionMouse.moveTo(x=485, y=62)
actionMouse.click()
actionMouse.mouseDown(x=544, y=386)
actionMouse.mouseUp(x= 774, y=565)

timeWait.sleep(1)
actionMouse.moveTo(x=336, y=69)
actionMouse.click()
timeWait.sleep(2)

actionMouse.moveTo(x=960, y=166)
actionMouse.click(x=960, y=166)
actionMouse.moveTo(x=1003, y=59)
actionMouse.click(x=1003, y=59)
actionMouse.moveTo(x=931, y=263)
actionMouse.click(x=931, y=263)
actionMouse.moveTo(x=983, y=61)
actionMouse.click(x=983, y=61)
actionMouse.moveTo(x=806, y= 393)
actionMouse.click(x=806, y= 393)
actionMouse.moveTo(x= 1048, y= 58)
actionMouse.click(x= 1048, y= 58)
actionMouse.moveTo(x=657, y=455)
actionMouse.click(x=657, y=455)


print(actionMouse.position())