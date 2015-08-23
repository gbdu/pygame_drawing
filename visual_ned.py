










































   
        
        
        
        
        
        
        
        
        
        
        
        
        
                
                
                
                
                
                
                
                
                
                
                
                
                
                        
                        
                        
                                
                                 "sid simulator " + __version__)
                                a = color_ut.get_tween_value("active_box")
                                b = color_ut.get_tween_value("nearbox_1")
                                color = [200, a, a]
                                color = [a+b+t, a+b+t, t/2]
                                color = [d,d,d]
                                color=[a+b+t + 1 , a+b+t + 5 , t/2 + 40]
                                component_counter += 1
                                d = color_ut.get_tween_value("default_box")
                                draw_box(i, inrow, color, component_counter)
                                global selected_component_id
                                selected_component_id = component_counter
                        # Display some text
                        '''draw a single box'''
                        a = b = c = 0
                        boxrect = pygame.Rect(inrow*width, i*height, width, height)
                        boxrect = pygame.Rect(inrow*width, i*height, width, height)
                        boxrect_big = pygame.Rect(inrow*width - width*1, i*height - height*1, width*3, height*3)
                        draw_box_label(i, inrow, get_color_inverse(color), component_counter)
                        elif boxrect_big.collidepoint(pos):
                        else: # This is a regular component, draw it using its tween
                        for inrow in range(8):
                        global bigned
                        global color_ut
                        global gfont
                        if boxrect.collidepoint(pos): # this is an active box
                        pygame.draw.rect(surf, color, boxrect , 0)
                        pygame.mouse.set_visible(0)
                        pygame.mouse.set_visible(1)
                        rpos = pygame.Rect(0, (number*gfont.get_height()), 20,20) # location of text 
                        surf.blit(text, rpos)
                        surf.blit(text, textpos)
                        t = color_ut.get_tween_value(str(component_counter))
                        text = gfont.render(line, 1, (100,200,100))
                        text = gfont.render(str(component_counter), 1, color)
                        textpos = boxrect
                # hide the cursor if we're in here
                # left, top, width, height
                ## draw the border
                ## This is our main loop, draw input screen and update tweener
                #globals()['color_ut'].update_frame(increase_by=1)
                #llog.info("set up '%s' with %d and %d", str(i), st, 100)
                #proc_mouse()
                #return component.get_color_dim()
                '''Draw a grid of 16x16 boxes representing our components'''
                '''draw the bottom panel label'''
                '''get the color of the box that represents the component'''
                c_dict = bigned.get_component_by_id(selected_component_id)
                c_dict['lock'].acquire()
                c_dict['lock'].release()
                c_r = pygame.Rect(0, 0, 256, 256)
                c_r = pygame.Rect(0,0, 256, 100)
                color_ut.add_tweener(str(i))
                color_ut.tween_cycle(str(i), st, 0)
                color_ut.update_frame()
                component_counter = 0
                def draw_box(i, inrow, color, component_counter):
                def draw_box_label(i, inrow, color, component_counter):
                dlog.info("drew component grid....")
                dlog.info("drew version label")
                dlog.log("draw component info")
                draw_components_on_surf(component_surf)
                draw_panel_label(panel_label_surf)        
                draw_version_label(screen)
                else:
                exit(1)
                exit(1)
                for i in range(8):
                for number,line in enumerate(info_paragraph):
                global dlogs
                global gfont
                global selected_component_id
                global user_console
                height= 32
                if(c_r.collidepoint(pos)):
                info_paragraph = []
                info_paragraph.append("")
                info_paragraph.append("Currently selected component: %d " % selected_component_id)
                info_paragraph.append("Internal octo: ")
                info_paragraph.append(s_octo)
                llog.error("Couldnt setup color tweens for components...")
                llog.error("unable to init console %s" % sys.exc_info()[0])
                octo = c_dict['component'].get_octo()
                pass
                pos = (pygame.mouse.get_pos()[0] - 20 , pygame.mouse.get_pos()[1] - 20)
                print e
                pygame.display.flip()
                pygame.draw.rect(surf, (30, 40, 80), c_r, 0)
                pygame.draw.rect(surf, (45, 45, 45), c_r, 0 )
                r = pygame.Rect(300, 20, 320, 256)
                return ## Draw components
                return component_pipe.recv()
                return uc
                s_octo = str(octo)
                screen.blit(component_surf, component_box_where)
                screen.blit(panel_label_surf, panel_label_where)
                setup_color_tweens()
                st = random.randint(40, 90)
                surf.fill((40,40,40))
                uc = pyconsole.Console(screen, r, key_calls=key_calls  )
                user_console.draw()
                user_console.process_input()
                version_text.draw()
                version_text=Text(screen, globals()["gfont"], pygame.Rect(0,0,0,0) ,
                width = 32
        """draw the given Ned on global scr"""
        #       - components that fire together wire together
        #       - output from one of the text components
        #       - Right-click menu
        #       - What sid thinks it looks like (as a person)
        # Create ned process
        # Things to draw on main screen:
        # Things to input:
        # TODO:
        ## Actual Draw() starts here
        ## Draw() ends here
        color_ut = ut.Ut(1)
        color_ut.add_tweener("active_box")
        color_ut.add_tweener("default_box")
        color_ut.add_tweener("default_box_text")
        color_ut.add_tweener("nearbox_1")
        color_ut.add_tweener("nearbox_2")
        color_ut.constant("default_box", 50)
        color_ut.tween_cycle("active_box", 0, 100)
        color_ut.tween_cycle("default_box_text", random.randint(0,50), random.randint(50, 200))
        color_ut.tween_cycle("nearbox_1", 0, 40)
        color_ut.tween_cycle("nearbox_2", 0, 20)
        component_box_where= (20,20)
        component_surf = pygame.Surface((256, 256))
        def draw_component_info_on_surf(surf, where):
        def draw_components_on_surf(surf):
        def draw_info_about_component_from_id(where):
        def draw_panel_label(surf):
        def draw_version_label(screen):
        def get_component_color(component_pipe):
        dlog.info('create console')
        except Exception as e :
        except:
        exit(1)
        exit(1)
        exit(1)
        for i in range(256):
        global bigned
        global color_ut
        global color_ut
        global dlog
        global llog
        global main_breakout
        global screen
        globals()["bigned"].signal_extinguish()
        globals()["color_ut"] = None
        globals()["gfont"] = g.create_font()
        globals()["gselected_component"] = 1
        globals()["llog"].info("extinguished")
        globals()["main_breakout"] = Value("d", 0)
        globals()["main_breakout"].value = 0
        globals()["screen"] = g.init_pygame()
        init_color_tweeners()
        inverse = [abs(250-color[0]), abs(250-color[1]), abs(250-color[2])]
        inverse = [color[0]-a, color[1]-a, color[2]-a]
        key_calls={"d": extinguish_and_deload})
        llog.error("error while init  [ FAIL ] ")
        llog.error("failed to init tweeners: %s", e)
        llog.error("unknown error while init tweeners")
        llog.info("* PROCESS: Draw")
        llog.info("---> ABOUT TO DELOAD")
        llog.info("entering main draw loop")
        llog.info("exiting main draw loop...")
        llog.info("here we go")
        llog.info("init'd font successful [ SUCCESS ] ")
        llog.info("init'd screen [ SUCCESS ]")
        llog.info("signaled extinguish  [ SUCCESS ]")
        llog.info("ut init'd successfully...  [ SUCCESS ] ")
        panel_label_surf = pygame.Surface((256, 100))
        panel_label_where = (20, 300)
        pass
        pass
        print e
        return
        return
        return inverse
        return inverse
        screen.fill((35, 35, 35))
        try:
        try:
        while main_breakout.value == 1:
"""2 processes: NedProcess, DrawProcess"""
"""draw a visual AI window"""
## Innit is done        
#### Start here
__version__ = "base"
def Draw(theNed):
def extinguish_and_deload():
def get_color_dimmer(color,a=20):
def get_color_inverse(color):
def init_color_tweeners():
def init_console(screen, key_calls):
def setup_color_tweens(): ## This is a list of tweens set up by default...
except Exception as e:
except ValueError as e:
except:
from getmylogger import silent_logger,loud_logger
from multiprocessing import Process, Value
from Text import Text
from time import sleep
globals()["bigned"] = None
globals()["dlog"] = silent_logger("drawing_examples") #silent drawing logger
globals()["llog"] = loud_logger("drawing_examples") #loud logger (shows in console)
globals()["llog"].info("log setup! [ SUCCESS ] ")
globals()["selected_component_id"] = 0
globals()["user_console"] = init_console(globals()["screen"],
if __name__ == '__main__':
import exceptions
import gui_helpers as g
import os,sys
import pygame,pyconsole
import random
import ut
llog = globals()["llog"]
try:
try:
USER_CONSOLE_ENABLED = True #only checked when drawing