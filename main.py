try:
    import selenium
except ImportError as e:
    print(f"{e}\n\n\n\n\n\n\n\n\n\n")
    os.system("pip install selenium")
except:
    print("some dumb error occured")

try:
    import chromedriver_autoinstaller
except ImportError as e:
    print(f"{e}\n\n\n\n\n\n\n\n\n\n")
    os.system("pip install chromedriver-autoinstaller")
except:
    print("some dumb error occured")

input("press enter to continue [1]")

from importall import *

input("press enter to continue [2]")

#driver = start_browser()
open_link('https://web.whatsapp.com')
is_open_wait(True)
goto_clas("11A Official 2021-22")
while True:
    #input("class, and now scroll")
    time.sleep(1)
    msg_raw=get_messages()
    msg_info=update_info(msg_raw)
    rnclas , rnindex = which_class_rn(msg_info)
    print("right now is class: ", rnclas)
    if(rnclas):
        #print("rnclas")
        describe_clas(msg_info,rnindex)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(msg_info[rnindex]["link"])
        time.sleep(5)
        driver.close()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
    print("looping ", get_time()[0] )
    time.sleep(300)
